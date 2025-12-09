# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from uuid import uuid4
import statistics
# app/main.py 상단 근처에 추가
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Auction Lab API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Pydantic 모델
# -----------------------------
class AuctionCreate(BaseModel):
    title: str
    description: Optional[str] = None
    # 예: KOICA처럼 예정가격 대비 투찰률 분석을 위해
    base_price: float = Field(..., gt=0, description="예정가격(기초예가)")
    lower_bound_rate: float = Field(0.8, gt=0, le=1,
                                    description="하한율 (예: 0.8이면 80%)")

class Auction(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    base_price: float
    lower_bound_rate: float

class BidCreate(BaseModel):
    bidder_id: str          # 업체 ID 또는 이름
    bid_price: float        # 실제 제출가격

class Bid(BaseModel):
    id: str
    auction_id: str
    bidder_id: str
    bid_price: float
    bid_rate: float         # 투찰률 = bid_price / base_price

class AuctionStats(BaseModel):
    auction_id: str
    num_bids: int
    mean_bid_rate: Optional[float]
    std_bid_rate: Optional[float]
    min_bid_rate: Optional[float]
    max_bid_rate: Optional[float]

class WinnerResult(BaseModel):
    auction_id: str
    winner_bidder_id: Optional[str]
    winning_price: Optional[float]
    winning_rate: Optional[float]
    reason: str

# -----------------------------
# 간단한 In-memory 저장소
# -----------------------------
AUCTIONS: Dict[str, Auction] = {}
BIDS: Dict[str, List[Bid]] = {}  # auction_id -> bids

# -----------------------------
# 경매 생성
# -----------------------------
@app.post("/auctions", response_model=Auction)
def create_auction(auction_in: AuctionCreate):
    auction_id = str(uuid4())
    auction = Auction(
        id=auction_id,
        title=auction_in.title,
        description=auction_in.description,
        base_price=auction_in.base_price,
        lower_bound_rate=auction_in.lower_bound_rate
    )
    AUCTIONS[auction_id] = auction
    BIDS[auction_id] = []
    return auction

# 경매 리스트
@app.get("/auctions", response_model=List[Auction])
def list_auctions():
    return list(AUCTIONS.values())

# 경매 조회
@app.get("/auctions/{auction_id}", response_model=Auction)
def get_auction(auction_id: str):
    auction = AUCTIONS.get(auction_id)
    if not auction:
        raise HTTPException(status_code=404, detail="Auction not found")
    return auction

# -----------------------------
# 입찰 제출
# -----------------------------
@app.post("/auctions/{auction_id}/bids", response_model=Bid)
def submit_bid(auction_id: str, bid_in: BidCreate):
    auction = AUCTIONS.get(auction_id)
    if not auction:
        raise HTTPException(status_code=404, detail="Auction not found")

    bid_id = str(uuid4())
    bid_rate = bid_in.bid_price / auction.base_price

    bid = Bid(
        id=bid_id,
        auction_id=auction_id,
        bidder_id=bid_in.bidder_id,
        bid_price=bid_in.bid_price,
        bid_rate=bid_rate
    )
    BIDS[auction_id].append(bid)
    return bid

# -----------------------------
# 낙찰자 선정 (예: 하한율 이상 중 최저가 낙찰)
# -----------------------------
@app.get("/auctions/{auction_id}/winner", response_model=WinnerResult)
def get_winner(auction_id: str):
    auction = AUCTIONS.get(auction_id)
    if not auction:
        raise HTTPException(status_code=404, detail="Auction not found")

    bids = BIDS.get(auction_id, [])
    if not bids:
        return WinnerResult(
            auction_id=auction_id,
            winner_bidder_id=None,
            winning_price=None,
            winning_rate=None,
            reason="No bids submitted"
        )

    # 하한율 이상인 입찰만 유효
    valid_bids = [b for b in bids if b.bid_rate >= auction.lower_bound_rate]

    if not valid_bids:
        return WinnerResult(
            auction_id=auction_id,
            winner_bidder_id=None,
            winning_price=None,
            winning_rate=None,
            reason="No bids above lower bound rate"
        )

    # 최저 가격 낙찰 (조달/KOICA형)
    winning_bid = min(valid_bids, key=lambda b: b.bid_price)

    return WinnerResult(
        auction_id=auction_id,
        winner_bidder_id=winning_bid.bidder_id,
        winning_price=winning_bid.bid_price,
        winning_rate=winning_bid.bid_rate,
        reason="Winner selected: lowest valid bid"
    )

# -----------------------------
# 간단 통계 (담합 의심 1차 지표용)
# -----------------------------
@app.get("/auctions/{auction_id}/stats", response_model=AuctionStats)
def get_auction_stats(auction_id: str):
    auction = AUCTIONS.get(auction_id)
    if not auction:
        raise HTTPException(status_code=404, detail="Auction not found")

    bids = BIDS.get(auction_id, [])
    if not bids:
        return AuctionStats(
            auction_id=auction_id,
            num_bids=0,
            mean_bid_rate=None,
            std_bid_rate=None,
            min_bid_rate=None,
            max_bid_rate=None,
        )

    rates = [b.bid_rate for b in bids]

    if len(rates) > 1:
        std_rate = statistics.pstdev(rates)
    else:
        std_rate = 0.0

    return AuctionStats(
        auction_id=auction_id,
        num_bids=len(bids),
        mean_bid_rate=statistics.mean(rates),
        std_bid_rate=std_rate,
        min_bid_rate=min(rates),
        max_bid_rate=max(rates),
    )
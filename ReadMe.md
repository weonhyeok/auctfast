✅ README.md (복붙용 Markdown 버전)
# 🏷️ Auction Fast — Fullstack Auction Demo

A full-stack auction demo project built with:

- **FastAPI** (Backend API)
- **Next.js 14 App Router + TypeScript** (Frontend)
- **Tailwind CSS** (UI Styling)

This repository demonstrates a clean monorepo setup for a simple auction system with:
- Auction creation
- Listing all auctions
- Future extension for bidding, winner calculation, and analytics

---

## 📁 Project Structure



auctfast/
├── backend/
│ └── auction-lab-api/
│ ├── app/
│ │ └── main.py
│ ├── requirements.txt
│ └── ...
└── frontend/
└── auction-web-next/
├── app/
│ ├── page.tsx
│ └── auctions/
│ └── new/page.tsx
├── package.json
└── ...


---

## 🚀 Getting Started

### 🔧 Backend Setup (FastAPI)

```bash
cd backend/auction-lab-api
pip install -r requirements.txt
python -m uvicorn app.main:app --reload


Server runs at:

👉 http://localhost:8000/docs

Here you can test:

POST /auctions

GET /auctions

POST /auctions/{id}/bids

GET /auctions/{id}/winner

GET /auctions/{id}/stats

💻 Frontend Setup (Next.js 14)
cd frontend/auction-web-next
npm install
npm run dev


Frontend runs at:

👉 http://localhost:3000

Available pages:

/ — View all auctions

/auctions/new — Create new auction

🔌 API Overview
Create Auction

POST /auctions
Body:

{
  "title": "Sample Auction",
  "description": "Optional auction description",
  "base_price": 1000,
  "lower_bound_rate": 0.8
}

List Auctions

GET /auctions

Submit Bid

POST /auctions/{auction_id}/bids

Get Winner

GET /auctions/{auction_id}/winner

Auction Statistics

GET /auctions/{auction_id}/stats

📌 Tech Stack Summary

FastAPI with in-memory storage

Next.js 14 App Router

Client Components for Forms

TailwindCSS for styling

CORS enabled for local frontend-backend communication

🧱 Future Enhancements

Auction detail view (/auctions/[id])

Bid submission form

Winner result popup

Persistent DB (PostgreSQL, SQLite)

Docker + docker-compose

Authentication (e.g., Clerk, Auth.js)

Deployment (Railway, Vercel)

📜 License

This project is for learning and demo purposes.
Feel free to fork and extend it.


---

완료!  
이 README는 GitHub에서 아주 깔끔하게 렌더링되는 레이아웃입니다.

원하면:

- 한국어 버전 README  
- FastAPI + Next.js를 도커로 돌릴 수 있는 docker-compose.yml  
- 프로젝트 로고/배지 추가  
도 만들어드릴게요!
# 🏷️ Auction Fast — Fullstack Auction Demo

A full-stack auction demo project built with FastAPI (backend) and Next.js 14 (frontend).  
This monorepo includes a simple auction system with creation, listing, and future-ready architecture for bidding and winner calculation.

---

## 📁 Project Structure

auctfast/  
├── backend/  
│   └── auction-lab-api/  
│       ├── app/  
│       │   └── main.py  
│       ├── requirements.txt  
│       └── ...  
└── frontend/  
    └── auction-web-next/  
        ├── app/  
        │   ├── page.tsx  
        │   └── auctions/new/page.tsx  
        ├── package.json  
        └── ...

---

## 🚀 Backend Setup (FastAPI)

cd backend/auction-lab-api  
pip install -r requirements.txt  
python -m uvicorn app.main:app --reload  

Backend running at:  
http://localhost:8000/docs

Available API Routes:  
- POST /auctions — Create auction  
- GET /auctions — List auctions  
- GET /auctions/{id} — Get auction  
- POST /auctions/{id}/bids — Submit bid  
- GET /auctions/{id}/winner — Winner information  
- GET /auctions/{id}/stats — Auction stats  

---

## 💻 Frontend Setup (Next.js)

cd frontend/auction-web-next  
npm install  
npm run dev  

Frontend running at:  
http://localhost:3000

Pages:  
- `/` — Auction list  
- `/auctions/new` — New auction form

---

## 🔌 API Example

Create Auction (POST /auctions):  
{  
  "title": "Sample Auction",  
  "description": "Optional description",  
  "base_price": 1000,  
  "lower_bound_rate": 0.8  
}

List Auctions (GET /auctions) example:  
[  
  {  
    "id": "uuid",  
    "title": "Sample Auction",  
    "description": "Optional description",  
    "base_price": 1000,  
    "lower_bound_rate": 0.8  
  }  
]

---

## ⚙️ Tech Stack

- FastAPI  
- Next.js 14 App Router  
- TypeScript  
- TailwindCSS  
- Uvicorn  
- Pydantic  
- CORS middleware  
- In-memory backend storage  

---

## 🧱 Future Enhancements

- Auction detail page (`/auctions/[id]`)  
- Bid submission UI  
- Winner display  
- PostgreSQL / SQLite support  
- Docker & docker-compose  
- Authentication  
- Deployment (Vercel + Railway)

---

## 📜 License

This project is for educational and demo purposes.  
Feel free to fork, modify, and extend it.

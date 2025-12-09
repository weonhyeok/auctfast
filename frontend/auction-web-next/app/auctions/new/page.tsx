"use client";

import { useState } from "react";

export default function CreateAuction() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [basePrice, setBasePrice] = useState("");
  const [lowerBoundRate, setLowerBoundRate] = useState("0.8");

  const handleSubmit = async (e: any) => {
    e.preventDefault();

    const res = await fetch("http://localhost:8000/auctions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title,
        description,
        base_price: Number(basePrice),
        lower_bound_rate: Number(lowerBoundRate),
      }),
    });

    if (res.ok) {
      alert("Auction created!");
      window.location.href = "/";
    } else {
      alert("Failed to create auction");
    }
  };

  return (
    <main className="p-6 max-w-lg mx-auto">
      <h1 className="text-2xl font-bold mb-4">Create Auction</h1>

      <form className="space-y-4" onSubmit={handleSubmit}>
        <div>
          <label className="font-semibold">Title</label>
          <input
            className="border w-full p-2 rounded"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>

        <div>
          <label className="font-semibold">Description</label>
          <textarea
            className="border w-full p-2 rounded"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </div>

        <div>
          <label className="font-semibold">Base Price</label>
          <input
            type="number"
            className="border w-full p-2 rounded"
            value={basePrice}
            onChange={(e) => setBasePrice(e.target.value)}
            required
          />
        </div>

        <div>
          <label className="font-semibold">Lower Bound Rate</label>
          <input
            type="number"
            step="0.01"
            className="border w-full p-2 rounded"
            value={lowerBoundRate}
            onChange={(e) => setLowerBoundRate(e.target.value)}
            required
          />
        </div>

        <button
          type="submit"
          className="bg-green-600 text-white px-4 py-2 rounded"
        >
          Create
        </button>
      </form>

      <a href="/" className="text-blue-600 underline block mt-4">
        Back to list
      </a>
    </main>
  );
}

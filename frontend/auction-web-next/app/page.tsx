// app/page.tsx

async function getAuctions() {
  const res = await fetch("http://localhost:8000/auctions", {
    cache: "no-store",
  });

  if (!res.ok) {
    return [];
  }
  return res.json();
}

export default async function Home() {
  const auctions = await getAuctions();

  return (
    <main className="p-6 space-y-4">
      <h1 className="text-2xl font-bold">Auction List</h1>

      <a 
        href="/auctions/new" 
        className="bg-blue-600 text-white px-4 py-2 rounded inline-block"
      >
        Create New Auction
      </a>

      <ul className="space-y-3">
        {auctions.length === 0 && (
          <p className="text-gray-500">No auctions yet.</p>
        )}

        {auctions.map((a: any) => (
          <li key={a.id} className="border p-4 rounded shadow">
            <h2 className="font-bold text-lg">{a.title}</h2>
            <p className="text-sm text-gray-600">{a.description}</p>

            <p className="mt-1">
              <strong>Base Price:</strong> {a.base_price}
            </p>
            <p>
              <strong>Lower Bound Rate:</strong> {a.lower_bound_rate}
            </p>
          </li>
        ))}
      </ul>
    </main>
  );
}

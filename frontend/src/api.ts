const BASE_URL = "http://127.0.0.1:8000";

export async function askQuestion(query: string) {
  const res = await fetch(`${BASE_URL}/query`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query }),
  });

  if (!res.ok) {
    throw new Error("API failed");
  }

  return res.json();
}
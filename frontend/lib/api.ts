import type { TicketInput, TicketAnalysis } from "./types";

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export class ApiError extends Error {
  constructor(
    public status: number,
    public detail: string,
  ) {
    super(detail);
  }
}

export async function analyzeTicket(input: TicketInput): Promise<TicketAnalysis> {
  const res = await fetch(`${API_URL}/tickets/analyze`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(input),
  });

  if (!res.ok) {
    let detail = `HTTP ${res.status}`;
    try {
      const data = await res.json();
      detail = data.detail ?? detail;
    } catch (_) {}
    throw new ApiError(res.status, detail);
  }

  return res.json() as Promise<TicketAnalysis>;
}

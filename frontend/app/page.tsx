"use client";

import { useState, useRef } from "react";
import { TicketForm } from "@/components/TicketForm";
import { AnalysisResult } from "@/components/AnalysisResult";
import { analyzeTicket, ApiError } from "@/lib/api";
import type { TicketAnalysis, TicketInput } from "@/lib/types";

export default function Home() {
  const [result, setResult] = useState<TicketAnalysis | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<{ status?: number; message: string } | null>(null);
  const lastInput = useRef<TicketInput | null>(null);

  async function handleSubmit(input: TicketInput) {
    lastInput.current = input;
    setLoading(true);
    setResult(null);
    setError(null);
    try {
      const data = await analyzeTicket(input);
      setResult(data);
    } catch (err) {
      if (err instanceof ApiError) {
        setError({ status: err.status, message: err.detail });
      } else {
        setError({ message: "Could not reach the server. Check your connection and retry." });
      }
    } finally {
      setLoading(false);
    }
  }

  const is422 = error?.status === 422;

  return (
    <main className="mx-auto max-w-3xl px-4 py-10 space-y-8">
      <header>
        <h1 className="text-2xl font-bold tracking-tight">DevSupport Copilot</h1>
        <p className="text-sm text-gray-500 mt-1">AI-powered Stripe support ticket analyzer</p>
      </header>

      <TicketForm onSubmit={handleSubmit} loading={loading} />

      {error && (
        <div
          role="alert"
          className={`rounded-card border px-4 py-3 flex items-start gap-3 ${
            is422
              ? "bg-red-50 border-red-300"
              : "bg-yellow-50 border-yellow-300"
          }`}
        >
          <div className="flex-1 min-w-0">
            <p className={`text-sm font-medium ${is422 ? "text-red-700" : "text-yellow-800"}`}>
              {is422 ? "Validation error" : "Request failed"}
            </p>
            <p className={`text-sm mt-0.5 ${is422 ? "text-red-600" : "text-yellow-700"}`}>
              {error.message}
            </p>
          </div>
          <div className="flex items-center gap-2 shrink-0">
            {!is422 && lastInput.current && (
              <button
                type="button"
                onClick={() => lastInput.current && handleSubmit(lastInput.current)}
                className="text-xs px-2 py-1 rounded border border-yellow-400 bg-white text-yellow-800 hover:bg-yellow-50"
              >
                Retry
              </button>
            )}
            <button
              type="button"
              className="text-xs underline text-gray-500"
              onClick={() => setError(null)}
            >
              Dismiss
            </button>
          </div>
        </div>
      )}

      {result && <AnalysisResult analysis={result} />}
    </main>
  );
}

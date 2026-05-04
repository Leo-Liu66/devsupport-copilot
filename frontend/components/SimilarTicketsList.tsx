"use client";

import { useState } from "react";
import type { SimilarTicket } from "@/lib/types";

interface Props {
  tickets: SimilarTicket[];
}

export function SimilarTicketsList({ tickets }: Props) {
  const [expanded, setExpanded] = useState(false);

  if (tickets.length === 0) return null;

  return (
    <div className="bg-white border border-gray-200 rounded-card shadow-sm p-4">
      <button
        type="button"
        className="flex items-center justify-between w-full text-sm font-semibold text-gray-700"
        onClick={() => setExpanded(v => !v)}
      >
        <span>Similar tickets ({tickets.length})</span>
        <span className="text-gray-400">{expanded ? "▲" : "▼"}</span>
      </button>

      {expanded && (
        <ul className="mt-3 space-y-3">
          {tickets.map(t => (
            <li key={t.ticket_id} className="text-xs border-t border-gray-100 pt-3 first:border-t-0 first:pt-0">
              <div className="flex items-start justify-between gap-2">
                <span className="font-medium text-gray-800">{t.subject}</span>
                <span className="shrink-0 text-gray-400 tabular-nums">
                  {Math.round(t.similarity_score * 100)}%
                </span>
              </div>
              <span className="text-gray-500 font-mono">{t.ticket_id}</span>
              {t.resolution && (
                <p className="mt-1 text-gray-600 leading-relaxed">{t.resolution}</p>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

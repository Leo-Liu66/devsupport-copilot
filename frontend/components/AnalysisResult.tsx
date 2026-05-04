"use client";

import { useState } from "react";
import type { TicketAnalysis } from "@/lib/types";
import { ClassificationChips } from "./ClassificationChips";
import { CitedAnswer } from "./CitedAnswer";
import { DraftReplyCard } from "./DraftReplyCard";
import { SimilarTicketsList } from "./SimilarTicketsList";
import { WorkflowTrace } from "./WorkflowTrace";

interface Props {
  analysis: TicketAnalysis;
}

export function AnalysisResult({ analysis }: Props) {
  return (
    <div className="space-y-4">
      <div className="bg-white rounded-card shadow p-6 space-y-3">
        <div className="flex items-start justify-between gap-4 flex-wrap">
          <div>
            <p className="text-xs text-gray-400 font-mono">{analysis.ticket_id}</p>
            {analysis.persisted_ticket_id && analysis.persisted_ticket_id !== analysis.ticket_id && (
              <p className="text-xs text-gray-400 font-mono">
                persisted as {analysis.persisted_ticket_id}
              </p>
            )}
          </div>
        </div>

        <ClassificationChips classification={analysis.classification} action={analysis.action} />

        <ActionBanner analysis={analysis} />
      </div>

      {analysis.answer.answer && (
        <div className="bg-white rounded-card shadow p-6">
          <h3 className="text-sm font-semibold text-gray-700 mb-3">Answer</h3>
          <CitedAnswer answer={analysis.answer} />
        </div>
      )}

      {analysis.action === "auto_reply" && (
        <DraftReplyCard draft={analysis.draft_reply} />
      )}

      <SimilarTicketsList tickets={analysis.similar_tickets} />

      <WorkflowTrace steps={analysis.workflow_trace} />
    </div>
  );
}

function ActionBanner({ analysis }: { analysis: TicketAnalysis }) {
  const [copied, setCopied] = useState(false);

  async function copyQuestion() {
    if (!analysis.clarification_question) return;
    await navigator.clipboard.writeText(analysis.clarification_question);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  }

  switch (analysis.action) {
    case "auto_reply":
      return (
        <div className="flex items-center gap-2 text-sm text-green-700 bg-green-50 rounded px-3 py-2 border border-green-200">
          <span className="font-semibold">✓ Auto-replied</span>
          <span className="text-green-600">Draft ready to send</span>
        </div>
      );

    case "needs_review":
      return (
        <div className="rounded px-4 py-3 bg-amber-50 border border-amber-300 space-y-1">
          <p className="text-sm font-semibold text-amber-800">⚠ Awaiting Human Review</p>
          <p className="text-xs text-amber-700">
            This ticket has been flagged for engineer review (P1 severity or low retrieval confidence).
            A human will respond within 1 business hour.
          </p>
        </div>
      );

    case "needs_info":
      return (
        <div className="rounded px-4 py-3 bg-sky-50 border border-sky-300 space-y-2">
          <p className="text-sm font-semibold text-sky-800">💬 Clarification Needed</p>
          {analysis.clarification_question && (
            <>
              <p className="text-sm text-sky-900 italic">&ldquo;{analysis.clarification_question}&rdquo;</p>
              <button
                type="button"
                onClick={copyQuestion}
                className={`text-xs px-2 py-1 rounded border transition-colors ${
                  copied
                    ? "bg-green-50 border-green-300 text-green-700"
                    : "bg-white border-sky-300 text-sky-700 hover:bg-sky-50"
                }`}
              >
                {copied ? "✓ Copied" : "Copy question"}
              </button>
            </>
          )}
        </div>
      );

    case "escalate":
      return (
        <div className="rounded px-4 py-3 bg-gray-50 border border-gray-300 space-y-1">
          <p className="text-sm font-semibold text-gray-700">↑ Escalated</p>
          <p className="text-xs text-gray-600">{analysis.draft_reply}</p>
        </div>
      );

    default:
      return null;
  }
}

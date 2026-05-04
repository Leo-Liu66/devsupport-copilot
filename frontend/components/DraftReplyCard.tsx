"use client";

import { useState } from "react";

interface Props {
  draft: string;
}

// Strip internal citation markers ([1], [2] etc.) — they're for agent context,
// not for the customer-facing text.
function stripMarkers(text: string): string {
  return text.replace(/\[\d+\]/g, "").replace(/  +/g, " ").trim();
}

export function DraftReplyCard({ draft }: Props) {
  const [copied, setCopied] = useState(false);
  const displayText = stripMarkers(draft);

  async function handleCopy() {
    await navigator.clipboard.writeText(displayText);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  }

  return (
    <div className="bg-white border border-gray-200 rounded-card shadow-sm p-4">
      <div className="flex items-center justify-between mb-2">
        <h4 className="text-sm font-semibold text-gray-700">Draft reply</h4>
        <button
          type="button"
          onClick={handleCopy}
          className={`text-xs px-2 py-1 rounded border transition-colors ${
            copied
              ? "bg-green-50 border-green-300 text-green-700"
              : "bg-white border-gray-300 text-gray-600 hover:bg-gray-50"
          }`}
        >
          {copied ? "✓ Copied" : "Copy reply"}
        </button>
      </div>
      <pre className="text-sm text-gray-800 whitespace-pre-wrap font-sans leading-relaxed">
        {displayText}
      </pre>
    </div>
  );
}

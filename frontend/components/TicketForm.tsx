"use client";

import { useState } from "react";
import type { TicketInput } from "@/lib/types";

const SOFT_LIMIT = 5000;
const WARN_AT = 4500;

interface Props {
  onSubmit: (input: TicketInput) => void;
  loading: boolean;
}

export function TicketForm({ onSubmit, loading }: Props) {
  const [subject, setSubject] = useState("");
  const [body, setBody] = useState("");
  const [email, setEmail] = useState("");
  const [fieldError, setFieldError] = useState<string | null>(null);

  const bodyLen = body.length;

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!subject.trim()) {
      setFieldError("Subject is required.");
      return;
    }
    if (!body.trim()) {
      setFieldError("Body is required.");
      return;
    }
    setFieldError(null);
    onSubmit({ subject: subject.trim(), body: body.trim(), user_email: email.trim() || undefined });
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4 bg-white rounded-card shadow p-6">
      <div>
        <label className="block text-sm font-medium mb-1" htmlFor="subject">
          Subject
        </label>
        <input
          id="subject"
          type="text"
          value={subject}
          onChange={e => setSubject(e.target.value)}
          placeholder="e.g. Webhook endpoint returns 500 after key rotation"
          className={`w-full rounded border px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400 ${
            fieldError && !subject.trim() ? "border-red-400 bg-red-50" : "border-gray-300"
          }`}
        />
      </div>

      <div>
        <label className="block text-sm font-medium mb-1" htmlFor="body">
          Body
          <span
            className={`ml-2 text-xs font-normal ${bodyLen > WARN_AT ? "text-red-500 font-semibold" : "text-gray-400"}`}
          >
            {bodyLen.toLocaleString()} / {SOFT_LIMIT.toLocaleString()}
          </span>
        </label>
        <textarea
          id="body"
          rows={6}
          value={body}
          onChange={e => setBody(e.target.value)}
          placeholder="Describe the issue in detail..."
          className={`w-full rounded border px-3 py-2 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-indigo-400 resize-y ${
            fieldError && !body.trim() ? "border-red-400 bg-red-50" : "border-gray-300"
          }`}
        />
      </div>

      <div>
        <label className="block text-sm font-medium mb-1" htmlFor="email">
          Email <span className="text-gray-400 font-normal">(optional)</span>
        </label>
        <input
          id="email"
          type="email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          placeholder="customer@example.com"
          className="w-full rounded border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
        />
      </div>

      {fieldError && (
        <p role="alert" className="text-sm text-red-600">
          {fieldError}
        </p>
      )}

      <button
        type="submit"
        disabled={loading}
        className="w-full rounded bg-indigo-600 text-white py-2 text-sm font-medium hover:bg-indigo-700 disabled:opacity-60 disabled:cursor-not-allowed flex items-center justify-center gap-2"
      >
        {loading ? (
          <>
            <Spinner />
            Analyzing…
          </>
        ) : (
          "Analyze ticket"
        )}
      </button>
    </form>
  );
}

function Spinner() {
  return (
    <svg
      className="animate-spin h-4 w-4 text-white"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
    >
      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="3" />
      <path
        className="opacity-75"
        fill="currentColor"
        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
      />
    </svg>
  );
}

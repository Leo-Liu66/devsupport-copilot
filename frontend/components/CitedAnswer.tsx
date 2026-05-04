"use client";

import { useState, useEffect, useRef } from "react";
import type { CitedAnswer as CitedAnswerType, Citation } from "@/lib/types";

interface Props {
  answer: CitedAnswerType;
}

export function CitedAnswer({ answer }: Props) {
  // key = "${marker}-${occurrenceIndex}" so the same marker appearing twice
  // doesn't open two popovers simultaneously
  const [openKey, setOpenKey] = useState<string | null>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  const citMap: Record<string, Citation> = {};
  answer.citations.forEach(c => { citMap[c.marker] = c; });

  // Track which excerpts have already been shown — subsequent identical ones
  // get a dimmed non-interactive badge instead of a full popover.
  const seenExcerpts = new Set<string>();

  useEffect(() => {
    function handleClickOutside(e: MouseEvent) {
      if (containerRef.current && !containerRef.current.contains(e.target as Node)) {
        setOpenKey(null);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const parts = answer.answer.split(/(\[\d+\])/g);
  const occurrenceCounters: Record<string, number> = {};

  return (
    <div ref={containerRef} className="text-sm leading-relaxed text-gray-800 space-y-1">
      <p className="whitespace-pre-wrap">
        {parts.map((part, i) => {
          const cit = citMap[part];
          if (!cit) return <span key={i}>{part}</span>;

          const occIdx = occurrenceCounters[part] ?? 0;
          occurrenceCounters[part] = occIdx + 1;
          const instanceKey = `${part}-${occIdx}`;
          const isOpen = openKey === instanceKey;

          const isDuplicate = seenExcerpts.has(cit.excerpt);
          if (!isDuplicate) seenExcerpts.add(cit.excerpt);

          if (isDuplicate) {
            return (
              <sup
                key={i}
                className="text-[9px] text-gray-400 mx-0.5 align-super"
                title="Same source as a previous citation"
              >
                {part.replace(/\[|\]/g, "")}
              </sup>
            );
          }

          return (
            <span key={i} className="relative inline-block">
              <button
                type="button"
                className="inline-flex items-center justify-center w-5 h-5 rounded-full bg-indigo-600 text-white text-[10px] font-bold align-middle mx-0.5 cursor-pointer hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-400"
                onClick={() => setOpenKey(isOpen ? null : instanceKey)}
                onMouseEnter={() => setOpenKey(instanceKey)}
                onMouseLeave={() => setOpenKey(null)}
                aria-label={`Citation ${part}`}
              >
                {part.replace(/\[|\]/g, "")}
              </button>

              {isOpen && (
                <span
                  className="absolute z-50 left-full top-1/2 -translate-y-1/2 ml-2 bg-white border border-gray-200 rounded-lg shadow-lg p-3 text-xs text-left"
                  style={{ width: "300px", minWidth: "240px", maxWidth: "320px" }}
                  onMouseEnter={() => setOpenKey(instanceKey)}
                  onMouseLeave={() => setOpenKey(null)}
                >
                  <span className="block font-semibold text-gray-900 mb-1">{cit.source_title}</span>
                  <span className="block text-gray-600 mb-2 leading-relaxed">{cit.excerpt}</span>
                  <a
                    href={cit.source_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-indigo-600 hover:underline break-all"
                  >
                    {cit.source_url}
                  </a>
                </span>
              )}
            </span>
          );
        })}
      </p>
    </div>
  );
}

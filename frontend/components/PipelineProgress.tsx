"use client";

import { useState, useEffect, useRef } from "react";

const STAGES = [
  { label: "Classifying ticket", endMs: 1400     },
  { label: "Retrieving docs",    endMs: 4000     },
  { label: "Investigating",      endMs: 7500     },
  { label: "Drafting reply",     endMs: Infinity },
] as const;

const ACTIVE_CAP = 0.85;
const TICK_MS = 80;

// Two-phase exit:
//   "completing" → all bars flash green (200 ms), height still full
//   "collapsing" → opacity+height both go to 0 (250 ms), no layout gap
type ExitPhase = "idle" | "completing" | "collapsing";

interface Props {
  loading: boolean;
}

export function PipelineProgress({ loading }: Props) {
  const [elapsed, setElapsed]     = useState(0);
  const [exit, setExit]           = useState<ExitPhase>("idle");
  const startRef                  = useRef<number | null>(null);
  const timerRef                  = useRef<ReturnType<typeof setInterval> | null>(null);

  useEffect(() => {
    if (loading) {
      setElapsed(0);
      setExit("idle");
      startRef.current = Date.now();
      timerRef.current = setInterval(() => {
        setElapsed(Date.now() - (startRef.current ?? Date.now()));
      }, TICK_MS);
    } else {
      if (timerRef.current) clearInterval(timerRef.current);
      // Phase 1: complete all bars
      setExit("completing");
      setTimeout(() => setExit("collapsing"), 220);
    }
    return () => { if (timerRef.current) clearInterval(timerRef.current); };
  }, [loading]);

  if (exit === "idle" && !loading) return null;

  const collapsing = exit === "collapsing";

  return (
    <div
      className="overflow-hidden transition-all duration-250 ease-in-out"
      style={{
        maxHeight: collapsing ? 0 : 300,
        opacity:   collapsing ? 0 : 1,
        marginBottom: collapsing ? 0 : undefined,
      }}
      onTransitionEnd={() => { if (collapsing) setExit("idle"); }}
    >
      <div className="bg-white rounded-card shadow p-5 space-y-3">
        <p className="text-xs font-medium text-gray-500 uppercase tracking-wide">
          Analyzing…
        </p>

        {STAGES.map((stage, i) => {
          const prevEnd   = i === 0 ? 0 : STAGES[i - 1].endMs;
          const stageEnd  = stage.endMs;
          const completing = exit === "completing" || exit === "collapsing";

          let fill: number;
          let status: "done" | "active" | "pending";

          if (completing) {
            fill = 1; status = "done";
          } else if (elapsed >= stageEnd) {
            fill = 1; status = "done";
          } else if (elapsed >= prevEnd) {
            const stageDuration = stageEnd === Infinity ? 8000 : stageEnd - prevEnd;
            fill   = Math.min((elapsed - prevEnd) / stageDuration, ACTIVE_CAP);
            status = "active";
          } else {
            fill = 0; status = "pending";
          }

          return (
            <div key={stage.label} className="space-y-1">
              <div className="flex items-center justify-between">
                <span className={`text-xs font-medium ${
                  status === "pending" ? "text-gray-300" : "text-gray-700"
                }`}>
                  {stage.label}
                </span>
                <span className="text-[10px] text-gray-400 w-4 text-right">
                  {status === "done" ? "✓" : ""}
                </span>
              </div>

              <div className="h-1.5 bg-gray-100 rounded-full overflow-hidden">
                <div
                  className={`h-full rounded-full transition-all ${
                    status === "done"
                      ? "bg-green-500 duration-150"
                      : status === "active"
                      ? "bg-indigo-500 duration-75"
                      : ""
                  }`}
                  style={{ width: `${Math.round(fill * 100)}%` }}
                />
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

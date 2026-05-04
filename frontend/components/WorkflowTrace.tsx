import type { WorkflowStep } from "@/lib/types";

const STATUS_ICON: Record<string, string> = {
  completed: "✓",
  skipped:   "—",
  failed:    "✗",
};

const STATUS_COLOR: Record<string, string> = {
  completed: "bg-green-500 text-white",
  skipped:   "bg-gray-300 text-gray-600",
  failed:    "bg-red-500 text-white",
};

const NODE_LABELS: Record<string, string> = {
  classify:           "Classify",
  retrieve:           "Retrieve",
  investigate:        "Investigate",
  draft:              "Draft reply",
  await_human_review: "Await human review",
  ask_clarification:  "Ask clarification",
  escalate:           "Escalate",
  persist:            "Persist",
};

interface Props {
  steps: WorkflowStep[];
}

export function WorkflowTrace({ steps }: Props) {
  return (
    <div className="bg-white border border-gray-200 rounded-card shadow-sm p-4">
      <h4 className="text-sm font-semibold text-gray-700 mb-4">Workflow trace</h4>
      <ol className="space-y-0">
        {steps.map((step, i) => {
          const icon = STATUS_ICON[step.status] ?? "?";
          const color = STATUS_COLOR[step.status] ?? "bg-gray-200 text-gray-500";
          const isLast = i === steps.length - 1;

          return (
            <li key={i} className="flex gap-3">
              <div className="flex flex-col items-center">
                <span
                  className={`flex items-center justify-center w-6 h-6 rounded-full text-xs font-bold shrink-0 ${color}`}
                >
                  {icon}
                </span>
                {!isLast && <div className="w-0.5 bg-gray-200 flex-1 my-1" style={{ minHeight: "20px" }} />}
              </div>
              <div className="pb-4 min-w-0">
                <div className="flex items-baseline gap-2 flex-wrap">
                  <span className="text-sm font-medium text-gray-800">
                    {NODE_LABELS[step.node] ?? step.node}
                  </span>
                  {step.duration_ms != null && (
                    <span className="text-xs text-gray-400 tabular-nums">
                      {step.duration_ms} ms
                    </span>
                  )}
                </div>
                {step.output_summary && (
                  <p className="text-xs text-gray-500 mt-0.5 leading-relaxed">{step.output_summary}</p>
                )}
              </div>
            </li>
          );
        })}
      </ol>
    </div>
  );
}

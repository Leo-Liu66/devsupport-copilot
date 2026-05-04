import type { TicketClassification, Action } from "@/lib/types";

const SEV_COLORS: Record<string, string> = {
  "P1 - Critical": "bg-red-100 text-red-700 border-red-300",
  "P2 - High":     "bg-orange-100 text-orange-700 border-orange-300",
  "P3 - Medium":   "bg-blue-100 text-blue-700 border-blue-300",
  "P4 - Low":      "bg-green-100 text-green-700 border-green-300",
};

const ACTION_COLORS: Record<Action, string> = {
  auto_reply:   "bg-indigo-100 text-indigo-700 border-indigo-300",
  needs_review: "bg-amber-100 text-amber-700 border-amber-300",
  needs_info:   "bg-sky-100 text-sky-700 border-sky-300",
  escalate:     "bg-gray-100 text-gray-600 border-gray-300",
};

const ACTION_LABELS: Record<Action, string> = {
  auto_reply:   "Auto-replied",
  needs_review: "Needs review",
  needs_info:   "Needs info",
  escalate:     "Escalated",
};

interface Props {
  classification: TicketClassification;
  action: Action;
}

export function ClassificationChips({ classification, action }: Props) {
  const sevColor = SEV_COLORS[classification.severity] ?? "bg-gray-100 text-gray-600 border-gray-300";
  const actColor = ACTION_COLORS[action];

  return (
    <div className="flex flex-wrap gap-2 text-xs font-medium">
      <Chip label={classification.category} color="bg-purple-100 text-purple-700 border-purple-300" />
      <Chip label={classification.severity} color={sevColor} />
      <Chip label={ACTION_LABELS[action]} color={actColor} />
      <span className="self-center text-gray-400 text-xs">
        conf {Math.round(classification.confidence * 100)}%
      </span>
    </div>
  );
}

function Chip({ label, color }: { label: string; color: string }) {
  return (
    <span className={`inline-flex items-center px-2 py-0.5 rounded border ${color}`}>
      {label}
    </span>
  );
}

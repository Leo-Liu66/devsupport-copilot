// Hand-maintained mirror of backend/app/models/ticket.py + kb.py

export interface TicketInput {
  subject: string;
  body: string;
  user_email?: string;
}

export interface Citation {
  marker: string;        // "[1]", "[2]"
  chunk_id: string;
  source_url: string;
  source_title: string;
  excerpt: string;
}

export interface CitedAnswer {
  answer: string;        // text containing [1], [2] markers
  citations: Citation[];
  confidence: number;
  retrieval_sufficient: boolean;
}

export interface TicketClassification {
  category: string;
  severity: string;
  confidence: number;
  keywords: string[];
  needs_more_info: boolean;
}

export interface SimilarTicket {
  ticket_id: string;
  subject: string;
  similarity_score: number;
  resolution?: string;
}

export interface WorkflowStep {
  node: string;
  status: string;        // "completed" | "skipped" | "failed"
  duration_ms?: number;
  output_summary?: string;
}

export type Action = "auto_reply" | "needs_review" | "needs_info" | "escalate";

export interface TicketAnalysis {
  ticket_id: string;
  classification: TicketClassification;
  answer: CitedAnswer;
  draft_reply: string;
  action: Action;
  similar_tickets: SimilarTicket[];
  workflow_trace: WorkflowStep[];
  persisted_ticket_id?: string;
  clarification_question?: string;
}

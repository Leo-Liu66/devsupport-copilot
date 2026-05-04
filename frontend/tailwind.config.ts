import type { Config } from "tailwindcss";
import tokens from "./prototype/frozen-tokens.json";

const config: Config = {
  content: [
    "./app/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
  ],
  theme: {
    extend: {
      spacing: {
        base: `${tokens.space.base}px`,
        "card-padding": `${tokens.space.cardPadding}px`,
      },
      fontSize: {
        base: [`${tokens.fontSize.base}px`, { lineHeight: String(tokens.lineHeight.body) }],
        heading: [`${tokens.fontSize.heading}px`, { lineHeight: "1.25" }],
      },
      borderRadius: {
        card: `${tokens.radius.card}px`,
      },
      transitionDuration: {
        DEFAULT: `${tokens.transitionMs}ms`,
      },
    },
  },
  plugins: [],
};

export default config;

import path from "node:path";
import { fileURLToPath } from "node:url";
import { FlatCompat } from "@eslint/eslintrc";
import js from "@eslint/js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const compat = new FlatCompat({
  baseDirectory: __dirname,
  recommendedConfig: js.configs.recommended,
});

const tsConfigs = compat
  .config({
    root: true,
    env: {
      browser: true,
      es2022: true,
      node: true,
    },
    parser: "@typescript-eslint/parser",
    parserOptions: {
      ecmaFeatures: {
        jsx: true,
      },
      ecmaVersion: "latest",
      sourceType: "module",
      project: [path.resolve(__dirname, "tsconfig.json")],
      tsconfigRootDir: __dirname,
    },
    plugins: ["@typescript-eslint", "react", "react-hooks", "jsx-a11y"],
    extends: [
      "eslint:recommended",
      "plugin:@typescript-eslint/recommended",
      "plugin:@typescript-eslint/recommended-requiring-type-checking",
      "plugin:react/recommended",
      "plugin:react/jsx-runtime",
      "plugin:react-hooks/recommended",
      "plugin:jsx-a11y/recommended",
    ],
    settings: {
      react: {
        version: "detect",
      },
    },
    rules: {
      "react/prop-types": "off",
      "@typescript-eslint/consistent-type-imports": [
        "error",
        { fixStyle: "inline-type-imports" },
      ],
      "@typescript-eslint/explicit-module-boundary-types": "off",
      "@typescript-eslint/no-unused-vars": [
        "error",
        { argsIgnorePattern: "^_", varsIgnorePattern: "^_" },
      ],
    },
  })
  .map((config) => ({
    ...config,
    files: ["**/*.{ts,tsx}"],
  }));

const storybookConfigs = compat
  .extends("plugin:storybook/recommended")
  .map((config) => ({
    ...config,
    files: ["**/*.stories.@(ts|tsx|js|jsx)"],
  }));

export default [
  {
    ignores: ["dist", "build", "coverage", "node_modules", "storybook-static"],
  },
  ...tsConfigs,
  ...storybookConfigs,
];

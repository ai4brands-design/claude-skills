---
name: Slidev Presentation
description: Create and run developer-friendly presentations using Markdown and Vue.js.
---

# Slidev Skill

Slidev is a web-based presentation tool for developers. It uses Markdown for content and Vue.js for components.

## Prerequisites

- Node.js (v18.0.0+)
- npm or pnpm

## Setup

To create a new presentation:

1. Run the setup script: `powershell -ExecutionPolicy Bypass -File scripts/setup.ps1`
   OR
2. Run manually: `npm init slidev@latest` in your desired directory.

## Usage

- **Edit Slides**: Open `slides.md` in your editor.
- **Start Server**: Run `npm run dev` to start the local presentation server (usually at <http://localhost:3030>).
- **Export**: Run `npm run export` to generate a PDF.

## Directory Structure

- `slides.md`: The main presentation content.
- `components/`: Custom Vue components.
- `styles/`: Custom CSS.

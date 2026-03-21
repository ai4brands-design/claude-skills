---
name: antigravity-mcp-mastery
description: "Master Guide for Model Context Protocol (MCP) in Antigravity"
source: "https://antigravity.codes/blog/antigravity-mcp-tutorial"
risk: safe
---

# Antigravity MCP Mastery

## Overview

This skill encapsulates the best practices for configuring, using, and building MCP servers within the Antigravity IDE. It enables the agent to connect to databases, cloud services, and custom local tools without context switching.

## 1. Configuration (`mcp_config.json`)

To add existing servers, edit your global or project-specific `mcp_config.json`.

### Template: Supabase + Git

```json
{
  "mcpServers": {
    "supabase": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://user:password@db.supabase.co:5432/postgres" // Use env vars in production!
      ],
      "env": {
        // "PGPASSWORD": "your-password"
      }
    },
    "git-tool": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-server-git",
        "--repository",
        "/absolute/path/to/repo"
      ]
    }
  }
}
```

## 2. Building Custom MCP Servers

Use this boilerplate to create a Node.js/TypeScript server that exposes custom tools to the agent.

### Prerequisites

`npm install @modelcontextprotocol/sdk zod`

### Server Boilerplate (`src/index.ts`)

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { ListToolsRequestSchema, CallToolRequestSchema } from "@modelcontextprotocol/sdk/types.js";
import { z } from "zod";

// Initialize Server
const server = new Server(
  { name: "custom-tool-server", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

// Define Tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "check_status",
        description: "Checks system status",
        inputSchema: {
          type: "object",
          properties: {
            service: { type: "string", description: "Service name (api, db, cache)" }
          },
          required: ["service"]
        }
      }
    ]
  };
});

// Handle Tool Calls
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "check_status") {
    const service = request.params.arguments?.service;
    return {
      content: [{ type: "text", text: \`Service \${service} is OPERATIONAL\` }]
    };
  }
  throw new Error("Tool not found");
});

// Connect
const transport = new StdioServerTransport();
await server.connect(transport);
```

## 3. Best Practices

- **Least Privilege**: Only give tools access to necessary resources.
- **Trusted Workspaces**: Be cautious when running MCP servers in untrusted repositories.
- **Context Pruning**: Use specific tools rather than generic "read everything" tools to save token budget.

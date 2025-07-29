# FastMCP Framework Guide

**Source**: https://github.com/punkpeye/fastmcp/blob/main/README.md  
**Date Fetched**: July 29, 2025

## Overview

FastMCP is a TypeScript framework for building MCP (Model Context Protocol) servers capable of handling client sessions. It provides an opinionated, higher-level abstraction over the official MCP SDK, eliminating boilerplate code and providing simple, intuitive APIs for common tasks.

## Key Features

- Simple Tool, Resource, Prompt definition
- Authentication with session support
- Passing headers through context
- Image and audio content support
- Embedded resources
- Logging and error handling
- HTTP Streaming (with SSE compatibility)
- CORS (enabled by default)
- Progress notifications
- Streaming output
- Typed server events
- Prompt argument auto-completion
- Sampling
- Configurable ping behavior
- Health-check endpoint
- Roots management
- CLI for testing and debugging

## When to Use FastMCP vs Official SDK

FastMCP is built **on top of the official SDK** and eliminates complexity by:

- Handling all boilerplate automatically
- Providing simple, intuitive APIs for common tasks
- Including built-in best practices and error handling
- Letting you focus on your MCP's core functionality

**Choose FastMCP when**: You want to build MCP servers quickly without dealing with low-level implementation details.

**Use the official SDK when**: You need maximum control or have specific architectural requirements.

## Installation

```bash
npm install fastmcp
```

## Quick Start

```typescript
import { FastMCP } from "fastmcp";
import { z } from "zod"; // Or any validation library that supports Standard Schema

const server = new FastMCP({
  name: "My Server",
  version: "1.0.0",
});

server.addTool({
  name: "add",
  description: "Add two numbers",
  parameters: z.object({
    a: z.number(),
    b: z.number(),
  }),
  execute: async (args) => {
    return String(args.a + args.b);
  },
});

server.start({
  transportType: "stdio",
});
```

## Core Concepts

### Tools

Tools expose executable functions that can be invoked by clients and used by LLMs. FastMCP uses the Standard Schema specification for defining tool parameters, supporting Zod, ArkType, and Valibot.

**Basic Tool Example:**
```typescript
server.addTool({
  name: "fetch-content",
  description: "Fetch content from a URL",
  parameters: z.object({
    url: z.string(),
  }),
  execute: async (args) => {
    return await fetchWebpageContent(args.url);
  },
});
```

**Tool Authorization:**
```typescript
server.addTool({
  name: "admin-tool",
  description: "An admin-only tool",
  canAccess: (auth) => auth?.role === "admin",
  execute: async () => "Welcome, admin!",
});
```

**Tool Annotations:**
```typescript
server.addTool({
  name: "fetch-content",
  description: "Fetch content from a URL",
  parameters: z.object({
    url: z.string(),
  }),
  annotations: {
    title: "Web Content Fetcher",
    readOnlyHint: true,
    openWorldHint: true,
  },
  execute: async (args) => {
    return await fetchWebpageContent(args.url);
  },
});
```

### Resources

Resources represent any kind of data that an MCP server wants to make available to clients:

```typescript
server.addResource({
  uri: "file:///logs/app.log",
  name: "Application Logs",
  mimeType: "text/plain",
  async load() {
    return {
      text: await readLogFile(),
    };
  },
});
```

**Resource Templates:**
```typescript
server.addResourceTemplate({
  uriTemplate: "file:///logs/{name}.log",
  name: "Application Logs",
  mimeType: "text/plain",
  arguments: [
    {
      name: "name",
      description: "Name of the log",
      required: true,
    },
  ],
  async load({ name }) {
    return {
      text: `Example log content for ${name}`,
    };
  },
});
```

### Prompts

Prompts enable servers to define reusable prompt templates and workflows:

```typescript
server.addPrompt({
  name: "git-commit",
  description: "Generate a Git commit message",
  arguments: [
    {
      name: "changes",
      description: "Git diff or description of changes",
      required: true,
    },
  ],
  load: async (args) => {
    return `Generate a concise but descriptive commit message for these changes:\n\n${args.changes}`;
  },
});
```

### Content Types

**Image Content:**
```typescript
import { imageContent } from "fastmcp";

server.addTool({
  name: "get-image",
  execute: async (args) => {
    return imageContent({
      url: "https://example.com/image.png",
      // or path: "/path/to/image.png",
      // or buffer: Buffer.from("base64data", "base64"),
    });
  },
});
```

**Audio Content:**
```typescript
import { audioContent } from "fastmcp";

server.addTool({
  name: "get-audio",
  execute: async (args) => {
    return audioContent({
      url: "https://example.com/audio.mp3",
    });
  },
});
```

### Streaming Output

FastMCP supports streaming partial results from tools while they're executing:

```typescript
server.addTool({
  name: "generateText",
  description: "Generate text incrementally",
  parameters: z.object({
    prompt: z.string(),
  }),
  annotations: {
    streamingHint: true,
    readOnlyHint: true,
  },
  execute: async (args, { streamContent }) => {
    await streamContent({ type: "text", text: "Starting generation...\n" });
    
    const words = "The quick brown fox jumps over the lazy dog.".split(" ");
    for (const word of words) {
      await streamContent({ type: "text", text: word + " " });
      await new Promise((resolve) => setTimeout(resolve, 300));
    }
    
    return; // or return final content to append
  },
});
```

## Transport Options

### stdio (Default)
```typescript
server.start({
  transportType: "stdio",
});
```

### HTTP Streaming
```typescript
server.start({
  transportType: "httpStream",
  httpStream: {
    port: 8080,
  },
});
```

### Server-Sent Events (SSE)
```typescript
server.start({
  transportType: "sse",
  sse: {
    port: 8080,
  },
});
```

## Authentication

FastMCP supports session-based authentication:

```typescript
const server = new FastMCP({
  name: "My Server",
  version: "1.0.0",
  authenticate: (request) => {
    const apiKey = request.headers["x-api-key"];
    
    if (apiKey !== "123") {
      throw new Response(null, {
        status: 401,
        statusText: "Unauthorized",
      });
    }
    
    return {
      id: 1,
      role: "user",
    };
  },
});
```

### OAuth Support

FastMCP includes built-in OAuth discovery endpoints compliant with RFC 8414 and RFC 9470:

```typescript
const server = new FastMCP({
  name: "My Server",
  version: "1.0.0",
  oauth: {
    enabled: true,
    authorizationServer: {
      issuer: "https://auth.example.com",
      authorizationEndpoint: "https://auth.example.com/oauth/authorize",
      tokenEndpoint: "https://auth.example.com/oauth/token",
      jwksUri: "https://auth.example.com/.well-known/jwks.json",
      responseTypesSupported: ["code"],
    },
    protectedResource: {
      resource: "mcp://my-server",
      authorizationServers: ["https://auth.example.com"],
    },
  },
  authenticate: async (request) => {
    // JWT token validation logic
  },
});
```

## Advanced Features

### Progress Reporting
```typescript
server.addTool({
  name: "long-task",
  execute: async (args, { reportProgress }) => {
    await reportProgress({
      progress: 0,
      total: 100,
    });
    
    // ... do work ...
    
    await reportProgress({
      progress: 100,
      total: 100,
    });
    
    return "done";
  },
});
```

### Logging
```typescript
server.addTool({
  name: "my-tool",
  execute: async (args, { log }) => {
    log.info("Starting task...", { args });
    log.error("Something went wrong", { error: "details" });
    return "result";
  },
});
```

### Error Handling
```typescript
import { UserError } from "fastmcp";

server.addTool({
  name: "my-tool",
  execute: async (args) => {
    if (args.invalid) {
      throw new UserError("This input is not allowed");
    }
    return "success";
  },
});
```

## Testing and Development

### CLI Testing
```bash
npx fastmcp dev server.ts
```

### MCP Inspector
```bash
npx fastmcp inspect server.ts
```

### Claude Desktop Integration
Add to Claude Desktop configuration:
```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "npx",
      "args": ["tsx", "/PATH/TO/YOUR_PROJECT/src/index.ts"],
      "env": {
        "YOUR_ENV_VAR": "value"
      }
    }
  }
}
```

## Official SDK Information

The **official MCP SDK** is referenced throughout the FastMCP documentation as the foundational building blocks that FastMCP is built upon. Based on the documentation, the official SDK can be found at:

**Official MCP SDK Locations:**
- Client transports: `@modelcontextprotocol/sdk/client/streamableHttp.js`
- SSE transport: `@modelcontextprotocol/sdk/client/sse.js`
- Client: `@modelcontextprotocol/sdk/client/index.js`

**Key differences:**
- **Official SDK**: Provides foundational blocks but requires handling connection management, tool handling, response handling, resource management, etc.
- **FastMCP**: Eliminates this complexity by providing an opinionated framework with built-in best practices

The official SDK appears to be the `@modelcontextprotocol/sdk` npm package, which provides the low-level MCP protocol implementation that FastMCP abstracts over.

## Showcase Projects

Notable projects built with FastMCP include:
- Computer control MCP
- Dradis vulnerability management
- Meeting transcription tools
- Unsplash photo search
- HaloPSA workflows integration
- Discogs music collection interface
- And many more...

## Conclusion

FastMCP significantly simplifies MCP server development by providing a high-level, opinionated framework over the official SDK. It's ideal for developers who want to quickly build robust MCP servers without dealing with low-level protocol implementation details.

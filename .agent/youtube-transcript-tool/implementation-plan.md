# YouTube Transcript MCP Tool - Implementation Plan

## Folder Organization

### Project Code Location
- **Project Folder:** `tools\youtube-transcript-tool`
  - Contains all implementation code (main.py, transcript_handler.py, etc.)
  - Used as the root directory for the MCP tool codebase
  - All production files and dependencies

### Agent Status & Reports Location  
- **Agent Folder:** `.agent\youtube-transcript-tool`
  - Contains project management and status files
  - Progress reports, completion summaries, validation reports
  - All status files prefixed with underscore (e.g., `_progress-report.md`, `_completion-summary.md`, `_validation-report.md`)
  - Implementation plan and requirements documentation

## Overview
Create a lightweight Python MCP (Model Context Protocol) server that enables downloading YouTube video transcripts for AI assistant integration.

## Project Structure
```
tools/youtube-transcript-tool/          # Main project code
├── main.py                             # MCP server entry point
├── transcript_handler.py               # Core transcript logic
├── requirements.txt                    # Dependencies
└── README.md                          # Usage documentation

.agent/youtube-transcript-tool/         # Project management & status
├── implementation-plan.md              # This implementation plan
├── requirements.md                     # Original requirements
├── _progress-report.md                 # Implementation progress
├── _completion-summary.md              # Final completion report
└── _validation-report.md               # Testing & validation results
```

## Required Dependencies
- `youtube-transcript-api` - For fetching YouTube transcripts
- `mcp` - Model Context Protocol server implementation
- Built-in modules: `asyncio`, `json`, `logging`, `re`, `urllib.parse`

## Implementation Steps

### 1. Create main.py (MCP Server Entry Point)
- Initialize MCP server with stdio transport (default for local usage)
- Define tool schema for YouTube transcript extraction
- Handle server lifecycle and error management
- Expose `get_youtube_transcript` tool to MCP clients
- Support standard MCP command line arguments (--stdio, --port, --help)
- Include proper error logging and graceful shutdown

### 2. Create transcript_handler.py (Core Logic)
- Implement `extract_video_id()` function to parse YouTube URLs
- Create `get_transcript()` function using youtube-transcript-api
- Add `format_transcript_data()` for structured output
- Include error handling for common failure cases

### 3. Tool Interface Design
**Tool Name:** `get_youtube_transcript`
**Parameters:**
- `video_url` (required): YouTube video URL or ID
- `language` (optional): Preferred transcript language (default: auto-detect)
- `format` (optional): Output format - "text" or "structured" (default: "structured")

**Output Format:**
```json
{
  "video_id": "string",
  "title": "string", 
  "language": "string",
  "transcript": [
    {
      "text": "string",
      "start": "float",
      "duration": "float"
    }
  ],
  "plain_text": "string"
}
```

### 4. Error Handling
- Invalid YouTube URLs → Clear error message
- No transcript available → Informative response
- Private/restricted videos → Appropriate error
- Network issues → Retry mechanism
- Rate limiting → Graceful degradation

### 5. Key Implementation Features
- Support both youtube.com and youtu.be URL formats
- Extract video ID from various YouTube URL patterns
- Handle multiple transcript languages when available
- Provide both timestamped and plain text formats
- Minimal memory footprint and fast response times

## Installation & Dependencies
```bash
pip install youtube-transcript-api mcp
```

## MCP Workspace Configuration

### MCP Client Configuration File
Create or update `.mcp/config.json` in the workspace root:
```json
{
  "mcpServers": {
    "youtube-transcript": {
      "command": "python",
      "args": ["${workspaceFolder}/tools/youtube-transcript-tool/main.py"],
      "env": {},
      "description": "YouTube transcript extraction tool"
    }
  }
}
```

### Alternative Configuration (VSCode Settings)
If using VSCode with MCP extension, add to `.vscode/settings.json`:
```json
{
  "mcp.servers": {
    "youtube-transcript": {
      "command": "python",
      "args": ["${workspaceFolder}/tools/youtube-transcript-tool/main.py"],
      "cwd": "${workspaceFolder}/tools/youtube-transcript-tool"
    }
  }
}
```

### Environment Setup
1. Ensure Python is in system PATH
2. Install dependencies globally: `pip install youtube-transcript-api mcp`
3. Make main.py executable and add proper shebang for cross-platform compatibility
4. Test MCP server startup: `python main.py --test`

### MCP Server Arguments
The main.py should accept standard MCP arguments:
- `--stdio` - Use stdio transport (default)
- `--port <number>` - TCP transport on specified port
- `--help` - Display usage information

## Usage Integration
The MCP server will expose the transcript tool to compatible AI assistants, enabling natural language requests like:
- "Get the transcript from this YouTube video"
- "Extract transcript in Spanish if available"
- "Download transcript as plain text"

## Performance Targets
- Server startup: < 2 seconds
- Transcript retrieval: < 5 seconds per video
- Memory usage: < 50MB during operation
- Support for concurrent requests via asyncio

## Next Steps
1. Create project code directory: `tools/youtube-transcript-tool/`
2. Implement main.py with MCP server setup in project folder
3. Create transcript_handler.py with core logic in project folder
4. Add comprehensive error handling
5. Create requirements.txt and README.md in project folder
6. Set up MCP workspace configuration files
7. Create `_progress-report.md` in agent folder to track implementation status
8. Test MCP server connectivity and tool registration
9. Validate with various YouTube video types and scenarios
10. Generate `_completion-summary.md` and `_validation-report.md` in agent folder

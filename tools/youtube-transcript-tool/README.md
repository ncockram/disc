# YouTube Transcript MCP Tool

A Model Context Protocol (MCP) server that enables AI assistants to extract transcripts from YouTube videos. Supports both timestamped and plain text formats with automatic language detection.

## Features

- **Multiple URL Formats**: Supports youtube.com, youtu.be, and direct video IDs
- **Language Support**: Auto-detects best available language or use specific language codes
- **Flexible Output**: Choose between structured (with timestamps) or plain text format
- **Error Handling**: Comprehensive error handling for common scenarios
- **API Key Support**: Optional YouTube Data API key for enhanced features
- **MCP Integration**: Full Model Context Protocol compatibility

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. (Optional) Get a YouTube Data API key:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a project and enable YouTube Data API v3
   - Create an API key credential

## Usage

### As MCP Server

Configure in your MCP client (e.g., `.mcp/config.json`):

```json
{
  "mcpServers": {
    "youtube-transcript": {
      "command": "python",
      "args": ["path/to/tools/youtube-transcript-tool/main.py"],
      "env": {
        "YOUTUBE_API_KEY": "your-api-key-here"
      },
      "description": "YouTube transcript extraction tool"
    }
  }
}
```

### Command Line Testing

Test the server:
```bash
python main.py --test
```

Run with API key:
```bash
python main.py --api-key YOUR_API_KEY
```

### Tool Usage

The MCP server exposes the `get_youtube_transcript` tool with these parameters:

- **video_url** (required): YouTube video URL or video ID
- **language** (optional): Language code (e.g., 'en', 'es', 'fr')
- **format** (optional): "structured" (default) or "text"

#### Example Requests

**Structured output with timestamps:**
```json
{
  "tool": "get_youtube_transcript",
  "arguments": {
    "video_url": "https://youtube.com/watch?v=dQw4w9WgXcQ",
    "format": "structured"
  }
}
```

**Plain text output in Spanish:**
```json
{
  "tool": "get_youtube_transcript",
  "arguments": {
    "video_url": "dQw4w9WgXcQ",
    "language": "es",
    "format": "text"
  }
}
```

## Output Format

### Structured Format
```json
{
  "video_id": "dQw4w9WgXcQ",
  "language": "en",
  "is_generated": false,
  "transcript": [
    {
      "text": "We're no strangers to love",
      "start": 0.0,
      "duration": 2.5
    }
  ],
  "plain_text": "We're no strangers to love...",
  "status": "success",
  "total_segments": 150,
  "duration_seconds": 212.0
}
```

### Text Format
```json
{
  "video_id": "dQw4w9WgXcQ",
  "language": "en",
  "is_generated": false,
  "text": "We're no strangers to love...",
  "status": "success"
}
```

### Error Format
```json
{
  "error": "No transcript found for this video",
  "video_id": "dQw4w9WgXcQ",
  "status": "no_transcript"
}
```

## Error Handling

The tool handles various error conditions:

- **invalid_input**: Invalid YouTube URL or video ID
- **no_transcript**: No transcript available for the video
- **transcripts_disabled**: Transcripts disabled for the video
- **video_unavailable**: Video is private or unavailable
- **rate_limited**: API rate limit exceeded
- **server_error**: Internal server error

## Configuration

### Environment Variables

- `YOUTUBE_API_KEY`: YouTube Data API key (optional)

### MCP Configuration

You can pass the API key through MCP server configuration:

```json
{
  "mcpServers": {
    "youtube-transcript": {
      "command": "python",
      "args": ["main.py", "--api-key", "${YOUTUBE_API_KEY}"],
      "env": {
        "YOUTUBE_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## Supported URL Formats

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://youtube.com/watch?v=VIDEO_ID`
- `https://m.youtube.com/watch?v=VIDEO_ID`
- `VIDEO_ID` (direct video ID)

## Limitations

- Requires videos to have available transcripts (auto-generated or manual)
- Subject to YouTube's rate limiting
- Private videos require authentication (not currently supported)
- Some videos may have transcripts disabled by the uploader

## Development

### Project Structure
```
tools/youtube-transcript-tool/
├── main.py                 # MCP server entry point
├── transcript_handler.py   # Core transcript logic
├── requirements.txt        # Dependencies
└── README.md              # This file
```

### Testing
```bash
# Test server startup
python main.py --test

# Test with debug logging
python main.py --log-level DEBUG --test
```

## License

This project is part of a larger research and development workspace.

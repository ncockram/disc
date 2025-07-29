#!/usr/bin/env python3
"""
YouTube Transcript MCP Server

A Model Context Protocol server that provides YouTube video transcript extraction capabilities.
Supports both timestamped and plain text transcript formats.
"""

import asyncio
import json
import logging
import sys
from typing import Any, Sequence
import argparse

from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    CallToolRequest,
    CallToolResult,
    ListToolsRequest,
    TextContent,
    Tool,
)

from transcript_handler import get_youtube_transcript

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the MCP server instance
server = Server("youtube-transcript")

# Global configuration to store API key and other settings
config = {
    "api_key": None
}


@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    """
    List available tools.
    """
    return [
        Tool(
            name="get_youtube_transcript",
            description="Extract transcript/captions from YouTube videos. Supports various URL formats and provides both timestamped and plain text output.",
            inputSchema={
                "type": "object",
                "properties": {
                    "video_url": {
                        "type": "string",
                        "description": "YouTube video URL or video ID (e.g., 'https://youtube.com/watch?v=VIDEO_ID' or 'VIDEO_ID')"
                    },
                    "language": {
                        "type": "string",
                        "description": "Preferred transcript language code (e.g., 'en', 'es', 'fr'). If not specified, auto-detects best available language.",
                        "default": None
                    },
                    "format": {
                        "type": "string",
                        "enum": ["structured", "text"],
                        "description": "Output format: 'structured' includes timestamps and metadata, 'text' returns plain text only",
                        "default": "structured"
                    }
                },
                "required": ["video_url"]
            }
        )
    ]


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[TextContent]:
    """
    Handle tool execution requests.
    """
    if name == "get_youtube_transcript":
        try:
            # Extract parameters
            video_url = arguments.get("video_url")
            language = arguments.get("language")
            format_type = arguments.get("format", "structured")
            
            if not video_url:
                return [TextContent(
                    type="text",
                    text=json.dumps({
                        "error": "video_url parameter is required",
                        "status": "invalid_request"
                    }, indent=2)
                )]
            
            # Get transcript using the API key from configuration
            result = get_youtube_transcript(
                video_url=video_url,
                language=language,
                format_type=format_type,
                api_key=config.get("api_key")
            )
            
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]
            
        except Exception as e:
            logger.error(f"Error in get_youtube_transcript: {e}")
            return [TextContent(
                type="text",
                text=json.dumps({
                    "error": f"Internal server error: {str(e)}",
                    "status": "server_error"
                }, indent=2)
            )]
    else:
        return [TextContent(
            type="text",
            text=json.dumps({
                "error": f"Unknown tool: {name}",
                "status": "unknown_tool"
            }, indent=2)
        )]


async def run_server():
    """
    Run the MCP server with stdio transport.
    """
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="youtube-transcript",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                )
            )
        )


def parse_arguments():
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description="YouTube Transcript MCP Server")
    parser.add_argument(
        "--stdio", 
        action="store_true", 
        default=True,
        help="Use stdio transport (default)"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        help="YouTube Data API key for enhanced features (optional)"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run a simple test to verify server startup"
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Set logging level"
    )
    
    return parser.parse_args()


def setup_logging(level: str):
    """
    Configure logging based on the specified level.
    """
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {level}')
    
    logging.basicConfig(
        level=numeric_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


async def test_server():
    """
    Simple test to verify server can start and list tools.
    """
    try:
        tools = await handle_list_tools()
        print("✓ Server startup successful")
        print(f"✓ Available tools: {len(tools)}")
        for tool in tools:
            print(f"  - {tool.name}: {tool.description}")
        return True
    except Exception as e:
        print(f"✗ Server test failed: {e}")
        return False


def main():
    """
    Main entry point for the MCP server.
    """
    args = parse_arguments()
    
    # Setup logging
    setup_logging(args.log_level)
    
    # Store API key in global config if provided
    if args.api_key:
        config["api_key"] = args.api_key
        logger.info("API key configured")
    
    # Run test mode if requested
    if args.test:
        success = asyncio.run(test_server())
        sys.exit(0 if success else 1)
    
    # Start the server
    logger.info("Starting YouTube Transcript MCP Server...")
    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        logger.info("Server shutdown requested")
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

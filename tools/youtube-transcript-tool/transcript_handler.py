"""
Core transcript handling logic for YouTube video transcripts.
"""

import re
import logging
from urllib.parse import urlparse, parse_qs
from typing import Optional, Dict, List, Any
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled, 
    NoTranscriptFound, 
    VideoUnavailable
)

logger = logging.getLogger(__name__)


def extract_video_id(url_or_id: str) -> Optional[str]:
    """
    Extract YouTube video ID from various URL formats or return ID if already provided.
    
    Supports:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://youtube.com/watch?v=VIDEO_ID
    - https://m.youtube.com/watch?v=VIDEO_ID
    - VIDEO_ID (direct ID)
    """
    if not url_or_id:
        return None
    
    # If it's already just a video ID (11 characters, alphanumeric)
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url_or_id):
        return url_or_id
    
    # Parse URL patterns
    patterns = [
        r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})',
        r'youtube\.com/watch\?.*v=([a-zA-Z0-9_-]{11})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    
    # Try parsing as URL
    try:
        parsed = urlparse(url_or_id)
        if 'youtube.com' in parsed.netloc or 'youtu.be' in parsed.netloc:
            if 'youtu.be' in parsed.netloc:
                return parsed.path.lstrip('/')
            elif 'youtube.com' in parsed.netloc:
                query_params = parse_qs(parsed.query)
                if 'v' in query_params:
                    return query_params['v'][0]
    except Exception as e:
        logger.warning(f"Failed to parse URL {url_or_id}: {e}")
    
    return None


def get_transcript(video_id: str, language: Optional[str] = None, api_key: Optional[str] = None) -> Dict[str, Any]:
    """
    Fetch transcript for a YouTube video using the instance approach.
    
    Args:
        video_id: YouTube video ID
        language: Preferred language code (e.g., 'en', 'es', 'fr')
        api_key: YouTube Data API key (optional, for enhanced features)
    
    Returns:
        Dictionary containing transcript data and metadata
    """
    try:
        # Create API instance
        api = YouTubeTranscriptApi()
        
        # Try to get transcript with language preference
        if language:
            try:
                transcript_data = api.fetch(video_id, languages=[language])
                selected_language = language
                is_generated = False
            except Exception:
                # Fall back to auto-detect
                transcript_data = api.fetch(video_id)
                selected_language = 'auto-detected'
                is_generated = True
        else:
            transcript_data = api.fetch(video_id)
            selected_language = 'auto-detected'
            is_generated = True
        
        # Format the response - extract the transcript list from the FetchedTranscript object
        return format_transcript_data(video_id, list(transcript_data), selected_language, is_generated)
        
    except TranscriptsDisabled:
        return {
            "error": "Transcripts are disabled for this video",
            "video_id": video_id,
            "status": "transcripts_disabled"
        }
    except NoTranscriptFound:
        return {
            "error": "No transcript found for this video",
            "video_id": video_id,
            "status": "no_transcript"
        }
    except VideoUnavailable:
        return {
            "error": "Video is unavailable or private",
            "video_id": video_id,
            "status": "video_unavailable"
        }
    except Exception as e:
        # Handle rate limiting and other exceptions
        error_msg = str(e).lower()
        if "too many requests" in error_msg or "rate limit" in error_msg:
            return {
                "error": "Rate limit exceeded. Please try again later.",
                "video_id": video_id,
                "status": "rate_limited"
            }
        logger.error(f"Unexpected error fetching transcript for {video_id}: {e}")
        return {
            "error": f"Unexpected error: {str(e)}",
            "video_id": video_id,
            "status": "error"
        }


def format_transcript_data(video_id: str, transcript_data: Any, language: str, is_generated: bool) -> Dict[str, Any]:
    """
    Format transcript data into a structured response.
    
    Args:
        video_id: YouTube video ID
        transcript_data: Raw transcript data from API (FetchedTranscriptSnippet objects or dicts)
        language: Language code of the transcript
        is_generated: Whether transcript is auto-generated
    
    Returns:
        Formatted transcript dictionary
    """
    # Create structured transcript with timestamps
    structured_transcript = []
    plain_text_parts = []
    
    for entry in transcript_data:
        # Handle both FetchedTranscriptSnippet objects and dict entries
        if hasattr(entry, 'text'):
            # FetchedTranscriptSnippet object
            text = entry.text.strip()
            start = round(entry.start, 2)
            duration = round(entry.duration, 2)
        else:
            # Dict entry (fallback)
            text = entry["text"].strip()
            start = round(entry["start"], 2)
            duration = round(entry["duration"], 2)
        
        structured_entry = {
            "text": text,
            "start": start,
            "duration": duration
        }
        structured_transcript.append(structured_entry)
        plain_text_parts.append(text)
    
    # Join all text for plain text version
    plain_text = " ".join(plain_text_parts)
    
    return {
        "video_id": video_id,
        "language": language,
        "is_generated": is_generated,
        "transcript": structured_transcript,
        "plain_text": plain_text,
        "status": "success",
        "total_segments": len(structured_transcript),
        "duration_seconds": structured_transcript[-1]["start"] + structured_transcript[-1]["duration"] if structured_transcript else 0
    }


def get_youtube_transcript(video_url: str, language: Optional[str] = None, format_type: str = "structured", api_key: Optional[str] = None) -> Dict[str, Any]:
    """
    Main function to get YouTube transcript from URL or video ID.
    
    Args:
        video_url: YouTube video URL or video ID
        language: Preferred transcript language (optional)
        format_type: Output format - "text" or "structured"
        api_key: YouTube Data API key (optional)
    
    Returns:
        Transcript data in requested format
    """
    # Extract video ID
    video_id = extract_video_id(video_url)
    if not video_id:
        return {
            "error": "Invalid YouTube URL or video ID",
            "input": video_url,
            "status": "invalid_input"
        }
    
    # Get transcript
    result = get_transcript(video_id, language, api_key)
    
    # If there was an error, return as-is
    if "error" in result:
        return result
    
    # Format based on requested type
    if format_type == "text":
        return {
            "video_id": video_id,
            "language": result["language"],
            "is_generated": result["is_generated"],
            "text": result["plain_text"],
            "status": "success"
        }
    else:
        return result

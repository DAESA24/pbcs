"""
Audio extraction wrapper for transcription pipeline.

STATUS: STUB - Not yet implemented

Usage:
    python extract_audio.py <url>
    python extract_audio.py <url> --format wav --quality 192

Expected functionality:
    - Extract audio in various formats (mp3, wav, flac)
    - Quality/bitrate control
    - Optimized for speech transcription
"""

import sys


def main():
    print("ERROR: extract_audio.py is a stub - not yet implemented", file=sys.stderr)
    print("   Use: download_youtube.py --audio-only <url>", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()

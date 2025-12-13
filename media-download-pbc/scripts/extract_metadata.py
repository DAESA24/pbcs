"""
Extract metadata JSON without downloading media.

STATUS: STUB - Not yet implemented

Usage:
    python extract_metadata.py <url>
    python extract_metadata.py <url> --output metadata.json

Expected functionality:
    - Extract full metadata from URL
    - Output JSON to stdout or file
    - Support for playlists (list all video metadata)
"""

import sys


def main():
    print("ERROR: extract_metadata.py is a stub - not yet implemented", file=sys.stderr)
    print("   Use: download_youtube.py --metadata-only <url>", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()

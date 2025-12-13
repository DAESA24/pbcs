"""
Download YouTube videos with metadata extraction.

Full-featured YouTube download script with format selection, playlist support,
and metadata JSON output for RAG pipeline integration.

Usage:
    python download_youtube.py <url> [options]

Examples:
    python download_youtube.py https://youtube.com/watch?v=VIDEO_ID
    python download_youtube.py https://youtube.com/watch?v=VIDEO_ID --audio-only
    python download_youtube.py https://youtube.com/watch?v=VIDEO_ID --metadata-only
    python download_youtube.py https://youtube.com/playlist?list=PLAYLIST_ID --playlist
"""

import argparse
import json
import sys
from pathlib import Path

from yt_dlp import YoutubeDL


# Default output directory
DEFAULT_OUTPUT_DIR = Path(__file__).parent.parent / "downloads"


def get_base_opts(output_dir: Path, write_metadata: bool = True) -> dict:
    """Get base yt-dlp options."""
    opts = {
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "restrictfilenames": False,
        "windowsfilenames": True,
        "quiet": False,
        "no_warnings": False,
    }

    if write_metadata:
        opts["writeinfojson"] = True

    return opts


def download_video(
    url: str,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    audio_only: bool = False,
    max_resolution: int = None,
    write_metadata: bool = True,
) -> dict:
    """
    Download a video with optional format constraints.

    Args:
        url: YouTube video URL
        output_dir: Directory to save files
        audio_only: If True, extract audio only as mp3
        max_resolution: Max video height (e.g., 720, 1080)
        write_metadata: Write .info.json sidecar file

    Returns:
        dict with download info (title, filename, etc.)
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    opts = get_base_opts(output_dir, write_metadata)

    if audio_only:
        opts.update({
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "0",
            }, {
                "key": "FFmpegMetadata",
                "add_metadata": True,
            }, {
                "key": "EmbedThumbnail",
            }],
            "writethumbnail": True,
        })
    elif max_resolution:
        opts["format"] = f"bestvideo[height<={max_resolution}]+bestaudio/best[height<={max_resolution}]"
        opts["merge_output_format"] = "mp4"
    else:
        opts["format"] = "bestvideo+bestaudio/best"
        opts["merge_output_format"] = "mp4"

    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)

        return {
            "title": info.get("title"),
            "id": info.get("id"),
            "duration": info.get("duration"),
            "uploader": info.get("uploader"),
            "upload_date": info.get("upload_date"),
            "view_count": info.get("view_count"),
            "description": info.get("description", "")[:500],
            "output_dir": str(output_dir),
        }


def extract_metadata(url: str, output_dir: Path = DEFAULT_OUTPUT_DIR) -> dict:
    """
    Extract metadata without downloading.

    Args:
        url: YouTube video URL
        output_dir: Directory to save .info.json

    Returns:
        Full metadata dict
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    opts = {
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "writeinfojson": True,
        "skip_download": True,
        "quiet": True,
    }

    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)

        # Write JSON manually for metadata-only mode
        json_path = output_dir / f"{info.get('title', 'video')}.info.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(info, f, indent=2, ensure_ascii=False)

        return info


def download_playlist(
    url: str,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    audio_only: bool = False,
) -> list:
    """
    Download all videos in a playlist.

    Args:
        url: YouTube playlist URL
        output_dir: Directory to save files
        audio_only: If True, extract audio only

    Returns:
        List of download info dicts
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    opts = get_base_opts(output_dir)
    opts["ignoreerrors"] = True

    if audio_only:
        opts.update({
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "0",
            }],
        })
    else:
        opts["format"] = "bestvideo+bestaudio/best"
        opts["merge_output_format"] = "mp4"

    results = []

    with YoutubeDL(opts) as ydl:
        playlist_info = ydl.extract_info(url, download=True)

        if "entries" in playlist_info:
            for entry in playlist_info["entries"]:
                if entry:
                    results.append({
                        "title": entry.get("title"),
                        "id": entry.get("id"),
                        "duration": entry.get("duration"),
                    })

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Download YouTube videos with metadata extraction"
    )
    parser.add_argument(
        "url",
        help="YouTube video or playlist URL"
    )
    parser.add_argument(
        "-o", "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Output directory (default: {DEFAULT_OUTPUT_DIR})"
    )
    parser.add_argument(
        "--audio-only",
        action="store_true",
        help="Extract audio only as mp3"
    )
    parser.add_argument(
        "--metadata-only",
        action="store_true",
        help="Extract metadata JSON without downloading"
    )
    parser.add_argument(
        "--max-resolution",
        type=int,
        choices=[480, 720, 1080, 1440, 2160],
        help="Maximum video resolution"
    )
    parser.add_argument(
        "--playlist",
        action="store_true",
        help="Download entire playlist"
    )
    parser.add_argument(
        "--no-metadata",
        action="store_true",
        help="Don't write .info.json sidecar file"
    )

    args = parser.parse_args()

    try:
        if args.metadata_only:
            print(f"Extracting metadata from: {args.url}", file=sys.stderr)
            info = extract_metadata(args.url, args.output_dir)
            print(f"SUCCESS: Metadata extracted: {info.get('title')}", file=sys.stderr)
            print(f"   Duration: {info.get('duration')}s", file=sys.stderr)
            print(f"   Uploader: {info.get('uploader')}", file=sys.stderr)
            print(f"   Views: {info.get('view_count')}", file=sys.stderr)
            print(json.dumps(info, indent=2))

        elif args.playlist:
            print(f"Downloading playlist: {args.url}", file=sys.stderr)
            results = download_playlist(args.url, args.output_dir, args.audio_only)
            print(f"SUCCESS: Downloaded {len(results)} videos", file=sys.stderr)
            for r in results:
                print(f"   - {r['title']}", file=sys.stderr)

        else:
            print(f"Downloading: {args.url}", file=sys.stderr)
            info = download_video(
                args.url,
                args.output_dir,
                audio_only=args.audio_only,
                max_resolution=args.max_resolution,
                write_metadata=not args.no_metadata,
            )
            print(f"SUCCESS: Downloaded: {info['title']}", file=sys.stderr)
            print(f"   Duration: {info['duration']}s", file=sys.stderr)
            print(f"   Output: {info['output_dir']}", file=sys.stderr)

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

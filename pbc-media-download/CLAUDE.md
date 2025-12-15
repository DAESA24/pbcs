# Media Download PBC - Claude Instructions

## When to Use This PBC

Use this PBC when the user needs to:

- Download video or audio from YouTube or other supported sites
- Extract audio from video content
- Get metadata from online videos
- Batch download multiple URLs
- Process media for the RAG pipeline (transcription workflow)

## Quick Reference

**Global CLI (simple tasks):**

```bash
yt-dlp https://youtube.com/watch?v=VIDEO_ID
```

**PBC venv (Python scripts):**

```bash
/c/Users/drewa/pbcs/pbc-media-download/.venv/Scripts/python.exe script.py
```

## Common CLI Commands

| Task | Command |
|------|---------|
| Download video (best quality) | `yt-dlp <url>` |
| Download audio only | `yt-dlp -x --audio-format mp3 <url>` |
| List available formats | `yt-dlp -F <url>` |
| Download specific format | `yt-dlp -f <format_id> <url>` |
| Get metadata only | `yt-dlp --dump-json <url>` |
| Download with metadata file | `yt-dlp --write-info-json <url>` |

## Config Presets

Use config presets for common operations:

```bash
yt-dlp --config-location /c/Users/drewa/pbcs/pbc-media-download/configs/audio-only.conf <url>
```

Available presets:

- `audio-only.conf` - Extract best audio as mp3
- `video-720p.conf` - Video capped at 720p
- `video-1080p.conf` - Video capped at 1080p
- `metadata-only.conf` - Extract metadata JSON, no download

## Scripts Inventory

Check `pbc-definition.yaml` for available scripts and their status.

| Script | Status | Description |
|--------|--------|-------------|
| `download_youtube.py` | Active | Full YouTube download with metadata |
| `batch_download.py` | Stub | Download from URL list file |
| `extract_metadata.py` | Stub | Get metadata JSON without downloading |
| `extract_audio.py` | Stub | Audio extraction wrapper |

## Default Output Location

**Global Default:** Downloaded files go to: `/c/Users/drewa/pbcs/pbc-media-download/downloads/`

The global yt-dlp configuration (at `%APPDATA%\yt-dlp\config.txt`) is configured to use this directory by default. This means:

```bash
# Automatically downloads to PBC downloads folder
yt-dlp <url>
```

Override with `-o` flag or `--output` in scripts:

```bash
# Download to different location
yt-dlp -o "/some/other/path/%(title)s.%(ext)s" <url>
```

**Global Config Details:**
- Location: `C:\Users\drewa\AppData\Roaming\yt-dlp\config.txt`
- Writes metadata JSON files automatically
- Embeds metadata and thumbnails by default
- Downloads best quality (bestvideo+bestaudio/best)

## Constraints

- **Fair use only** - Only download content you have rights to
- **No copyrighted material** - Respect intellectual property
- **Rate limiting** - Don't hammer servers; yt-dlp has built-in delays

## Composability

**Status:** PLANNED (not yet active)

This PBC is designed to feed into:

- `rag-pipeline` - Audio files -> transcription -> text indexing

Peer capabilities:

- `pbc-web-crawling` - Both acquire content for RAG pipeline

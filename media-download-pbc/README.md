# Media Download PBC

Media acquisition from web sources - video, audio, and metadata extraction.

- **Status:** Experimental
- **Created:** 2025-12-12
- **Version:** 0.1.0
- **Role:** Content acquisition (planned: feeds into rag-pipeline)

## What This PBC Provides

- Download video/audio from YouTube and 700+ other sites
- Format selection (quality, resolution, audio-only)
- Metadata extraction (title, description, duration, etc.)
- Playlist and channel batch downloads
- Subtitle extraction

## Tool Inventory

### Global CLI Tool

| Tool | Command | Installed Via |
|------|---------|---------------|
| yt-dlp | `yt-dlp` | `uv tool install yt-dlp` |

**Use cases for CLI:**

- Quick one-off downloads: `yt-dlp <url>`
- List formats: `yt-dlp -F <url>`
- Audio extraction: `yt-dlp -x --audio-format mp3 <url>`

### PBC Virtual Environment

| Tool | Location | Purpose |
|------|----------|---------|
| yt-dlp (Python) | `.venv/` | Python scripting with full API access |

**Use cases for venv:**

- Reusable scripts in `scripts/` directory
- Metadata extraction for pipelines
- Batch processing with custom logic
- Integration with other PBCs

## Quick Reference

### CLI Examples

```bash
# Download best quality video
yt-dlp https://youtube.com/watch?v=VIDEO_ID

# Download audio only as mp3
yt-dlp -x --audio-format mp3 https://youtube.com/watch?v=VIDEO_ID

# List available formats
yt-dlp -F https://youtube.com/watch?v=VIDEO_ID

# Download with metadata JSON sidecar
yt-dlp --write-info-json https://youtube.com/watch?v=VIDEO_ID

# Get metadata only (no download)
yt-dlp --dump-json https://youtube.com/watch?v=VIDEO_ID

# Use config preset
yt-dlp --config-location configs/audio-only.conf https://youtube.com/watch?v=VIDEO_ID
```

### Python Script Invocation

```bash
# Run a script from this PBC (from any directory)
/c/Users/drewa/pbcs/media-download-pbc/.venv/Scripts/python.exe \
    /c/Users/drewa/pbcs/media-download-pbc/scripts/download_youtube.py \
    --url https://youtube.com/watch?v=VIDEO_ID \
    --output ./downloads/
```

## Scripts

| Script | Status | Description |
|--------|--------|-------------|
| `download_youtube.py` | Active | Full YouTube download with metadata |
| `batch_download.py` | Stub | Download from URL list file |
| `extract_metadata.py` | Stub | Get metadata JSON without downloading |
| `extract_audio.py` | Stub | Audio extraction wrapper |

See [pbc-definition.yaml](pbc-definition.yaml) for detailed script specifications.

## Config Presets

| Preset | File | Description |
|--------|------|-------------|
| Audio Only | `configs/audio-only.conf` | Extract best audio as mp3 |
| Video 720p | `configs/video-720p.conf` | Video capped at 720p |
| Video 1080p | `configs/video-1080p.conf` | Video capped at 1080p |
| Metadata Only | `configs/metadata-only.conf` | JSON metadata, no download |

## Default Output Location

Downloaded files are saved to: `downloads/`

This directory is gitignored to avoid committing large media files.

## Composability

**Status:** PLANNED

This PBC is designed as a **content acquisition** capability:

```
media-download-pbc ──────┐
                         ├──► rag-pipeline (transcription, indexing)
web-crawling-pbc ────────┘
```

- **Feeds into:** rag-pipeline (audio files for transcription -> text indexing)
- **Peer capability:** web-crawling-pbc (both acquire content for RAG)

## Dependencies

- **ffmpeg** - Required for merging video+audio streams, format conversion, audio extraction
  - Install: `winget install ffmpeg`
  - Verify: `ffmpeg -version`

## Installation

### 1. Global CLI (for quick commands)

```bash
uv tool install yt-dlp
```

### 2. PBC Virtual Environment (for scripting)

```bash
cd /c/Users/drewa/pbcs/media-download-pbc
uv venv
uv pip install yt-dlp
```

## External Documentation

- [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)
- [Usage and Options](https://github.com/yt-dlp/yt-dlp#usage-and-options)
- [Supported Sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

---

- **Document Status:** Active
- **Last Updated:** 2025-12-12

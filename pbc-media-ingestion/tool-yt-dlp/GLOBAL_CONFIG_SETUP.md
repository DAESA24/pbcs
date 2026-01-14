# Global yt-dlp Configuration Setup

## Overview

A global yt-dlp configuration has been installed to make the pbc-media-ingestion the default download location for all yt-dlp commands run globally.

## Configuration File Location

```
C:\Users\drewa\AppData\Roaming\yt-dlp\config.txt
```

## Default Behaviors

When running `yt-dlp` from any terminal:

- **Output Directory:** `/c/Users/drewa/pbcs/pbc-media-ingestion/tool-yt-dlp/downloads/`
- **Metadata:** Writes `.info.json` sidecar files automatically
- **Embeddings:** Adds metadata and thumbnails to files
- **Quality:** Downloads best available (bestvideo+bestaudio/best)

## Example Usage

```bash
# Downloads to PBC downloads folder by default
yt-dlp https://youtube.com/watch?v=VIDEO_ID

# Override output location if needed
yt-dlp -o "C:\Custom\Path\%(title)s.%(ext)s" https://youtube.com/watch?v=VIDEO_ID

# Use config preset
yt-dlp --config-location /c/Users/drewa/pbcs/pbc-media-ingestion/tool-yt-dlp/configs/audio-only.conf https://youtube.com/watch?v=VIDEO_ID
```

## Customization

Edit the config file to change default behavior:

```bash
# Open in editor
notepad C:\Users\drewa\AppData\Roaming\yt-dlp\config.txt
```

Common options:
- `--output` - Change output directory/format
- `--format` - Change quality preference
- `--extract-audio` - Extract audio by default
- `--write-description` - Write video descriptions

For full options, see: https://github.com/yt-dlp/yt-dlp#usage-and-options

## Setup Date

- **Configured:** 2025-12-12
- **Reason:** PBC-wide default download location

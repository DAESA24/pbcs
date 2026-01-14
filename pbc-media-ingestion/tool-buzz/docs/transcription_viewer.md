# Transcription Viewer | Buzz

- **Source:** https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer
- **Status:** 200
- **Validation:** PASS

---

[Skip to main content](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#__docusaurus_skipToContent_fallback)
On this page
# Transcription Viewer
The Buzz transcription viewer provides a powerful interface for reviewing, editing, and navigating through your transcriptions. This guide covers all the features available in the transcription viewer.
## Overview[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#overview "Direct link to Overview")
The transcription viewer is organized into several key sections:
  * **Top Toolbar** : Contains view mode, export, translate, resize, and search
  * **Search Bar** : Find and navigate through transcript text
  * **Transcription Segments** : Table view of all transcription segments with timestamps
  * **Playback Controls** : Audio playback settings and speed controls (since version 1.3.0)
  * **Audio Player** : Standard media player with progress bar
  * **Current Segment Display** : Shows the currently selected or playing segment


## Top Toolbar[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#top-toolbar "Direct link to Top Toolbar")
### View Mode Button[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#view-mode-button "Direct link to View Mode Button")
  * **Function** : Switch between different viewing modes
  * **Options** :
    * **Timestamps** : Shows segments in a table format with start/end times
    * **Text** : Shows combined text without timestamps
    * **Translation** : Shows translated text (if available)


### Export Button[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#export-button "Direct link to Export Button")
  * **Function** : Export transcription in various formats
  * **Formats** : SRT, VTT, TXT, JSON, and more
  * **Usage** : Click to open export menu and select desired format


### Translate Button[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#translate-button "Direct link to Translate Button")
  * **Function** : Translate transcription to different languages
  * **Usage** : Click to open translation settings and start translation


### Resize Button[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#resize-button "Direct link to Resize Button")
  * **Function** : Adjust transcription segment boundaries
  * **Usage** : Click to open resize dialog for fine-tuning timestamps
  * **More information** : See [Edit and Resize](https://chidiwilliams.github.io/buzz/docs/usage/edit_and_resize) section


### Playback Controls Button[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#playback-controls-button "Direct link to Playback Controls Button")
(since version 1.3.0)
  * **Function** : Show/hide playback control panel
  * **Shortcut** : `Ctrl+Alt+P` (Windows/Linux) or `Cmd+Alt+P` (macOS)
  * **Behavior** : Toggle button that shows/hides the playback controls below


### Find Button[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#find-button "Direct link to Find Button")
(since version 1.3.0)
  * **Function** : Show/hide search functionality
  * **Shortcut** : `Ctrl+F` (Windows/Linux) or `Cmd+F` (macOS)
  * **Behavior** : Toggle button that shows/hides the search bar


### Scroll to Current Button[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#scroll-to-current-button "Direct link to Scroll to Current Button")
(since version 1.3.0)
  * **Function** : Automatically scroll to the currently playing text
  * **Shortcut** : `Ctrl+G` (Windows/Linux) or `Cmd+G` (macOS)
  * **Usage** : Click to jump to the current audio position in the transcript


## Search Functionality[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#search-functionality "Direct link to Search Functionality")
(since version 1.3.0)
### Search Bar[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#search-bar "Direct link to Search Bar")
The search bar appears below the toolbar when activated and provides:
  * **Search Input** : Type text to find in the transcription (wider input field for better usability)
  * **Navigation** : Up/down arrows to move between matches
  * **Status** : Shows current match position and total matches (e.g., "3 of 15 matches")
  * **Clear** : Remove search text and results (larger button for better accessibility)
  * **Results** : Displays found text with context
  * **Consistent Button Sizing** : All navigation buttons have uniform height for better visual consistency


### Search Shortcuts[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#search-shortcuts "Direct link to Search Shortcuts")
  * **`Ctrl+F`/`Cmd+F`** : Toggle search bar on/off
  * **`Enter`**: Find next match
  * **`Shift+Enter`**: Find previous match
  * **`Escape`**: Close search bar


### Search Features[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#search-features "Direct link to Search Features")
  * **Real-time Search** : Results update as you type
  * **Case-insensitive** : Finds matches regardless of capitalization
  * **Word Boundaries** : Respects word boundaries for accurate matching
  * **Cross-view Search** : Works in all view modes (Timestamps, Text, Translation)


## Playback Controls[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#playback-controls "Direct link to Playback Controls")
(since version 1.3.0)
### Loop Segment[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#loop-segment "Direct link to Loop Segment")
  * **Function** : Automatically loop playback of selected segments
  * **Usage** : Check the "Loop Segment" checkbox
  * **Behavior** : When enabled, clicking on a transcript segment will set a loop range
  * **Visual Feedback** : Loop range is highlighted in the audio player


### Follow Audio[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#follow-audio "Direct link to Follow Audio")
  * **Function** : Automatically scroll to current audio position
  * **Usage** : Check the "Follow Audio" checkbox
  * **Behavior** : Transcript automatically follows the audio playback
  * **Benefits** : Easy to follow along with long audio files


### Speed Controls[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#speed-controls "Direct link to Speed Controls")
  * **Function** : Adjust audio playback speed
  * **Range** : 0.5x to 2.0x speed
  * **Controls** :
    * **Speed Dropdown** : Select from preset speeds or enter custom value
    * **Decrease Button (-)** : Reduce speed by 0.05x increments
    * **Increase Button (+)** : Increase speed by 0.05x increments
  * **Persistence** : Speed setting is saved between sessions
  * **Button Sizing** : Speed control buttons match the size of search navigation buttons for visual consistency


## Keyboard Shortcuts[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#keyboard-shortcuts "Direct link to Keyboard Shortcuts")
(since version 1.3.0)
### Audio Playback[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#audio-playback "Direct link to Audio Playback")
  * **`Ctrl+P`/`Cmd+P`** : Play/Pause audio
  * **`Ctrl+Shift+P`/`Cmd+Shift+P`** : Replay current segment from start


### Timestamp Adjustment[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#timestamp-adjustment "Direct link to Timestamp Adjustment")
  * **`Ctrl+←`/`Cmd+←`** : Decrease segment start time by 0.5s
  * **`Ctrl+→`/`Cmd+→`** : Increase segment start time by 0.5s
  * **`Ctrl+Shift+←`/`Cmd+Shift+←`** : Decrease segment end time by 0.5s
  * **`Ctrl+Shift+→`/`Cmd+Shift+→`** : Increase segment end time by 0.5s


### Navigation[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#navigation "Direct link to Navigation")
  * **`Ctrl+F`/`Cmd+F`** : Toggle search bar
  * **`Ctrl+Alt+P`/`Cmd+Alt+P`** : Toggle playback controls
  * **`Ctrl+G`/`Cmd+G`** : Scroll to current position
  * **`Ctrl+O`/`Cmd+O`** : Open file import dialog


### Search[​](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#search "Direct link to Search")
  * **`Enter`**: Find next match
  * **`Shift+Enter`**: Find previous match
  * **`Escape`**: Close search bar


  * [Overview](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#overview)
  * [Top Toolbar](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#top-toolbar)
    * [View Mode Button](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#view-mode-button)
    * [Export Button](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#export-button)
    * [Translate Button](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#translate-button)
    * [Resize Button](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#resize-button)
    * [Playback Controls Button](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#playback-controls-button)
    * [Find Button](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#find-button)
    * [Scroll to Current Button](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#scroll-to-current-button)
  * [Search Functionality](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#search-functionality)
    * [Search Bar](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#search-bar)
    * [Search Shortcuts](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#search-shortcuts)
    * [Search Features](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#search-features)
  * [Playback Controls](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#playback-controls)
    * [Loop Segment](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#loop-segment)
    * [Follow Audio](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#follow-audio)
    * [Speed Controls](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#speed-controls)
  * [Keyboard Shortcuts](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#keyboard-shortcuts)
    * [Audio Playback](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#audio-playback)
    * [Timestamp Adjustment](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#timestamp-adjustment)
    * [Navigation](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#navigation)
    * [Search](https://chidiwilliams.github.io/buzz/docs/usage/transcription_viewer#search)



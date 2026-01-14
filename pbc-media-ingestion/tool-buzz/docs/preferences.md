# Preferences | Buzz

- **Source:** https://chidiwilliams.github.io/buzz/docs/preferences
- **Status:** 200
- **Validation:** PASS

---

[Skip to main content](https://chidiwilliams.github.io/buzz/docs/preferences#__docusaurus_skipToContent_fallback)
On this page
Open the Preferences window from the Menu bar, or click `Ctrl/Cmd + ,`.
## General Preferences[​](https://chidiwilliams.github.io/buzz/docs/preferences#general-preferences "Direct link to General Preferences")
### OpenAI API preferences[​](https://chidiwilliams.github.io/buzz/docs/preferences#openai-api-preferences "Direct link to OpenAI API preferences")
**API Key** - key to authenticate your requests to OpenAI API. To get API key from OpenAI see 
**Base URL** - By default all requests are sent to API provided by OpenAI company. Their API URL is `https://api.openai.com/v1/`. Compatible APIs are also provided by other companies. List of available API URLs and services to run yourself are available on 
### Default export file name[​](https://chidiwilliams.github.io/buzz/docs/preferences#default-export-file-name "Direct link to Default export file name")
Sets the default export file name for file transcriptions. For example, a value of `{{ input_file_name }} ({{ task }}d on {{ date_time }})` will save TXT exports as `Input Filename (transcribed on 19-Sep-2023 20-39-25).txt` by default.
Available variables:
Key | Description | Example  
---|---|---  
`input_file_name` | File name of the imported file |  `audio` (e.g. if the imported file path was `/path/to/audio.wav`  
`task` | Transcription task |  `transcribe`, `translate`  
`language` | Language code |  `en`, `fr`, `yo`, etc.  
`model_type` | Model type |  `Whisper`, `Whisper.cpp`, `Faster Whisper`, etc.  
`model_size` | Model size |  `tiny`, `base`, `small`, `medium`, `large`, etc.  
`date_time` | Export time (format: `%d-%b-%Y %H-%M-%S`) | `19-Sep-2023 20-39-25`  
### Live transcript exports[​](https://chidiwilliams.github.io/buzz/docs/preferences#live-transcript-exports "Direct link to Live transcript exports")
Live transcription export can be used to integrate Buzz with other applications like OBS Studio. When enabled, live text transcripts will be exported to a text file as they get generated and translated.
If AI translation is enabled for live recordings, the translated text will also be exported to the text file. Filename for the translated text will end with `.translated.txt`.
### Live transcription mode[​](https://chidiwilliams.github.io/buzz/docs/preferences#live-transcription-mode "Direct link to Live transcription mode")
Three transcription modes are available:
**Append below** - New sentences will be added below existing with an empty space between them. Last sentence will be at the bottom.
**Append above** - New sentences will be added above existing with an empty space between them. Last sentence will be at the top.
**Append and correct** - New sentences will be added at the end of existing transcript without extra spaces between. This mode will also try to correct errors at the end of previously transcribed sentences. This mode requires more processing power and more powerful hardware to work.
## Model Preferences[​](https://chidiwilliams.github.io/buzz/docs/preferences#model-preferences "Direct link to Model Preferences")
This section lets you download new models for transcription and delete unused ones.
For Whisper.cpp you can also download custom models. Select `Custom` in the model size list and paste the download url to the model `.bin` file. Use the link from "download" button from the Huggingface. 
To improve transcription speed and memory usage you can select a quantized version of some larger model. For example `q_5` version. Whisper.cpp base models in different quantizations are 
## Advanced Preferences[​](https://chidiwilliams.github.io/buzz/docs/preferences#advanced-preferences "Direct link to Advanced Preferences")
To keep preferences section simple for new users, some more advanced preferences are settable via OS environment variables. Set the necessary environment variables in your OS before starting Buzz or create a script to set them.
On MacOS and Linux crete `run_buzz.sh` with the following content:
```
#!/bin/bash  
exportVARIABLE=value  
exportSOME_OTHER_VARIABLE=some_other_value  
buzz  

```

On Windows crete `run_buzz.bat` with the following content:
```
@echo off  
set VARIABLE=value  
set SOME_OTHER_VARIABLE=some_other_value  
"C:\Program Files (x86)\Buzz\Buzz.exe"  

```

Alternatively you can set environment variables in your OS settings. See 
### Available variables[​](https://chidiwilliams.github.io/buzz/docs/preferences#available-variables "Direct link to Available variables")
**BUZZ_WHISPERCPP_N_THREADS** - Number of threads to use for Whisper.cpp model. Default is half of available CPU cores.
On a laptop with 16 threads setting `BUZZ_WHISPERCPP_N_THREADS=8` leads to some 15% speedup in transcription time. Increasing number of threads even more will lead in slower transcription time as results from parallel threads has to be combined to produce the final answer.
**BUZZ_TRANSLATION_API_BASE_URL** - Base URL of OpenAI compatible API to use for translation.
**BUZZ_TRANSLATION_API_KEY** - Api key of OpenAI compatible API to use for translation.
**BUZZ_MODEL_ROOT** - Root directory to store model files. You may also want to set `HF_HOME` to the same folder as some libraries used in Buzz download their models independently. Defaults to 
**BUZZ_FAVORITE_LANGUAGES** - Coma separated list of supported language codes to show on top of language list.
**BUZZ_DOWNLOAD_COOKIEFILE** - Location of a 
**BUZZ_FORCE_CPU** - Will force Buzz to use CPU and not GPU, useful for setups with older GPU if that is slower than GPU or GPU has issues. Example usage `BUZZ_FORCE_CPU=true`. Available since `1.2.1`
**BUZZ_REDUCE_GPU_MEMORY** - Will use 8bit quantization for Huggingface adn Faster Whisper transcriptions to reduce required GPU memory. Example usage `BUZZ_REDUCE_GPU_MEMORY=true`. Available since `1.4.0`
**BUZZ_MERGE_REGROUP_RULE** - Custom regroup merge rule to use when combining transcripts with word-level timings. More information on available options `1.3.0`
**BUZZ_DISABLE_TELEMETRY** - Buzz collects basic OS name and architecture usage statistics to better focus development efforts. This variable lets disable collection of these statistics. Example usage `BUZZ_DISABLE_TELEMETRY=true`. Available since `1.3.0`
**BUZZ_UPLOAD_URL** - Live recording transcripts and translations can be uploaded to a server for display on the web. Set this variable to the desired upload url. You can use `json` via `POST` requests - `{"kind": "transcript", "text": "Sample transcript"}` or `{"kind": "translation", "text": "Sample translation"}`. Example usage `BUZZ_UPLOAD_URL=http://localhost:5000/upload`. Available since `1.3.0`
Example of data collected by telemetry:
```
Buzz: 1.3.0, locale: ('lv_LV', 'UTF-8'), system: Linux, release: 6.14.0-27-generic, machine: x86_64, version: #27~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Jul 22 17:38:49 UTC 2,  

```

**BUZZ_PARAGRAPH_SPLIT_TIME** - Time in milliseconds of silence to split paragraphs in transcript and add two newlines when exporting the transcripts as text. Default is `2000` or 2 seconds. Available since `1.3.0`
  * [General Preferences](https://chidiwilliams.github.io/buzz/docs/preferences#general-preferences)
    * [OpenAI API preferences](https://chidiwilliams.github.io/buzz/docs/preferences#openai-api-preferences)
    * [Default export file name](https://chidiwilliams.github.io/buzz/docs/preferences#default-export-file-name)
    * [Live transcript exports](https://chidiwilliams.github.io/buzz/docs/preferences#live-transcript-exports)
    * [Live transcription mode](https://chidiwilliams.github.io/buzz/docs/preferences#live-transcription-mode)
  * [Model Preferences](https://chidiwilliams.github.io/buzz/docs/preferences#model-preferences)
  * [Advanced Preferences](https://chidiwilliams.github.io/buzz/docs/preferences#advanced-preferences)
    * [Available variables](https://chidiwilliams.github.io/buzz/docs/preferences#available-variables)



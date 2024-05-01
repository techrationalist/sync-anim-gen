# SyncAnimGen: Synchronize Animations with Audio using Manim animation library

## Introduction

`SyncAnimGen` is an open-source tool designed to facilitate the creation of animations that are synchronized with audio. It is developed for use with [Manim](https://www.manim.community/), the tool generates skeleton scripts that lay the foundation for precise audio-visual alignment in educational and explanatory videos.

## Features

- **Automatic Script Generation**: Generates base scripts for animations that align with specified audio files, saving time and reducing manual synchronization efforts.
- **User-Friendly**: Simple command-line interface for specifying input files (audio and timing metadata) and generating the output scripts.
- **Customizable Output**: Generated scripts are only the starting point—users can easily modify and enhance these to match specific aesthetic and timing needs.

## Getting Started

To get started with `SyncAnimGen`, clone this repository and ensure you have Python installed on your system.

### Prerequisites

- Python 3.12 or higher
- Manim Community Edition
- Pydantic

### Usage

1. Clone this repository to your local machine and navigate to the cloned directory:

    ```bash
    cd sync-anim-gen
    ```

2. Generate transcript from the audio file using [OpenAI](https://platform.openai.com/docs/guides/speech-to-text):

    ```bash
    python src/generate_transcript.py -a /path/to/audio/file -o /path/to/output/transcript
    ```

    Use the sample audio file in the `example` folder to generate the transcript:

    ```bash
    python src/generate_transcript.py -a example/sample_audio.mp3 -o /tmp/generated_transcript.json
    ```

3. Edit the generated transcript to match the audio file.

    Check the `example/edited_transcription.json` file for the expected format.

4. Run the script with the following command to generate the animation script:

    ```bash
    python src/main.py -a /path/to/audio/file -t /path/to/edited/transcript/file -o /path/to/output/script
    ```

    Sample run:

    `example` folder contains sample audio and transcript files that can be used to generate the animation script.

    ```bash
    python src/main.py -a example/sample_audio.mp3 -t example/edited_transcription.json -o /tmp/generated_output_file.py
    ```

5. Run the generated script to see the animation:

    ```bash
    manim -pql /tmp/generated_output_file.py
    ```

6. Once you have generated the animation script, you can modify it to suit your specific needs.

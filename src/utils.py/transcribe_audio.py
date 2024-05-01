#!/usr/bin/env python3
import argparse
import json
import os

from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TRANSCRIPTION_MODEL = os.getenv("TRANSCRIPTION_MODEL")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

if not TRANSCRIPTION_MODEL:
    raise ValueError("TRANSCRIPTION_MODEL not found in environment variables")

# Set up command line argument parsing
parser = argparse.ArgumentParser(
    description="Transcribe audio file using OpenAI's Whisper model."
)
parser.add_argument(
    "audio_file_path", type=str, help="Path to the audio file to transcribe."
)

args = parser.parse_args()

client = OpenAI()

# Open the audio file specified by the command line argument
with open(args.audio_file_path, "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        file=audio_file,
        model=TRANSCRIPTION_MODEL,
        response_format="verbose_json",
        timestamp_granularities=["word"],
    )

print(json.dumps(transcript.words, indent=4))
# print(transcript.text)

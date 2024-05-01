#!/usr/bin/env python3
import argparse

from generate_script import (
    generate_animation_script,  # Assume this is your script generating function
)


def main():
    parser = argparse.ArgumentParser(
        description="Generate animation scripts synchronized with audio using SyncAnimGen."
    )
    parser.add_argument(
        "-a", "--audio-file", required=True, help="Path to the mp3 audio file."
    )
    parser.add_argument(
        "-t",
        "--timestamps-file",
        required=True,
        help="Path to the JSON file containing timestamps and text.",
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Path to the output script file."
    )

    args = parser.parse_args()

    generate_animation_script(
        audio_file_path=args.audio_file,
        timestamps_file_path=args.timestamps_file,
        output_file_path=args.output,
    )


if __name__ == "__main__":
    main()

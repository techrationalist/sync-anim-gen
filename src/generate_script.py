import json
from typing import List

from models import AnimationDataOutput, AnimationMarkerType, TimeStampsData


class SyncTextWithAudio:
    def __init__(self, audio_file_path, timestamps_file_path, output_file_path):
        self.audio_file_path = audio_file_path
        self.timestamps_file_path = timestamps_file_path
        self.output_file_path = output_file_path

    def generate_script(self):
        self.animation_steps: List[AnimationDataOutput] = [
            AnimationDataOutput(
                id="start_with_wait",
                startTime=0,
                endTime=0,
                type=AnimationMarkerType.wait,
            )
        ]

        timestamps_data_list = [
            TimeStampsData(**data)
            for data in json.load(open(self.timestamps_file_path))
        ]

        for data in timestamps_data_list:
            if data.animationStart:
                self.animation_steps[-1].endTime = data.start
                current_animation_step = AnimationDataOutput(
                    id=data.animationStart.id,
                    text=data.animationStart.text,
                    startTime=data.start,
                    type=data.animationStart.type,
                )
                self.animation_steps.append(current_animation_step)
            if data.animationEnd:
                self.animation_steps[-1].endTime = data.end
                self.animation_steps.append(
                    AnimationDataOutput(
                        id=self.animation_steps[-1].id,
                        startTime=data.end,
                        type=AnimationMarkerType.wait,
                    )
                )
            else:
                self.animation_steps[-1].endTime = data.end

        if self.animation_steps[-1].endTime is None:
            self.animation_steps[-1].endTime = self.animation_steps[-1].startTime + 1

        for animation_step in self.animation_steps:
            print(json.dumps(animation_step.model_dump(exclude_none=True), indent=4))

        python_code = f"""# This code is generated. This is starting point for your animation.
# You can modify this code as per your requirements.
from manim import *

class SyncTextWithAudio(Scene):
    def construct(self):
        self.add_sound("{self.audio_file_path}")
"""
        text = None
        for animation_step in self.animation_steps:
            if type(animation_step) is AnimationDataOutput:
                if animation_step.type == AnimationMarkerType.write.value:
                    if animation_step.text is None:
                        raise Exception("Text is required for write animation")
                    if animation_step.endTime is None:
                        raise Exception("End time is required for write animation")
                    text = animation_step.text
                    python_code += f"""
        obj = Text("{animation_step.text}")
"""
                    print(
                        f"Writing {animation_step.text}, start time: {animation_step.startTime}, end time: {animation_step.endTime}"
                    )
                    python_code += f"""
        self.play(
                        Write(
                            obj,
                            run_time=({animation_step.endTime - animation_step.startTime}),
                        )
                )
"""

                elif animation_step.type == AnimationMarkerType.wait.value:
                    if text is None:
                        python_code += f"""
        self.wait({animation_step.endTime - animation_step.startTime})
"""
                    else:
                        python_code += f"""
        self.play(
                        FadeOut(
                            obj,
                            run_time={animation_step.endTime - animation_step.startTime},
                        )
                )
"""
                else:
                    raise Exception(f"Unknown animation type: {animation_step.type}")

        with open(self.output_file_path, "w") as f:
            f.write(python_code)


def generate_animation_script(audio_file_path, timestamps_file_path, output_file_path):
    sync_text_with_audio = SyncTextWithAudio(
        audio_file_path, timestamps_file_path, output_file_path
    )
    sync_text_with_audio.generate_script()
    print(
        f"Animation script generated successfully. Output file path: {output_file_path}"
    )

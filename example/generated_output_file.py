# This code is generated. This is starting point for your animation.
# You can modify this code as per your requirements.
from manim import *

class SyncTextWithAudio(Scene):
    def construct(self):
        self.add_sound("example/sample_audio.mp3")

        self.wait(0.3400000035762787)

        obj = Text("Countdown Begins")

        self.play(
                        Write(
                            obj,
                            run_time=(2.0400001108646393),
                        )
                )

        self.play(
                        FadeOut(
                            obj,
                            run_time=4.319999694824219,
                        )
                )

        obj = Text("Halfway there")

        self.play(
                        Write(
                            obj,
                            run_time=(3.1000003814697266),
                        )
                )

        self.play(
                        FadeOut(
                            obj,
                            run_time=1.859999656677246,
                        )
                )

        obj = Text("Ignition")

        self.play(
                        Write(
                            obj,
                            run_time=(0.8400001525878906),
                        )
                )

        self.play(
                        FadeOut(
                            obj,
                            run_time=1.0,
                        )
                )

from manim import FadeOut, Scene, Text


class Countdown(Scene):
    def construct(self):
        for i in range(10, -1, -1):
            number = Text(str(i), font_size=96)
            self.add(number)
            self.play(FadeOut(number))


# Ensure to add this block if you want to directly execute this script with Manim
if __name__ == "__main__":
    scene = Countdown()
    scene.render()

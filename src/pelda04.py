from manim import *

class SpecialAnimations(Scene):
    def construct(self):
        circle = Circle(radius=1, color=YELLOW)
        self.play(Create(circle), run_time=2, rate_func= smooth)
        self.play(Circumscribe(circle, fade_in=True), run_time=2)
        self.play(Uncreate(circle), run_time=1)
        self.wait(1)
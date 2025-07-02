from manim import *

class ObjectManipulation(Scene):
    def construct(self):
        square = Square(side_length=1, color=ORANGE)
        self.play(Create(square), run_time=1)
        self.play(square.animate.move_to(np.array([2, 1, 0])), run_time=1)
        self.play(square.animate.scale(1.5), run_time=1)
        self.wait(1)
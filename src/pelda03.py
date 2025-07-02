from manim import *

class GraphExample(Scene):
    def construct(self):
        axes = Axes(x_range=[-5, 5], y_range=[-5, 5])
        graph = axes.plot(lambda x: x**2, color=BLUE)
        self.play(Create(axes), Create(graph), run_time=2)
        self.wait(1)
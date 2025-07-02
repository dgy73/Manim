from manim import *
import numpy as np
config.pixel_width = 1280
config.pixel_height = 720
class Pelda01(Scene):
    def construct(self):
        # Csúcsok megadása
        A = np.array([-6.5, -2, 0])
        B = np.array([2, -2, 0])
        C = np.array([0, 2, 0])
        D = np.array([-5, 2, 0])

        a = np.linalg.norm(A-B)
        c = np.linalg.norm(C-D)



        Trapez = Polygon(A,B,C,D, color=WHITE)

        # Animáció
        self.play(Create(Trapez))

        self.wait(5)

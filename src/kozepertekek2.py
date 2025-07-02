from manim import *
import numpy as np

# renderelés
# manim -pqh kozepertekek2.py

class KOZEP01(Scene):
    def construct(self):
        # trapéz pontjai
        A = np.array([-6,-2,0])
        B = np.array([2,-2,0])
        C = np.array([0,2,0])
        D = np.array([-5,2,0])

        a = np.linalg.norm(A-B)
        c = np.linalg.norm(C-D)

        # trapéz oldalai
        old_a = Line(A,B)
        old_b = Line(C,B)
        old_c = Line(C,D)
        old_d = Line(A,D)

        # csúcsok cimkézése
        label_A = MathTex(r"A").next_to(A, LEFT+DOWN, buff=.1)

        # cimkék az oldalakhoz
        label_a = MathTex(r"a").next_to(old_a, DOWN)
        label_c = MathTex(r"c").next_to(old_c, UP)

        # középértékeket szemléltető szakaszok
        F1, F2 = (A+D)/2, (B+C)/2
        dot_F1 = Dot(F1)
        label_F1 = MathTex(r"F_1").next_to(F1, LEFT, buff=.1)
        algebrai = Line(F1, F2, color=RED)
        label_algebrai = MathTex(r"k=\frac{a+c}{2}", font_size=20).next_to(algebrai, DOWN)


        # animáció
        self.play(Create(old_a), Create(old_b), Create(old_c), Create(old_d))
        self.play(Write(label_a), Write(label_c), Write(label_A))

        self.wait(2)
        self.play(Create(dot_F1),Write(label_F1),Create(algebrai), Write(label_algebrai))

        self.wait(5)

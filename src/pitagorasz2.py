from manim import *
import numpy as np

class PitagoraszTétel(Scene):
    def construct(self):
        # Háromszög csúcsai
        A = np.array([0.0, 0.0, 0])
        B = np.array([1.5, 0.0, 0])
        C = np.array([0.0, 2.0, 0])

        # Négyzetek csúcsai
        B1 = np.array([-2.0, 2.0, 0])
        B2 = np.array([-2.0, 0, 0])
        A1 = np.array([1.5, -1.5, 0])
        A2 = np.array([0, -1.5, 0])
        C1 = np.array([2, 3.5, 0])
        C2 = np.array([3.5, 1.5, 0])

        # Darabolások csúcsai
        Q = np.array([-2, 0.5, 0])
        R = np.array([-2, 0.0, 0])
        P = np.array([-2, 2.0, 0])
        N = np.array([-1.5, 2.0, 0])
        M = np.array([-0.96, 1.28, 0])
        S = np.array([0.96, 2.72, 0])
        T = np.array([0.96, 0.72, 0])
        U = np.array([2.46, 0.72, 0])
        E = np.array([0.96, 2.22, 0])
        F = np.array([2.46, 2.22, 0])
        G = np.array([2.96, 2.22, 0])

        # Háromszög létrehozása
        triangle = Polygon(A, B, C, color=WHITE, fill_opacity=0.2).set_stroke(WHITE, 1)

        # Oldalak jelölése
        label_a = Tex("$a$").next_to(Line(A, B).get_midpoint(), DOWN, buff=0.1)
        label_b = Tex("$b$").next_to(Line(A, C).get_midpoint(), LEFT, buff=0.1)
        label_c = Tex("$c$").next_to(Line(B, C).get_midpoint(), RIGHT, buff=0.1)

        # Négyzetek létrehozása
        square_a = Polygon(A, B, A1, A2).set_stroke(color=WHITE, width=1).set_fill(BLUE, opacity=0.5)
        square_b = Polygon(A, C, B1, B2).set_stroke(color=WHITE, width=1).set_fill(GREEN, opacity=0.5)
        square_c = Polygon(B, C, C1, C2).set_stroke(color=WHITE, width=1).set_fill(RED, opacity=0.5)

        #négyzet oldalainak jelölése
        label_negyzetek = VGroup(
        Tex("$a$").next_to(Line(A, B).get_midpoint(), UP, buff=0.1),
        Tex("$b$").next_to(Line(A, C).get_midpoint(), RIGHT, buff=0.1),
        Tex("$c$").next_to(Line(B, C).get_midpoint(), LEFT, buff=0.1),
        Tex("$a$").next_to(Line(A, A2).get_midpoint(), LEFT, buff=0.1),
        Tex("$b$").next_to(Line(C, B1).get_midpoint(), UP, buff=0.1),
        Tex("$c$").next_to(Line(C, C1).get_midpoint(), UP, buff=0.1)
        )

        # Területek jelölése
        label_a2 = Tex("$a^2$").next_to(Line(A, A1).get_midpoint(), LEFT, buff=0)
        label_b2 = Tex("$b^2$").next_to(Line(A, B1).get_midpoint(), LEFT, buff=0)
        label_c2 = Tex("$c^2$").next_to(Line(B, C1).get_midpoint(), LEFT, buff=0)

        # Darabolások létrehozása
        H1 = Polygon(A, C, M).set_fill(GREEN_A, opacity=0.7).set_stroke(color=BLACK, width=1)
        H2 = Polygon(N, C, M).set_fill(GREEN_B, opacity=0.7).set_stroke(color=BLACK, width=1)
        N1 = Polygon(M, N, P, Q).set_fill(GREEN_C, opacity=0.7).set_stroke(color=BLACK, width=1)
        N2 = Polygon(Q, R, A, M).set_fill(GREEN_D, opacity=0.7).set_stroke(color=BLACK, width=1)

        # Cél sokszögek
        H1_cel = Polygon(T, S, C).set_fill(GREEN_A, opacity=0.7).set_stroke(color=BLACK, width=1)
        H2_cel = Polygon(T, U, B).set_fill(GREEN_B, opacity=0.7).set_stroke(color=BLACK, width=1)
        N1_cel = Polygon(C2, G, F, U).set_fill(GREEN_C, opacity=0.7).set_stroke(color=BLACK, width=1)
        N2_cel = Polygon(S, E, G, C1).set_fill(GREEN_D, opacity=0.7).set_stroke(color=BLACK, width=1)
        A_cel = Polygon(E, F, U, T).set_fill(BLUE, opacity=0.7).set_stroke(color=BLACK, width=1)

        # Pitagorasz-tétel képlete
        theorem = Tex("$a^2 + b^2 = c^2$").to_edge(DOWN)
        szovegesen = Text("Egy derékszögű háromszög befogóira emelt\nnégyzetek területének összege egyenlő\naz átfogóra emelt négyzet területével.")
        # Animáció
        self.play(Create(triangle))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(1)
        self.play(FadeOut(label_a, label_b, label_c))
        self.play(Create(square_a), Create(square_b), Create(square_c))
        self.wait(1)
        self.play(Write(label_negyzetek))
        
        self.wait(1)
        self.play(Write(label_a2), Write(label_b2), Write(label_c2))
        self.wait(1)
        self.play(FadeOut(label_a2, label_b2, label_c2))

        # Darabolások
        self.play(Create(H1), Create(H2), Create(N1), Create(N2))
        self.wait(1)

        # Átalakítás
        self.play(Transform(H1, H1_cel), Transform(H2, H2_cel))
        self.wait(1)
        self.play(Transform(N1, N1_cel), Transform(N2, N2_cel))
        self.wait(1)
        # Az A_cel átalakítást változóba mentjük
        a_cel_transformed = square_a.copy()
        self.play(Transform(a_cel_transformed, A_cel))
        self.wait(1)
        self.play(Write(label_a2), Write(label_b2), Write(label_c2))
        self.wait(1)
        self.play(FadeOut(label_a2, label_b2, label_c2))
        
        # Képlet és lezárás
        self.play(Write(theorem))
        self.wait(2)
        self.play(FadeOut(label_negyzetek))
        # Az A_cel (átalakított verzió) is eltűnik
        self.play(FadeOut(triangle, square_a, square_b, square_c, H1, H2, N1, N2, theorem, a_cel_transformed))
        self.wait(1)
        self.play(Write(szovegesen))
        self.wait(5)
        self.play(FadeOut(szovegesen))
        self.wait(.5)
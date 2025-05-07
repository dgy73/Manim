from manim import *
import numpy as np

class TriangleCircles(Scene):
    def magyarazo_szoveg(self, szoveg, position_obj=None, font_size=24, duration=1, use_tex=True):
        """
        Megjelenít egy magyarázó szöveget a megadott pozícióban.
        
        Args:
            szoveg (str): A megjelenítendő szöveg.
            position_obj: A Mobject, amelynek középpontjára a szöveg kerül (alapértelmezett: self.text_area1).
            font_size (int): A szöveg betűmérete (alapértelmezett: 24).
            duration (float): Várakozási idő a megjelenítés után (másodpercben).
            use_tex (bool): True esetén Tex, False esetén Text objektumot használ.
        
        Returns:
            Mobject: A létrehozott szöveg objektum.
        """
        position_obj = position_obj or self.text_area1
        if position_obj is None:
            raise ValueError("position_obj is None and self.text_area1 is not defined")
        
        felirat = Tex(szoveg, font_size=font_size).scale(1.25) if use_tex else Text(szoveg, font_size=font_size)
        felirat.move_to(position_obj.get_center())
        self.play(Write(felirat))
        self.wait(duration)
        return felirat

    def construct(self):
        # text_area1 definiálása
        self.text_area1 = Rectangle(
            width=5.5, height=4.5, color=RED, stroke_width=2
        ).move_to([4, -2, 0])
        #self.add(self.text_area1)  # Megjelenítés a vásznon

        CIM = Text("A háromszögek érintő körei")

        # Csúcsok koordinátái (2D vektorok)
        A_2d = np.array([-1, 3])
        B_2d = np.array([-2, -1])
        C_2d = np.array([1, 0])
        A = np.append(A_2d, 0)
        B = np.append(B_2d, 0)
        C = np.append(C_2d, 0)

        # Oldalak hossza
        a = np.linalg.norm(C_2d - B_2d)
        b = np.linalg.norm(A_2d - C_2d)
        c = np.linalg.norm(B_2d - A_2d)
        s = (a + b + c) / 2

        # Terület
        P = np.array([[A_2d[0], A_2d[1], 1],
                      [B_2d[0], B_2d[1], 1],
                      [C_2d[0], C_2d[1], 1]])
        Terulet = 0.5 * abs(np.linalg.det(P))

        # Beírt kör középpontja és sugara
        O_2d = (a * A_2d + b * B_2d + c * C_2d) / (a + b + c)
        O = np.append(O_2d, 0)
        rho = Terulet / s

        # Hozzáírt körök középpontjai
        O_a_2d = (-a * A_2d + b * B_2d + c * C_2d) / (-a + b + c)
        O_b_2d = (a * A_2d - b * B_2d + c * C_2d) / (a - b + c)
        O_c_2d = (a * A_2d + b * B_2d - c * C_2d) / (a + b - c)
        O_a = np.append(O_a_2d, 0)
        O_b = np.append(O_b_2d, 0)
        O_c = np.append(O_c_2d, 0)
        rho_a = Terulet / (s - a)
        rho_b = Terulet / (s - b)
        rho_c = Terulet / (s - c)

        # Háromszög és címkék
        triangle = Polygon(A, B, C, stroke_color=WHITE)
        label_A = MathTex("A").next_to(A, UP, buff=0.1)
        label_B = MathTex("B").next_to(B, LEFT, buff=0.1)
        label_C = MathTex("C").next_to(C, RIGHT, buff=0.1)
        label_a = MathTex("a").next_to(Line(B, C).get_center(), DOWN, buff=0.1)
        label_b = MathTex("b").next_to(Line(A, C).get_center(), RIGHT+UP, buff=0.1)
        label_c = MathTex("c").next_to(Line(B, A).get_center(), LEFT+DOWN, buff=0.2)

        # Szögfelezők
        def szogfelezo_irany(p1, vertex, p2, ratio=0.5):
            v1 = p1 - vertex
            v2 = p2 - vertex
            angle = angle_of_vector(v2) - angle_of_vector(v1)
            angle = (angle + PI) % TAU - PI
            return np.array(rotate_vector(v1 / np.linalg.norm(v1), angle * ratio))

        def szogfelezo(vertex, p1, p2, length=8, color=GREY, stroke_width=2):
            return Line(
                vertex, vertex + szogfelezo_irany(p1, vertex, p2) * length,
                color=color, stroke_width=stroke_width
            )

        bisector_A = szogfelezo(A, B, C)
        bisector_B = szogfelezo(B, C, A)
        bisector_C = szogfelezo(C, A, B)

        # Külső szögfelezők
        triangle_diameter = max(a, b, c)
        line_length = triangle_diameter * 2
        v_kulso_A = (O_b - O_c) / np.linalg.norm(O_b - O_c)
        kulso_A = DashedLine(A - line_length * v_kulso_A, A + line_length * v_kulso_A, color=GREEN, stroke_width=2)
        v_kulso_B = (O_a - O_c) / np.linalg.norm(O_a - O_c)
        kulso_B = DashedLine(B - line_length * v_kulso_B, B + line_length * v_kulso_B, color=GREEN, stroke_width=2)
        v_kulso_C = (O_b - O_a) / np.linalg.norm(O_b - O_a)
        kulso_C = DashedLine(C - line_length * v_kulso_C, C + line_length * v_kulso_C, color=GREEN, stroke_width=2)

        # Körök
        in_circle = Circle(radius=rho, color=BLUE).move_to(O)
        ex_circle_a = Circle(radius=rho_a, color=GREEN).move_to(O_a)
        ex_circle_b = Circle(radius=rho_b, color=GREEN).move_to(O_b)
        ex_circle_c = Circle(radius=rho_c, color=GREEN).move_to(O_c)

        # Középpontok címkézése
        label_O = MathTex("O").next_to(O, DOWN + LEFT, buff=0.1)
        label_O_a = MathTex("O_a").next_to(O_a, DOWN, buff=0.1)
        label_O_b = MathTex("O_b").next_to(O_b, RIGHT, buff=0.1)
        label_O_c = MathTex("O_c").next_to(O_c, LEFT, buff=0.1)

        # Sugár és érintési pontok
        v_AB = A_2d - B_2d
        v_AC = C_2d - A_2d
        v_BC = B_2d - C_2d
        n_AB = np.array([-v_AB[1], v_AB[0]]) / np.linalg.norm([-v_AB[1], v_AB[0]])
        n_AC = np.array([-v_AC[1], v_AC[0]]) / np.linalg.norm([-v_AC[1], v_AC[0]])
        n_BC = np.array([-v_BC[1], v_BC[0]]) / np.linalg.norm([-v_BC[1], v_BC[0]])
        P_AB_2d = O_2d + n_AB * rho
        P_AB = np.append(P_AB_2d, 0)
        P_AC_2d = O_2d + n_AC * rho
        P_AC = np.append(P_AC_2d, 0)
        P_BC_2d = O_2d + n_BC * rho
        P_BC = np.append(P_BC_2d, 0)
        radius_AB = Line(O, P_AB, color=YELLOW)
        radius_AC = Line(O, P_AC, color=YELLOW)
        radius_BC = Line(O, P_BC, color=YELLOW)
        label_radius_BC = MathTex(r"\varrho", font_size=30).next_to(radius_BC, RIGHT, buff=0.1)

        # Hozzáírt körök sugarai
        K_AB_2d = O_c_2d - n_AB * rho_c
        K_AB = np.append(K_AB_2d, 0)
        K_AC_2d = O_b_2d - n_AC * rho_b
        K_AC = np.append(K_AC_2d, 0)
        K_BC_2d = O_a_2d - n_BC * rho_a
        K_BC = np.append(K_BC_2d, 0)
        kulso_AB = Line(O_c, K_AB, color=RED_C)
        label_kulso_AB = MathTex(r"\varrho_c", font_size=30).next_to(kulso_AB.get_center(), UP, buff=0.2)
        kulso_AC = Line(O_b, K_AC, color=RED_B)
        label_kulso_AC = MathTex(r"\varrho_b", font_size=30).next_to(kulso_AC.get_center(), UP, buff=0.2)
        kulso_BC = Line(O_a, K_BC, color=RED_A)
        label_kulso_BC = MathTex(r"\varrho_a", font_size=30).next_to(kulso_BC.get_center(), LEFT, buff=0.2)

        # Szövegek
        text01 = Tex(
            r"A beírtható kör $\varrho$ sugarának meghatározása",
            font_size=25
        ).move_to(self.text_area1.get_center()).scale(0.8)
        text02 = Tex(
            r"A háromszög területe: $$T_{ABC}=T_{AOB}+T_{BOC}+T_{COA}$$",
            font_size=25
        ).move_to(self.text_area1.get_center()).scale(0.8)
        text_list = [
            Tex(r"$$T=T_{ABC}=T_{AOB}+T_{BOC}+T_{COA}$$", font_size=30),
            Tex(r"$T=\dfrac{c \cdot \varrho}{2}+\dfrac{a \cdot \varrho}{2}+\dfrac{b \cdot \varrho}{2}$", font_size=30),
            Tex(r"$T=\dfrac{a+b+c}{2} \cdot \varrho$", font_size=30),
            Tex(r"$T=s \cdot \varrho$", font_size=30),
            Tex(r"$\varrho = \dfrac{T}{s}=\dfrac{2T}{K}$", font_size=30)
        ]
        for text in text_list:
            text.move_to(self.text_area1.get_center()).scale(0.8)

        # Animáció
        self.play(Write(CIM))
        self.wait(2)
        self.play(FadeOut(CIM))
        felirat = self.magyarazo_szoveg(
            szoveg="Tekintsünk egy $ABC$ háromszöget!",
            font_size=24,
            duration=1,
            use_tex=True
        )
        self.play(Create(triangle))
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.wait(2)
        self.play(FadeOut(felirat))
        felirat = self.magyarazo_szoveg(
            szoveg="Vegyük fel a belső szögfelezőket!",
            font_size=24,
            duration=1,
            use_tex=False
        )
        self.play(Create(bisector_A), Create(bisector_B), Create(bisector_C))
        self.wait(2)
        self.play(FadeOut(felirat))
        self.play(Write(label_O))
        self.play(Create(in_circle))
        self.wait(1)
        self.play(Create(radius_AB), Create(radius_AC), Create(radius_BC))
        self.wait(1)
        self.play(Write(label_radius_BC), Write(label_a), Write(label_b), Write(label_c))
        self.wait(1)
        self.play(Write(text01))
        self.wait(2)
        self.play(FadeOut(text01))
        self.play(Write(text02))
        self.wait(2)
        self.play(FadeOut(text02))
        current_text = text_list[0]
        self.play(Write(current_text))
        self.wait(3)
        for next_text in text_list[1:]:
            self.play(Transform(current_text, next_text))
            self.wait(3)
        self.play(FadeOut(current_text))
        felirat = self.magyarazo_szoveg(
            szoveg="Vegyük fel a külső szögfelezőket is!",
            font_size=24,
            duration=1,
            use_tex=False
        )
        self.play(Create(kulso_A), Create(kulso_B), Create(kulso_C))
        self.wait(1)
        self.play(FadeOut(felirat))
        self.play(Write(label_O_a), Write(label_O_b), Write(label_O_c))
        self.play(Create(ex_circle_a), Create(ex_circle_b), Create(ex_circle_c))
        self.play(Create(kulso_AB), Write(label_kulso_AB))
        self.play(Create(kulso_AC), Write(label_kulso_AC))
        self.play(Create(kulso_BC), Write(label_kulso_BC))
        felirat = self.magyarazo_szoveg(
            szoveg="Az $ABC$ háromszög oldalpárjaitól\negyenlő távolságú pontok\nmértani helyét keresve azt látjuk,\nhogy a belső és a külső szögfelezők\- hármasával - négy pontban,\naz $O$, $O_a$ $O_b$ és $O_c$\npontokban metszik egymást.",
                      font_size=20,
            duration=3,
            use_tex=True
        )
        self.wait(2)

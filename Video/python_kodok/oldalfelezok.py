from manim import *
import numpy as np
import geo_utils as gu

# Globális háttérszín beállítása
config.background_color = WHITE

# Egyéni MathTex osztály
class MathTex2(MathTex):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, font_size=24, color="#000000", **kwargs)

# Egyéni Tex osztály
class Tex2(Tex):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, font_size=24, color="#000000", **kwargs)

class OldalFelezok(Scene):
    def construct(self):
        # A háromszög csúcsai
        A = np.array([-6, -3, 0])
        B = np.array([1, -1, 0])
        C = np.array([-3, 3, 0])

        # A háromszög
        T_ABC = Polygon(A, B, C, color=BLACK, stroke_width=2)
        Csucsok = [
            MathTex2(r"A").next_to(A, LEFT, buff=0.1),
            MathTex2(r"B").next_to(B, RIGHT, buff=0.1),
            MathTex2(r"C").next_to(C, UP, buff=0.1)
        ]

        # Felezési pontok
        F_AB = (A + B) / 2
        F_AC = (A + C) / 2
        F_BC = (C + B) / 2

        # Normálvektorok
        v = A - B
        n_AB = np.array([v[1], -v[0], 0])
        v = B - C
        n_BC = np.array([v[1], -v[0], 0])
        v = A - C
        n_AC = np.array([v[1], -v[0], 0])

        # Oldalfelező egyenesek
        f_AB = DashedLine(*gu.get_line_endpoints(F_AB, n_AB), stroke_width=1, color=BLACK)
        f_BC = DashedLine(*gu.get_line_endpoints(F_BC, n_BC), stroke_width=1, color=BLACK)
        f_AC = DashedLine(*gu.get_line_endpoints(F_AC, n_AC), stroke_width=1, color="#000080")

        f_AB2 = DashedLine(*gu.get_line_endpoints(F_AB, n_AB), stroke_width=1.5, color="#000080")
        f_BC2 = DashedLine(*gu.get_line_endpoints(F_BC, n_BC), stroke_width=1.5, color="#000080")

        # Oldalfelezők metszéspontja
        O = gu.get_intersection_point(F_AB, n_AB, F_BC, n_BC)
        O_pont = Dot(O, color=RED, radius=0.05)

        # Sugarak
        R_AO = Line(A, O, color="#0000CD", stroke_width=2)
        R_BO = Line(B, O, color="#0000CD", stroke_width=2)
        R_CO = Line(C, O, color="#0000CD", stroke_width=2)

        Sugarak = [
            MathTex2(r"R").next_to(R_AO.get_center(), UP, buff=0.1),
            MathTex2(r"R").next_to(R_BO.get_center(), UP, buff=0.1),
            MathTex2(r"R").next_to(R_CO.get_center(), LEFT, buff=0.1)
        ]

        # Szövegek
        # A szövegek háttere
        TextArea = Rectangle(width=5, height=7).move_to([4, 0, 0])
        TextArea_Bg = Rectangle(width=5.3, height=7.1).move_to([4, 0, 0])
        TextArea_Bg.set_fill(color="#FAEBD7", opacity=0.7)
        # Szövegek
        Lines1 = [
            Tex2(r"\textit{Tétel}: A háromszögek oldalfelező merőlegesei"),  # 0
            Tex2(r"egy pontban metszik egymást."),  # 1
            Tex2(r"\textbf{\textit{Bizonyítás:}}"),  # 2
            Tex2(r"Vegyünk fel egy $ABC$ háromszöget!"),
            Tex2(r"Vegyük fel az $AB$ és $BC$ oldalak felező"),
            Tex2(r"merőlegeseit!"),  # 5
            Tex2(r"E két egyenes biztosan metszi egymást, mert"),
            Tex2(r"akkor $ABC \angle = 180^{\circ}$ lenne, ami lehetetlen."),
            Tex2(r"Legyen a metszéspont $O$"),  # 8
            Tex2(r"Mivel $O$ rajta van az $AB$ oldal"),  # 9
            Tex2(r"felező merőlegesén $OA = OB = R$."),  # 10
            Tex2(r"Mivel $O$ rajta van az $BC$ oldal"),  # 11
            Tex2(r"felező merőlegesén $OB = OC = R$."),  # 12
            Tex2(r"Ez azt jelenti, hogy $OA = OB = OC = R$."),  # 13
            Tex2(r"Vagyis $O$ illeszkedik az $AC$ oldal"),  # 14
            Tex2(r"felezőmerőlegesére is."),  # 15
            Tex2(r"Tehát a háromszög mindhárom felező"),  # 16
            Tex2(r"merőlegese egy ponton megy át."),  # 17
            Tex2(r"Mivel $OA = OB = OC = R$"),  # 18
            Tex2(r"$O$ a háromszög köré írható kör középpontja.")  # 19
        ]

        for i, l in enumerate(Lines1):
            if i == 0:
                l.next_to(TextArea.get_top(), DOWN)
            else:
                l.next_to(Lines1[i-1], DOWN, buff=0.1)
            l.align_to(TextArea, LEFT)

        # Animáció
        self.play(Create(TextArea_Bg))
        self.play(Write(Lines1[0]))  # Kiírja a tételt
        self.play(Write(Lines1[1]))  # Kiírja a tételt
        self.wait(1)
        self.play(Write(Lines1[2]))
        self.play(Write(Lines1[3]))
        self.play(Create(T_ABC))
        for c in Csucsok:
            self.play(Write(c))
        self.play(Write(Lines1[4]), Write(Lines1[5]))
        self.play(Create(f_AB))
        self.play(Create(f_BC))
        self.play(Write(Lines1[6]), Write(Lines1[7]))
        self.play(Create(O_pont))
        self.play(Write(MathTex2(r"O").next_to(O, LEFT + UP, buff=0.07)))
        self.wait(1)
        self.play(Write(Lines1[8]))
        self.play(Write(Lines1[9]))
        self.play(Write(Lines1[10]))
        # Transzformálás f_AB-ból f_AB2-be
        
        self.play(Transform(f_AB, f_AB2, run_time=1))
        
        self.play(Write(Lines1[11]))
        self.play(Write(Lines1[12]))
       
        self.play(Transform(f_BC, f_BC2, run_time=1))
        
        self.play(Create(R_AO), Create(R_BO), Write(Sugarak[0]), Write(Sugarak[1]))
        self.wait(1)

        self.play(Create(R_CO), Write(Sugarak[2]))
        self.wait(1)
        self.play(Write(Lines1[13]))
        self.play(Write(Lines1[14]))
        self.play(Write(Lines1[15]))
        self.play(Create(f_AC))
        self.play(Write(Lines1[16]))
        self.play(Write(Lines1[17]))
        self.wait(2)
        self.play(Write(Lines1[18]), Write(Lines1[19]))
        self.play(Create(Circle(radius=np.linalg.norm(A-O), color="#006400", stroke_width=1).move_to(O)))
        self.wait(5)
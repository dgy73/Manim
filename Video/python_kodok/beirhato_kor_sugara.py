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

class BeirhatoKorSugara(Scene):
    def construct(self):
        # A háromszög csúcsai
        A = np.array([-6, -3, 0])
        B = np.array([1, -1, 0])
        C = np.array([-3, 3, 0])

        # A háromszög
        T_ABC = Polygon(A, B, C, color=BLACK, stroke_width=2)
        Csucsok = [
            MathTex2(r"A").next_to(A, LEFT + UP, buff=0.1),
            MathTex2(r"B").next_to(B, RIGHT + UP, buff=0.1),
            MathTex2(r"C").next_to(C, RIGHT, buff=0.1)
        ]

        Oldalak = [
            MathTex2(r"c").next_to((A+B)/2, DOWN, buff=.1),
            MathTex2(r"a").next_to((C+B)/2, RIGHT, buff=.1),
            MathTex2(r"b").next_to((A+C)/2, LEFT, buff=.1)
        ]

        # Belső szögfelezők
        f_CAB = DashedLine(*gu.get_line_endpoints(A, gu.get_angle_bisectors(C,A,B)[0], scene_bounds=(-7,1.3,-4,4)), color=BLACK, stroke_width=1)
        f_ABC = DashedLine(*gu.get_line_endpoints(B, gu.get_angle_bisectors(A,B,C)[0], scene_bounds=(-7,1.3,-4,4)), color=BLACK, stroke_width=1)
        f_BCA = DashedLine(*gu.get_line_endpoints(C, gu.get_angle_bisectors(B,C,A)[0], scene_bounds=(-7,1.3,-4,4)), color=BLACK, stroke_width=1)


        # Belső szögfelezők metszéspontja
        O = gu.get_intersection_point(A, gu.get_angle_bisectors(C,A,B)[0],B, gu.get_angle_bisectors(A,B,C)[0])
        O_pont = Dot(O, color=RED, radius=0.05)

        # O vetületei az egyenesekre
        O_pr_AB = gu.get_perpendicular_projection(O, A, A-B)
        O_pr_BC = gu.get_perpendicular_projection(O, B, B-C)
        O_pr_CA = gu.get_perpendicular_projection(O, C, A-C)

        # r sugarak
        r_AB_O = Line(O, O_pr_AB, color="#0000CD", stroke_width=2)
        r_BC_O = Line(O, O_pr_BC, color="#0000CD", stroke_width=2)
        r_CA_O = Line(O, O_pr_CA, color="#0000CD", stroke_width=2)

        sugarak = [
            MathTex2(r"r").next_to(r_AB_O.get_center(),RIGHT,buff=.1),
            MathTex2(r"r").next_to(r_BC_O.get_center(),UP,buff=.1),
            MathTex2(r"r").next_to(r_CA_O.get_center(),UP,buff=.1)
        ]

        # derékszögek jelölése
        DP = [
            gu.get_right_angle_notation(O_pr_AB, B-A, .25),
            gu.get_right_angle_notation(O_pr_BC, C-B, .25),
            gu.get_right_angle_notation(O_pr_CA, A-C, .25)
        ]

        # A három háromszög
        T1 = Polygon(A, O, B, color="#191970", stroke_width=2)
        T1.set_fill(color="#191970", opacity=.3)
        T2 = Polygon(B, O, C, color="#FA8072", stroke_width=2)
        T2.set_fill(color="#FA8072", opacity=.3)
        T3 = Polygon(C, O, A, color="#ADFF2F", stroke_width=2)
        T3.set_fill(color="#ADFF2F", opacity=.3)


        # Szövegek
        # A szövegek háttere
        TextArea = Rectangle(width=5, height=7).move_to([4, 0, 0])
        TextArea_Bg = Rectangle(width=5.3, height=7.1).move_to([4, 0, 0])
        TextArea_Bg.set_fill(color="#FAEBD7", opacity=0.7)

        # Rétegek beállítása
        # Először adjuk hozzá a TextArea-t és hátterét a legfelső rétegbe
        
        # TextArea_Bg.z_index = 100  # Magas z_index a TextArea-hoz
        # TextArea.z_index = 101     # Még magasabb z_index a szöveg fölé

        # Szövegek
        Lines1 = [
            Tex2(r"\textit{Tétel}: A háromszögbe írható kör sugara:"),  # 0
            Tex2(r"$r = \dfrac{T}{s}$, ahol $T$ a terület, $s$ a félkerület"),  # 1
            Tex2(r"\textbf{\textit{Bizonyítás:}}"),  # 2
            Tex2(r"Vegyünk fel egy $ABC$ háromszöget!"), #3
            Tex2(r"A háromszög oldalai rendre $a, b, c$"), #4
            Tex2(r"A baírható kör középpontja a belső"),  # 5
            Tex2(r"szögfelezők metszéspontja"), #6
            Tex2(r"Legyen a metszéspont $O$"), #7
            Tex2(r"Állítsunk merőlegeseket $O$-ból az oldalakra"),  # 8
            Tex2(r"$T=T_{AOB}+T_{BOC}+T_{COA}$"),  # 9
            Tex2(r"Az $AOB$ háromszög területe: $T_{AOB}=\dfrac{c\cdot r}{2}$"),  # 10
            Tex2(r"A $BOC$ háromszög területe: $T_{BOC}=\dfrac{a\cdot r}{2}$"),  # 11
            Tex2(r"A $COA$ háromszög területe: $T_{COA}=\dfrac{b\cdot r}{2}$"),  # 12
            Tex2(r"Így az $ABC$ háromszög területe:"),  # 13
            Tex2(r"$T = \dfrac{c\cdot r}{2} + \dfrac{a\cdot r}{2} + \dfrac{c\cdot r}{2} = \dfrac{a+b+c}{2} \cdot r = s \cdot r$ "),  # 14
            Tex2(r"Így $r = \dfrac{T}{s}$"),  # 15
            Tex2(r"Tehát a háromszög mindhárom belső"),  # 16
            Tex2(r"szögfelezője egy ponton megy át."),  # 17
            Tex2(r"Mivel $d(AB, O) = d(BC, O) = d(AC, O) = r$"),  # 18
            Tex2(r"$O$ a háromszög beírható körének középpontja.")  # 19
        ]

        for i, l in enumerate(Lines1):
            if i == 0:
                l.next_to(TextArea.get_top(), DOWN, buff=.1)
            else:
                l.next_to(Lines1[i-1], DOWN, buff=0.1)
            l.align_to(TextArea, LEFT)
            # l.z_index = 102


        # Animáció
        self.play(Create(TextArea_Bg))
        self.play(Write(Lines1[0])) # Kiírja a tételt
        self.play(Write(Lines1[1]))  # Kiírja a tételt
        self.wait(1)
        self.play(Write(Lines1[2]))
        self.play(Write(Lines1[3]))
        self.play(Write(Lines1[4]))
        self.play(Create(T_ABC))
        for c in Csucsok:
            self.play(Write(c))
        for c in Oldalak:
            self.play(Write(c))
        self.play(Write(Lines1[5]))
        self.play(Write(Lines1[6]))
        self.play(Create(f_CAB))
        self.play(Create(f_ABC))
        self.play(Create(f_BCA))
        self.play(Write(Lines1[7]))

        self.play(Create(O_pont))
        self.play(Write(MathTex2(r"O").next_to(O, LEFT + UP, buff=0.1)))
        self.wait(1)
        self.play(Create(Circle(radius=np.linalg.norm(O_pr_AB-O), color="#006400", stroke_width=1).move_to(O)))
        self.play(Write(Lines1[8]))
        self.play(Create(r_CA_O),Create(r_AB_O), Create(r_BC_O))
        self.play(Create(Line(*DP[0][0],color="#0000CD", stroke_width=2)), Create(Line(*DP[0][1],color="#0000CD", stroke_width=2)))
        self.play(Create(Line(*DP[1][0],color="#0000CD", stroke_width=2)), Create(Line(*DP[1][1],color="#0000CD", stroke_width=2)))
        self.play(Create(Line(*DP[2][0],color="#0000CD", stroke_width=2)), Create(Line(*DP[2][1],color="#0000CD", stroke_width=2)))
        self.play(Write(sugarak[0]), Write(sugarak[2]), Write(sugarak[1]))
        self.wait(1)
        self.play(Write(Lines1[9]))
        # AOB háromszög
        self.play(Create(T1))
        self.play(Write(Lines1[10]))
        self.wait(1)
        # BOC háromszög
        self.play(Create(T2))
        self.play(Write(Lines1[11]))
        self.wait(1)
        # COA háromszög
        self.play(Create(T3))
        self.play(Write(Lines1[12]))
        self.wait(1)
        self.play(Write(Lines1[13]))
        self.play(Write(Lines1[14]))
        self.play(Write(Lines1[15]))
        self.wait(10)
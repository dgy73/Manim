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

class BelsoSzogfelezok(Scene):
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

        # Belső szögfelezők
        f_CAB = DashedLine(*gu.get_line_endpoints(A, gu.get_angle_bisectors(C,A,B)[0], scene_bounds=(-7,1.5,-4,4)), color=BLACK, stroke_width=1)
        f_ABC = DashedLine(*gu.get_line_endpoints(B, gu.get_angle_bisectors(A,B,C)[0], scene_bounds=(-7,1.5,-4,4)), color=BLACK, stroke_width=1)
        f_BCA = DashedLine(*gu.get_line_endpoints(C, gu.get_angle_bisectors(B,C,A)[0], scene_bounds=(-7,1.5,-4,4)), color=BLACK, stroke_width=1)


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

        # Szövegek
        # A szövegek háttere
        TextArea = Rectangle(width=5, height=7).move_to([4, 0, 0])
        TextArea_Bg = Rectangle(width=5.3, height=7.1).move_to([4, 0, 0])
        TextArea_Bg.set_fill(color="#FAEBD7", opacity=0.7)
        # Szövegek
        Lines1 = [
            Tex2(r"\textit{Tétel}: A háromszögek belső szögfelezői"),  # 0
            Tex2(r"egy pontban metszik egymást."),  # 1
            Tex2(r"\textbf{\textit{Bizonyítás:}}"),  # 2
            Tex2(r"Vegyünk fel egy $ABC$ háromszöget!"), #3
            Tex2(r"Vegyük fel a $CAB$ és az $ABC$ szögek felező"), #4
            Tex2(r"egyeneseit!"),  # 5
            Tex2(r"E két egyenes biztosan metszi egymást, mert"),
            Tex2(r"ha párhuzamosak, akkor\\ $CAB \angle + ABC \angle = 180^{\circ}$ lenne."),
            Tex2(r"Legyen a metszéspont $O$"),  # 8
            Tex2(r"Mivel $O$ rajta van az $CAB$ szög felezőjén,"),  # 9
            Tex2(r"ezért $d(AC, O) = d(AB, O) = r$."),  # 10
            Tex2(r"Mivel $O$ rajta van az $ABC$ szög felezőjén,"),  # 11
            Tex2(r"ezért $d(AB, O) = d(BC, O) = r$."),  # 12
            Tex2(r"Ez azt jelenti, hogy $d(BC, O) = d(AC, O) = r$."),  # 13
            Tex2(r"Vagyis $O$ illeszkedik az $BCA$ szög"),  # 14
            Tex2(r"felezőjére is."),  # 15
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
        self.play(Write(Lines1[4]))
        self.play(Write(Lines1[5]))
        self.play(Create(f_CAB))
        self.play(Create(f_ABC))
        self.play(Write(Lines1[6]), Write(Lines1[7]), Write(Lines1[8]))

        self.play(Create(O_pont))
        self.play(Write(MathTex2(r"O").next_to(O, LEFT + UP, buff=0.1)))
        self.wait(1)
        self.play(Write(Lines1[9]), Write(Lines1[10]))
        self.play(Create(r_CA_O),Create(r_AB_O))
        self.play(Write(sugarak[0]), Write(sugarak[2]))
        self.wait(1)
        self.play(Write(Lines1[11]), Write(Lines1[12]))
        self.play(Create(r_BC_O))
        self.play(Write(sugarak[1]))
        self.wait(1)
        self.play(Write(Lines1[13]), Write(Lines1[14]), Write(Lines1[15]))
        self.play(Create(f_BCA))
        self.wait(1)
        self.play(Write(Lines1[16]), Write(Lines1[17]))
        self.wait(2)
        self.play(Write(Lines1[18]), Write(Lines1[19]))
        self.play(Create(Circle(radius=np.linalg.norm(O_pr_AB-O), color="#006400", stroke_width=1).move_to(O)))
        self.wait(5)
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

class Heron(Scene):
    def construct(self):
        # A háromszög csúcsai
        A = np.array([-6.5, -3, 0])
        B = np.array([-2.5, -2, 0])
        C = np.array([-5, 1, 0])

        # A háromszög
        T_ABC = Polygon(A, B, C, color=BLACK, stroke_width=2)
        Csucsok = [
            MathTex2(r"A").next_to(A, DOWN, buff=0.1),
            MathTex2(r"B").next_to(B, DOWN, buff=0.1),
            MathTex2(r"C").next_to(C, LEFT, buff=0.1)
        ]

        # Belső szögfelezők
        f_CAB = DashedLine(*gu.get_line_endpoints(A, gu.get_angle_bisectors(C,A,B)[0], scene_bounds=(-7,1.5,-4,4)), color=BLACK, stroke_width=1)
        f_ABC = DashedLine(*gu.get_line_endpoints(B, gu.get_angle_bisectors(A,B,C)[0], scene_bounds=(-7,1.5,-4,4)), color=BLACK, stroke_width=1)
        f_ABC_k = DashedLine(*gu.get_line_endpoints(B, gu.get_angle_bisectors(A,B,C)[1], scene_bounds=(-7,1.5,-4,4)), color=BLACK, stroke_width=1)
        
        # oldalegyenesek
        c_oldal = Line(*gu.get_line_endpoints(A, A-B, scene_bounds=(-7,1.5,-4,4)), color=BLACK, stroke_width=2)
        b_oldal = Line(*gu.get_line_endpoints(A, A-C, scene_bounds=(-7,1.5,-4,4)), color=BLACK, stroke_width=2)

        # Belső és külső szögfelezők metszéspontjai
        O = gu.get_intersection_point(A, gu.get_angle_bisectors(C,A,B)[0],B, gu.get_angle_bisectors(A,B,C)[0])
        O_pont = Dot(O, color=RED, radius=0.05)
        O_a = gu.get_intersection_point(A, gu.get_angle_bisectors(C,A,B)[0],B, gu.get_angle_bisectors(A,B,C)[1])
        O_a_pont = Dot(O_a, color=RED, radius=0.05)

        # O és O_a vetületei az egyenesekre
        O_pr_AB = gu.get_perpendicular_projection(O, A, A-B)
        O_a_pr_AB = gu.get_perpendicular_projection(O_a, A, A-B)
        O_a_pr_AC = gu.get_perpendicular_projection(O_a, A, A-C)
        O_a_pr_BC = gu.get_perpendicular_projection(O_a, B, B-C)

        Erintesi_Pontok_Cimkei = [
            MathTex2(r"E").next_to(O_pr_AB,DOWN,buff=0.1),
            MathTex2(r"F").next_to(O_a_pr_AB,DOWN,buff=0.1),
            MathTex2(r"G").next_to(O_a_pr_AC,LEFT,buff=0.2),
            MathTex2(r"H").next_to(O_a_pr_BC,UP,buff=0.1)
        ]

        Erintesi_Pontok = [
            Dot(O_pr_AB, color="#0000CD", radius=0.03),
            Dot(O_a_pr_AB, color="#0000CD", radius=0.03),
            Dot(O_a_pr_AC, color="#0000CD", radius=0.03),
            Dot(O_a_pr_BC, color="#0000CD", radius=0.03)
        ]
                

        # r sugarak
        Sugarak = [
                Line(O, O_pr_AB, color="#0000CD", stroke_width=1),
                Line(O_a, O_a_pr_AB, color="#0000CD", stroke_width=1),
                Line(O_a, O_a_pr_AC, color="#0000CD", stroke_width=1),
                Line(O_a, O_a_pr_BC, color="#0000CD", stroke_width=1)
        ]
        

        Sugarak_Cimkei = [
            MathTex2(r"\varrho").next_to(Sugarak[0].get_center(),LEFT,buff=.08),
            MathTex2(r"\varrho_{a}").next_to(Sugarak[1].get_center(),RIGHT,buff=.08),
            MathTex2(r"\varrho_{a}").next_to(Sugarak[2].get_center(),RIGHT,buff=.17),
            MathTex2(r"\varrho_{a}").next_to(Sugarak[3].get_center(),UP,buff=.1)
            
        ]

        # derékszögek jelölése
        DP = [
            gu.get_right_angle_notation(O_pr_AB, B-A, .25),
            gu.get_right_angle_notation(O_a_pr_AB, O_a-O_a_pr_AB, .25),
            gu.get_right_angle_notation(O_a_pr_AC, A-C, .25),
            gu.get_right_angle_notation(O_a_pr_BC, B-C, .25),
            gu.get_right_angle_notation(B, O_a-B, .25)
        ]

        DP_Line = []
        for d in DP:
            DP_Line.append(Line(*d[0],color="#0000CD", stroke_width=1))
            DP_Line.append(Line(*d[1],color="#0000CD", stroke_width=1))
            
        

        # körök
        K = Circle(radius=np.linalg.norm(O_pr_AB-O), color="#006400", stroke_width=1).move_to(O)
        K_a = Circle(radius=np.linalg.norm(O_a_pr_AB-O_a), color="#006400", stroke_width=1).move_to(O_a)

        # Szög jelölése a B csúcsnál
        vector_BA = A - B
        vector_BO = O - B
        angle = np.arccos(np.dot(vector_BA, vector_BO) / (np.linalg.norm(vector_BA) * np.linalg.norm(vector_BO)))
        start_angle=np.arctan2(vector_BO[1], vector_BO[0])
        arcB = Arc(radius=.5, start_angle=start_angle, angle=angle, arc_center=B, color="#FF4500", stroke_width=6)
        
        # Szög jelölése a O_a csúcsnál
        vector_O_aB = B - O_a
        vector_O_aF = O_a_pr_AB - O_a
        angle = np.arccos(np.dot(vector_O_aB, vector_O_aF) / (np.linalg.norm(vector_O_aB) * np.linalg.norm(vector_O_aF)))
        start_angle=np.arctan2(vector_O_aB[1], vector_O_aB[0])
        arcO_a = Arc(radius=.5, start_angle=start_angle, angle=angle, arc_center=O_a, color="#FF4500", stroke_width=6)
        




        # Szövegek
        # A szövegek háttere
        TextArea = Rectangle(width=5, height=7).move_to([4.5, 0, 0])
        TextArea_Bg = Rectangle(width=5.3, height=7.1).move_to([4.5, 0, 0])
        TextArea_Bg.set_fill(color="#FAEBD7", opacity=0.7)
        # Szövegek
        Lines1 = [
            Tex2(r"\textit{Tétel}: \textbf{Heron-képlet}:"),  # 0
            Tex2(r"$T = \sqrt{s(s-a)(s-b)(s-c)}$,"),  # 1
            Tex2(r"ahol $T$ a terület, $a, b, c$ a háromszög oldalai,"),  # 2
            Tex2(r" $s$ a félkerület."),  # 3
            Tex2(r"\textbf{\textit{Bizonyítás:}}"),  # 4
            Tex2(r"Vegyünk fel egy $ABC$ háromszöget!"), #5
            Tex2(r"Vegyük fel a $CAB$ szög belső- és az $ABC$ szög"), #6
            Tex2(r"belső- és külső szögfelező egyeneseit!"),  # 7
            Tex2(r"Jelöljük a metszéspontokat az ábra szerint\\ $O$ és $O_a$"), #8
            Tex2(r"Vegyük fel a köröket és az érintési pontokat."), #9
            Tex2(r"Felhasználjuk, hogy $\varrho = \dfrac{T}{s}, \varrho_a = \dfrac{T}{s-a}$"),  # 10
            Tex2(r"Mivel külső pontból húzott érintő"),  # 11
            Tex2(r"szakaszok egyenlőek, $AF = AG$ "),  # 12
            Tex2(r"valamint $BF = BH$ és $CG = CH$."),  # 13
            Tex2(r"Így $AF = AG$ és $AF+AG = a + b + c$"),  # 14
            Tex2(r"ezért $AF = AG = \dfrac{a+b+c}{2} = s$."),  # 15
            Tex2(r"Ez azt jelenti, hogy $BF = s-c$."),  # 16
            Tex2(r"Ismert, hogy $BE = s-b$")  # 17
            
        ]

        for i, l in enumerate(Lines1):
            if i == 0:
                l.next_to(TextArea.get_top(), DOWN, buff=.1)
            else:
                l.next_to(Lines1[i-1], DOWN, buff=0.1)
            l.align_to(TextArea, LEFT)

        Lines2 = [
            Tex2(r"Mivel a belső és külső szögfelezők merőlegesek"), #0
            Tex2(r"$OBO_a \angle = 90^{\circ}$"), #1
            Tex2(r"Ezért $EBO \angle = BO_aF \angle$,"), #2
            Tex2(r"mert merőleges szárú hegyesszögek."), #3
            Tex2(r"Így $EBO \Delta \sim FO_aB \Delta$ "), #4
            Tex2(r"mert szögeik páronként egyenlőek."), #5
            Tex2(r"A megfelelő oldalak arányait felírva: "), #6
            Tex2(r"$\dfrac{\varrho}{s-b}=\dfrac{s-c}{\varrho_a} \rightarrow \varrho \varrho_a = (s-b)(s-c)$ "), #7
            Tex2(r"$\dfrac{T}{s} \dfrac{T}{s-a} = (s-b)(s-c)$"), #8
            Tex2(r"Így $T^2 = s(s-a)(s-b)(s-c)$ ") #9
        ]

        for i, l in enumerate(Lines2):
            if i == 0:
                l.next_to(TextArea.get_top(), DOWN, buff=.1)
            else:
                l.next_to(Lines2[i-1], DOWN, buff=0.1)
            l.align_to(TextArea, LEFT)


        # kapcsos zárójelek
        iranyAF = (A - O_a_pr_AB)/np.linalg.norm(A - O_a_pr_AB)
        normalAF = np.array([-iranyAF[1],iranyAF[0],0])
        kpcsAF = BraceBetweenPoints(A, O_a_pr_AB, direction=normalAF).set_color(RED)
        cimke_AF = MathTex2(r"s").next_to(kpcsAF.get_center(), DOWN, buff=.3)
        kpcsAB = BraceBetweenPoints(A, B, direction=normalAF).set_color("#008000")
        cimke_AB = MathTex2(r"c").next_to(kpcsAB.get_center(), DOWN, buff=.3)
        kpcsBF = BraceBetweenPoints(B, O_a_pr_AB, direction=normalAF).set_color("#008000")
        cimke_BF = MathTex2(r"s-c").next_to(kpcsBF.get_center(), DOWN, buff=.3)

        iranyAG = (A - O_a_pr_AC)/np.linalg.norm(A - O_a_pr_AC)
        normalAG = np.array([-iranyAG[1],iranyAG[0],0])
        kpcsAG = BraceBetweenPoints(A, O_a_pr_AC, direction=-normalAG).set_color(RED)
        cimke_AG = MathTex2(r"s").next_to(kpcsAG.get_center(), LEFT, buff=.3)
        kpcsAC = BraceBetweenPoints(A, C, direction=-normalAG).set_color("#008000")
        cimke_AC = MathTex2(r"b").next_to(kpcsAC.get_center(), UP, buff=.3)
        kpcsCG = BraceBetweenPoints(C, O_a_pr_AC, direction=-normalAG).set_color("#008000")
        cimke_CG = MathTex2(r"s-b").next_to(kpcsCG.get_center(), UP, buff=.3)

        kpcs_s = VGroup(kpcsAF, cimke_AF, kpcsAG, cimke_AG)
        kpcs_AF = VGroup(kpcsAB, cimke_AB, kpcsBF, cimke_BF)

        # érintő szakaszok
        eirnto_s = VGroup(
            Line(A, O_a_pr_AB, color=RED, stroke_width =3),
            Line(A, O_a_pr_AC, color=RED, stroke_width =3)
        )
      
        erinto_CGH = VGroup(
            Line(C, O_a_pr_AC, color="#FF00FF", stroke_width =4),
            Line(C, O_a_pr_BC, color="#FF00FF", stroke_width =4)
        )

        erinto_BFH = VGroup(
            Line(B, O_a_pr_AB, color="#FFFF00", stroke_width =4),
            Line(B, O_a_pr_BC, color="#FFFF00", stroke_width =4)
        )

        szakaszBF = Line(B, O_a_pr_AB, color="#FFFF00", stroke_width =3)
        cimkeBF = MathTex2(r"s-c").next_to(szakaszBF.get_center(), DOWN, buff=.1)
        szakaszBE = Line(B, O_pr_AB, color="#00FF00", stroke_width =3)
        cimkeBE = MathTex2(r"s-b").next_to(szakaszBE.get_center(), DOWN, buff=.1)
        szakaszok =  VGroup(
            szakaszBE, szakaszBF, cimkeBE, cimkeBF
        )
        
        
        # hasonló háromszögek
        # EBO háromszög
        T_EBO = Polygon(O_pr_AB, B, O, color="#00FF00", stroke_width = 1)
        T_EBO.set_fill(color="#00FF00", opacity=.3)
        
        # FOaB háromszög
        T_FOaB = Polygon(O_a_pr_AB, O_a, B, color="#FFFF00", stroke_width = 1)
        T_FOaB.set_fill(color="#FFFF00", opacity=.3)
        
        # Animáció
        self.play(Create(TextArea_Bg))
        self.play(*[Write(l) for l in Lines1[:4]])
        self.wait(2)
        self.play(Write(Lines1[4]))
        self.play(*[Write(l) for l in Lines1[5:10]])
        self.play(Create(T_ABC))
        for c in Csucsok:
            self.play(Write(c))
        self.play(Create(b_oldal), Create(c_oldal))
        self.play(Create(f_ABC), Create(f_CAB), Create(f_ABC_k))
        self.play(Create(O_pont), Create(O_a_pont))
        self.play(Write(MathTex2(r"O").next_to(O, UP, buff=0.1)))
        self.play(Write(MathTex2(r"O_a").next_to(O_a, UP, buff=0.1)))

        self.play(Create(K), Create(K_a))
        self.play(*[Create(d) for d in Erintesi_Pontok])
        self.play(*[Write(c) for c in Erintesi_Pontok_Cimkei])
        self.play(*[Create(s) for s in Sugarak])
        self.play(*[Write(c) for c in Sugarak_Cimkei])
        self.play(*[Create(d) for d in DP_Line[:8]])
        self.play(Write(Lines1[10]))
        self.play(*[FadeOut(c) for c in Sugarak_Cimkei[:2]])
        self.play(Write(MathTex2(r"\varrho=\dfrac{T}{s}").next_to(Sugarak[0].get_center(),LEFT,buff=.08)))
        self.play(Write(MathTex2(r"\varrho_{a}=\dfrac{T}{s-a}").next_to(Sugarak[1].get_center(),RIGHT,buff=.08)))
        self.wait(2)
        self.play(*[Write(l) for l in Lines1[11:13]])
        self.play(Create(eirnto_s))
        self.wait(2)      
        self.play(FadeOut(eirnto_s))
        self.play(Write(Lines1[13]))
        self.play(Create(erinto_BFH))
        self.wait(2)
        self.play(Create(erinto_CGH))
        self.wait(2)
        self.play(Write(Lines1[14]))
        self.play(Write(Lines1[15]))
        self.play(FadeOut(erinto_BFH))
        self.play(FadeOut(erinto_CGH))
        self.play(Create(kpcs_s))
        self.wait(2)
        self.play(FadeOut(kpcs_s))
        self.wait(2)
        self.play(Write(Lines1[16]))
        self.play(Create(kpcs_AF))
        self.wait(2)
        self.play(FadeOut(kpcs_AF))
        self.play(Write(Lines1[17]))
        self.play(Create(szakaszok))
        self.wait(2)
        self.play(*[FadeOut(l) for l in Lines1])
        self.play(Write(Lines2[0]))
        self.play(Write(Lines2[1])) 
        self.play(*[Create(d) for d in DP_Line[8:]])
        self.wait(2)
        self.play(Write(Lines2[2]))
        self.play(Write(Lines2[3])) 

        self.play(Create(arcB))
        self.play(Create(arcO_a))
        self.play(Write(Lines2[4]))
        self.play(Write(Lines2[5]))
        self.play(Create(T_EBO)) 
        self.play(Create(T_FOaB))
        self.wait(1) 
        self.play(Write(Lines2[6]))
        self.play(Write(Lines2[7]))
        self.play(Write(Lines2[8]))
        self.play(Write(Lines2[9]))

        self.wait(5)
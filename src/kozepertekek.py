from manim import *
import numpy as np

#
# manim -pqh kozepertekek.py Kozepertekek

# Egyéni MathTex osztály
class MathTex2(MathTex):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, font_size=28, **kwargs)

class Kozepertekek(Scene):


    def construct(self):

        # a két szakasz: a >= b
        a = 10
        b = 4

        # a sugár r meghatározása
        r = (a-b)/2

        delta = (a-14)//2  #ezzel eltolom a képernyő középpontjától
        derekszog = 0.3 # a derekszögek oldalhossza

        # Csúcsok
        A = np.array([delta,0,0])
        
        N = np.array([-r+A[0],0,0])
                
        P = np.array([r+A[0],0,0])
                
        
        Q = np.array([A[0],r,0])
        
        M = np.array([(a+b)/2+A[0],0,0])
        
        H = np.array([(a+b)/2-2*a*b/(a+b)+A[0],0,0])
        G = np.array([(a+b)/2-2*a*b/(a+b)+A[0],-np.sqrt(r**2-((a+b)/2-2*a*b/(a+b))**2),0])

        # Hogy az eltérő színű szakaszok ne takarják egymást, eltoljuk egymás alá vagy fölé
        elt = 0.05
        v = np.array([0,elt,0])
        # Pontok felvétele

        Pont_A = Dot(A, color=RED)
        labelA = MathTex2("A", color=GRAY).next_to(A, UP+LEFT, buff=0.1)
        Pont_N = Dot(N, color=GRAY)
        labelN = MathTex2("N", color=GRAY).next_to(N, UP+LEFT, buff=0.1)
        Pont_M = Dot(M, color=GRAY)
        labelM = MathTex2("M", color=GRAY).next_to(M, UP, buff=0.1)
        Pont_P = Dot(P, color=GRAY)
        labelP = MathTex2("P", color=GRAY).next_to(P, UP+LEFT, buff=0.1)
        Pont_Q = Dot(Q, color=GRAY)
        labelQ = MathTex2("Q", color=GRAY).next_to(Q, UP+LEFT, buff=0.2)
        Pont_G = Dot(G, color=GREEN)
        labelG = MathTex2("G", color=GREEN).next_to(G, DOWN, buff=0.2)
        Pont_H = Dot(H, color=PURPLE)
        labelH = MathTex2("H", color=PURPLE).next_to(H, UP, buff=.1)

        # Szakaszok felvétele
        # a szakasz
        szakaszNM = Line(N,M, color=RED)
        Label_szakaszNM = MathTex2("a", color=RED).next_to(szakaszNM.get_center(),UP+RIGHT, buff=0.1)
        # b szakasz, a felett elt értékkel
        szakaszMP = Line(M+v,P+v,color=BLUE)
        Label_szakaszMP = MathTex2("b", color=BLUE).next_to(szakaszMP.get_center(), UP, buff=0.2)
        # számtani közép MA szakasz
        szakaszMA = Line(M-v, A-v, color=ORANGE)
        Label_szakaszMA = MathTex2("A=\dfrac{a+b}{2}", color=ORANGE).next_to(szakaszMA.get_center(), DOWN+3*LEFT, buff=0.2)
        # harmonikus közép MH szakasz
        szakaszMH = Line(M-2*v, H-2*v, color=PURPLE)
        Label_szakaszMH = MathTex2("H=\dfrac{2 a b}{a+b}", color=PURPLE).next_to(szakaszMH.get_center(), DOWN, buff=0.2)
        # AQ sugár 
        szakaszAQ = Line(A,Q, color=GRAY)
        Label_szakaszAQ = MathTex2("r = \dfrac{a-b}{2}").next_to(szakaszAQ.get_center(), LEFT, buff=.2)
        
        
        # geometriai közép MG szakasz
        szakaszMG = Line(M,G, color=GREEN)
        Label_szakaszMG = MathTex2("G = \sqrt{a \cdot b}").next_to(szakaszMG.get_center(), .5*RIGHT+2*DOWN, buff=.2)
        Label_szakaszMG1 = MathTex2(
            r"\text{Pitagorasz tétel alapján:} \\",
            r"MA^2 - AG^2 = MG^2 \text{, így } MG = \sqrt{MA^2 - AG^2}\\",
            r"MG = \sqrt{\left(\dfrac{a+b}{2}\right)^2- \left( \dfrac{a-b}{2} \right)^2 } = \sqrt{ab}",
            color = GREEN
        ).next_to([G[0], G[1]/2, 0], DOWN+RIGHT, buff=0.2, aligned_edge=UP+LEFT)
        Label_szakaszMG = MathTex2(
            "G=\sqrt{ab}",
            color= GREEN
            
            ).next_to(szakaszMG.get_center(), DOWN+RIGHT, buff=.1)
        
        
        # négyzetes közép MQ szakasz
        szakaszMQ = Line(M,Q, color=BLUE_A)
        Label_szakaszMQ1 = MathTex2(
        r"\text{Pitagorasz tétel alapján:} \\",
        r"\sqrt{AM^2 + AQ^2} = MQ \\",
        r"MQ = \sqrt{\left( \dfrac{a+b}{2} \right)^2 + \left( \dfrac{a-b}{2} \right)^2} = \sqrt{\dfrac{a^2 + b^2}{2}}",
        color = BLUE_A
        ).next_to(Q, DOWN+RIGHT, buff=0.2, aligned_edge=UP+LEFT)
        Label_szakaszMQ = MathTex2(
            "Q=\sqrt{\dfrac{a^2+b^2}{2}}",
            color= BLUE_A
            
            ).next_to(szakaszMQ.get_center(), UP+RIGHT, buff=.1)

        # harmonikus közép
        szakasz_GH = Line(G, H, color=GRAY)
        Label_szakaszGH1 = MathTex2(
            r"\text{Az }AGM \text{ derékszögű háromszögben a befogótétel alapján:} \\",
            r"GM = \sqrt{AM \cdot HM} \text{, így } HM = \dfrac{GM^2}{AM} \\",
            r"HM=\dfrac{a\cdot b}{\dfrac{a+b}{2}} = \dfrac{2\cdot a \cdot b}{a+b}"
        ).next_to(Q, DOWN+RIGHT, buff=0.2, aligned_edge=UP+LEFT)


        szakasz_AG = Line(A, G, color=GRAY)
        Label_szakaszAG = MathTex2("r = \dfrac{a-b}{2}").next_to(szakasz_AG.get_center(), LEFT, buff=.2)


        # kapcsos zárójelek
        kapcs_NP = BraceBetweenPoints(N,P,direction=DOWN).set_color(RED).shift(DOWN*0.1)
        label_NP = MathTex2(r"a-b", color=RED).next_to(kapcs_NP, DOWN, buff=0.05)
        kapcs_NA = BraceBetweenPoints(N,A,direction=DOWN).set_color(RED).shift(DOWN*0.1)
        label_NA = MathTex2(r"\dfrac{a-b}{2}", color=RED).next_to(kapcs_NA, DOWN, buff=0.05)
        kapcs_PA = BraceBetweenPoints(P,A,direction=DOWN).set_color(RED).shift(DOWN*0.1)
        label_PA = MathTex2(r"\dfrac{a-b}{2}", color=RED).next_to(kapcs_PA, DOWN, buff=0.05)
        kapcs_MA = BraceBetweenPoints(M,A,direction=DOWN).set_color(RED).shift(DOWN*0.1)
        label_MA = MathTex2(r"\dfrac{a-b}{2}+b=\dfrac{a+b}{2}", color=RED).next_to(kapcs_MA, DOWN, buff=0.05)

        # Kör
        CC = Circle(radius=r, color=GRAY).move_to(A)

        # derékszögek jelölése
        # QAP szög
        QAPSzog = Polygon(
            A, [A[0], A[1]+derekszog, 0], [A[0]+derekszog, A[1]+derekszog, 0], [A[0]+derekszog, A[1], 0],
            color= GRAY,
            fill_opacity = 0,
            stroke_width = 2
        )

        # AGM szög
        v1 = A-G
        v2 = M-G
        AGMszog = Polygon(
            G + derekszog * v1/np.linalg.norm(v1), G + derekszog*v1/np.linalg.norm(v1) + derekszog*v2/np.linalg.norm(v2), G + derekszog*v2/np.linalg.norm(v2),G,
            color = GRAY,
            fill_opacity = 0,
            stroke_width = 2

        )
        
        # GHM szög
        v1 = G-H
        v2 = M-H
        GHMszog = Polygon(
            H + derekszog * v1/np.linalg.norm(v1), H + derekszog*v1/np.linalg.norm(v1) + derekszog*v2/np.linalg.norm(v2), H + derekszog*v2/np.linalg.norm(v2),H,
            color = GRAY,
            fill_opacity = 0,
            stroke_width = 2

        )

        #  Nyitókép szövegei
        nyito = [MathTex(r"\text{Középértékek}"),
         MathTex2(r"\text{Adott egy } n \text{ elemű pozitív valós számokból álló számhalmaz} \\",
                  r"a_1,a_2,\dots a_n \in \mathbb{R}^+ \text{, ekkor } K \in \mathbb{R}^+ \text{ a minta középértéke, ha } \\",
                  r"\min(a_1,a_2,\dots , a_n) \leq K \leq \max(a_1, a_2, \dots , a_n) "
                  
                  ),
                  MathTex2(r"\text{Ez a rövid videó két pozitív valós szám } a, b \in \mathbb{R}^+ \text{ négy középértékének geometriai vizualizációját mutatja be.}"),
                  MathTex2(r"A: \text{ Aritmetikai vagy számtani, } G: \text{ Geometriai, } H: \text{ Harmonikus, } Q: \text{ Quadratikus, vagy négyzetes közép.}")        
        ]

        # A téglalapok amikre írni fogunk
        # A négyzetes közép téglalapja 
        TeglalapNegyzetesKozephez = Polygon (
            Q, [Q[0], (A[1]+Q[1])/2-1,0], [M[0], (A[1]+Q[1])/2-1,0], [M[0],Q[1],0],
            color = BLACK,
            fill_opacity = 1,
            stroke_width = 0
        )
        # A geometriai közép téglalapja 
        TeglalapGeometriaiKozephez = Polygon (
            G, [G[0], G[1]/2, 0], [M[0], G[1]/2 ,0], [M[0],G[1],0],
            color = BLACK,
            fill_opacity = 1,
            stroke_width = 0
        )

        # Ívek a végére
        # Quadratikus, vagy négyzetes középhez
        QQ = [M[0]-np.sqrt((a**2+b**2)/2),M[1],0]
        Pont_QQ = Dot(QQ, color=BLUE_A)
        Label_QQ = MathTex2(r"Q", color=BLUE_A).next_to(QQ, UP+LEFT, buff=.1)
        # Ív létrehozása Q és QQ között
        # Először hozzuk létre az ívet, majd tegyük szaggatottá
        arcQ = ArcBetweenPoints(Q, QQ, radius=np.sqrt((a ** 2 +b ** 2)/2),  stroke_width=1)
        dashed_arcQ = DashedVMobject(arcQ, num_dashes=15)  # Szaggatott ív
        # Geometrai középhez
        GG = [M[0]-np.sqrt(a*b),M[1],0]
        Pont_GG = Dot(GG, color=GREEN)
        Label_GG = MathTex2(r"G", color=GREEN).next_to(GG, UP+LEFT, buff=.1)
        # Ív létrehozása G és GG között
        # Először hozzuk létre az ívet, majd tegyük szaggatottá
        arcG = ArcBetweenPoints(GG, G, radius=np.sqrt(a*b),  stroke_width=1, color=GREEN)
        dashed_arcG = DashedVMobject(arcG, num_dashes=15)  # Szaggatott ív
        
        zaroszovegek = [
            MathTex(r"Q \geq A \geq G \geq H"),
            MathTex2(r"\sqrt{\dfrac{a^2+b^2}{2}} \geq \dfrac{a+b}{2} \geq \sqrt{a \cdot b} \geq \dfrac{2 \cdot a \cdot b}{a+b} \text{, ahol } a, b \in \mathbb{R}^+")
        ]

        # Animáció
        self.wait(2)
        for t in nyito:
            self.play(Write(t))
            self.wait(5)
            self.play(FadeOut(t))
        self.play(Create(szakaszNM), Write(Label_szakaszNM))
        self.play(Create(Pont_M), Write(labelM))
        self.play(Create(Pont_N), Write(labelN))
        self.wait(2)


        self.play(Create(szakaszMP), Write(Label_szakaszMP))
        self.play(Create(Pont_P), Write(labelP))
        self.wait(5)
        
        self.play(Create(kapcs_NP), Write(label_NP))
        self.wait(5)
        self.play(Create(Pont_A))
        self.play(FadeOut(kapcs_NP), FadeOut(label_NP))
        self.play(Create(kapcs_NA), Write(label_NA))
        self.play(Create(kapcs_PA), Write(label_PA))
        self.wait(5)
        self.play(FadeOut(kapcs_NA), FadeOut(label_NA))
        self.play(FadeOut(kapcs_PA), FadeOut(label_PA))
        self.play(Create(kapcs_MA), Write(label_MA))
        self.wait(5)
        self.play(FadeOut(kapcs_MA), FadeOut(label_MA))
        self.play(Create(szakaszMA), Write(Label_szakaszMA), Write(labelA))
        self.wait(5)
        self.play(Create(CC))
        self.play(Create(Pont_Q), Write(labelQ))
        self.play(Create(szakaszAQ), Write(Label_szakaszAQ))
        self.play(Create(QAPSzog))
        self.wait(2)
        # Négyzetes közép megrajzolása
        self.play(Create(szakaszMQ))
        self.play(Create(TeglalapNegyzetesKozephez), Write(Label_szakaszMQ1))
        self.wait(5)
        self.play(FadeOut(Label_szakaszMQ1))
        self.wait(1)
        self.play(FadeOut(TeglalapNegyzetesKozephez))
        self.play(Write(Label_szakaszMQ))
        self.wait(2)
        # Geometrai közép megrajzolása
        self.play(Create(szakaszMG))
        self.play(Create(Pont_G), Write(labelG))
        self.play(Create(szakasz_AG), Write(Label_szakaszAG), Create(AGMszog))

        self.wait(2)
        
        self.play(Create(TeglalapGeometriaiKozephez), Write(Label_szakaszMG1))
        self.wait(5)
        self.play(FadeOut(Label_szakaszMG1), FadeOut(TeglalapGeometriaiKozephez))
        self.play(Write(Label_szakaszMG))
        self.wait(2)
        # Harmonikus közép
        self.play(Create(szakasz_GH), Create(Pont_H), Create(GHMszog), Write(labelH))
        self.wait(1)
        self.play(Create(TeglalapNegyzetesKozephez), Write(Label_szakaszGH1))
        self.wait(5)
        self.play(FadeOut(TeglalapNegyzetesKozephez), FadeOut(Label_szakaszGH1))
        self.play(Create(szakaszMH), Write(Label_szakaszMH))
        
        # A középértékek összehasonlítása
        self.play(Create(dashed_arcQ)) 
        self.play(Create(Pont_QQ),Write(Label_QQ))

        self.play(Create(dashed_arcG)) 
        self.play(Create(Pont_GG),Write(Label_GG))
        
        amimarad = VGroup(Pont_GG, Label_GG, Pont_QQ, Label_QQ, Pont_A, labelA, Pont_H, labelH)
        objects_to_fade = [m for m in self.mobjects if m not in amimarad]
        self.play(*[FadeOut(obj) for obj in objects_to_fade], run_time=1)
        self.wait(2)
        self.play(*[FadeOut(obj) for obj in amimarad], run_time=1)
        for t in zaroszovegek:
            self.play(Write(t))
            self.wait(5)
            self.play(FadeOut(t))



        self.wait(2)
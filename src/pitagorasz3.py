from manim import *
import numpy as np
from math import sqrt

class Pitagorasz(Scene):
    def construct(self):
        # A háromszög oldalainak hossza
        szorzo = 0.4
        a = 3 * szorzo
        b = 4 * szorzo
        c = sqrt(a**2+b**2)
        # A háromszög csúcsai
        A = np.array([0,0,0])
        B = np.array([a,0,0])
        C = np.array([0,b,0])

        # A négyzetek csúcsai
        A1 = np.array([0,-a,0])
        A2 = np.array([a,-a,0])
        B1 = np.array([-b,0,0])
        B2 = np.array([-b,b,0])
        C1 = B + np.array([b,a,0])
        C2 = C + np.array([b,a,0])
        

        # Háromszög létrehozása
        triangle = Polygon(A, B, C, color=WHITE, fill_opacity=0.5).set_stroke(WHITE, 1)

        # Oldalak jelölése
        label_a = Tex("$a$").next_to(Line(A, B).get_midpoint(), DOWN, buff=0.1)
        label_b = Tex("$b$").next_to(Line(A, C).get_midpoint(), LEFT, buff=0.1)
        label_c = Tex("$c$").next_to(Line(B, C).get_midpoint(), RIGHT, buff=0.1)


        # Négyszögek az oldalakra írva
        N_aold = Polygon(A,B,A2,A1).set_fill(color=RED, opacity=0.5).set_stroke(RED, 1)
        N_bold = Polygon(A,C,B2,B1).set_fill(color=GREEN, opacity=0.5).set_stroke(GREEN, 1)
        N_cold = Polygon(B,C1,C2,C).set_fill(color=BLUE_A, opacity=0.5).set_stroke(BLUE_A, 1)
        
        #Négyszögekhez tartozó kapcsos zárójelek
        kapcs_af = BraceBetweenPoints(A,A1,direction=LEFT).set_color(RED).shift(RIGHT*0.1)
        label_af = kapcs_af.get_tex("a", buff=0.05).set_color(RED)
        kapcs_av = BraceBetweenPoints(A1,A2,direction=DOWN).set_color(RED).shift(UP*0.1)
        label_av = kapcs_av.get_tex("a", buff=0.05).set_color(RED)
        kapcs_bf = BraceBetweenPoints(B1,B2,direction=LEFT).set_color(GREEN).shift(RIGHT*0.1)
        label_bf = kapcs_bf.get_tex("b", buff=0.05).set_color(GREEN)
        kapcs_bv = BraceBetweenPoints(C,B2,direction=UP).set_color(GREEN).shift(DOWN*0.1)
        label_bv = kapcs_bv.get_tex("b", buff=0.05).set_color(GREEN)
        
        # normálvektor kiszámítása egyszer
        irany_BC1 = C1 - B
        normal_BC1 = np.array([-irany_BC1[1], irany_BC1[0], 0])
        normal_BC1 = normal_BC1 / np.linalg.norm(normal_BC1)

        irany_BC1 = irany_BC1 / np.linalg.norm(irany_BC1)

        # zárójel B és C1 között
        kapcs_BC1 = BraceBetweenPoints(B, C1, direction=-normal_BC1).set_color(BLUE)
        label_BC1 = kapcs_BC1.get_tex("c", buff=0.05).set_color(BLUE)

        # zárójel C1 és C2 között
        kapcs_C1C2 = BraceBetweenPoints(C1, C2, direction=irany_BC1).set_color(BLUE)
        label_C1C2 = kapcs_C1C2.get_tex("c", buff=0.05).set_color(BLUE)




        alapabra = VGroup(
            triangle, 
            N_aold, N_bold, N_cold, 
            label_a, label_b, label_c,
            kapcs_af, kapcs_av, kapcs_bf, kapcs_bv,kapcs_BC1,kapcs_C1C2,
            label_af, label_av, label_bf, label_bv, label_BC1, label_C1C2 
            )
        alapabra.move_to(ORIGIN)

        kezdoszoveg = Tex("Tekintsünk egy $a$ és $b$ befogójú $c$ átfogójú derészögű háromszöget.")
        # Animáció
        self.play(Write(kezdoszoveg))
        self.wait(2)
        self.play(FadeOut(kezdoszoveg))
        self.play(Create(triangle))
        self.wait(1)
        self.play(Write(label_a),Write(label_b),Write(label_c))
        self.wait(1)
        self.play(FadeOut(label_a), FadeOut(label_b), FadeOut(label_c))
        self.play(Create(N_aold))
        self.wait(.5)
        self.play(Create(N_bold))
        self.wait(.5)
        self.play(Create(N_cold))
        self.wait(.5)
        # animáció
        self.play(Create(kapcs_af), Write(label_af))
        self.play(Create(kapcs_av), Write(label_av))
        self.play(Create(kapcs_bf), Write(label_bf))
        self.play(Create(kapcs_bv), Write(label_bv))
        self.play(Create(kapcs_BC1), Write(label_BC1))
        self.play(Create(kapcs_C1C2), Write(label_C1C2))
        alapabra.remove(label_a, label_b, label_c)
        self.play(alapabra.animate.to_corner(UP + RIGHT))
        self.wait(2)

        # Az elmozgatott háromszög csúcsainak lekérdezése
        A_m, B_m, C_m = triangle.get_vertices()
        
        
        elso = [
            [0,0,0],[a,0,0], [a+b,0,0], [a+b,a,0], [a+b,a+b,0], [a,a+b,0],
            [0,a+b,0], [0,a,0], [a,a,0]
        ]
        elso_pontok = VGroup()
        for p in elso:
            elso_pontok.add(Dot(p))
        
        elso_pontok.move_to(2.2*UP + 4*LEFT)
        elso_poziciok = [dot.get_center() for dot in elso_pontok]

        # Az alapvonal – AB
        alap_vonal = Line(A_m, B_m).set_stroke(RED, 6)
        self.play(Create(alap_vonal))
        self.wait(1)

        # Itt fogjuk gyűjteni a létrejött "átalakult" vonalakat
        transzformalt_vonalaka = VGroup()

        # A célpozíciók
        parok = [(0, 1), (2, 3), (5, 6), (7, 0)]

        for i, j in parok:
            cel_vonal = Line(elso_poziciok[i], elso_poziciok[j]).set_stroke(RED, 6)
            self.play(TransformFromCopy(alap_vonal, cel_vonal))
            transzformalt_vonalaka.add(cel_vonal)
            self.wait(0.5)

        # Az alapvonal – AC
        alap_vonal = Line(A_m, C_m).set_stroke(GREEN, 6)
        self.play(Create(alap_vonal))
        self.wait(1)

        # Itt fogjuk gyűjteni a létrejött "átalakult" vonalakat
        transzformalt_vonalakb = VGroup()

        # A célpozíciók
        parok = [(1, 2), (3, 4), (4, 5), (6, 7)]

        for i, j in parok:
            cel_vonal = Line(elso_poziciok[i], elso_poziciok[j]).set_stroke(GREEN, 6)
            self.play(TransformFromCopy(alap_vonal, cel_vonal))
            transzformalt_vonalakb.add(cel_vonal)
            self.wait(0.5)

        masodik = [
            [0,0,0],[a,0,0], [a+b,0,0], [a+b,a,0], [a+b,a+b,0], [b,a+b,0],
            [0,a+b,0], [0,b,0]
        ]
        masodik_pontok = VGroup()
        for p in masodik:
            masodik_pontok.add(Dot(p))
        
        masodik_pontok.move_to(1.8*DOWN + 4*LEFT)
        masodik_poziciok = [dot.get_center() for dot in masodik_pontok]

        # Az alapvonal – AB
        alap_vonal = Line(A_m, B_m).set_stroke(RED, 6)
        self.play(Create(alap_vonal))
        self.wait(1)

        # Itt fogjuk gyűjteni a létrejött "átalakult" vonalakat
        transzformalt_vonalaka2 = VGroup()

        # A célpozíciók
        parok = [(0, 1), (2, 3), (4, 5), (6, 7)]

        for i, j in parok:
            cel_vonal = Line(masodik_poziciok[i], masodik_poziciok[j]).set_stroke(RED, 6)
            self.play(TransformFromCopy(alap_vonal, cel_vonal))
            transzformalt_vonalaka2.add(cel_vonal)
            self.wait(0.5)

        # Az alapvonal – AC
        alap_vonal = Line(A_m, C_m).set_stroke(GREEN, 6)
        self.play(Create(alap_vonal))
        self.wait(1)

        # Itt fogjuk gyűjteni a létrejött "átalakult" vonalakat
        transzformalt_vonalakb2 = VGroup()

        # A célpozíciók
        parok = [(1, 2), (3, 4), (5, 6), (7, 0)]

        for i, j in parok:
            cel_vonal = Line(masodik_poziciok[i], masodik_poziciok[j]).set_stroke(GREEN, 6)
            self.play(TransformFromCopy(alap_vonal, cel_vonal))
            transzformalt_vonalakb2.add(cel_vonal)
            self.wait(0.5)

        #kapcsos zárójelek és feliratok
        #vízszintesek
        brace_a = BraceBetweenPoints(
            elso_poziciok[0], 
            elso_poziciok[1], 
            direction=DOWN
        ).set_color(RED).shift(UP * 0.1)
        brace_a2 = BraceBetweenPoints(
            masodik_poziciok[0], 
            masodik_poziciok[1], 
            direction=DOWN
        ).set_color(RED).shift(UP * 0.1)
        brace_b = BraceBetweenPoints(
            elso_poziciok[1], 
            elso_poziciok[2], 
            direction=DOWN
        ).set_color(GREEN).shift(UP * 0.1)
        brace_b2 = BraceBetweenPoints(
            masodik_poziciok[1], 
            masodik_poziciok[2], 
            direction=DOWN
        ).set_color(GREEN).shift(UP * 0.1)
        #függőlegesek
        brace_a_f = BraceBetweenPoints(
            elso_poziciok[0], 
            elso_poziciok[7], 
            direction=LEFT
        ).set_color(RED).shift(RIGHT * 0.1)
        brace_a2_f = BraceBetweenPoints(
            masodik_poziciok[6], 
            masodik_poziciok[7], 
            direction=LEFT
        ).set_color(RED).shift(RIGHT * 0.1)
        brace_b_f = BraceBetweenPoints(
            elso_poziciok[6], 
            elso_poziciok[7], 
            direction=LEFT
        ).set_color(GREEN).shift(RIGHT * 0.1)
        brace_b2_f = BraceBetweenPoints(
            masodik_poziciok[0], 
            masodik_poziciok[7], 
            direction=LEFT
        ).set_color(GREEN).shift(RIGHT * 0.1)
        #vízszintes feliratok 
        brace_a_label = brace_a.get_tex("a", buff=0.05).set_color(RED)
        brace_a_label2 = brace_a2.get_tex("a", buff=0.05).set_color(RED)
        brace_b_label = brace_b.get_tex("b", buff=0.05).set_color(GREEN)
        brace_b_label2 = brace_b2.get_tex("b", buff=0.05).set_color(GREEN)
        #függőleges feliratok 
        brace_af_label = brace_a_f.get_tex("a", buff=0.05).set_color(RED)
        brace_af_label2 = brace_a2_f.get_tex("a", buff=0.05).set_color(RED)
        brace_bf_label = brace_b_f.get_tex("b", buff=0.05).set_color(GREEN)
        brace_bf_label2 = brace_b2_f.get_tex("b", buff=0.05).set_color(GREEN)
        #vízszintes kapcsoszárójelek és feliratok megjelenítése
        self.play(Create(brace_a), Write(brace_a_label))
        self.play(Create(brace_a2), Write(brace_a_label2))
        self.play(Create(brace_b), Write(brace_b_label))
        self.play(Create(brace_b2), Write(brace_b_label2))
        #függőleges kapcsoszárójelek és feliratok megjelenítése
        self.play(Create(brace_a_f), Write(brace_af_label))
        self.play(Create(brace_a2_f), Write(brace_af_label2))
        self.play(Create(brace_b_f), Write(brace_bf_label))
        self.play(Create(brace_b2_f), Write(brace_bf_label2))
        self.wait(1)




        #a és b oldalú négyzet az a+b oldalú négyzetbe való transzformálása
        A_m,B_m,A2_m,A1_m = N_aold.get_vertices()
        A_m,C_m,B2_m,B1_m = N_bold.get_vertices()
        N_aold_m = Polygon(A_m,B_m,A2_m,A1_m).set_fill(color=RED, opacity=0.5).set_stroke(RED, 1)
        N_bold_m = Polygon(A_m,C_m,B2_m,B1_m).set_fill(color=GREEN, opacity=0.5).set_stroke(GREEN, 1)
        self.play(Create(N_aold_m), Create(N_bold_m))
        self.wait(1)
        cel_N_aold = Polygon(*[elso_poziciok[i] for i in (7,8,1,0)]).set_fill(color=RED, opacity=0.5).set_stroke(RED, 1)
        cel_N_bold = Polygon(*[elso_poziciok[i] for i in (3,4,5,8)]).set_fill(color=GREEN, opacity=0.5).set_stroke(GREEN, 1)
        self.play(TransformFromCopy(N_aold_m, cel_N_aold), TransformFromCopy(N_bold_m,cel_N_bold))
        self.wait(1)




        #c oldalú négyzet a+b oldalú négyzetbe való transzformálása
        B_m,C1_m,C2_m,C_m = N_cold.get_vertices()
        N_cold_m = Polygon(B_m,C1_m,C2_m,C_m).set_fill(color=BLUE_A, opacity=0.5).set_stroke(BLUE_A, 1)
        self.play(Create(N_cold_m))
        self.wait(1)
        cel_N_cold = Polygon(masodik_poziciok[1],masodik_poziciok[3],masodik_poziciok[5], masodik_poziciok[7]).set_fill(color=BLUE_A, opacity=0.5).set_stroke(BLUE_A, 1)
        self.play(TransformFromCopy(N_cold_m,cel_N_cold))
        self.wait(1)

        #a háromszögek bedobálása a két a+b oldalú négyzetbe
        haromszog_m  = Polygon(A_m, B_m, C_m, color=WHITE, fill_opacity=0.7).set_stroke(WHITE, 1)
        cel11 = Polygon(*[elso_poziciok[i] for i in (2,3,1)], color=WHITE, fill_opacity=0.7).set_stroke(WHITE, 1)
        cel12 = Polygon(*[elso_poziciok[i] for i in (8,1,3)], color=WHITE, fill_opacity=0.7).set_stroke(WHITE, 1)
        cel13 = Polygon(*[elso_poziciok[i] for i in (6,5,7)], color=WHITE, fill_opacity=0.7).set_stroke(WHITE, 1)
        cel14 = Polygon(*[elso_poziciok[i] for i in (8,7,5)], color=WHITE, fill_opacity=0.7).set_stroke(WHITE, 1)
        cel21 = Polygon(*[masodik_poziciok[i] for i in (2,3,1)], color=WHITE, fill_opacity=0.7).set_stroke(WHITE, 1)
        cel22 = Polygon(*[masodik_poziciok[i] for i in (4,5,3)], color=WHITE, fill_opacity=0.7).set_stroke(WHITE, 1)
        cel23 = Polygon(*[masodik_poziciok[i] for i in (6,7,5)], color=WHITE, fill_opacity=0.7).set_stroke(WHITE, 1)
        cel24 = Polygon(*[masodik_poziciok[i] for i in (0,1,7)], color=WHITE, fill_opacity=0.7).set_stroke(WHITE, 1)
        self.play(Create(haromszog_m))
        self.wait(1)
        for cc in (cel11,cel12, cel13, cel14, cel21, cel22, cel23, cel24):
            self.play(TransformFromCopy(haromszog_m, cc))
        
        self.wait(10)




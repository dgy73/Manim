from manim import *
import numpy as np


class TriangleCircumcenter(Scene):

    def get_edge_points(self, midpoint, normal, stroke_width=1):
        # Normalizáljuk a merőleges vektort
        normal = normalize(normal)
        x, y = midpoint[0], midpoint[1]
        points = []

        # 1. pont: x = -7 vagy 7
        if abs(normal[0]) > 0.1:
            t1 = (-7 - x) / normal[0]
            p1 = midpoint + t1 * normal
            if -4 <= p1[1] <= 4:
                points.append(p1)
            t2 = (7 - x) / normal[0]
            p2 = midpoint + t2 * normal
            if -4 <= p2[1] <= 4:
                points.append(p2)

        # 2. pont: y = -4 vagy 4 (ha még nincs elég pont)
        if len(points) < 2 and abs(normal[1]) > 0.1:
            t3 = (-4 - y) / normal[1]
            p3 = midpoint + t3 * normal
            if -7 <= p3[0] <= 7:
                points.append(p3)
            t4 = (4 - y) / normal[1]
            p4 = midpoint + t4 * normal
            if -7 <= p4[0] <= 7:
                points.append(p4)

        # Ha még mindig csak egy pont van, kényszerítjük a másikat a legközelebbi szélre
        if len(points) == 1:
            if abs(normal[0]) > abs(normal[1]):
                t5 = (7 - x) / normal[0] if x < 7 else (-7 - x) / normal[0]
                p5 = midpoint + t5 * normal
                points.append(p5)
            else:
                t5 = (4 - y) / normal[1] if y < 4 else (-4 - y) / normal[1]
                p5 = midpoint + t5 * normal
                points.append(p5)

        return DashedLine(points[0], points[1], color=GREEN, stroke_width=stroke_width)


    def line_intersection(self, line1_start, line1_end, line2_start, line2_end):
        x1, y1 = line1_start[0], line1_start[1]
        x2, y2 = line1_end[0], line1_end[1]
        x3, y3 = line2_start[0], line2_start[1]
        x4, y4 = line2_end[0], line2_end[1]

        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denom == 0:
            return None
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
        return np.array([x1 + t * (x2 - x1), y1 + t * (y2 - y1), 0])

    def construct(self):

        # Tex szövegek font mérete
        TexFontSize = 20

        # A háromszög csúcsai
        A = np.array([-6.5,-2.5,0])
        B = np.array([.5,-.5,0])
        C = np.array([-3.5,3,0])

        # Háromszög létrehozása
        triangle = Polygon(A,B,C, color=BLUE)
        triangle.set_fill(BLUE, opacity=0.3)

        Csucsok = [
        MathTex(r"A", font_size=TexFontSize).next_to(A, LEFT, buff=.1),
        MathTex(r"B", font_size=TexFontSize).next_to(B, RIGHT, buff=.1),
        MathTex(r"C", font_size=TexFontSize).next_to(C, LEFT, buff=.1),
        ]

        # Cím hozzáadása
        title = Text("A Háromszög oldalfelező merőlegeseinek metszéspontja (Köréírt kör középpontja)", font_size=24)
        title.to_edge(UP)

        # A Magyarázó szövegek helyének kialakítása
        T_pontok = [
            np.array([1,-3.5,0]), np.array([6.5,-3.5,0]), np.array([6.5,3.5,0]), np.array([1,3.5,0])] 
        TextArea = Polygon(*T_pontok, color=YELLOW, fill_opacity=.2)

        # Magyarázó szövegek
        M_szoveg = [
                MathTex(r"\text{Vegyünk fel egy }ABC \text{ háromszöget!}", font_size=TexFontSize),
                MathTex(r"\text{Vegyünk fel az }AB \text{ és a } BC \text{ oldalak felező merőlegeseit!}", font_size=TexFontSize),
                MathTex(r"\text{Legyen az oldalfelező merőlegesek metszéspontja }O", font_size=TexFontSize),
                MathTex(r"\text{Mivel }O \text{ rajta van } AB \text{ oldal felező merőlegesén }AO=BO=R", font_size=TexFontSize),
                MathTex(r"\text{Mivel }O \text{ rajta van } BC \text{ oldal felező merőlegesén }BO=CO=R", font_size=TexFontSize),
                MathTex(r"\text{Ami azt jelenti, hogy }AO=CO=R", font_size=TexFontSize),
                MathTex(r"\text{Ezért }O \text{ rajta van }AC \text{ oldal felezőmerőlegesén}", font_size=TexFontSize),
                MathTex(r"\text{Tehát a háromszög mindhárom oldalfelező merőlegese egy ponton megy át!}", font_size=TexFontSize)

        ]
        for i, line in enumerate(M_szoveg):
            if i == 0:
                line.next_to(TextArea.get_top(), DOWN)
                
            else:
                line.next_to(M_szoveg[i-1], DOWN)

        # Oldalfelező merőlegesek meghatározása
        points = [A, B, C]
        midpoints = [
            (points[0] + points[1]) / 2,
            (points[1] + points[2]) / 2,
            (points[2] + points[0]) / 2
        ]
        

        

        
        
        perpendiculars = [
            self.get_edge_points(midpoints[0], rotate_vector(points[1] - points[0], PI / 2)),
            self.get_edge_points(midpoints[1], rotate_vector(points[2] - points[1], PI / 2)),
            self.get_edge_points(midpoints[2], rotate_vector(points[0] - points[2], PI / 2))
        ]

        intersection_point = self.line_intersection(perpendiculars[0].get_start(), perpendiculars[0].get_end(),
                                                  perpendiculars[1].get_start(), perpendiculars[1].get_end())
        
        

        # Koordináták kiíratása
        if intersection_point is not None:
            print(f"Metszéspont koordináták: {intersection_point}")
            kozeppont = Dot(intersection_point, color=RED)
            Label_kozepppont = MathTex(r"O", font_size=TexFontSize).next_to(kozeppont, LEFT, buff=.1)

        # sugarak
        OA = Line(kozeppont, A, color=YELLOW, stroke_width=1)
        OB = Line(kozeppont, B, color=YELLOW, stroke_width=1)
        OC = Line(kozeppont, C, color=YELLOW, stroke_width=1)

        # Animáció
        self.add(title)
        self.play(Create(triangle), run_time=1)
        self.play(*[Write(cimke) for cimke in Csucsok])
        self.play(FadeOut(title), run_time=1)
        self.play(Write(M_szoveg[0]))
        self.play(Create(perpendiculars[0]),Create(perpendiculars[1]), run_time=2)
        self.play(Write(M_szoveg[1]))
        self.play(Create(kozeppont), run_time=1)
        self.play(Write(Label_kozepppont))
        self.play(Write(M_szoveg[2]))
        self.wait(2)
        self.play(Write(M_szoveg[3]))
        self.play(Create(OA), Create(OB))
        self.play(Write(MathTex(r"R", font_size=TexFontSize).next_to(OA.get_center(), LEFT+UP, buff=.1)))
        self.play(Write(MathTex(r"R", font_size=TexFontSize).next_to(OB.get_center(), RIGHT+UP, buff=.1)))
        self.wait(2)
        self.play(Write(M_szoveg[4]))
        self.play(Create(OC), Write(MathTex(r"R", font_size=TexFontSize).next_to(OC.get_center(), RIGHT, buff=.1)))
        self.wait(2) 
        self.play(Write(M_szoveg[5]))
        self.play(Write(M_szoveg[6]))
        self.wait(2)
        self.play(Create(perpendiculars[2]))
        self.wait(2) 
        self.play(Write(M_szoveg[7]))
      
       
        
        self.wait(10)
from manim import *
import numpy as np

#
# manim -pqh polya.py Polya

# Egyéni MathTex osztály
class MathTex2(MathTex):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, font_size=28, **kwargs)

class Polya(Scene):

    def construct(self):
        # Többsoros szöveg definiálása külön Text objektumokkal
        lines1 = [
            MathTex2(r"\text{Tegyük fel tehát, hogy adottak az }a_1,a_2,\dots a_n \text{ nemnegatív valós számok, számtani közepük } A."),
            MathTex2(r"\text{Ha }A=0, \text{ akkor }a_i=0 (i=1,2,\dots,n) \text{ tehát az egyenlőség teljesül: } \sqrt[n]{a_1 a_2 \dots a_n}= \dfrac{a_1+a_2+\dots + a_n}{n}."),
            MathTex2(r"\text{Tegyük fel, hogy a számok pizitívak }a_i>0, \quad i=1,2,\dots , n \text{ ekkor }A>0"),
            MathTex2(r"\text{Legyen }f(x):=e^x-x-1, \quad x \in \mathbb{R}"),
            MathTex2(r"f \text{ függvény első deriváltja:}"),
            MathTex2(r"f^{\prime}(x)=e^x-1"),
            MathTex2(r"f \text{ második deriváltja:}"),
            MathTex2(r"f^{\prime \prime}(x)=e^x"),
            MathTex2(r"\text{A második derivált mindenhol pozitív: }f^{\prime \prime}(x)=e^x>0, \quad x \in \mathbb{R}"),
            MathTex2(r"\text{A } 0=f^{\prime}(x)=e^x-1 \text{ egyenlet egyetlen megoldása: }x=0"),
            MathTex2(r"\text{Így az }f \text{ függvénynek csak } x= 0 \text{ helyen van szélsőértéke, ami minimum és }f(0) = 0. "),
            MathTex2(r"\forall x \in \mathbb{R}: \quad f(x) \geq 0, \quad f(x) = 0 	\text{ akkor és csak akkor, ha } x = 0")
        ]

        lines2 = [
            MathTex2(r"\text{Tehát: }\forall x \in \mathbb{R} \text{ esetén } e^x-x-1 \geq 0 \text{, így } e^x \geq x+1 \text{ és egyenlőség csak ha }x=0"),
            MathTex2(r"\text{A fenti egyenlőséget felírva az }\dfrac{a_i}{A}+1 \quad (i =1,2,\dots n) \text{ számokra}  "),
            MathTex2(r"e^{\dfrac{a_1}{A}-1} \geq \dfrac{a_1}{A}, \quad e^{\dfrac{a_2}{A}-1} \geq \dfrac{a_2}{A}, \quad \dots e^{\dfrac{a_n}{A}-1} \geq \dfrac{a_n}{A}"),
            MathTex2(r"\text{Az egyenlőtlenségek mindkét oldala pozitív, így összeszorzva kapjuk:}"),
            MathTex2(r"e^{\dfrac{a_1+a_2+\dots + a_n}{A}-n} \geq \dfrac{a_1 \cdot a_2 \cdots a_n}{A^n}"),
            MathTex2(r"\text{Mivel }a_1+a_2+\dots + a_n = nA \text{ így }\dfrac{a_1+a_2+\dots + a_n}{A}-n = n - n =0. \text{ Ezért a fenti egynlőtlenség: }"),
            MathTex2(r"1 \geq  \dfrac{a_1 \cdot a_2 \cdots a_n}{A^n} \text{ amiből }A^n \geq a_1 \cdot a_2 \cdots a_n"),
            MathTex2(r"\text{Egyenlőség csak akkor áll fenn, ha }\dfrac{a_i}{A}-1 = 0 \text{ azaz }\dfrac{a_1}{A}=\dfrac{a_2}{A}= \dots = \dfrac{a_n}{A}=1"),
            MathTex2(r"\text{Ami azt jelenti, hogy minden szám egyenlő }a_1=a_2=\dots = a_n = A.")
        ]

        # Szöveg pozicionálása a képernyő tetejétől kezdődően
        for i, line in enumerate(lines1):
            if i == 0:
                # Az első sor a képernyő tetejéhez igazítva
                line.to_edge(UP)
            else:
                # A többi sor az előző alá kerül
                line.next_to(lines1[i-1], DOWN)

        # Sorok késleltetett megjelenítése
        for line in lines1:
            self.play(Write(line, run_time=2))  # 2 másodperc alatt írja ki az egyes sorokat
            self.wait(1)  # 1 másodperc várakozás az egyes sorok között

        # Várakozás a végén
        self.wait(5)
        self.play(*[FadeOut(l) for l in lines1], run_time = 1)

        for i, line in enumerate(lines2):
            if i == 0:
                # Az első sor a képernyő tetejéhez igazítva
                line.to_edge(UP)
            else:
                # A többi sor az előző alá kerül
                line.next_to(lines2[i-1], DOWN)

        # Sorok késleltetett megjelenítése
        for line in lines2:
            self.play(Write(line, run_time=2))  # 2 másodperc alatt írja ki az egyes sorokat
            self.wait(1)  # 1 másodperc várakozás az egyes sorok között
        
        self.wait(8)


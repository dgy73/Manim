from manim import *

class PetersenGraphScene(Scene):
    def construct(self):
        title = Text("Petersen-gráf", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Petersen-gráf csúcsai (0–9), dupla ötágú csillag struktúra
        vertices = list(range(10))
        outer = [0, 1, 2, 3, 4]
        inner = [5, 6, 7, 8, 9]
        edges = []

        # Külső kör: 5-ös ciklus
        for i in range(5):
            edges.append((outer[i], outer[(i + 1) % 5]))

        # Belső csillag: (i, (i+2)%5)
        for i in range(5):
            edges.append((inner[i], inner[(i + 2) % 5]))

        # Összekötés: minden külsőhöz egy belső csúcs
        for i in range(5):
            edges.append((outer[i], inner[i]))

        # Elrendezés: manuális pozíciók, hogy szabályos legyen
        layout = {
            0: LEFT * 2 + UP * 2,
            1: RIGHT * 2 + UP * 2,
            2: RIGHT * 3,
            3: RIGHT * 1 + DOWN * 2,
            4: LEFT * 1 + DOWN * 2,
            5: LEFT * 1 + UP * 0.5,
            6: RIGHT * 1 + UP * 0.5,
            7: RIGHT * 1.5 + DOWN * 1,
            8: ORIGIN,
            9: LEFT * 1.5 + DOWN * 1,
        }

        graph = Graph(
            vertices=vertices,
            edges=edges,
            layout=layout,
            vertex_config={"radius": 0.1},
        )

        self.play(Create(graph))
        self.wait(1)

        # Címkék (csúcs fölé helyezve)
        labels = VGroup()
        for v in vertices:
            pos = graph[v].get_center()
            label = Text(str(v), font_size=24).move_to(pos + UP * 0.3)
            labels.add(label)

        self.play(Write(labels))
        self.wait(1)

        # Szöveges magyarázat
        self.play(graph.animate.scale(0.85).to_edge(DOWN), labels.animate.scale(0.85).to_edge(DOWN))
        explanation = Tex(
            r"A Petersen-gráf nem síkbarajzolható, $3$-reguláris,\\ "
            r"és \emph{nem tartalmaz Hamilton-kört}.", font_size=32
        ).move_to(2*UP)
        self.play(Write(explanation))
        self.wait(3)

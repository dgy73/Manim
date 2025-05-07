from manim import *
import networkx as nx
import numpy as np

class PetersenGraphManualLayout(Scene):
    def construct(self):
        title = Text("Petersen-gráf", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Petersen-gráf létrehozása
        nx_graph = nx.petersen_graph()

        # Saját elrendezés: 2 konc. kör – külső és belső csúcsok
        angle = lambda i, n: 2 * PI * i / n
        radius_outer = 3
        radius_inner = 1.5

        layout_3d = {}
        for i in range(5):
            # Külső 5 csúcs (0–4)
            theta = angle(i, 5)
            layout_3d[i] = [radius_outer * np.cos(theta), radius_outer * np.sin(theta), 0]

            # Belső 5 csúcs (5–9)
            theta = angle(i , 5)  # eltolva, hogy ne fedjék egymást
            layout_3d[i + 5] = [radius_inner * np.cos(theta), radius_inner * np.sin(theta), 0]

        # Gráf Manimban
        graph = Graph.from_networkx(
            nx_graph,
            layout=layout_3d,
            vertex_config={"radius": 0.1},
            edge_config={"stroke_width": 2}
        )

        self.play(Create(graph))
        self.wait(1)

        # Címkék a pontok fölé
        labels = VGroup()
        for v in nx_graph.nodes:
            pos = graph[v].get_center()
            label = Text(str(v), font_size=28).move_to(pos + UP * 0.4)
            labels.add(label)

        self.play(Write(labels))
        self.wait(2)
        self.play(graph.animate.scale(.7).to_edge(DOWN),labels.animate.scale(.7).to_edge(DOWN))
        explanation = Tex(
            r"A Petersen-gráf kézzel elrendezve: jól látható struktúra,\\ "
            r"nem síkbarajzolható, $3$-reguláris, nem Hamiltoni.", font_size=30
        )
        explanation.next_to(graph, UP, buff=1)

        self.play(Write(explanation))
        self.wait(3)

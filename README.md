## Manim Matematikai Vizualizáció

Üdvözöllek a Manim projektemben! Ez a repository matematikai tételek, fogalmak, feladatok vizualizációját bemutató programokat és segédanyagokat tartalmaz, a [Manim](https://www.manim.community/) könyvtár használatával. Az oldal célja, hogy szemléletes és interaktív animációkkal segítse a tanulókat a matematikai jelenségek, struktúrák megértésében.

## Tartalom
- Matematikai animációk és vizualizációk Python és Manim segítségével.
- Segédanyagok, például kódminták, dokumentációk és példák.
- Különböző matematikai témák, például geometria, analízis, algebra, gráfelmélet és egyebek.

## Telepítés
A projekt futtatásához a Manim könyvtárra, valamint további Python csomagokra van szükség, különösen gráfokhoz és LaTeX rendereléshez. Az alábbi lépésekkel állíthatod be a környezetet:

### Előfeltételek
- **Python**: Telepítsd a [Python 3.8+](https://www.python.org/downloads/) verzióját. Győződj meg róla, hogy a `pip` naprakész:
  ```bash
  python -m pip install --upgrade pip
  ```
- **Git**: Telepítsd a [Git](https://git-scm.com/downloads)-et a repository klónozásához.
- **LaTeX (Windows)**: A Manim LaTeX-et használ matematikai képletek rendereléséhez. Windows alatt telepítsd a [MiKTeX](https://miktex.org/download) rendszert:
  1. Töltsd le és telepítsd a MiKTeX-et az alapértelmezett beállításokkal.
  2. A telepítés után futtasd a MiKTeX Console-t, és frissítsd a csomagokat.
  3. Ellenőrizd, hogy a `latex` parancs elérhető-e a parancssorban:
     ```bash
     latex --version
     ```
  4. Ha nem működik, add hozzá a MiKTeX bin mappáját (pl. `C:\Program Files\MiKTeX\miktex\bin\x64`) a Windows PATH környezeti változóhoz.

### Manim és szükséges csomagok telepítése
1. **Manim telepítése**:
   ```bash
   pip install manim
   ```
2. **További csomagok**:
   - **NumPy**: Szükséges matematikai számításokhoz és gráfok adatkezeléséhez.
   - **NetworkX** (opcionális): Gráfok létrehozásához és vizualizációjához.
   - **Matplotlib** (opcionális): Statikus gráfok és ábrák készítéséhez, ha nem animált kimenetre van szükség.
   Telepítsd őket:
   ```bash
   pip install numpy networkx matplotlib
   ```
3. **Requirements fájl** (ajánlott):
   Hozz létre egy `requirements.txt` fájlt a következő tartalommal:
   ```
   manim
   numpy
   networkx
   matplotlib
   ```
   Majd telepítsd:
   ```bash
   pip install -r requirements.txt
   ```

4. **Repository klónozása**:
   ```bash
   git clone https://github.com/<felhasználóneved>/<repository-neve>.git
   cd <repository-neve>
   ```

## Használat
1. **Animáció futtatása**:
   - Nyisd meg az egyik Python fájlt (pl. `example.py`) a `src` mappában.
   - Futtasd az animációt a következő paranccsal:
     ```bash
     manim -pql example.py Név
     ```
     - `-p`: Lejátssza az animációt a generálás után.
     - `-ql`: Alacsony minőségű renderelés (gyorsabb teszteléshez).
     - `Név`: Az animáció osztály neve a Python fájlban.

2. **Gráfok vizualizációja**:
   - A gráfokhoz használhatsz NetworkX-et a gráfok adatstruktúrájának létrehozására, majd Manimmal animálhatod őket.
   - Példa kód egy egyszerű gráf animációhoz:
     ```python
     from manim import *
     import networkx as nx

     class GraphExample(Scene):
         def construct(self):
             G = nx.Graph([(1, 2), (2, 3), (3, 1)])
             graph = Graph(list(G.nodes), list(G.edges), layout="circular")
             self.play(Create(graph))
             self.wait()
     ```

3. **LaTeX használata**:
   - Matematikai képletek rendereléséhez használhatod a Manim `Tex` vagy `MathTex` osztályait. Példa:
     ```python
     from manim import *

     class FormulaExample(Scene):
         def construct(self):
             formula = MathTex(r"f(x) = \int_{-\infty}^{\infty} e^{-x^2} dx")
             self.play(Write(formula))
             self.wait()
     ```
   - Győződj meg róla, hogy a MiKTeX telepítve van, különben a LaTeX renderelés hibát dob.

4. **Saját animáció készítése**:
   - Hozz létre egy új Python fájlt, és használd a Manim dokumentációját ([docs.manim.community](https://docs.manim.community/en/stable/)) az animációk készítéséhez.

## Példák
- `src/geometry.py`: Alapvető geometriai alakzatok animációi.
- `src/calculus.py`: Függvények és deriváltak vizualizációja.
- `src/graphs.py`: Gráfelméleti vizualizációk NetworkX és Manim segítségével.
- `src/formulas.py`: Matematikai képletek LaTeX-szel renderelve.
- *(További példák hamarosan...)*

## Gyakori problémák
- **LaTeX hiba**: Ha a Manim nem találja a LaTeX-et, ellenőrizd, hogy a MiKTeX telepítve van, és a `latex` parancs elérhető a PATH-ban.
- **"Module not found"**: Telepítsd a hiányzó csomagokat a `pip install` paranccsal, vagy használd a `requirements.txt` fájlt.
- **Gráfok nem renderelődnek**: Győződj meg róla, hogy a NetworkX és a Manim legfrissebb verzióit használod.

---

*Készítette: Dezsőfi György*  
*Utolsó frissítés: 2025. május 6.*




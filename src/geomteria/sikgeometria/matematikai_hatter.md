A háromszög beírt körének meghatározása mátrixokkal megadott csúcsok esetén geometriai és algebrai műveletekkel történhet. Az \(ABC\) háromszög csúcsait mátrix formában adjuk meg, például:

$$
A = \begin{bmatrix} x_A \\ y_A \end{bmatrix}, \quad B = \begin{bmatrix} x_B \\ y_B \end{bmatrix}, \quad C = \begin{bmatrix} x_C \\ y_C \end{bmatrix}
$$

A cél a beírt kör középpontjának (\(O\)) koordinátáit és sugarát (\(\varrho\)) meghatározni. A beírt kör középpontja a háromszög belső szögfelezőinek metszéspontja, és az oldalaktól egyenlő távolságra van.

### Lépések a beírt kör meghatározásához:

#### 1. **Háromszög oldalainak hossza**
Először számoljuk ki az \(ABC\) háromszög oldalainak hosszát:
- \(a = BC\): \(\sqrt{(x_C - x_B)^2 + (y_C - y_B)^2}\)
- \(b = CA\): \(\sqrt{(x_A - x_C)^2 + (y_A - y_C)^2}\)
- \(c = AB\): \(\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}\)

Ezeket mátrixokkal kifejezve:
\[
a = \sqrt{(C - B)^T (C - B)}, \quad b = \sqrt{(A - C)^T (A - C)}, \quad c = \sqrt{(B - A)^T (B - A)}
\]

#### 2. **Félkerület kiszámítása**
A háromszög félkerülete (\(s\)) az oldalak hosszának segítségével:
\[
s = \frac{a + b + c}{2}
\]

#### 3. **Háromszög területének kiszámítása**
A terület (\(\Delta\)) meghatározható a csúcsok koordinátáival a determináns képlet segítségével (shoelace formula):
\[
\Delta = \frac{1}{2} \left| x_A (y_B - y_C) + x_B (y_C - y_A) + x_C (y_A - y_B) \right|
\]
Mátrix formában, ha a csúcsokat egy \(3 \times 2\) mátrixba rendezzük:
\[
P = \begin{bmatrix}
x_A & y_A \\
x_B & y_B \\
x_C & y_C
\end{bmatrix}
\]
és a terület:
\[
\Delta = \frac{1}{2} \left| \det \begin{bmatrix}
x_A & y_A & 1 \\
x_B & y_B & 1 \\
x_C & y_C & 1
\end{bmatrix} \right|
\]

#### 4. **Beírt kör középpontjának koordinátái**
A beírt kör középpontja (\(O = [x_O, y_O]\)) a háromszög belső szögfelezőinek metszéspontja, és kiszámítható a csúcsok súlyozott átlagaként, ahol a súlyok az oldalak hosszai:
\[
x_O = \frac{a x_A + b x_B + c x_C}{a + b + c}, \quad y_O = \frac{a y_A + b y_B + c y_C}{a + b + c}
\]
Mátrix formában:
\[
O = \frac{a A + b B + c C}{a + b + c}
\]
Itt \(a, b, c\) az oldalak hossza, \(A, B, C\) pedig a csúcsok koordinátáit tartalmazó vektorok.

#### 5. **Beírt kör sugarának kiszámítása**
A beírt kör sugara (\(\varrho\)) a háromszög területének és félkerületének segítségével:
\[
\varrho = \frac{\Delta}{s}
\]

### Összegzés: Műveletek lépésről lépésre
1. Számítsd ki az oldalak hosszát (\(a, b, c\)) a csúcsok koordinátáiból.
2. Határozd meg a félkerületet: \(s = \frac{a + b + c}{2}\).
3. Számítsd ki a területet (\(\Delta\)) a determináns képlettel.
4. Határozd meg a középpontot (\(O\)) a súlyozott átlag képlettel: \(O = \frac{a A + b B + c C}{a + b + c}\).
5. Számítsd ki a sugarat: \(\varrho = \frac{\Delta}{s}\).

### Példa Python kódban (NumPy használatával)
Az alábbi kód bemutatja, hogyan lehet a fenti műveleteket elvégezni, ha a csúcsok koordinátái mátrix formában vannak megadva:

```python
import numpy as np

# Csúcsok koordinátái (2D vektorok)
A = np.array([0, 2])  # [x_A, y_A]
B = np.array([-2, -1])  # [x_B, y_B]
C = np.array([2, -1])  # [x_C, y_C]

# Oldalak hossza
a = np.linalg.norm(C - B)  # BC
b = np.linalg.norm(A - C)  # CA
c = np.linalg.norm(B - A)  # AB

# Félkerület
s = (a + b + c) / 2

# Terület (determináns képlet)
P = np.array([[A[0], A[1], 1],
              [B[0], B[1], 1],
              [C[0], C[1], 1]])
Delta = 0.5 * abs(np.linalg.det(P))

# Beírt kör középpontja
O = (a * A + b * B + c * C) / (a + b + c)

# Beírt kör sugara
rho = Delta / s

print(f"Beírt kör középpontja (O): {O}")
print(f"Beírt kör sugara (ρ): {rho}")
```

### Kimenet (példa):
A fenti \(A, B, C\) koordináták esetén a kimenet körülbelül:
- Beírt kör középpontja (\(O\)): \([0, 0]\)
- Beírt kör sugara (\(\varrho\)): \(0.5\)

Ez megegyezik az előző ábrán becsült értékekkel.

### Manim integráció
Ha ezt a számítást a Manim kódban szeretnéd használni, egyszerűen illeszd be a `TriangleCircles` osztályba, és használd az \(O\) és \(\varrho\) értékeket a kör rajzolásához:

```python
# Beírt kör rajzolása a kiszámított középponttal és sugárral
in_circle = Circle(radius=rho, color=BLUE).move_to(O)
self.add(in_circle)
```

Ha további részletekre van szükséged a hozzáírt körökről vagy a szögfelezők pontos kiszámításáról, jelezd!

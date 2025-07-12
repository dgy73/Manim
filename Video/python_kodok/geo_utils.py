import numpy as np
from manim import config

def get_line_endpoints(point, direction, scene_bounds=None):
    """
    Calculate the start and end points of a line passing through a given point with a given direction vector,
    intersecting the boundaries of the Manim Scene.

    Parameters:
    - point: np.array or list, the point through which the line passes [x, y, z]
    - direction: np.array or list, the direction vector of the line [dx, dy, dz]
    - scene_bounds: tuple of (x_min, x_max, y_min, y_max), optional custom scene boundaries.
                    If None, uses Manim's default frame boundaries.

    Returns:
    - start_point: np.array, one endpoint of the line on the scene boundary
    - end_point: np.array, the other endpoint of the line on the scene boundary
    """
    # Convert inputs to numpy arrays
    point = np.array(point)
    direction = np.array(direction)

    # Use default Manim frame boundaries if none provided
    if scene_bounds is None:
        frame_width = config["frame_width"]
        frame_height = config["frame_height"]
        x_min, x_max = -frame_width / 2, frame_width / 2
        y_min, y_max = -frame_height / 2, frame_height / 2
    else:
        x_min, x_max, y_min, y_max = scene_bounds

    # Parametric line equation: P(t) = point + t * direction
    # We need to find intersections with the scene boundaries
    intersections = []

    # Intersection with left boundary (x = x_min)
    if direction[0] != 0:
        t = (x_min - point[0]) / direction[0]
        y = point[1] + t * direction[1]
        if y_min <= y <= y_max:
            intersections.append((point + t * direction, t))

    # Intersection with right boundary (x = x_max)
    if direction[0] != 0:
        t = (x_max - point[0]) / direction[0]
        y = point[1] + t * direction[1]
        if y_min <= y <= y_max:
            intersections.append((point + t * direction, t))

    # Intersection with bottom boundary (y = y_min)
    if direction[1] != 0:
        t = (y_min - point[1]) / direction[1]
        x = point[0] + t * direction[0]
        if x_min <= x <= x_max:
            intersections.append((point + t * direction, t))

    # Intersection with top boundary (y = y_max)
    if direction[1] != 0:
        t = (y_max - point[1]) / direction[1]
        x = point[0] + t * direction[0]
        if x_min <= x <= x_max:
            intersections.append((point + t * direction, t))

    # Sort intersections by parameter t to get start and end points
    if len(intersections) < 2:
        raise ValueError("Line does not intersect the scene boundaries at two points.")

    intersections.sort(key=lambda x: x[1])  # Sort by t value
    start_point, end_point = intersections[0][0], intersections[1][0]

    # Ensure points are 3D for Manim compatibility (z=0 if not provided)
    start_point = np.array([start_point[0], start_point[1], 0]) if len(start_point) == 2 else start_point
    end_point = np.array([end_point[0], end_point[1], 0]) if len(end_point) == 2 else end_point

    return start_point, end_point

def get_intersection_point(point1, direction1, point2, direction2):
    """
    Kiszámítja két egyenes metszéspontját 2D-ben, 3D vektorként visszaadva (z=0).

    Paraméterek:
    - point1: np.array, első egyenes egy pontja [x, y] vagy [x, y, z]
    - direction1: np.array, első egyenes irányvektora [dx, dy] vagy [dx, dy, dz]
    - point2: np.array, második egyenes egy pontja [x, y] vagy [x, y, z]
    - direction2: np.array, második egyenes irányvektora [dx, dy] vagy [dx, dy, dz]

    Visszatér:
    - np.array: a metszéspont koordinátái [x, y, 0], ha létezik pontosan egy metszéspont
    - ValueError: hibaüzenet, ha a két egyenes párhuzamos vagy egybeesik
    """
    point1 = np.array(point1)[:2]
    direction1 = np.array(direction1)[:2]
    point2 = np.array(point2)[:2]
    direction2 = np.array(direction2)[:2]

    # Ellenőrizzük, hogy az irányvektorok párhuzamosak-e (keresztszorzat = 0)
    cross_product = np.cross(direction1, direction2)
    if abs(cross_product) < 1e-10:  # Párhuzamos vagy egybeeső egyenesek
        delta = point2 - point1
        if abs(np.cross(direction1, delta)) < 1e-10:  # Egybeesnek
            raise ValueError("A két egyenes egybeesik.")
        else:
            raise ValueError("A két egyenes párhuzamos, nincs metszéspont.")

    # Paraméteres egyenletek: P1 + t * D1 = P2 + s * D2
    # Mátrixegyenlet: A * [t, s] = b
    A = np.array([direction1, -direction2]).T
    b = point2 - point1
    try:
        t, _ = np.linalg.solve(A, b)
        intersection = point1 + t * direction1
        return np.array([intersection[0], intersection[1], 0])  # 3D vektor, z=0
    except np.linalg.LinAlgError:
        raise ValueError("Nem sikerült meghatározni a metszéspontot.")
    



def get_angle_bisectors(A, B, C):
    """
    Kiszámítja a B csúcsban lévő szög belső és külső szögfelezőjének irányvektorát
    három pont (A, B, C) alapján.

    Paraméterek:
    - A, B, C: np.array, a három pont koordinátái [x, y, z] formában

    Visszatér:
    - tuple: (belso_bisector, kulso_bisector)
      - belso_bisector: np.array, a belső szögfelező egységvektora, vagy merőleges vektor egyenes szög esetén
      - kulso_bisector: np.array, a külső szögfelező egységvektora, vagy None egyenes szög esetén
    """
    # Vektorok kiszámítása
    BA = A - B
    BC = C - B

    # Egységvektorok normalizálása
    BA_unit = BA / np.linalg.norm(BA) if np.linalg.norm(BA) > 0 else BA
    BC_unit = BC / np.linalg.norm(BC) if np.linalg.norm(BC) > 0 else BC

    # Belső szögfelező irányvektora
    belso_bisector = BA_unit + BC_unit
    belso_norm = np.linalg.norm(belso_bisector)

    if belso_norm < 1e-10:  # Egyenes szög esetén (vektorok összege közel nulla)
        # Belső szögfelező: BA-ra merőleges vektor
        belso_bisector = np.array([-BA_unit[1], BA_unit[0], 0])  # 90 fokkal elfordítva
        belso_bisector = belso_bisector / np.linalg.norm(belso_bisector) if np.linalg.norm(belso_bisector) > 0 else belso_bisector
        kulso_bisector = None
    else:
        # Belső szögfelező normalizálása
        belso_bisector = belso_bisector / belso_norm
        # Külső szögfelező: belső szögfelezőre merőleges vektor
        kulso_bisector = np.array([-belso_bisector[1], belso_bisector[0], 0])  # 90 fokkal elfordítva
        kulso_bisector = kulso_bisector / np.linalg.norm(kulso_bisector) if np.linalg.norm(kulso_bisector) > 0 else kulso_bisector

    return belso_bisector, kulso_bisector



def get_perpendicular_projection(point, line_point, direction):
    """
    Kiszámítja egy pont egyenesre eső merőleges vetületét.

    Paraméterek:
    - point: np.array([x, y, z]), a vetítendő pont koordinátái
    - line_point: np.array([x, y, z]), az egyenesen lévő pont koordinátái
    - direction: np.array([x, y, z]), az egyenes irányvektora

    Visszatér:
    - np.array([x, y, z]), a vetületi pont koordinátái
    """
    # Vektor a ponttól az egyenes pontjáig
    PQ = point - line_point
    
    # Irányvektor normálása (opcionális, de stabilitás miatt célszerű)
    direction_norm = np.linalg.norm(direction)
    if direction_norm < 1e-10:
        raise ValueError("Az irányvektor hossza túl kicsi vagy nulla!")
    direction_unit = direction / direction_norm
    
    # Vetítési tényező kiszámítása (skaláris szorzat az irányvektorral)
    t = np.dot(PQ, direction_unit) / np.dot(direction_unit, direction_unit)
    
    # Vetületi pont kiszámítása
    projection = line_point + t * direction_unit
    
    return projection



def get_angle_at_vertex(A, B, C):
    """
    Kiszámítja az ABC szög nagyságát a B csúcsban három 3D-s pont alapján.

    Paraméterek:
    - A, B, C: np.array([x, y, z]), a három pont koordinátái

    Visszatér:
    - tuple: (degrees, radians), ahol
      - degrees: a szög nagysága fokban (float)
      - radians: a szög nagysága radiánban (float)
    """
    # Vektorok kiszámítása
    BA = A - B
    BC = C - B

    # Vektorok normái
    norm_BA = np.linalg.norm(BA)
    norm_BC = np.linalg.norm(BC)

    # Ellenőrzés: ha valamelyik vektor hossza nulla, szög nem definiálható
    if norm_BA < 1e-10 or norm_BC < 1e-10:
        raise ValueError("A vektorok hossza nem lehet nulla!")

    # Skaláris szorzat
    dot_product = np.dot(BA, BC)

    # Koszinusz kiszámítása
    cos_theta = dot_product / (norm_BA * norm_BC)

    # Numerikus stabilitás miatt korlátozzuk a cos_theta értéket [-1, 1] intervallumra
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    # Szög radiánban
    theta_radians = np.arccos(cos_theta)

    # Szög fokban
    theta_degrees = np.degrees(theta_radians)

    return (theta_degrees, theta_radians)


def get_right_angle_notation(P, v, d):
    """
    Kiszámítja a derékszög jelöléshez szükséges pontokat és visszaad két pontpárt.

    Paraméterek:
    - P: np.array([x, y, z]), a kiindulási pont
    - v: np.array([x, y, z]), az irányvektor
    - d: float, a derékszög jelölés hossza

    Visszatér:
    - tuple: ((Line(Q, R), (Line(R, S))), ahol
      - Q = P + v1
      - R = P + v1 + v2
      - S = P + v2
      - v1: normalizált v vektor
      - v2: v1 90 fokkal pozitív irányba elforgatott vektora
    """
    # Normalizálás: v1 az egységvektor
    v_norm = np.linalg.norm(v)
    if v_norm < 1e-10:
        raise ValueError("Az irányvektor hossza nem lehet nulla!")
    v1 = v / v_norm

    # v1 elforgatása pozitív irányba (90 fokkal az óramutató járásával ellentétesen)
    v2 = np.array([-v1[1], v1[0], v1[2]])  # 2D elforgatás, z megtartva
    v2 = v2 / np.linalg.norm(v2) if np.linalg.norm(v2) > 0 else v2

    # Pontok kiszámítása
    Q = P + v1 * d
    R = P + v1 * d + v2 * d
    S = P + v2 * d

    return (Q, R), (R, S)


def get_triangle_type(A, B, C):
    """
    Egy háromszög típusának meghatározása.

    Paraméterek: A, B, C: np.array([x, y, z]), a három csúcs koordinátái
    Visszatérési érték: Derékszögű, Hegyesszögű, Tompaszögű
    """
    a = np.linalg.norm(B - C)
    b = np.linalg.norm(A - C)
    c = np.linalg.norm(A - B)
    sides = sorted([a, b, c])
    # Koszinusz-tétel legnagyobb szög kiszámításához
    cos_gamma = (a**2 + b**2 - c**2) / (2 * a * b)
    angle = np.arccos(cos_gamma) * 180 / np.pi
    if abs(angle - 90) < 1e-2:
        return "Derékszögű"
    elif angle < 90:
        return "Hegyesszögű"
    else:
        return "Tompaszögű"
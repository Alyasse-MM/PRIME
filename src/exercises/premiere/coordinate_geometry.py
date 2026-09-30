import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from exercises.base_exercise import BaseExercise
from exercises.question import Question

# Module-level registry key
CHAPTER = {"fr": "Géométrie Repérée", "en": "Coordinate Geometry"}

def format_sign(val):
    """Helper to format + and - signs cleanly."""
    if val == 0:
        return ""
    elif val > 0:
        return f"+ {val}"
    else:
        return f"- {abs(val)}"

def format_coeff(val, var):
    """Helper to format coefficients (e.g., 1x -> x, -1x -> -x)."""
    if val == 0:
        return ""
    elif val == 1:
        return f"+ {var}"
    elif val == -1:
        return f"- {var}"
    elif val > 0:
        return f"+ {val}{var}"
    else:
        return f"- {abs(val)}{var}"


# ==========================================
# MÉTHODE 1 : Équation de droite (Point + Vecteur directeur)
# ==========================================
class EquationLinePointVector(BaseExercise):
    id = "GEO_001"
    title = {"fr": "Équation de droite (Point et vecteur directeur)", "en": "Line equation (Point and direction vector)"}
    tags = ["geometrie", "droite", "vecteur directeur", "equation cartesienne"]

    def generate(self):
        ax = self.rng.randint(-5, 5)
        ay = self.rng.randint(-5, 5)
        
        # Avoid 0 to keep the general ax + by + c form
        ux = self.rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        uy = self.rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])

        self.statement_fr = [
            f"Déterminer une équation cartésienne de la droite $d$ passant par le point $A\\binom{{{ax}}}{{{ay}}}$ et de vecteur directeur $\\vec{{u}}\\binom{{{ux}}}{{{uy}}}$."
        ]
        self.statement_en = [
            f"Determine a Cartesian equation of the line $d$ passing through the point $A\\binom{{{ax}}}{{{ay}}}$ with direction vector $\\vec{{u}}\\binom{{{ux}}}{{{uy}}}$."
        ]

        q1_fr = ["Détailler les étapes du calcul."]
        q1_en = ["Detail the calculation steps."]
        insight1_fr = ["Si $\\vec{u}\\binom{-b}{a}$ est vecteur directeur, l'équation est de la forme $ax+by+c=0$. Trouvez $c$ à l'aide des coordonnées de $A$."]
        insight1_en = ["If $\\vec{u}\\binom{-b}{a}$ is a direction vector, the equation is of the form $ax+by+c=0$. Find $c$ using the coordinates of $A$."]
        
        a = uy
        b = -ux
        
        c = -a*ax - b*ay
        
        # Formatting the equation strings nicely
        str_a = f"{a}x" if a != 1 and a != -1 else ("x" if a == 1 else "-x")
        str_b = format_coeff(b, "y")
        str_c = format_sign(c)
        eq_final = f"{str_a} {str_b} {str_c} = 0".strip()
        if eq_final.startswith("+"): eq_final = eq_final[1:].strip()

        ans1_fr = [
            f"• La droite $d$ admet une équation cartésienne de la forme $ax+by+c=0$.",
            f"Comme $\\vec{{u}}\\binom{{{ux}}}{{{uy}}}$ est un vecteur directeur, on a $\\binom{{{ux}}}{{{uy}}} = \\binom{{-b}}{{a}}$.",
            f"Soit $a = {a}$ et $b = {b}$.",
            f"Une équation de $d$ est donc de la forme : ${a}x {format_sign(b)}y + c = 0$.",
            f"• Pour déterminer $c$, on substitue les coordonnées de $A\\binom{{{ax}}}{{{ay}}}$ :",
            f"${a} \\times ({ax}) {format_sign(b)} \\times ({ay}) + c = 0$",
            f"${a*ax} {format_sign(b*ay)} + c = 0 \\implies {a*ax + b*ay} + c = 0 \\implies c = {c}$.",
            f"Une équation cartésienne de $d$ est : **${eq_final}$**."
        ]
        ans1_en = [
            f"• The line $d$ admits a Cartesian equation of the form $ax+by+c=0$.",
            f"Since $\\vec{{u}}\\binom{{{ux}}}{{{uy}}}$ is a direction vector, we have $\\binom{{{ux}}}{{{uy}}} = \\binom{{-b}}{{a}}$.",
            f"Thus $a = {a}$ and $b = {b}$.",
            f"An equation of $d$ is therefore of the form: ${a}x {format_sign(b)}y + c = 0$.",
            f"• To determine $c$, we substitute the coordinates of $A\\binom{{{ax}}}{{{ay}}}$:",
            f"${a} \\times ({ax}) {format_sign(b)} \\times ({ay}) + c = 0$",
            f"${a*ax} {format_sign(b*ay)} + c = 0 \\implies {a*ax + b*ay} + c = 0 \\implies c = {c}$.",
            f"A Cartesian equation of $d$ is: **${eq_final}$**."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 2 : Équation de droite (Deux points)
# ==========================================
class EquationLineTwoPoints(BaseExercise):
    id = "GEO_002"
    title = {"fr": "Équation de droite (Deux points)", "en": "Line equation (Two points)"}
    tags = ["geometrie", "droite", "vecteur", "equation cartesienne"]

    def generate(self):
        bx = self.rng.randint(-5, 5)
        by = self.rng.randint(-5, 5)
        cx = self.rng.randint(-5, 5)
        cy = self.rng.randint(-5, 5)
        
        # Ensure B and C are distinct points
        while bx == cx and by == cy:
            cx = self.rng.randint(-5, 5)
            cy = self.rng.randint(-5, 5)

        self.statement_fr = [
            f"Déterminer une équation cartésienne de la droite $d$ passant par les points $B\\binom{{{bx}}}{{{by}}}$ et $C\\binom{{{cx}}}{{{cy}}}$."
        ]
        self.statement_en = [
            f"Determine a Cartesian equation of the line $d$ passing through the points $B\\binom{{{bx}}}{{{by}}}$ and $C\\binom{{{cx}}}{{{cy}}}$."
        ]

        q1_fr = ["Détailler les étapes du calcul."]
        q1_en = ["Detail the calculation steps."]
        insight1_fr = ["Le vecteur $\\vec{BC}$ est un vecteur directeur de la droite $d$. Calculez ses coordonnées puis appliquez la méthode précédente."]
        insight1_en = ["The vector $\\vec{BC}$ is a direction vector of the line $d$. Calculate its coordinates then apply the previous method."]
        
        ux = cx - bx
        uy = cy - by
        
        a = uy
        b = -ux
        
        c_val = -a*bx - b*by
        
        # Clean string formatting to hide 0x entirely
        if a == 0:
            str_a = ""
        elif a == 1:
            str_a = "x"
        elif a == -1:
            str_a = "-x"
        else:
            str_a = f"{a}x"

        str_b = format_coeff(b, "y")
        str_c = format_sign(c_val)
        
        # Formatting the final equation
        eq_final = f"{str_a} {str_b} {str_c} = 0".strip()
        if eq_final.startswith("+"): 
            eq_final = eq_final[1:].strip()
            
        # Formatting the intermediate equation step smoothly
        eq_inter = f"{str_a} {str_b} + c = 0".strip()
        if eq_inter.startswith("+"):
            eq_inter = eq_inter[1:].strip()

        ans1_fr = [
            f"• $B$ et $C$ appartiennent à $d$ donc $\\vec{{BC}}$ est un vecteur directeur de $d$.",
            f"On a : $\\vec{{BC}}\\binom{{ {cx} - ({bx}) }}{{ {cy} - ({by}) }} = \\binom{{{ux}}}{{{uy}}} = \\binom{{-b}}{{a}}$.",
            f"Donc $a = {a}$ et $b = {b}$.",
            f"Une équation cartésienne de $d$ est de la forme : ${eq_inter}$.",
            f"• $B\\binom{{{bx}}}{{{by}}}$ appartient à $d$ donc : ${a} \\times ({bx}) {format_sign(b)} \\times ({by}) + c = 0$.",
            f"${a*bx + b*by} + c = 0 \\implies c = {c_val}$.",
            f"Une équation cartésienne de $d$ est : **${eq_final}$**."
        ]
        ans1_en = [
            f"• $B$ and $C$ belong to $d$, so $\\vec{{BC}}$ is a direction vector of $d$.",
            f"We have: $\\vec{{BC}}\\binom{{ {cx} - ({bx}) }}{{ {cy} - ({by}) }} = \\binom{{{ux}}}{{{uy}}} = \\binom{{-b}}{{a}}$.",
            f"Thus $a = {a}$ and $b = {b}$.",
            f"A Cartesian equation of $d$ is of the form: ${eq_inter}$.",
            f"• $B\\binom{{{bx}}}{{{by}}}$ belongs to $d$, so: ${a} \\times ({bx}) {format_sign(b)} \\times ({by}) + c = 0$.",
            f"${a*bx + b*by} + c = 0 \\implies c = {c_val}$.",
            f"A Cartesian equation of $d$ is: **${eq_final}$**."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 3 : Équation de droite (Point + Vecteur normal)
# ==========================================
class EquationLinePointNormal(BaseExercise):
    id = "GEO_003"
    title = {"fr": "Équation de droite (Point et vecteur normal)", "en": "Line equation (Point and normal vector)"}
    tags = ["geometrie", "droite", "vecteur normal", "equation cartesienne"]

    def generate(self):
        ax = self.rng.randint(-5, 5)
        ay = self.rng.randint(-5, 5)
        
        nx = self.rng.choice([-3, -2, -1, 1, 2, 3])
        ny = self.rng.choice([-3, -2, -1, 1, 2, 3])

        self.statement_fr = [
            f"On considère la droite $d$ passant par le point $A\\binom{{{ax}}}{{{ay}}}$ et dont un vecteur normal est $\\vec{{n}}\\binom{{{nx}}}{{{ny}}}$."
        ]
        self.statement_en = [
            f"Consider the line $d$ passing through the point $A\\binom{{{ax}}}{{{ay}}}$ with a normal vector $\\vec{{n}}\\binom{{{nx}}}{{{ny}}}$."
        ]

        q1_fr = ["Déterminer une équation cartésienne de la droite $d$."]
        q1_en = ["Determine a Cartesian equation of the line $d$."]
        insight1_fr = ["Un vecteur normal $\\vec{n}\\binom{a}{b}$ donne directement les coefficients $a$ et $b$ de l'équation $ax+by+c=0$."]
        insight1_en = ["A normal vector $\\vec{n}\\binom{a}{b}$ directly provides the coefficients $a$ and $b$ of the equation $ax+by+c=0$."]
        
        c = -nx*ax - ny*ay
        
        str_a = f"{nx}x" if nx != 1 and nx != -1 else ("x" if nx == 1 else "-x")
        str_b = format_coeff(ny, "y")
        str_c = format_sign(c)
        eq_final = f"{str_a} {str_b} {str_c} = 0".strip()
        if eq_final.startswith("+"): eq_final = eq_final[1:].strip()

        ans1_fr = [
            f"• Comme $\\vec{{n}}\\binom{{{nx}}}{{{ny}}}$ est un vecteur normal de $d$, une équation cartésienne est de la forme :",
            f"${nx}x {format_sign(ny)}y + c = 0$.",
            f"• Le point $A\\binom{{{ax}}}{{{ay}}}$ appartient à $d$, donc ses coordonnées vérifient l'équation :",
            f"${nx} \\times ({ax}) {format_sign(ny)} \\times ({ay}) + c = 0$",
            f"${nx*ax} {format_sign(ny*ay)} + c = 0 \\implies c = {c}$.",
            f"Une équation cartésienne de $d$ est : **${eq_final}$**."
        ]
        ans1_en = [
            f"• Since $\\vec{{n}}\\binom{{{nx}}}{{{ny}}}$ is a normal vector of $d$, a Cartesian equation is of the form:",
            f"${nx}x {format_sign(ny)}y + c = 0$.",
            f"• The point $A\\binom{{{ax}}}{{{ay}}}$ belongs to $d$, so its coordinates satisfy the equation:",
            f"${nx} \\times ({ax}) {format_sign(ny)} \\times ({ay}) + c = 0$",
            f"${nx*ax} {format_sign(ny*ay)} + c = 0 \\implies c = {c}$.",
            f"A Cartesian equation of $d$ is: **${eq_final}$**."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 4 : Projeté orthogonal d'un point sur une droite
# ==========================================
class OrthogonalProjection(BaseExercise):
    id = "GEO_004"
    title = {"fr": "Coordonnées du projeté orthogonal", "en": "Coordinates of orthogonal projection"}
    tags = ["geometrie", "droite", "projeté orthogonal", "systeme"]

    def generate(self):
        # To guarantee clean integer coordinates, we build backwards.
        # H is the intersection.
        hx = self.rng.randint(-3, 3)
        hy = self.rng.randint(-3, 3)
        
        # d passes through H with direction vector u(ux, uy)
        ux = self.rng.choice([1, 2, 3])
        uy = self.rng.choice([1, 2, 3])
        # eq of d: uy * x - ux * y + cd = 0
        a1, b1 = uy, -ux
        c1 = -a1*hx - b1*hy
        
        # Normal to d is u(ux, uy). So line AH has direction vector n(-uy, ux) => normal is u(ux, uy)
        # So eq of AH is: ux * x + uy * y + cah = 0
        a2, b2 = ux, uy
        c2 = -a2*hx - b2*hy
        
        # A is a point on AH distinct from H. A = H + k * n
        k = self.rng.choice([-2, -1, 1, 2])
        ax = hx - k * uy
        ay = hy + k * ux

        str_a1 = f"{a1}x" if a1 != 1 and a1 != -1 else ("x" if a1 == 1 else "-x")
        str_b1 = format_coeff(b1, "y")
        str_c1 = format_sign(c1)
        eq_d = f"{str_a1} {str_b1} {str_c1} = 0".strip()
        if eq_d.startswith("+"): eq_d = eq_d[1:].strip()

        str_a2 = f"{a2}x" if a2 != 1 and a2 != -1 else ("x" if a2 == 1 else "-x")
        str_b2 = format_coeff(b2, "y")
        str_c2 = format_sign(c2)
        eq_ah = f"{str_a2} {str_b2} {str_c2} = 0".strip()
        if eq_ah.startswith("+"): eq_ah = eq_ah[1:].strip()

        self.statement_fr = [
            f"Soit la droite $d$ d'équation ${eq_d}$ et le point $A\\binom{{{ax}}}{{{ay}}}$."
        ]
        self.statement_en = [
            f"Let $d$ be the line with equation ${eq_d}$ and the point $A\\binom{{{ax}}}{{{ay}}}$."
        ]

        q1_fr = ["Déterminer les coordonnées du point $H$, projeté orthogonal de $A$ sur la droite $d$."]
        q1_en = ["Determine the coordinates of point $H$, the orthogonal projection of $A$ onto line $d$."]
        insight1_fr = ["Déterminez d'abord l'équation de la droite $(AH)$ perpendiculaire à $d$. Puis résolvez le système formé par les équations de $d$ et $(AH)$."]
        insight1_en = ["First determine the equation of line $(AH)$ perpendicular to $d$. Then solve the system formed by the equations of $d$ and $(AH)$."]
        
        ans1_fr = [
            f"• Déterminons une équation de la droite $(AH)$ :",
            f"Comme $d$ et $(AH)$ sont perpendiculaires, un vecteur directeur de $d$ est un vecteur normal de $(AH)$.",
            f"L'équation de $d$ est ${eq_d}$, donc le vecteur $\\vec{{u}}\\binom{{{-b1}}}{{{a1}}}$ est un vecteur directeur de $d$.",
            f"Et donc $\\vec{{u}}\\binom{{{-b1}}}{{{a1}}}$ est un vecteur normal de $(AH)$.",
            f"Une équation de $(AH)$ est de la forme : ${-b1}x {format_sign(a1)}y + c = 0$.",
            f"Le point $A\\binom{{{ax}}}{{{ay}}}$ appartient à $(AH)$, donc : ${-b1}({ax}) {format_sign(a1)}({ay}) + c = 0 \\implies c = {c2}$.",
            f"Une équation de $(AH)$ est donc : **${eq_ah}$**.",
            f"• $H$ est le point d'intersection de $d$ et $(AH)$. On résout le système :",
            f"$\\begin{{cases}} {eq_d} \\\\ {eq_ah} \\end{{cases}}$",
            f"La résolution du système donne $x = {hx}$ et $y = {hy}$.",
            f"Le projeté orthogonal a pour coordonnées **$H\\binom{{{hx}}}{{{hy}}}$**."
        ]
        ans1_en = [
            f"• Let's determine an equation of the line $(AH)$:",
            f"Since $d$ and $(AH)$ are perpendicular, a direction vector of $d$ is a normal vector of $(AH)$.",
            f"The equation of $d$ is ${eq_d}$, so the vector $\\vec{{u}}\\binom{{{-b1}}}{{{a1}}}$ is a direction vector of $d$.",
            f"And therefore $\\vec{{u}}\\binom{{{-b1}}}{{{a1}}}$ is a normal vector of $(AH)$.",
            f"An equation of $(AH)$ is of the form: ${-b1}x {format_sign(a1)}y + c = 0$.",
            f"The point $A\\binom{{{ax}}}{{{ay}}}$ belongs to $(AH)$, so: ${-b1}({ax}) {format_sign(a1)}({ay}) + c = 0 \\implies c = {c2}$.",
            f"An equation of $(AH)$ is therefore: **${eq_ah}$**.",
            f"• $H$ is the intersection point of $d$ and $(AH)$. We solve the system:",
            f"$\\begin{{cases}} {eq_d} \\\\ {eq_ah} \\end{{cases}}$",
            f"Solving the system gives $x = {hx}$ and $y = {hy}$.",
            f"The orthogonal projection has coordinates **$H\\binom{{{hx}}}{{{hy}}}$**."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 5 : Déterminer une équation de cercle
# ==========================================
class CircleEquationFromPoints(BaseExercise):
    id = "GEO_005"
    title = {"fr": "Équation de cercle (Centre et point)", "en": "Circle equation (Center and point)"}
    tags = ["geometrie", "cercle", "equation cartesienne", "distance"]

    def generate(self):
        ax = self.rng.randint(-4, 4)
        ay = self.rng.randint(-4, 4)
        bx = self.rng.randint(-4, 4)
        by = self.rng.randint(-4, 4)
        while ax == bx and ay == by:
            bx = self.rng.randint(-4, 4)
            by = self.rng.randint(-4, 4)

        self.statement_fr = [
            f"On considère le cercle de centre $A\\binom{{{ax}}}{{{ay}}}$ et passant par le point $B\\binom{{{bx}}}{{{by}}}$."
        ]
        self.statement_en = [
            f"Consider the circle with center $A\\binom{{{ax}}}{{{ay}}}$ and passing through the point $B\\binom{{{bx}}}{{{by}}}$."
        ]

        q1_fr = ["Déterminer une équation cartésienne de ce cercle."]
        q1_en = ["Determine a Cartesian equation of this circle."]
        insight1_fr = ["La forme générale est $(x - x_A)^2 + (y - y_A)^2 = r^2$. Calculez $r^2$ grâce à la distance $AB$."]
        insight1_en = ["The general form is $(x - x_A)^2 + (y - y_A)^2 = r^2$. Calculate $r^2$ using the distance $AB$."]
        
        r_sq = (bx - ax)**2 + (by - ay)**2
        
        str_ax = format_sign(-ax)
        str_ay = format_sign(-ay)

        ans1_fr = [
            f"• Le cercle a pour centre le point $A\\binom{{{ax}}}{{{ay}}}$, donc son équation est de la forme :",
            f"$(x - ({ax}))^2 + (y - ({ay}))^2 = r^2 \\implies (x {str_ax})^2 + (y {str_ay})^2 = r^2$",
            f"• On détermine le carré du rayon à l'aide de la formule de la distance :",
            f"$r^2 = AB^2 = ({bx} - ({ax}))^2 + ({by} - ({ay}))^2 = ({bx - ax})^2 + ({by - ay})^2 = {r_sq}$.",
            f"• Une équation cartésienne du cercle est alors :",
            f"**$(x {str_ax})^2 + (y {str_ay})^2 = {r_sq}$**"
        ]
        ans1_en = [
            f"• The circle is centered at $A\\binom{{{ax}}}{{{ay}}}$, so its equation is of the form:",
            f"$(x - ({ax}))^2 + (y - ({ay}))^2 = r^2 \\implies (x {str_ax})^2 + (y {str_ay})^2 = r^2$",
            f"• We determine the square of the radius using the distance formula:",
            f"$r^2 = AB^2 = ({bx} - ({ax}))^2 + ({by} - ({ay}))^2 = ({bx - ax})^2 + ({by - ay})^2 = {r_sq}$.",
            f"• A Cartesian equation of the circle is then:",
            f"**$(x {str_ax})^2 + (y {str_ay})^2 = {r_sq}$**"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 6 : Caractéristiques d'un cercle
# ==========================================
class CircleFeaturesFromEquation(BaseExercise):
    id = "GEO_006"
    title = {"fr": "Caractéristiques d'un cercle", "en": "Features of a circle"}
    tags = ["geometrie", "cercle", "centre", "rayon", "equation"]

    def generate(self):
        # We start by building a clean circle equation: (x-cx)^2 + (y-cy)^2 = r^2
        cx = self.rng.randint(-5, 5)
        cy = self.rng.randint(-5, 5)
        r = self.rng.choice([2, 3, 4, 5])
        r_sq = r**2
        
        # Expanded form: x^2 + y^2 - 2cx x - 2cy y + cx^2 + cy^2 - r^2 = 0
        alpha = -2 * cx
        beta = -2 * cy
        gamma = cx**2 + cy**2 - r_sq
        
        str_alpha = format_coeff(alpha, "x")
        str_beta = format_coeff(beta, "y")
        str_gamma = format_sign(gamma)
        
        eq_exp = f"x^2 + y^2 {str_alpha} {str_beta} {str_gamma} = 0"

        self.statement_fr = [
            f"L'équation ${eq_exp}$ est-elle une équation de cercle ?"
        ]
        self.statement_en = [
            f"Is the equation ${eq_exp}$ a circle equation?"
        ]

        q1_fr = ["Si oui, déterminer son centre et son rayon."]
        q1_en = ["If yes, determine its center and radius."]
        insight1_fr = ["Regroupez les termes en $x$ et en $y$, puis forcez l'apparition d'identités remarquables de la forme $(x - a)^2$."]
        insight1_en = ["Group the terms in $x$ and $y$, then force the appearance of perfect squares of the form $(x - a)^2$."]
        
        cx_sign = format_sign(-cx)
        cy_sign = format_sign(-cy)

        ans1_fr = [
            f"$x^2 + y^2 {str_alpha} {str_beta} {str_gamma} = 0$",
            f"On regroupe et on identifie le début d'identités remarquables :",
            f"$(x^2 {str_alpha}) + (y^2 {str_beta}) {str_gamma} = 0$",
            f"$\\left[(x {cx_sign})^2 - {cx**2}\\right] + \\left[(y {cy_sign})^2 - {cy**2}\\right] {str_gamma} = 0$",
            f"$(x {cx_sign})^2 + (y {cy_sign})^2 - {cx**2} - {cy**2} {str_gamma} = 0$",
            f"$(x {cx_sign})^2 + (y {cy_sign})^2 = {r_sq}$",
            f"Comme ${r_sq} > 0$ (${r_sq} = {r}^2$), c'est bien l'équation d'un cercle.",
            f"**Le centre est $A\\binom{{{cx}}}{{{cy}}}$ et le rayon est $r = {r}$.**"
        ]
        ans1_en = [
            f"$x^2 + y^2 {str_alpha} {str_beta} {str_gamma} = 0$",
            f"We group the terms and identify the start of perfect squares:",
            f"$(x^2 {str_alpha}) + (y^2 {str_beta}) {str_gamma} = 0$",
            f"$\\left[(x {cx_sign})^2 - {cx**2}\\right] + \\left[(y {cy_sign})^2 - {cy**2}\\right] {str_gamma} = 0$",
            f"$(x {cx_sign})^2 + (y {cy_sign})^2 - {cx**2} - {cy**2} {str_gamma} = 0$",
            f"$(x {cx_sign})^2 + (y {cy_sign})^2 = {r_sq}$",
            f"Since ${r_sq} > 0$ (${r_sq} = {r}^2$), this is indeed a circle equation.",
            f"**The center is $A\\binom{{{cx}}}{{{cy}}}$ and the radius is $r = {r}$.**"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))
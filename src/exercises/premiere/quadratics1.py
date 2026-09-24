import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from exercises.base_exercise import BaseExercise
from exercises.question import Question

# Module-level registry key
CHAPTER = {"fr": "Polynômes du Second Degré Partie 1", "en": "Quadratic Polynomials Part 1"}

def _build_canonical_latex(a, alpha, beta):
    """Helper function to build the canonical string without SymPy auto-expanding it."""
    a_str = "" if a == 1 else ("-" if a == -1 else str(a))
    
    if alpha == 0:
        term_x = "x^2"
    else:
        sign_alpha = "-" if alpha > 0 else "+"
        term_x = f"(x {sign_alpha} {abs(alpha)})^2"
        
    term_beta = ""
    if beta > 0:
        term_beta = f" + {beta}"
    elif beta < 0:
        term_beta = f" - {abs(beta)}"
        
    return f"{a_str}{term_x}{term_beta}"


# ==========================================
# MÉTHODE 1 : Déterminer la forme canonique
# ==========================================
class DetermineCanonicalForm(BaseExercise):
    id = "SD_001"
    title = {"fr": "Déterminer la forme canonique", "en": "Determine the canonical form"}
    tags = ["second-degre", "canonique", "calcul"]

    def generate(self):
        # 1. Reverse Engineering: Pick answers to ensure clean calculations
        a = self.rng.choice([-3, -2, -1, 2, 3]) 
        alpha = self.rng.randint(-5, 5)
        beta = self.rng.randint(-10, 10)

        # 2. Calculate parameters for expanded form ax^2 + bx + c
        b = -2 * a * alpha
        c = a * (alpha ** 2) + beta

        # 3. Construct math expressions
        x = sp.Symbol('x')
        f_expanded = a * x**2 + b * x + c
        f_tex = sp.latex(f_expanded)
        canonical_tex = _build_canonical_latex(a, alpha, beta)

        # 4. Data Population
        self.statement_fr = [f"Soit la fonction polynôme $f$ du second degré définie sur $\\mathbb{{R}}$ par : $f(x) = {f_tex}$."]
        self.statement_en = [f"Let $f$ be a quadratic polynomial function defined on $\\mathbb{{R}}$ by: $f(x) = {f_tex}$."]

        q1_fr = ["Ecrire $f$ sous sa forme canonique."]
        q1_en = ["Write $f$ in its canonical form."]
        
        insight1_fr = [f"Identifiez les coefficients : $a={a}$, $b={b}$, $c={c}$. Calculez $\\alpha = -\\frac{{b}}{{2a}}$ et $\\beta = f(\\alpha)$."]
        insight1_en = [f"Identify the coefficients: $a={a}$, $b={b}$, $c={c}$. Calculate $\\alpha = -\\frac{{b}}{{2a}}$ and $\\beta = f(\\alpha)$."]
        
        ans1_fr = [f"{canonical_tex}$ est la forme canonique de $f$."]
        ans1_en = [f"{canonical_tex}$ is the canonical form of $f$."]

        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 2 : Caractéristiques d'une parabole
# ==========================================
class ParabolaCharacteristics(BaseExercise):
    id = "SD_002"
    title = {"fr": "Caractéristiques d'une parabole", "en": "Characteristics of a parabola"}
    tags = ["second-degre", "parabole", "sommet", "symetrie"]

    def generate(self):
        a = self.rng.choice([-4, -2, -1, 1, 2, 4]) 
        alpha = self.rng.randint(-4, 4)
        beta = self.rng.randint(-8, 8)

        b = -2 * a * alpha
        c = a * (alpha ** 2) + beta

        x = sp.Symbol('x')
        f_expanded = a * x**2 + b * x + c
        f_tex = sp.latex(f_expanded)

        self.statement_fr = [f"Soit la fonction polynôme du second degré définie par $f(x) = {f_tex}$."]
        self.statement_en = [f"Let the quadratic polynomial function be defined by $f(x) = {f_tex}$."]

        # Question 1: Sommet
        q1_fr = ["Déterminer les coordonnées du sommet de la parabole de $f$."]
        q1_en = ["Determine the coordinates of the vertex of the parabola of $f$."]
        
        insight1_fr = [f"Les coordonnées du sommet sont $(\\alpha ; \\beta)$. Calculez $\\alpha = -\\frac{{({b})}}{{2 \\times ({a})}}$."]
        insight1_en = [f"The coordinates of the vertex are $(\\alpha ; \\beta)$. Calculate $\\alpha = -\\frac{{({b})}}{{2 \\times ({a})}}$."]
        
        ans1_fr = [f"Le sommet de la parabole a pour coordonnées $({alpha} ; {beta})$."]
        ans1_en = [f"The vertex of the parabola has coordinates $({alpha} ; {beta})$."]

        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question 2: Axe de symétrie
        q2_fr = ["Déterminer l'équation de son axe de symétrie."]
        q2_en = ["Determine the equation of its axis of symmetry."]
        
        insight2_fr = ["La parabole admet pour axe de symétrie la droite d'équation $x = \\alpha$."]
        insight2_en = ["The parabola admits as an axis of symmetry the line with equation $x = \\alpha$."]
        
        ans2_fr = [f"La droite d'équation $x = {alpha}$ est l'axe de symétrie de la parabole."]
        ans2_en = [f"The line with equation $x = {alpha}$ is the axis of symmetry of the parabola."]

        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 3 : Variations et Représentation
# ==========================================
class QuadraticVariations(BaseExercise):
    id = "SD_003"
    title = {"fr": "Représentation graphique", "en": "Graphical representation"}
    tags = ["second-degre", "variations", "graphique"]

    def generate(self):
        a = self.rng.choice([-2, -1, 1, 2]) 
        alpha = self.rng.randint(-3, 3)
        beta = self.rng.randint(-5, 5)

        b = -2 * a * alpha
        c = a * (alpha ** 2) + beta

        x = sp.Symbol('x')
        f_expanded = a * x**2 + b * x + c
        f_tex = sp.latex(f_expanded)

        self.statement_fr = []
        self.statement_en = []

        # Single straightforward instruction
        q1_fr = [f"Représenter graphiquement la fonction polynôme $f$ du second degré définie sur $\\mathbb{{R}}$ par $f(x) = {f_tex}$."]
        q1_en = [f"Graph the second-degree polynomial function $f$ defined on $\\mathbb{{R}}$ by $f(x) = {f_tex}$."]

        insight1_fr = ["Pour tracer la parabole, déterminez son orientation (signe de $a$), calculez les coordonnées de son sommet, puis trouvez quelques points de passage évidents comme l'ordonnée à l'origine."]
        insight1_en = ["To draw the parabola, determine its orientation (sign of $a$), calculate its vertex coordinates, then find a few obvious passing points like the y-intercept."]

        # Calculate a passing point
        pt2_x = alpha + 1
        pt2_y = a * (pt2_x ** 2) + b * pt2_x + c

        # Graph generation
        x_vals = np.linspace(alpha - 4, alpha + 4, 400)
        y_vals = a * (x_vals - alpha)**2 + beta 

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x_vals, y_vals, color="blue", linewidth=2, label=f"$f(x)={f_tex}$")
        ax.plot(alpha, beta, 'ro', markersize=6, label="Sommet")
        
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend()

        var_dir_fr = "décroissante, puis croissante" if a > 0 else "croissante, puis décroissante"
        var_dir_en = "decreasing, then increasing" if a > 0 else "increasing, then decreasing"
        extremum_fr = "un minimum" if a > 0 else "un maximum"
        extremum_en = "a minimum" if a > 0 else "a maximum"

        ans1_fr = [
            f"• **Variations :** $a = {a}$. Comme $a {' > 0' if a > 0 else ' < 0'}$, la fonction $f$ est {var_dir_fr}.",
            f"• **Sommet :** La parabole admet {extremum_fr} en $x = {alpha}$ valant $y = {beta}$. Le sommet est donc le point $S({alpha}; {beta})$.",
            f"• **Points de passage :** Pour $x = 0$, $f(0) = {c}$ (point $(0; {c})$). Pour $x = {pt2_x}$, $f({pt2_x}) = {pt2_y}$ (point $({pt2_x}; {pt2_y})$).",
            f"• **Courbe représentative :**",
            fig
        ]
        
        ans1_en = [
            f"• **Variations:** $a = {a}$. Since $a {' > 0' if a > 0 else ' < 0'}$, the function $f$ is {var_dir_en}.",
            f"• **Vertex:** The parabola has {extremum_en} at $x = {alpha}$ with value $y = {beta}$. The vertex is the point $S({alpha}; {beta})$.",
            f"• **Passing points:** For $x = 0$, $f(0) = {c}$ (point $(0; {c})$). For $x = {pt2_x}$, $f({pt2_x}) = {pt2_y}$ (point $({pt2_x}; {pt2_y})$).",
            f"• **Representative curve:**",
            fig
        ]

        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))
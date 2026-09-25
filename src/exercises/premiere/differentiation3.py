import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from exercises.base_exercise import BaseExercise
from exercises.question import Question

# Module-level registry key
CHAPTER = {"fr": "Dérivation (Partie 3)", "en": "Differentiation (Part 3)"}

# ==========================================
# MÉTHODE 1 : Lien entre signe de dérivée et variations
# ==========================================
class SignAndVariations(BaseExercise):
    id = "DER3_001"
    title = {"fr": "Lien entre dérivée et variations", "en": "Link between derivative and variations"}
    tags = ["derivation", "variations", "signe", "graphique"]

    def generate(self):
        # Paramètres aléatoires
        x0_a = self.rng.randint(1, 5)
        y0_a = self.rng.randint(-5, 5)
        
        x0_b = self.rng.randint(2, 6)
        y0_b = self.rng.randint(1, 8)

        # Graphique pour c)
        fig_c, ax_c = plt.subplots(figsize=(6, 4))
        x_vals = np.linspace(-3, 3, 400)
        # Fonction cubique f(x) = x^3 - 3x (extrema en -1 et 1)
        y_vals = x_vals**3 - 3*x_vals
        ax_c.plot(x_vals, y_vals, color="blue", linewidth=2)
        ax_c.axhline(0, color='black', linewidth=1)
        ax_c.axvline(0, color='black', linewidth=1)
        ax_c.grid(True, linestyle='--', alpha=0.7)
        ax_c.set_xlim(-3, 3)
        ax_c.set_ylim(-5, 5)

        self.statement_fr = ["Comprendre le lien entre le signe de la dérivée et les variations de la fonction."]
        self.statement_en = ["Understand the link between the sign of the derivative and the variations of the function."]

        # Question a
        q1_fr = [
            f"a) Soit $f$ définie sur $\\mathbb{{R}}$ avec $f({x0_a}) = {y0_a}$. On donne le signe de la dérivée. Compléter le tableau de variations.",
            f"| $x$ | $-\\infty$ | | ${x0_a}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $-$ | $0$ | $+$ | |"
        ]
        q1_en = [
            f"a) Let $f$ be defined on $\\mathbb{{R}}$ with $f({x0_a}) = {y0_a}$. The sign of the derivative is given. Complete the variation table.",
            f"| $x$ | $-\\infty$ | | ${x0_a}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $-$ | $0$ | $+$ | |"
        ]
        insight1_fr = ["Si $f'(x) \\le 0$, $f$ est décroissante ($\\searrow$). Si $f'(x) \\ge 0$, $f$ est croissante ($\\nearrow$)."]
        insight1_en = ["If $f'(x) \\le 0$, $f$ is decreasing ($\\searrow$). If $f'(x) \\ge 0$, $f$ is increasing ($\\nearrow$)."]
        ans1_fr = [
            f"| $x$ | $-\\infty$ | | ${x0_a}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $-$ | $0$ | $+$ | |\n"
            f"| $f(x)$ | | $\\searrow$ | ${y0_a}$ | $\\nearrow$ | |"
        ]
        ans1_en = [
            f"| $x$ | $-\\infty$ | | ${x0_a}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $-$ | $0$ | $+$ | |\n"
            f"| $f(x)$ | | $\\searrow$ | ${y0_a}$ | $\\nearrow$ | |"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question b
        q2_fr = [
            f"b) Soit $f$ définie sur $\\mathbb{{R}}$ avec $f({x0_b}) = {y0_b}$. On donne les variations de $f$. Compléter avec le signe de la dérivée.",
            f"| $x$ | $-\\infty$ | | ${x0_b}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f(x)$ | | $\\nearrow$ | ${y0_b}$ | $\\searrow$ | |"
        ]
        q2_en = [
            f"b) Let $f$ be defined on $\\mathbb{{R}}$ with $f({x0_b}) = {y0_b}$. The variations of $f$ are given. Complete with the sign of the derivative.",
            f"| $x$ | $-\\infty$ | | ${x0_b}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f(x)$ | | $\\nearrow$ | ${y0_b}$ | $\\searrow$ | |"
        ]
        insight2_fr = ["Une fonction croissante a une dérivée positive. Une fonction décroissante a une dérivée négative."]
        insight2_en = ["An increasing function has a positive derivative. A decreasing function has a negative derivative."]
        ans2_fr = [
            f"| $x$ | $-\\infty$ | | ${x0_b}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $+$ | $0$ | $-$ | |\n"
            f"| $f(x)$ | | $\\nearrow$ | ${y0_b}$ | $\\searrow$ | |"
        ]
        ans2_en = [
            f"| $x$ | $-\\infty$ | | ${x0_b}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $+$ | $0$ | $-$ | |\n"
            f"| $f(x)$ | | $\\nearrow$ | ${y0_b}$ | $\\searrow$ | |"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))

        # Question c
        q3_fr = ["c) On donne la représentation graphique de la fonction $f$. Dresser son tableau de variations complet (signe de $f'$ et variations de $f$).", fig_c]
        q3_en = ["c) The graph of the function $f$ is given. Draw its complete variation table (sign of $f'$ and variations of $f$).", fig_c]
        insight3_fr = ["Repérez les abscisses où la courbe change de sens (tangentes horizontales). Ici, en $x=-1$ et $x=1$."]
        insight3_en = ["Identify the x-coordinates where the curve changes direction (horizontal tangents). Here, at $x=-1$ and $x=1$."]
        ans3_fr = [
            f"La courbe monte jusqu'en $x=-1$ ($y=2$), puis descend jusqu'en $x=1$ ($y=-2$), puis remonte.",
            f"| $x$ | $-\\infty$ | | $-1$ | | $1$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |\n"
            f"| $f(x)$ | | $\\nearrow$ | $2$ | $\\searrow$ | $-2$ | $\\nearrow$ | |"
        ]
        ans3_en = [
            f"The curve goes up until $x=-1$ ($y=2$), then down until $x=1$ ($y=-2$), then up again.",
            f"| $x$ | $-\\infty$ | | $-1$ | | $1$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |\n"
            f"| $f(x)$ | | $\\nearrow$ | $2$ | $\\searrow$ | $-2$ | $\\nearrow$ | |"
        ]
        self.questions.append(Question(q3_fr, q3_en, insight3_fr, insight3_en, ans3_fr, ans3_en))


# ==========================================
# MÉTHODE 2 : Variations du 2nd degré
# ==========================================
class VariationsDegree2(BaseExercise):
    id = "DER3_002"
    title = {"fr": "Variations d'un polynôme de degré 2", "en": "Variations of a 2nd degree polynomial"}
    tags = ["derivation", "second-degre", "variations"]

    def generate(self):
        a = self.rng.choice([2, 3, 4])
        b = self.rng.choice([-12, -8, -4, 4, 8, 12])
        c = self.rng.randint(-5, 5)
        
        x = sp.Symbol('x')
        f_expr = a*x**2 + b*x + c
        f_prime_expr = 2*a*x + b
        
        root = -b // (2*a)
        y_val = f_expr.subs(x, root)

        self.statement_fr = [f"Soit la fonction $f$ définie sur $\\mathbb{{R}}$ par $f(x) = {sp.latex(f_expr)}$."]
        self.statement_en = [f"Let $f$ be the function defined on $\\mathbb{{R}}$ by $f(x) = {sp.latex(f_expr)}$."]

        q1_fr = ["a) Calculer la fonction dérivée $f'$.", "b) Déterminer le signe de $f'$ en fonction de $x$.", "c) Dresser le tableau de variations de $f$."]
        q1_en = ["a) Calculate the derivative $f'$.", "b) Determine the sign of $f'$ depending on $x$.", "c) Draw the variation table of $f$."]
        
        insight1_fr = ["$f'$ est une fonction affine $mx + p$. Son signe dépend de $m$."]
        insight1_en = ["$f'$ is an affine function $mx + p$. Its sign depends on $m$."]
        
        ans1_fr = [
            f"a) $f'(x) = {sp.latex(f_prime_expr)}$.",
            f"b) On résout $f'(x) = 0 \\iff {2*a}x = {-b} \\iff x = {root}$.",
            f"La fonction $f'$ est une droite de coefficient directeur ${2*a} > 0$. Elle est donc d'abord négative, puis positive.",
            f"c) $f({root}) = {y_val}$.",
            f"| $x$ | $-\\infty$ | | ${root}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $-$ | $0$ | $+$ | |\n"
            f"| $f(x)$ | | $\\searrow$ | ${y_val}$ | $\\nearrow$ | |"
        ]
        ans1_en = [
            f"a) $f'(x) = {sp.latex(f_prime_expr)}$.",
            f"b) We solve $f'(x) = 0 \\iff {2*a}x = {-b} \\iff x = {root}$.",
            f"The function $f'$ is a line with slope ${2*a} > 0$. It is therefore first negative, then positive.",
            f"c) $f({root}) = {y_val}$.",
            f"| $x$ | $-\\infty$ | | ${root}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $-$ | $0$ | $+$ | |\n"
            f"| $f(x)$ | | $\\searrow$ | ${y_val}$ | $\\nearrow$ | |"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 3 : Variations du 3e degré
# ==========================================
class VariationsDegree3(BaseExercise):
    id = "DER3_003"
    title = {"fr": "Variations d'un polynôme de degré 3", "en": "Variations of a 3rd degree polynomial"}
    tags = ["derivation", "troisieme-degre", "variations"]

    def generate(self):
        # We construct f'(x) = 3a(x-x1)(x-x2) to have clean integer roots
        x1, x2 = sorted(self.rng.sample([-4, -3, -2, -1, 1, 2, 3, 4], k=2))
        a = 1
        x = sp.Symbol('x')
        f_prime = sp.expand(3 * a * (x - x1) * (x - x2))
        
        # Integrate to get f(x)
        f_expr = sp.integrate(f_prime, x) + self.rng.randint(-5, 5)
        
        y1 = f_expr.subs(x, x1)
        y2 = f_expr.subs(x, x2)

        self.statement_fr = [f"Soit la fonction $f$ définie sur $\\mathbb{{R}}$ par $f(x) = {sp.latex(f_expr)}$."]
        self.statement_en = [f"Let $f$ be the function defined on $\\mathbb{{R}}$ by $f(x) = {sp.latex(f_expr)}$."]

        q1_fr = ["a) Calculer $f'(x)$.", "b) Déterminer le signe de $f'$.", "c) Dresser le tableau de variations de $f$."]
        q1_en = ["a) Calculate $f'(x)$.", "b) Determine the sign of $f'$.", "c) Draw the variation table of $f$."]
        
        insight1_fr = ["$f'$ est un trinôme du second degré. Calculez son discriminant pour trouver ses racines, puis appliquez la règle du signe d'un trinôme."]
        insight1_en = ["$f'$ is a quadratic trinomial. Calculate its discriminant to find its roots, then apply the sign rule for a trinomial."]
        
        a_p, b_p, c_p = f_prime.coeff(x, 2), f_prime.coeff(x, 1), f_prime.subs(x, 0)
        delta = b_p**2 - 4*a_p*c_p

        ans1_fr = [
            f"a) $f'(x) = {sp.latex(f_prime)}$.",
            f"b) On étudie le signe du trinôme. $\\Delta = {delta}$. Les racines sont $x_1 = {x1}$ et $x_2 = {x2}$.",
            f"Comme $a = {a_p} > 0$, la parabole de la dérivée a les branches vers le haut. La dérivée est positive, puis négative, puis positive.",
            f"c) $f({x1}) = {y1}$ et $f({x2}) = {y2}$.",
            f"| $x$ | $-\\infty$ | | ${x1}$ | | ${x2}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |\n"
            f"| $f(x)$ | | $\\nearrow$ | ${y1}$ | $\\searrow$ | ${y2}$ | $\\nearrow$ | |"
        ]
        ans1_en = [
            f"a) $f'(x) = {sp.latex(f_prime)}$.",
            f"b) We study the sign of the trinomial. $\\Delta = {delta}$. The roots are $x_1 = {x1}$ and $x_2 = {x2}$.",
            f"Since $a = {a_p} > 0$, the branches of the derivative's parabola open upwards. The derivative is positive, negative, then positive.",
            f"c) $f({x1}) = {y1}$ and $f({x2}) = {y2}$.",
            f"| $x$ | $-\\infty$ | | ${x1}$ | | ${x2}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |\n"
            f"| $f(x)$ | | $\\nearrow$ | ${y1}$ | $\\searrow$ | ${y2}$ | $\\nearrow$ | |"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 4 : Variations d'une fonction rationnelle
# ==========================================
class VariationsRational(BaseExercise):
    id = "DER3_004"
    title = {"fr": "Variations d'une fonction rationnelle", "en": "Variations of a rational function"}
    tags = ["derivation", "rationnelle", "quotient"]

    def generate(self):
        # f(x) = (x + b) / (c - x) to closely match the PDF
        b = self.rng.randint(1, 5)
        c = self.rng.randint(1, 5)
        x = sp.Symbol('x')
        
        num = x + b
        den = c - x
        f_expr = num / den
        
        # Derivative: (1*(c-x) - (x+b)*(-1)) / (c-x)^2 = (c - x + x + b) / (c-x)^2 = (c+b) / (c-x)^2
        num_prime = c + b

        self.statement_fr = [f"Soit la fonction $f$ définie sur $\\mathbb{{R}} \\setminus \\{{{c}\\}}$ par $f(x) = {sp.latex(f_expr)}$."]
        self.statement_en = [f"Let $f$ be the function defined on $\\mathbb{{R}} \\setminus \\{{{c}\\}}$ by $f(x) = {sp.latex(f_expr)}$."]

        q1_fr = ["a) Calculer $f'(x)$.", "b) Déterminer le signe de $f'$.", "c) Dresser le tableau de variations de $f$."]
        q1_en = ["a) Calculate $f'(x)$.", "b) Determine the sign of $f'$.", "c) Draw the variation table of $f$."]
        
        insight1_fr = ["Utilisez la formule $\\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2}$. Le dénominateur étant un carré, il est toujours strictement positif sur le domaine de définition."]
        insight1_en = ["Use the formula $\\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2}$. The denominator is a square, so it is always strictly positive on the domain."]
        
        ans1_fr = [
            f"a) En appliquant la formule du quotient : $f'(x) = \\frac{{1 \\times ({c} - x) - (x + {b}) \\times (-1)}}{{({c} - x)^2}} = \\frac{{{num_prime}}}{{({c} - x)^2}}$.",
            f"b) $({c} - x)^2$ est un carré donc toujours strictement positif pour $x \\neq {c}$. Le numérateur {num_prime} est positif, donc $f'(x) > 0$.",
            f"c) La double-barre signifie que la fonction n'est pas définie en $x={c}$.",
            f"| $x$ | $-\\infty$ | | ${c}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $+$ | $\\|$ | $+$ | |\n"
            f"| $f(x)$ | | $\\nearrow$ | $\\|$ | $\\nearrow$ | |"
        ]
        ans1_en = [
            f"a) Applying the quotient formula: $f'(x) = \\frac{{1 \\times ({c} - x) - (x + {b}) \\times (-1)}}{{({c} - x)^2}} = \\frac{{{num_prime}}}{{({c} - x)^2}}$.",
            f"b) $({c} - x)^2$ is a square and thus always strictly positive for $x \\neq {c}$. The numerator {num_prime} is positive, so $f'(x) > 0$.",
            f"c) The double bar means the function is undefined at $x={c}$.",
            f"| $x$ | $-\\infty$ | | ${c}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $+$ | $\\|$ | $+$ | |\n"
            f"| $f(x)$ | | $\\nearrow$ | $\\|$ | $\\nearrow$ | |"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 5 : Extremum d'une fonction
# ==========================================
class FunctionExtremum(BaseExercise):
    id = "DER3_005"
    title = {"fr": "Déterminer un extremum", "en": "Determine an extremum"}
    tags = ["derivation", "extremum", "tangente"]

    def generate(self):
        a = self.rng.choice([2, 3, 4, 5])
        b_half = self.rng.choice([-5, -4, -3, 3, 4, 5])
        b = 2 * a * b_half # To ensure root of derivative is an integer (x0 = -b/2a = -b_half)
        c = self.rng.randint(-5, 5)
        
        x = sp.Symbol('x')
        f_expr = a*x**2 + b*x + c
        f_prime_expr = 2*a*x + b
        
        root = -b // (2*a)
        y_val = f_expr.subs(x, root)

        self.statement_fr = [f"Soit la fonction $f$ définie sur $\\mathbb{{R}}$ par $f(x) = {sp.latex(f_expr)}$."]
        self.statement_en = [f"Let $f$ be the function defined on $\\mathbb{{R}}$ by $f(x) = {sp.latex(f_expr)}$."]

        q1_fr = [
            "a) Calculer $f'(x)$ et déterminer son signe.",
            "b) Dresser le tableau de variations de $f$.",
            "c) En déduire que $f$ admet un extremum. Préciser sa valeur.",
            "d) Déterminer l'équation de la tangente au point de l'extremum."
        ]
        q1_en = [
            "a) Calculate $f'(x)$ and determine its sign.",
            "b) Draw the variation table of $f$.",
            "c) Deduce that $f$ has an extremum. Specify its value.",
            "d) Determine the equation of the tangent at the extremum point."
        ]
        
        insight1_fr = ["L'extremum est atteint lorsque la dérivée s'annule en changeant de signe. En ce point, la tangente est horizontale."]
        insight1_en = ["The extremum is reached when the derivative cancels out while changing sign. At this point, the tangent is horizontal."]
        
        ans1_fr = [
            f"a) $f'(x) = {sp.latex(f_prime_expr)}$. On résout $f'(x) = 0 \\implies x = {root}$. La fonction affine est croissante ($a={2*a}>0$), donc d'abord $-$ puis $+$.",
            f"b) Tableau de variations :",
            f"| $x$ | $-\\infty$ | | ${root}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $-$ | $0$ | $+$ | |\n"
            f"| $f(x)$ | | $\\searrow$ | ${y_val}$ | $\\nearrow$ | |",
            f"c) On lit dans le tableau que la fonction admet un minimum égal à ${y_val}$ atteint en $x={root}$.",
            f"d) À l'extremum, $f'({root}) = 0$. La tangente est horizontale. Son équation est $y = f({root})$, soit **$y = {y_val}$**."
        ]
        ans1_en = [
            f"a) $f'(x) = {sp.latex(f_prime_expr)}$. We solve $f'(x) = 0 \\implies x = {root}$. The affine function is increasing ($a={2*a}>0$), so first $-$ then $+$.",
            f"b) Variation table:",
            f"| $x$ | $-\\infty$ | | ${root}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $-$ | $0$ | $+$ | |\n"
            f"| $f(x)$ | | $\\searrow$ | ${y_val}$ | $\\nearrow$ | |",
            f"c) We read from the table that the function has a minimum equal to ${y_val}$ reached at $x={root}$.",
            f"d) At the extremum, $f'({root}) = 0$. The tangent is horizontal. Its equation is $y = f({root})$, which is **$y = {y_val}$**."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 6 : Tracer à l'aide du tableau
# ==========================================
class TraceFromTable(BaseExercise):
    id = "DER3_006"
    title = {"fr": "Tracer une courbe d'après ses variations", "en": "Draw a curve from its variations"}
    tags = ["derivation", "graphique", "variations"]

    def generate(self):
        # 1. Génération des abscisses (strictement croissantes)
        x1 = self.rng.randint(-6, -3)
        x2 = x1 + self.rng.randint(2, 4)
        x3 = x2 + self.rng.randint(3, 5)
        x4 = x3 + self.rng.randint(2, 4)

        # 2. Génération des ordonnées respectant les signes de la dérivée (+, -, +)
        y2 = self.rng.randint(2, 6)                 # Maximum local
        y1 = y2 - self.rng.randint(2, 5)            # Point de départ (y1 < y2)
        y3 = y2 - self.rng.randint(3, 7)            # Minimum local (y3 < y2)
        y4 = y3 + self.rng.randint(2, 5)            # Point d'arrivée (y4 > y3)

        self.statement_fr = [
            f"On donne le tableau de variations de la fonction $f$ définie sur l'intervalle $[{x1}; {x4}]$.",
            f"| $x$ | ${x1}$ | | ${x2}$ | | ${x3}$ | | ${x4}$ |\n"
            f"|---|---|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |\n"
            f"| $f(x)$ | ${y1}$ | $\\nearrow$ | ${y2}$ | $\\searrow$ | ${y3}$ | $\\nearrow$ | ${y4}$ |"
        ]
        self.statement_en = [
            f"The variation table of function $f$ defined on the interval $[{x1}; {x4}]$ is given.",
            f"| $x$ | ${x1}$ | | ${x2}$ | | ${x3}$ | | ${x4}$ |\n"
            f"|---|---|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |\n"
            f"| $f(x)$ | ${y1}$ | $\\nearrow$ | ${y2}$ | $\\searrow$ | ${y3}$ | $\\nearrow$ | ${y4}$ |"
        ]

        q1_fr = ["Tracer dans un repère une représentation graphique possible de la fonction $f$."]
        q1_en = ["Draw a possible graphical representation of the function $f$ in a coordinate system."]
        insight1_fr = [f"Placez les 4 points donnés par le tableau. Tracez des tangentes horizontales aux extrema ($x={x2}$ et $x={x3}$), puis reliez les points par une courbe lisse."]
        insight1_en = [f"Plot the 4 points given by the table. Draw horizontal tangents at the extrema ($x={x2}$ and $x={x3}$), then connect the points with a smooth curve."]
        
        # 3. Génération du graphique solution
        fig, ax = plt.subplots(figsize=(7, 5))
        
        from scipy.interpolate import CubicSpline
        xs = np.array([x1, x2, x3, x4])
        ys = np.array([y1, y2, y3, y4])
        
        # Spline cubique avec dérivées fixées aux bornes pour éviter des oscillations extrêmes
        cs = CubicSpline(xs, ys, bc_type=((1, 1.0), (1, 1.0))) 
        
        x_dense = np.linspace(x1, x4, 200)
        y_dense = cs(x_dense)
        
        ax.plot(x_dense, y_dense, color="green", linewidth=2)
        
        # Points and tangents
        ax.plot(xs, ys, 'r+', markersize=10, markeredgewidth=2)
        
        # Tangente en x2 (maximum local)
        ax.plot([x2 - 1.5, x2 + 1.5], [y2, y2], 'r--', alpha=0.7)
        # Tangente en x3 (minimum local)
        ax.plot([x3 - 1.5, x3 + 1.5], [y3, y3], 'r--', alpha=0.7)
        
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Ajustement dynamique des limites du repère
        ax.set_xlim(x1 - 1, x4 + 1)
        ax.set_ylim(min(y1, y3) - 2, max(y2, y4) + 2)

        ans1_fr = [
            f"On place les points $({x1}; {y1})$, $({x2}; {y2})$, $({x3}; {y3})$ et $({x4}; {y4})$.",
            f"La dérivée s'annule en $x={x2}$ et $x={x3}$, la courbe y possède des tangentes horizontales.",
            fig
        ]
        ans1_en = [
            f"We plot the points $({x1}; {y1})$, $({x2}; {y2})$, $({x3}; {y3})$, and $({x4}; {y4})$.",
            f"The derivative is zero at $x={x2}$ and $x={x3}$, so the curve has horizontal tangents there.",
            fig
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 7 : Fonction paire
# ==========================================
class EvenFunction(BaseExercise):
    id = "DER3_007"
    title = {"fr": "Démontrer qu'une fonction est paire", "en": "Prove that a function is even"}
    tags = ["derivation", "parite", "paire"]

    def generate(self):
        a = self.rng.choice([2, 3, 4, 5])
        b = self.rng.randint(1, 5)
        
        x = sp.Symbol('x')
        f_expr = a*x**2 + b

        self.statement_fr = [f"Soit la fonction $f$ définie par $f(x) = {sp.latex(f_expr)}$."]
        self.statement_en = [f"Let $f$ be the function defined by $f(x) = {sp.latex(f_expr)}$."]

        q1_fr = ["Démontrer que la fonction $f$ est paire."]
        q1_en = ["Prove that the function $f$ is even."]
        insight1_fr = ["Calculez $f(-x)$ et montrez que le résultat est rigoureusement égal à $f(x)$."]
        insight1_en = ["Calculate $f(-x)$ and show that the result is strictly equal to $f(x)$."]
        
        ans1_fr = [
            f"On calcule l'image de $-x$ :",
            f"$f(-x) = {a}(-x)^2 + {b}$",
            f"$f(-x) = {a}x^2 + {b}$ car $(-x)^2 = x^2$.",
            f"Donc $f(-x) = f(x)$. La fonction $f$ est bien paire (sa courbe est symétrique par rapport à l'axe des ordonnées)."
        ]
        ans1_en = [
            f"We calculate the image of $-x$:",
            f"$f(-x) = {a}(-x)^2 + {b}$",
            f"$f(-x) = {a}x^2 + {b}$ because $(-x)^2 = x^2$.",
            f"Thus $f(-x) = f(x)$. The function $f$ is indeed even (its curve is symmetric with respect to the y-axis)."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 8 : Fonction impaire
# ==========================================
class OddFunction(BaseExercise):
    id = "DER3_008"
    title = {"fr": "Démontrer qu'une fonction est impaire", "en": "Prove that a function is odd"}
    tags = ["derivation", "parite", "impaire"]

    def generate(self):
        a = self.rng.choice([1, 2, 3])
        b = self.rng.choice([-5, -4, -3, -2, 2, 3, 4, 5])
        
        x = sp.Symbol('x')
        f_expr = a*x**3 + b*x

        self.statement_fr = [f"Soit la fonction $f$ définie par $f(x) = {sp.latex(f_expr)}$."]
        self.statement_en = [f"Let $f$ be the function defined by $f(x) = {sp.latex(f_expr)}$."]

        q1_fr = ["Démontrer que la fonction $f$ est impaire."]
        q1_en = ["Prove that the function $f$ is odd."]
        insight1_fr = ["Calculez $f(-x)$ et factorisez par $-1$ pour montrer que le résultat est égal à $-f(x)$."]
        insight1_en = ["Calculate $f(-x)$ and factor out $-1$ to show that the result is equal to $-f(x)$."]
        
        a_str = "" if a == 1 else str(a)
        sign_b = f"- {abs(b)}" if b < 0 else f"+ {b}"
        opp_sign_b = f"+ {abs(b)}" if b < 0 else f"- {b}"

        ans1_fr = [
            f"On calcule $f(-x)$ :",
            f"$f(-x) = {a_str}(-x)^3 {sign_b}(-x)$",
            f"$= -{a_str}x^3 {opp_sign_b}x$",
            f"Et on calcule $-f(x)$ :",
            f"$-f(x) = -({a_str}x^3 {sign_b}x) = -{a_str}x^3 {opp_sign_b}x$",
            f"Donc $f(-x) = -f(x)$. La fonction $f$ est bien impaire (sa courbe est symétrique par rapport à l'origine du repère)."
        ]
        ans1_en = [
            f"We calculate $f(-x)$:",
            f"$f(-x) = {a_str}(-x)^3 {sign_b}(-x)$",
            f"$= -{a_str}x^3 {opp_sign_b}x$",
            f"And we calculate $-f(x)$:",
            f"$-f(x) = -({a_str}x^3 {sign_b}x) = -{a_str}x^3 {opp_sign_b}x$",
            f"Thus $f(-x) = -f(x)$. The function $f$ is indeed odd (its curve is symmetric with respect to the origin)."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 9 : Signe d'une fonction à l'aide des variations
# ==========================================
class SignFromVariations(BaseExercise):
    id = "DER3_009"
    title = {"fr": "Signe d'une fonction via ses variations", "en": "Sign of a function via its variations"}
    tags = ["derivation", "signe", "variations", "racine"]

    def generate(self):
        # f(x) = x^3 + cx + d with c > 0 so f'(x) = 3x^2 + c > 0
        c = self.rng.choice([2, 3, 4, 5])
        root = self.rng.choice([-2, -1, 1, 2])
        d = -(root**3 + c*root)
        
        x = sp.Symbol('x')
        f_expr = x**3 + c*x + d
        f_prime_expr = 3*x**2 + c

        self.statement_fr = [f"Soit la fonction $f$ définie sur $\\mathbb{{R}}$ par $f(x) = {sp.latex(f_expr)}$."]
        self.statement_en = [f"Let $f$ be the function defined on $\\mathbb{{R}}$ by $f(x) = {sp.latex(f_expr)}$."]

        q1_fr = [
            "a) Démontrer que la fonction $f$ est strictement croissante.",
            f"b) Vérifier que {root} est une racine de $f$.",
            "c) Dresser le tableau de variations de $f$ et en déduire le signe de $f$ en fonction de $x$."
        ]
        q1_en = [
            "a) Prove that the function $f$ is strictly increasing.",
            f"b) Verify that {root} is a root of $f$.",
            "c) Draw the variation table of $f$ and deduce the sign of $f$ depending on $x$."
        ]
        
        insight1_fr = ["Une fonction est strictement croissante si sa dérivée est strictement positive. Le tableau de variation couplé à la racine donne directement le signe de la fonction."]
        insight1_en = ["A function is strictly increasing if its derivative is strictly positive. The variation table coupled with the root directly gives the sign of the function."]
        
        ans1_fr = [
            f"a) $f'(x) = {sp.latex(f_prime_expr)}$. Comme un carré est toujours positif ou nul, $3x^2 \\ge 0$, donc $3x^2 + {c} > 0$. La dérivée est strictement positive, donc $f$ est strictement croissante.",
            f"b) $f({root}) = ({root})^3 + {c}\\times({root}) + ({d}) = 0$. Donc {root} est bien une racine.",
            f"c) Tableau de variations :",
            f"| $x$ | $-\\infty$ | | ${root}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $+$ | $+$ | $+$ | |\n"
            f"| $f(x)$ | | $\\nearrow$ | $0$ | $\\nearrow$ | |",
            f"D'après ce tableau, la fonction part des négatifs, croise 0 en $x={root}$, puis devient positive.",
            f"- $f$ est négative sur $]-\\infty ; {root}]$",
            f"- $f$ est positive sur $[{root} ; +\\infty[$"
        ]
        ans1_en = [
            f"a) $f'(x) = {sp.latex(f_prime_expr)}$. Since a square is always positive or zero, $3x^2 \\ge 0$, so $3x^2 + {c} > 0$. The derivative is strictly positive, thus $f$ is strictly increasing.",
            f"b) $f({root}) = ({root})^3 + {c}\\times({root}) + ({d}) = 0$. So {root} is indeed a root.",
            f"c) Variation table:",
            f"| $x$ | $-\\infty$ | | ${root}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $+$ | $+$ | $+$ | |\n"
            f"| $f(x)$ | | $\\nearrow$ | $0$ | $\\nearrow$ | |",
            f"According to this table, the function starts negative, crosses 0 at $x={root}$, then becomes positive.",
            f"- $f$ is negative on $(-\\infty ; {root}]$",
            f"- $f$ is positive on $[{root} ; +\\infty)$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 10 : Position relative de deux courbes
# ==========================================
class RelativePositionCubic(BaseExercise):
    id = "DER3_010"
    title = {"fr": "Étudier la position de deux courbes", "en": "Study the position of two curves"}
    tags = ["derivation", "position", "cubique"]

    def generate(self):
        # f(x) = x^3 and g(x) = mx + p. h(x) = x^3 - mx - p
        m = self.rng.choice([-6, -5, -4, -3]) # Negative so h'(x) = 3x^2 - m > 0
        root = self.rng.choice([1, 2, 3])
        p = root**3 - m*root
        
        x = sp.Symbol('x')
        f_expr = x**3
        g_expr = m*x + p

        self.statement_fr = [
            f"Soit $f$ et $g$ deux fonctions définies sur $[{root}; +\\infty[$ par : $f(x) = {sp.latex(f_expr)}$ et $g(x) = {sp.latex(g_expr)}$."
        ]
        self.statement_en = [
            f"Let $f$ and $g$ be two functions defined on $[{root}; +\\infty)$ by: $f(x) = {sp.latex(f_expr)}$ and $g(x) = {sp.latex(g_expr)}$."
        ]

        q1_fr = ["Étudier la position relative des courbes représentatives $C_f$ et $C_g$."]
        q1_en = ["Study the relative position of the representative curves $C_f$ and $C_g$."]
        insight1_fr = ["Étudiez le signe de la différence $h(x) = f(x) - g(x)$ en utilisant les variations de $h$."]
        insight1_en = ["Study the sign of the difference $h(x) = f(x) - g(x)$ by using the variations of $h$."]
        
        h_expr = f_expr - g_expr
        h_prime = sp.diff(h_expr, x)

        ans1_fr = [
            f"On pose $h(x) = f(x) - g(x) = {sp.latex(h_expr)}$.",
            f"On a $h'(x) = {sp.latex(h_prime)}$.",
            f"Comme un carré est positif, $3x^2 \\ge 0$, donc $h'(x) > 0$. $h$ est strictement croissante sur $[{root} ; +\\infty[$.",
            f"On calcule $h({root}) = {root}^3 - ({m})\\times{root} - {p} = 0$.",
            f"La fonction $h$ est croissante et vaut 0 en $x={root}$, elle est donc positive ($h(x) \\ge 0$) sur tout l'intervalle.",
            f"Puisque $f(x) - g(x) \\ge 0$, on conclut que **$C_f$ est toujours au-dessus de $C_g$** sur $[{root} ; +\\infty[$."
        ]
        ans1_en = [
            f"We define $h(x) = f(x) - g(x) = {sp.latex(h_expr)}$.",
            f"We have $h'(x) = {sp.latex(h_prime)}$.",
            f"Since a square is positive, $3x^2 \\ge 0$, thus $h'(x) > 0$. $h$ is strictly increasing on $[{root} ; +\\infty)$.",
            f"We calculate $h({root}) = {root}^3 - ({m})\\times{root} - {p} = 0$.",
            f"The function $h$ is increasing and equals 0 at $x={root}$, so it is positive ($h(x) \\ge 0$) on the whole interval.",
            f"Since $f(x) - g(x) \\ge 0$, we conclude that **$C_f$ is always above $C_g$** on $[{root} ; +\\infty)$."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 11 : Problème d'optimisation
# ==========================================
class OptimizationProblem(BaseExercise):
    id = "DER3_011"
    title = {"fr": "Résoudre un problème d'optimisation", "en": "Solve an optimization problem"}
    tags = ["derivation", "optimisation", "benefice", "maximum"]

    def generate(self):
        a = float(self.rng.choice([0.1, 0.2, 0.4, 0.5]))
        b = self.rng.randint(10, 30)
        max_x = self.rng.choice([10, 15, 20, 25, 30])
        
        # Encadrement de c pour garantir un bénéfice maximal strictement positif et réaliste
        max_possible_c = int(a * (max_x ** 2)) - 5
        if max_possible_c < 5:
            max_possible_c = 5
        c = self.rng.randint(2, max_possible_c)
        
        d = int(b + 2 * a * max_x)
        domain_max = max_x * 2
        
        x = sp.Symbol('x')
        C_expr = a*x**2 + b*x + c
        R_expr = d*x
        B_expr = R_expr - C_expr
        B_prime = sp.diff(B_expr, x)
        
        max_B = B_expr.subs(x, max_x)

        self.statement_fr = [
            f"Pour une quantité $x$ en milliers d'unités ($x \\in [0 ; {domain_max}]$), le coût total de fabrication en milliers d'euros est : $C(x) = {sp.latex(C_expr)}$.",
            f"La recette est donnée par : $R(x) = {sp.latex(R_expr)}$."
        ]
        self.statement_en = [
            f"For a quantity $x$ in thousands of units ($x \\in [0 ; {domain_max}]$), the total manufacturing cost in thousands of euros is: $C(x) = {sp.latex(C_expr)}$.",
            f"The revenue is given by: $R(x) = {sp.latex(R_expr)}$."
        ]

        q1_fr = ["Déterminer le bénéfice maximal et le nombre d'unités correspondantes à produire."]
        q1_en = ["Determine the maximum profit and the corresponding number of units to produce."]
        insight1_fr = ["Le bénéfice est $B(x) = R(x) - C(x)$. Étudiez les variations de $B(x)$ en calculant sa dérivée."]
        insight1_en = ["The profit is $B(x) = R(x) - C(x)$. Study the variations of $B(x)$ by calculating its derivative."]
        
        two_a = round(2 * a, 1)
        
        ans1_fr = [
            f"• L'expression du bénéfice est : $B(x) = R(x) - C(x) = {d}x - ({sp.latex(C_expr)}) = {sp.latex(B_expr)}$.",
            f"• On calcule la dérivée : $B'(x) = {sp.latex(B_prime)}$.",
            f"• On résout $B'(x) = 0 \\iff -{two_a}x + {d-b} = 0 \\iff x = \\frac{{{d-b}}}{{{two_a}}} = {max_x}$.",
            f"• La dérivée est une fonction affine de coefficient directeur $-{two_a} < 0$. Elle est donc positive puis négative.",
            f"La fonction $B(x)$ est donc croissante puis décroissante : elle admet bien un maximum en $x={max_x}$.",
            f"• On calcule $B({max_x}) = {max_B}$.",
            f"Le bénéfice maximal est de **{int(max_B * 1000)} €** pour **{max_x * 1000}** composants produits."
        ]
        ans1_en = [
            f"• The expression for the profit is: $B(x) = R(x) - C(x) = {d}x - ({sp.latex(C_expr)}) = {sp.latex(B_expr)}$.",
            f"• We calculate the derivative: $B'(x) = {sp.latex(B_prime)}$.",
            f"• We solve $B'(x) = 0 \\iff -{two_a}x + {d-b} = 0 \\iff x = \\frac{{{d-b}}}{{{two_a}}} = {max_x}$.",
            f"• The derivative is an affine function with a slope of $-{two_a} < 0$. It is therefore positive then negative.",
            f"The function $B(x)$ is thus increasing then decreasing: it indeed has a maximum at $x={max_x}$.",
            f"• We calculate $B({max_x}) = {max_B}$.",
            f"The maximum profit is **{int(max_B * 1000)} €** for **{max_x * 1000}** components produced."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))
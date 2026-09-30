import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from exercises.base_exercise import BaseExercise
from exercises.question import Question

# Module-level registry key
CHAPTER = {"fr": "Fonction Exponentielle", "en": "Exponential Function"}

# ==========================================
# MÉTHODE 1 : Simplifier les écritures
# ==========================================
class SimplifyExponential(BaseExercise):
    id = "EXP_001"
    title = {"fr": "Simplifier les écritures", "en": "Simplify expressions"}
    tags = ["exponentielle", "simplification", "puissances"]

    def generate(self):
        # A = (e^a * e^b) / e^c
        a = self.rng.randint(2, 9)
        b = self.rng.randint(-8, -2)
        c = self.rng.randint(-6, -1)
        A_ans = a + b - c
        
        # B = (e^d)^e * e^f
        d = self.rng.randint(2, 6)
        e = self.rng.randint(-5, -2)
        f = self.rng.randint(-5, -1)
        B_ans = d * e + f
        
        # C = 1 / (e^g)^h + (e^i)^j / (e^k * e^m)
        # We want both terms to simplify to e^X. Let's make X = 6.
        X = self.rng.choice([4, 5, 6, 7])
        g = self.rng.choice([-2, -3])
        h = X // (-g) if X % (-g) == 0 else -X  # Just ensure it's an integer
        X = -g * h
        i, j = 2, -2 # i*j = -4
        k = -X - 4 + 2 # to make it work
        m = -2
        # Then (e^i)^j / (e^k * e^m) = e^{-4} / e^{k+m} = e^{-4 - (k+m)} = e^{-4 - (-X - 2)} = e^{X - 2}
        # Let's adjust to match PDF strictly where both terms are e^6 or similar:
        k = -4 - X + 2
        
        # D = (e^{px})^q / (e^{rx+s} * e^{tx+u})
        p = self.rng.choice([2, 3])
        q = self.rng.choice([2, 3])
        r = self.rng.choice([1, 2, 3])
        t = p * q - r - self.rng.choice([2, 3]) # so final x coeff is > 0
        s = self.rng.randint(1, 3)
        u = -s # so constants cancel out

        self.statement_fr = ["Simplifier l'écriture des nombres suivants :"]
        self.statement_en = ["Simplify the following expressions:"]

        # Question A
        q1_fr = [f"a) $A = \\frac{{e^{{{a}}} \\times e^{{{b}}}}}{{e^{{{c}}}}}$"]
        q1_en = [f"a) $A = \\frac{{e^{{{a}}} \\times e^{{{b}}}}}{{e^{{{c}}}}}$"]
        insight1_fr = ["Utilisez les propriétés : $e^x \\times e^y = e^{x+y}$ et $\\frac{e^x}{e^y} = e^{x-y}$."]
        insight1_en = ["Use the properties: $e^x \\times e^y = e^{x+y}$ and $\\frac{e^x}{e^y} = e^{x-y}$."]
        ans1_fr = [
            f"$A = \\frac{{e^{{{a}{b}}}}}{{e^{{{c}}}}} = \\frac{{e^{{{a+b}}}}}{{e^{{{c}}}}}$",
            f"$= e^{{{a+b} - ({c})}} = e^{{{A_ans}}}$"
        ]
        ans1_en = [
            f"$A = \\frac{{e^{{{a}{b}}}}}{{e^{{{c}}}}} = \\frac{{e^{{{a+b}}}}}{{e^{{{c}}}}}$",
            f"$= e^{{{a+b} - ({c})}} = e^{{{A_ans}}}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question B
        q2_fr = [f"b) $B = (e^{{{d}}})^{{{e}}} \\times e^{{{f}}}$"]
        q2_en = [f"b) $B = (e^{{{d}}})^{{{e}}} \\times e^{{{f}}}$"]
        insight2_fr = ["Utilisez la propriété : $(e^x)^n = e^{nx}$."]
        insight2_en = ["Use the property: $(e^x)^n = e^{nx}$."]
        ans2_fr = [
            f"$B = e^{{{d} \\times ({e})}} \\times e^{{{f}}} = e^{{{d*e}}} \\times e^{{{f}}}$",
            f"$= e^{{{d*e} {f}}} = e^{{{B_ans}}}$"
        ]
        ans2_en = [
            f"$B = e^{{{d} \\times ({e})}} \\times e^{{{f}}} = e^{{{d*e}}} \\times e^{{{f}}}$",
            f"$= e^{{{d*e} {f}}} = e^{{{B_ans}}}$"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))

        # Question D (as c)
        q4_fr = [f"c) $C = \\frac{{(e^{{{p}x}})^{{{q}}}}}{{e^{{{r}x+{s}}} \\times e^{{{t}x{u}}}}}$"]
        q4_en = [f"c) $C = \\frac{{(e^{{{p}x}})^{{{q}}}}}{{e^{{{r}x+{s}}} \\times e^{{{t}x{u}}}}}$"]
        insight4_fr = ["Simplifiez le numérateur et le dénominateur séparément avant de faire le quotient."]
        insight4_en = ["Simplify the numerator and denominator separately before dividing."]
        ans4_fr = [
            f"$C = \\frac{{e^{{{p*q}x}}}}{{e^{{({r}x+{s}) + ({t}x{u})}}}}$",
            f"$= \\frac{{e^{{{p*q}x}}}}{{e^{{{r+t}x}}}}$",
            f"$= e^{{{p*q}x - {r+t}x}} = e^{{{p*q - r - t}x}}$"
        ]
        ans4_en = [
            f"$C = \\frac{{e^{{{p*q}x}}}}{{e^{{({r}x+{s}) + ({t}x{u})}}}}$",
            f"$= \\frac{{e^{{{p*q}x}}}}{{e^{{{r+t}x}}}}$",
            f"$= e^{{{p*q}x - {r+t}x}} = e^{{{p*q - r - t}x}}$"
        ]
        self.questions.append(Question(q4_fr, q4_en, insight4_fr, insight4_en, ans4_fr, ans4_en))


# ==========================================
# MÉTHODE 2 : Équations et Inéquations
# ==========================================
class SolveExpEquations(BaseExercise):
    id = "EXP_002"
    title = {"fr": "Résoudre équations et inéquations", "en": "Solve equations and inequalities"}
    tags = ["exponentielle", "equation", "inequation"]

    def generate(self):
        # Equation: e^{x^2 + P} - e^{Sx} = 0 => x^2 - Sx + P = 0
        r1 = self.rng.randint(-4, -1)
        r2 = self.rng.randint(1, 4)
        S = r1 + r2
        P = r1 * r2
        
        # Inequation: e^{ax - b} >= 1 => ax - b >= 0
        a = self.rng.choice([2, 3, 4, 5])
        b = self.rng.choice([1, 2, 3])

        self.statement_fr = ["Dans chaque cas, résoudre dans $\\mathbb{R}$ :"]
        self.statement_en = ["In each case, solve in $\\mathbb{R}$:"]

        # Question a
        sign_P = f"+ {P}" if P >= 0 else f"- {abs(P)}"
        sign_S = f"{S}x" if S < 0 else f"{S}x"
        if S == 0: sign_S = "0"
        
        q1_fr = [f"a) L'équation $e^{{x^2 {sign_P}}} - e^{{{sign_S}}} = 0$"]
        q1_en = [f"a) The equation $e^{{x^2 {sign_P}}} - e^{{{sign_S}}} = 0$"]
        insight1_fr = ["Passez un terme de l'autre côté pour obtenir $e^A = e^B$, ce qui équivaut à $A = B$. Résolvez ensuite l'équation du second degré."]
        insight1_en = ["Move a term to the other side to get $e^A = e^B$, which is equivalent to $A = B$. Then solve the quadratic equation."]
        
        delta = (-S)**2 - 4*1*P
        
        ans1_fr = [
            f"$e^{{x^2 {sign_P}}} = e^{{{sign_S}}}$",
            f"$x^2 {sign_P} = {sign_S}$",
            f"$x^2 - {S}x {sign_P} = 0$",
            f"C'est une équation du second degré. $\\Delta = (-{S})^2 - 4 \\times 1 \\times ({P}) = {delta}$",
            f"Les solutions sont $x_1 = {r1}$ et $x_2 = {r2}$.",
            f"**$S = \\{{{r1} ; {r2}\\}}$**"
        ]
        ans1_en = [
            f"$e^{{x^2 {sign_P}}} = e^{{{sign_S}}}$",
            f"$x^2 {sign_P} = {sign_S}$",
            f"$x^2 - {S}x {sign_P} = 0$",
            f"This is a quadratic equation. $\\Delta = (-{S})^2 - 4 \\times 1 \\times ({P}) = {delta}$",
            f"The solutions are $x_1 = {r1}$ and $x_2 = {r2}$.",
            f"**$S = \\{{{r1} ; {r2}\\}}$**"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question b
        q2_fr = [f"b) L'inéquation $e^{{{a}x - {b}}} \\ge 1$"]
        q2_en = [f"b) The inequality $e^{{{a}x - {b}}} \\ge 1$"]
        insight2_fr = ["Rappelez-vous que $1 = e^0$. Donc $e^A \\ge e^0 \\iff A \\ge 0$."]
        insight2_en = ["Remember that $1 = e^0$. Thus $e^A \\ge e^0 \\iff A \\ge 0$."]
        
        ans2_fr = [
            f"$e^{{{a}x - {b}}} \\ge e^0$",
            f"${a}x - {b} \\ge 0$",
            f"${a}x \\ge {b}$",
            f"$x \\ge \\frac{{{b}}}{{{a}}}$",
            f"**$S = \\left[\\frac{{{b}}}{{{a}}} ; +\\infty\\right[$**"
        ]
        ans2_en = [
            f"$e^{{{a}x - {b}}} \\ge e^0$",
            f"${a}x - {b} \\ge 0$",
            f"${a}x \\ge {b}$",
            f"$x \\ge \\frac{{{b}}}{{{a}}}$",
            f"**$S = \\left[\\frac{{{b}}}{{{a}}} ; +\\infty\\right)$**"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 3 : Dériver une fonction exponentielle
# ==========================================
class DeriveExponential(BaseExercise):
    id = "EXP_003"
    title = {"fr": "Dériver une fonction exponentielle", "en": "Derive an exponential function"}
    tags = ["exponentielle", "derivation", "produit", "quotient"]

    def generate(self):
        a = self.rng.randint(2, 5)
        b = self.rng.randint(2, 5)
        c = self.rng.randint(1, 5)

        self.statement_fr = ["Dériver les fonctions suivantes :"]
        self.statement_en = ["Derive the following functions:"]

        # a) f(x) = ax - b e^x
        q1_fr = [f"a) $f(x) = {a}x - {b}e^x$"]
        q1_en = [f"a) $f(x) = {a}x - {b}e^x$"]
        insight1_fr = ["Dérivez chaque terme séparément. La dérivée de $e^x$ est $e^x$."]
        insight1_en = ["Derive each term separately. The derivative of $e^x$ is $e^x$."]
        ans1_fr = [f"**$f'(x) = {a} - {b}e^x$**"]
        ans1_en = [f"**$f'(x) = {a} - {b}e^x$**"]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # b) g(x) = (x - c)e^x
        q2_fr = [f"b) $g(x) = (x - {c})e^x$"]
        q2_en = [f"b) $g(x) = (x - {c})e^x$"]
        insight2_fr = ["Utilisez la formule du produit : $(uv)' = u'v + uv'$ avec $u(x) = x - c$ et $v(x) = e^x$."]
        insight2_en = ["Use the product formula: $(uv)' = u'v + uv'$ with $u(x) = x - c$ and $v(x) = e^x$."]
        ans2_fr = [
            f"$g(x) = u(x)v(x)$ avec $u(x) = x - {c} \\rightarrow u'(x) = 1$ et $v(x) = e^x \\rightarrow v'(x) = e^x$.",
            f"$g'(x) = 1 \\times e^x + (x - {c})e^x$",
            f"$= e^x (1 + x - {c})$",
            f"**$g'(x) = e^x (x - {c - 1})$**"
        ]
        ans2_en = [
            f"$g(x) = u(x)v(x)$ with $u(x) = x - {c} \\rightarrow u'(x) = 1$ and $v(x) = e^x \\rightarrow v'(x) = e^x$.",
            f"$g'(x) = 1 \\times e^x + (x - {c})e^x$",
            f"$= e^x (1 + x - {c})$",
            f"**$g'(x) = e^x (x - {c - 1})$**"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))

        # c) h(x) = e^x / (x + d)
        d = self.rng.randint(1, 4)
        q3_fr = [f"c) $h(x) = \\frac{{e^x}}{{x + {d}}}$"]
        q3_en = [f"c) $h(x) = \\frac{{e^x}}{{x + {d}}}$"]
        insight3_fr = ["Utilisez la formule du quotient : $\\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2}$."]
        insight3_en = ["Use the quotient formula: $\\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2}$."]
        ans3_fr = [
            f"$h(x) = \\frac{{u(x)}}{{v(x)}}$ avec $u(x) = e^x \\rightarrow u'(x) = e^x$ et $v(x) = x + {d} \\rightarrow v'(x) = 1$.",
            f"$h'(x) = \\frac{{e^x(x + {d}) - e^x \\times 1}}{{(x + {d})^2}}$",
            f"$= \\frac{{e^x(x + {d} - 1)}}{{(x + {d})^2}}$",
            f"**$h'(x) = \\frac{{e^x(x + {d - 1})}}{{(x + {d})^2}}$**"
        ]
        ans3_en = [
            f"$h(x) = \\frac{{u(x)}}{{v(x)}}$ with $u(x) = e^x \\rightarrow u'(x) = e^x$ and $v(x) = x + {d} \\rightarrow v'(x) = 1$.",
            f"$h'(x) = \\frac{{e^x(x + {d}) - e^x \\times 1}}{{(x + {d})^2}}$",
            f"$= \\frac{{e^x(x + {d} - 1)}}{{(x + {d})^2}}$",
            f"**$h'(x) = \\frac{{e^x(x + {d - 1})}}{{(x + {d})^2}}$**"
        ]
        self.questions.append(Question(q3_fr, q3_en, insight3_fr, insight3_en, ans3_fr, ans3_en))


# ==========================================
# MÉTHODE 4 : Étudier une fonction exponentielle
# ==========================================
class StudyExponentialFunction(BaseExercise):
    id = "EXP_004"
    title = {"fr": "Étude complète d'une fonction", "en": "Complete study of a function"}
    tags = ["exponentielle", "etude", "variations", "tangente", "graphique"]

    def generate(self):
        a = self.rng.choice([1, 2, 3])
        
        self.statement_fr = [f"Soit $f$ la fonction définie sur $\\mathbb{{R}}$ par $f(x) = (x + {a})e^x$."]
        self.statement_en = [f"Let $f$ be the function defined on $\\mathbb{{R}}$ by $f(x) = (x + {a})e^x$."]

        # Questions
        q1_fr = [
            "a) Calculer la dérivée de $f$.",
            "b) Dresser le tableau de variations de $f$.",
            "c) Déterminer une équation de la tangente à la courbe au point d'abscisse $0$.",
            "d) Tracer l'allure de la courbe représentative de $f$."
        ]
        q1_en = [
            "a) Calculate the derivative of $f$.",
            "b) Draw the variation table of $f$.",
            "c) Determine an equation of the tangent to the curve at the point with abscissa $0$.",
            "d) Sketch the representative curve of $f$."
        ]
        
        insight1_fr = ["Factorisez $f'(x)$ par $e^x$ pour étudier facilement son signe ($e^x$ est toujours positif)."]
        insight1_en = ["Factor $f'(x)$ by $e^x$ to easily study its sign ($e^x$ is always positive)."]
        
        root = -a - 1
        
        fig, ax = plt.subplots(figsize=(6, 4))
        x_vals = np.linspace(-5, 2, 400)
        y_vals = (x_vals + a) * np.exp(x_vals)
        ax.plot(x_vals, y_vals, color="blue", linewidth=2)
        ax.plot([root], [(-a-1+a)*np.exp(root)], marker='x', color='red', markersize=10) # Minimum
        
        # Tangent at x=0
        tangent_x = np.linspace(-2, 1, 100)
        tangent_y = (a + 1) * tangent_x + a
        ax.plot(tangent_x, tangent_y, color='red', linestyle='--', alpha=0.7)
        
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_ylim(-3, max(y_vals))

        ans1_fr = [
            f"a) $f(x) = u(x)v(x)$ avec $u(x) = x + {a}$ et $v(x) = e^x$.",
            f"$f'(x) = 1 \\times e^x + (x + {a})e^x = e^x(1 + x + {a}) = e^x(x + {a+1})$.",
            f"b) Comme $e^x > 0$, $f'(x)$ est du signe de $x + {a+1}$. La dérivée s'annule en $x = {-a-1}$.",
            f"| $x$ | $-\\infty$ | | ${-a-1}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $-$ | $0$ | $+$ | |\n"
            f"| $f(x)$ | | $\\searrow$ | $-e^{{-{a+1}}}$ | $\\nearrow$ | |",
            f"c) $f(0) = (0 + {a})e^0 = {a}$. $f'(0) = (0 + {a+1})e^0 = {a+1}$.",
            f"Tangente : $y = f'(0)(x - 0) + f(0) \\implies y = {a+1}x + {a}$.",
            f"d) L'allure de la courbe :",
            fig
        ]
        ans1_en = [
            f"a) $f(x) = u(x)v(x)$ with $u(x) = x + {a}$ and $v(x) = e^x$.",
            f"$f'(x) = 1 \\times e^x + (x + {a})e^x = e^x(1 + x + {a}) = e^x(x + {a+1})$.",
            f"b) Since $e^x > 0$, $f'(x)$ has the sign of $x + {a+1}$. The derivative cancels at $x = {-a-1}$.",
            f"| $x$ | $-\\infty$ | | ${-a-1}$ | | $+\\infty$ |\n"
            f"|---|---|---|---|---|---|\n"
            f"| $f'(x)$ | | $-$ | $0$ | $+$ | |\n"
            f"| $f(x)$ | | $\\searrow$ | $-e^{{-{a+1}}}$ | $\\nearrow$ | |",
            f"c) $f(0) = (0 + {a})e^0 = {a}$. $f'(0) = (0 + {a+1})e^0 = {a+1}$.",
            f"Tangent: $y = f'(0)(x - 0) + f(0) \\implies y = {a+1}x + {a}$.",
            f"d) Sketch of the curve:",
            fig
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 5 : Dériver une fonction e^{kt}
# ==========================================
class DeriveExpK(BaseExercise):
    id = "EXP_005"
    title = {"fr": "Dériver une fonction en $e^{kt}$", "en": "Derive a function $e^{kt}$"}
    tags = ["exponentielle", "derivation", "composee"]

    def generate(self):
        a = self.rng.choice([3, 4, 5])
        b = self.rng.choice([-4, -3, -2, 2, 3])
        c = self.rng.choice([2, 3, 4])

        self.statement_fr = ["Dériver les fonctions suivantes par rapport à $t$ :"]
        self.statement_en = ["Derive the following functions with respect to $t$:"]

        # a) f(t) = a e^{bt}
        q1_fr = [f"a) $f(t) = {a}e^{{{b}t}}$"]
        q1_en = [f"a) $f(t) = {a}e^{{{b}t}}$"]
        insight1_fr = ["La dérivée de $e^{kt}$ est $k e^{kt}$."]
        insight1_en = ["The derivative of $e^{kt}$ is $k e^{kt}$."]
        ans1_fr = [
            f"$f'(t) = {a} \\times ({b})e^{{{b}t}} = {a*b}e^{{{b}t}}$"
        ]
        ans1_en = [
            f"$f'(t) = {a} \\times ({b})e^{{{b}t}} = {a*b}e^{{{b}t}}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # b) g(t) = t e^{ct}
        q2_fr = [f"b) $g(t) = te^{{{c}t}}$"]
        q2_en = [f"b) $g(t) = te^{{{c}t}}$"]
        insight2_fr = ["Utilisez la formule du produit $(uv)' = u'v + uv'$."]
        insight2_en = ["Use the product formula $(uv)' = u'v + uv'$."]
        ans2_fr = [
            f"$u(t) = t \\rightarrow u'(t) = 1$ et $v(t) = e^{{{c}t}} \\rightarrow v'(t) = {c}e^{{{c}t}}$.",
            f"$g'(t) = 1 \\times e^{{{c}t}} + t \\times {c}e^{{{c}t}} = e^{{{c}t}}(1 + {c}t)$"
        ]
        ans2_en = [
            f"$u(t) = t \\rightarrow u'(t) = 1$ and $v(t) = e^{{{c}t}} \\rightarrow v'(t) = {c}e^{{{c}t}}$.",
            f"$g'(t) = 1 \\times e^{{{c}t}} + t \\times {c}e^{{{c}t}} = e^{{{c}t}}(1 + {c}t)$"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 6 : Modélisation concrète (Bactéries)
# ==========================================
class StudyExpKConcrete(BaseExercise):
    id = "EXP_006"
    title = {"fr": "Modélisation : Évolution de bactéries", "en": "Modeling: Bacterial evolution"}
    tags = ["exponentielle", "modelisation", "evolution"]

    def generate(self):
        k = round(self.rng.choice([0.12, 0.15, 0.18, 0.20]), 2)
        n0 = self.rng.choice([10000, 20000, 50000])
        h1 = self.rng.choice([2, 3, 4])
        h2 = self.rng.choice([5.5, 6.5])

        self.statement_fr = [
            f"Le nombre de bactéries dans un organisme en fonction du temps $t$ (en heures) est modélisé par une fonction $f$ définie sur $[0 ; 10]$.",
            f"On a : $f'(t) = {k} f(t)$ et $f(0) = {n0}$."
        ]
        self.statement_en = [
            f"The number of bacteria in an organism as a function of time $t$ (in hours) is modeled by a function $f$ defined on $[0 ; 10]$.",
            f"We have: $f'(t) = {k} f(t)$ and $f(0) = {n0}$."
        ]

        q1_fr = [
            f"1) Montrer que $f(t) = A e^{{{k}t}}$ convient.",
            "2) Déterminer la valeur de $A$.",
            "3) Donner les variations de $f$ sur $[0 ; 10]$.",
            f"4) Estimer le nombre de bactéries après {h1}h puis {h2}h. Au bout de combien de temps le nombre de bactéries a-t-il doublé ?"
        ]
        q1_en = [
            f"1) Show that $f(t) = A e^{{{k}t}}$ is suitable.",
            "2) Determine the value of $A$.",
            "3) Give the variations of $f$ on $[0 ; 10]$.",
            f"4) Estimate the number of bacteria after {h1}h then {h2}h. How long does it take for the number of bacteria to double?"
        ]
        insight1_fr = ["Dérivez $A e^{kt}$ pour vérifier l'équation. Utilisez les conditions initiales pour trouver A."]
        insight1_en = ["Derive $A e^{kt}$ to verify the equation. Use initial conditions to find A."]
        
        val_h1 = int(round(n0 * np.exp(k * h1), -3))
        val_h2 = int(round(n0 * np.exp(k * h2), -3))
        t_double = np.log(2) / k
        t_double_round = round(t_double, 1)

        ans1_fr = [
            f"1) $f'(t) = A \\times {k} e^{{{k}t}} = {k} \\times (A e^{{{k}t}}) = {k} f(t)$. La fonction convient.",
            f"2) $f(0) = A e^0 = A$. Comme $f(0) = {n0}$, on a $A = {n0}$. Donc $f(t) = {n0} e^{{{k}t}}$.",
            f"3) Comme $k = {k} > 0$, la fonction $f$ est strictement croissante.",
            f"4) $f({h1}) = {n0} e^{{{k} \\times {h1}}} \\approx {val_h1}$ bactéries.",
            f"   $f({h2}) = {n0} e^{{{k} \\times {h2}}} \\approx {val_h2}$ bactéries.",
            f"   Le nombre double quand $e^{{{k}t}} = 2$. À la calculatrice, on trouve $t \\approx {t_double_round}$ heures."
        ]
        ans1_en = [
            f"1) $f'(t) = A \\times {k} e^{{{k}t}} = {k} \\times (A e^{{{k}t}}) = {k} f(t)$. The function is suitable.",
            f"2) $f(0) = A e^0 = A$. Since $f(0) = {n0}$, we have $A = {n0}$. Thus $f(t) = {n0} e^{{{k}t}}$.",
            f"3) Since $k = {k} > 0$, the function $f$ is strictly increasing.",
            f"4) $f({h1}) = {n0} e^{{{k} \\times {h1}}} \\approx {val_h1}$ bacteria.",
            f"   $f({h2}) = {n0} e^{{{k} \\times {h2}}} \\approx {val_h2}$ bacteria.",
            f"   The number doubles when $e^{{{k}t}} = 2$. Using a calculator, we find $t \\approx {t_double_round}$ hours."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 7 : Exponentielle et Suite géométrique
# ==========================================
class ExpGeometricSequence(BaseExercise):
    id = "EXP_007"
    title = {"fr": "Exponentielle et Suite géométrique", "en": "Exponential and Geometric Sequence"}
    tags = ["exponentielle", "suites", "geometrique"]

    def generate(self):
        a = self.rng.randint(2, 5)
        b = self.rng.randint(2, 5)
        c = self.rng.choice([2, 3])

        self.statement_fr = ["Dans chaque cas, déterminer la raison et le premier terme de la suite géométrique dont le terme général est donné :"]
        self.statement_en = ["In each case, determine the common ratio and the first term of the geometric sequence whose general term is given:"]

        # a) u_n = e^{an}
        q1_fr = [f"a) $u_n = e^{{{a}n}}$"]
        q1_en = [f"a) $u_n = e^{{{a}n}}$"]
        insight1_fr = ["Transformez l'expression pour obtenir la forme $u_0 \\times q^n$. Rappel : $e^{xy} = (e^x)^y$."]
        insight1_en = ["Transform the expression to get the form $u_0 \\times q^n$. Reminder: $e^{xy} = (e^x)^y$."]
        ans1_fr = [
            f"$u_n = e^{{{a}n}} = (e^{{{a}}})^n = 1 \\times (e^{{{a}}})^n$.",
            f"$(u_n)$ est une suite géométrique de raison $q = e^{{{a}}}$ et de premier terme $u_0 = 1$."
        ]
        ans1_en = [
            f"$u_n = e^{{{a}n}} = (e^{{{a}}})^n = 1 \\times (e^{{{a}}})^n$.",
            f"$(u_n)$ is a geometric sequence with common ratio $q = e^{{{a}}}$ and first term $u_0 = 1$."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # b) u_n = b e^{-cn}
        q2_fr = [f"b) $v_n = {b}e^{{-{c}n}}$"]
        q2_en = [f"b) $v_n = {b}e^{{-{c}n}}$"]
        insight2_fr = ["Isolez la puissance $n$ pour faire apparaître la raison $q$."]
        insight2_en = ["Isolate the power $n$ to reveal the common ratio $q$."]
        ans2_fr = [
            f"$v_n = {b}(e^{{-{c}}})^n$.",
            f"$(v_n)$ est une suite géométrique de raison $q = e^{{-{c}}}$ et de premier terme $v_0 = {b}$."
        ]
        ans2_en = [
            f"$v_n = {b}(e^{{-{c}}})^n$.",
            f"$(v_n)$ is a geometric sequence with common ratio $q = e^{{-{c}}}$ and first term $v_0 = {b}$."
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))

        # c) Suite géométrique -> expression (Inverse logic as seen in lesson part 2)
        q3_fr = [
            f"c) Déterminer l'expression en fonction de $n$ de la suite géométrique $(w_n)$ de raison $\\frac{{1}}{{e}}$ et de premier terme $3$.",
            "Donner les variations de cette suite."
        ]
        q3_en = [
            f"c) Determine the expression in terms of $n$ for the geometric sequence $(w_n)$ with common ratio $\\frac{{1}}{{e}}$ and first term $3$.",
            "Give the variations of this sequence."
        ]
        insight3_fr = ["Utilisez la formule $u_n = u_0 \\times q^n$. Rappel : $\\frac{1}{e} = e^{-1}$."]
        insight3_en = ["Use the formula $u_n = u_0 \\times q^n$. Reminder: $\\frac{1}{e} = e^{-1}$."]
        ans3_fr = [
            f"$w_n = 3 \\times \\left(\\frac{{1}}{{e}}\\right)^n = 3 \\times (e^{{-1}})^n = 3e^{{-n}}$.",
            f"La raison de la suite est telle que $0 < \\frac{{1}}{{e}} < 1$ et le premier terme est positif.",
            "La suite $(w_n)$ est donc strictement décroissante."
        ]
        ans3_en = [
            f"$w_n = 3 \\times \\left(\\frac{{1}}{{e}}\\right)^n = 3 \\times (e^{{-1}})^n = 3e^{{-n}}$.",
            f"The common ratio of the sequence satisfies $0 < \\frac{{1}}{{e}} < 1$ and the first term is positive.",
            "The sequence $(w_n)$ is therefore strictly decreasing."
        ]
        self.questions.append(Question(q3_fr, q3_en, insight3_fr, insight3_en, ans3_fr, ans3_en))
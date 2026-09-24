import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from exercises.base_exercise import BaseExercise
from exercises.question import Question

# Module-level registry key
CHAPTER = {"fr": "Polynômes du Second Degré (Partie 2)", "en": "Quadratic Polynomials (Part 2)"}

# ==========================================
# MÉTHODE 1 : Résoudre une équation du second degré
# ==========================================
class SolveQuadraticEquation(BaseExercise):
    id = "SD2_001"
    title = {"fr": "Résoudre une équation du second degré", "en": "Solve a quadratic equation"}
    tags = ["second-degre", "equation", "discriminant"]

    def generate(self):
        x = sp.Symbol('x')
        
        # a) Delta > 0 (Two roots)
        r1, r2 = self.rng.sample([-3, -2, -1, 1, 2, 3], k=2)
        a1 = self.rng.choice([1, 2])
        eq1_expr = sp.expand(a1 * (x - r1) * (x - r2))
        
        # b) Delta = 0 (One root)
        r0 = self.rng.randint(-4, 4)
        a2 = self.rng.choice([1, 2, 3])
        eq2_expr = sp.expand(a2 * (x - r0)**2)
        
        # c) Delta < 0 (No real root)
        a3 = self.rng.choice([1, 2])
        alpha = self.rng.randint(-3, 3)
        beta = self.rng.randint(1, 5) # Positive so a3 * beta > 0 means Delta < 0
        eq3_expr = sp.expand(a3 * (x - alpha)**2 + beta)

        self.statement_fr = ["Résoudre les équations suivantes dans $\\mathbb{R}$ :"]
        self.statement_en = ["Solve the following equations in $\\mathbb{R}$:"]

        # Question a
        a, b, c = eq1_expr.coeff(x, 2), eq1_expr.coeff(x, 1), eq1_expr.subs(x, 0)
        delta1 = b**2 - 4*a*c
        q1_fr = [f"a) ${sp.latex(eq1_expr)} = 0$"]
        q1_en = [f"a) ${sp.latex(eq1_expr)} = 0$"]
        insight1_fr = ["Calculez le discriminant $\\Delta = b^2 - 4ac$. S'il est positif, calculez les deux racines."]
        insight1_en = ["Calculate the discriminant $\\Delta = b^2 - 4ac$. If positive, calculate the two roots."]
        ans1_fr = [
            f"$\\Delta = ({b})^2 - 4 \\times ({a}) \\times ({c}) = {delta1}$",
            f"Comme $\\Delta > 0$, l'équation possède deux solutions distinctes :",
            f"$x_1 = \\frac{{-{b} - \\sqrt{{{delta1}}}}}{{2 \\times {a}}} = {sp.latex(r1)}$ et $x_2 = \\frac{{-{b} + \\sqrt{{{delta1}}}}}{{2 \\times {a}}} = {sp.latex(r2)}$",
            f"$S = \\{{{sp.latex(min(r1, r2))} ; {sp.latex(max(r1, r2))}\\}}$"
        ]
        ans1_en = [
            f"$\\Delta = ({b})^2 - 4 \\times ({a}) \\times ({c}) = {delta1}$",
            f"Since $\\Delta > 0$, the equation has two distinct solutions:",
            f"$x_1 = {sp.latex(r1)}$ and $x_2 = {sp.latex(r2)}$",
            f"$S = \\{{{sp.latex(min(r1, r2))} ; {sp.latex(max(r1, r2))}\\}}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question b
        a, b, c = eq2_expr.coeff(x, 2), eq2_expr.coeff(x, 1), eq2_expr.subs(x, 0)
        delta2 = b**2 - 4*a*c
        q2_fr = [f"b) ${sp.latex(eq2_expr)} = 0$"]
        q2_en = [f"b) ${sp.latex(eq2_expr)} = 0$"]
        insight2_fr = ["Calculez $\\Delta$. S'il vaut 0, l'équation a une unique solution $x_0 = \\frac{-b}{2a}$."]
        insight2_en = ["Calculate $\\Delta$. If it is 0, the equation has a unique solution $x_0 = \\frac{-b}{2a}$."]
        ans2_fr = [
            f"$\\Delta = ({b})^2 - 4 \\times ({a}) \\times ({c}) = {delta2}$",
            f"Comme $\\Delta = 0$, l'équation possède une unique solution :",
            f"$x_0 = -\\frac{{{b}}}{{2 \\times {a}}} = {sp.latex(r0)}$",
            f"$S = \\{{{sp.latex(r0)}\\}}$"
        ]
        ans2_en = [
            f"$\\Delta = ({b})^2 - 4 \\times ({a}) \\times ({c}) = {delta2}$",
            f"Since $\\Delta = 0$, the equation has a unique solution:",
            f"$x_0 = -\\frac{{{b}}}{{2 \\times {a}}} = {sp.latex(r0)}$",
            f"$S = \\{{{sp.latex(r0)}\\}}$"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))

        # Question c
        a, b, c = eq3_expr.coeff(x, 2), eq3_expr.coeff(x, 1), eq3_expr.subs(x, 0)
        delta3 = b**2 - 4*a*c
        q3_fr = [f"c) ${sp.latex(eq3_expr)} = 0$"]
        q3_en = [f"c) ${sp.latex(eq3_expr)} = 0$"]
        insight3_fr = ["Calculez $\\Delta$. S'il est strictement négatif, concluez."]
        insight3_en = ["Calculate $\\Delta$. If strictly negative, conclude."]
        ans3_fr = [
            f"$\\Delta = ({b})^2 - 4 \\times ({a}) \\times ({c}) = {delta3}$",
            f"Comme $\\Delta < 0$, l'équation ne possède pas de solution réelle.",
            f"$S = \\emptyset$"
        ]
        ans3_en = [
            f"$\\Delta = ({b})^2 - 4 \\times ({a}) \\times ({c}) = {delta3}$",
            f"Since $\\Delta < 0$, the equation has no real solution.",
            f"$S = \\emptyset$"
        ]
        self.questions.append(Question(q3_fr, q3_en, insight3_fr, insight3_en, ans3_fr, ans3_en))


# ==========================================
# MÉTHODE 2 : Somme et produit des racines
# ==========================================
class SumAndProductRoots(BaseExercise):
    id = "SD2_002"
    title = {"fr": "Somme et produit des racines", "en": "Sum and product of roots"}
    tags = ["second-degre", "racines", "somme", "produit"]

    def generate(self):
        x = sp.Symbol('x')
        x1 = self.rng.choice([-3, -2, -1, 1, 2, 3])
        num = self.rng.choice([-5, -3, -1, 1, 3, 5])
        den = self.rng.choice([2, 4])
        x2 = sp.Rational(num, den)
        
        a = den
        eq_expr = sp.expand(a * (x - x1) * (x - x2))
        a, b, c = eq_expr.coeff(x, 2), eq_expr.coeff(x, 1), eq_expr.subs(x, 0)

        self.statement_fr = [f"Soit $f$ la fonction polynôme définie par $f(x) = {sp.latex(eq_expr)}$."]
        self.statement_en = [f"Let $f$ be the polynomial function defined by $f(x) = {sp.latex(eq_expr)}$."]

        q1_fr = [f"1) Montrer que $x_1 = {x1}$ est une racine de $f$."]
        q1_en = [f"1) Show that $x_1 = {x1}$ is a root of $f$."]
        insight1_fr = [f"Calculez l'image de ${x1}$ par la fonction $f$."]
        insight1_en = [f"Calculate the image of ${x1}$ by the function $f$."]
        ans1_fr = [
            f"$f({x1}) = {a}({x1})^2 + ({b})({x1}) + ({c}) = 0$.",
            f"Donc $x_1 = {x1}$ est bien une racine."
        ]
        ans1_en = [
            f"$f({x1}) = {a}({x1})^2 + ({b})({x1}) + ({c}) = 0$.",
            f"Thus $x_1 = {x1}$ is indeed a root."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        q2_fr = ["2) Déterminer la deuxième racine sans calculer le discriminant."]
        q2_en = ["2) Determine the second root without calculating the discriminant."]
        insight2_fr = ["Utilisez la formule du produit des racines $P = \\frac{c}{a}$ ou de la somme $S = -\\frac{b}{a}$."]
        insight2_en = ["Use the formula for the product of roots $P = \\frac{c}{a}$ or sum $S = -\\frac{b}{a}$."]
        ans2_fr = [
            f"En utilisant le produit des racines, $P = x_1 \\times x_2 = {x1} \\times x_2$.",
            f"Or $P = \\frac{{c}}{{a}} = \\frac{{{c}}}{{{a}}} = {sp.latex(sp.Rational(c, a))}$.",
            f"Donc ${x1} \\times x_2 = {sp.latex(sp.Rational(c, a))}$, d'où $x_2 = {sp.latex(x2)}$."
        ]
        ans2_en = [
            f"Using the product of roots, $P = x_1 \\times x_2 = {x1} \\times x_2$.",
            f"But $P = \\frac{{c}}{{a}} = \\frac{{{c}}}{{{a}}} = {sp.latex(sp.Rational(c, a))}$.",
            f"Thus ${x1} \\times x_2 = {sp.latex(sp.Rational(c, a))}$, which gives $x_2 = {sp.latex(x2)}$."
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 3 : Trouver la fonction s'annulant en 2 réels
# ==========================================
class FindFactorizedForm(BaseExercise):
    id = "SD2_003"
    title = {"fr": "Déterminer une fonction avec ses racines", "en": "Determine a function from its roots"}
    tags = ["second-degre", "factorisation", "racines"]

    def generate(self):
        r1, r2 = self.rng.sample([-4, -3, -2, -1, 1, 2, 3, 4], k=2)
        x3 = self.rng.choice([x for x in range(-5, 6) if x not in (r1, r2)])
        a = self.rng.choice([-2, -1, 1, 2, 3])
        y3 = a * (x3 - r1) * (x3 - r2)

        self.statement_fr = [f"On considère la fonction polynôme $f$ du second degré s'annulant en ${r1}$ et ${r2}$ et telle que $f({x3}) = {y3}$."]
        self.statement_en = [f"Consider the quadratic function $f$ vanishing at ${r1}$ and ${r2}$ and such that $f({x3}) = {y3}$."]

        q1_fr = ["Déterminer une expression factorisée de la fonction $f$."]
        q1_en = ["Determine a factorized expression of the function $f$."]
        insight1_fr = ["Les racines permettent d'écrire $f(x) = a(x-x_1)(x-x_2)$. Utilisez $f(x_3)$ pour trouver $a$."]
        insight1_en = ["Roots allow writing $f(x) = a(x-x_1)(x-x_2)$. Use $f(x_3)$ to find $a$."]
        
        # CORRECTION ICI : Remplacement du "-" par un "+" si la racine est négative
        sign_r1 = f"+ {-r1}" if r1 < 0 else f"- {r1}"
        sign_r2 = f"+ {-r2}" if r2 < 0 else f"- {r2}"
        
        ans1_fr = [
            f"Comme la fonction s'annule en ${r1}$ et ${r2}$, on a : $f(x) = a(x {sign_r1})(x {sign_r2})$.",
            f"De plus, $f({x3}) = {y3}$. Donc $a({x3} {sign_r1})({x3} {sign_r2}) = {y3}$.",
            f"$a \\times ({x3 - r1}) \\times ({x3 - r2}) = {y3}$, soit $a \\times { (x3 - r1)*(x3 - r2) } = {y3}$. Donc $a = {a}$.",
            f"L'expression est : $f(x) = {a}(x {sign_r1})(x {sign_r2})$."
        ]
        ans1_en = [
            f"Since the function vanishes at ${r1}$ and ${r2}$, we have: $f(x) = a(x {sign_r1})(x {sign_r2})$.",
            f"Moreover, $f({x3}) = {y3}$. Thus $a({x3} {sign_r1})({x3} {sign_r2}) = {y3}$.",
            f"$a \\times ({x3 - r1}) \\times ({x3 - r2}) = {y3}$, which gives $a \\times { (x3 - r1)*(x3 - r2) } = {y3}$. So $a = {a}$.",
            f"The expression is: $f(x) = {a}(x {sign_r1})(x {sign_r2})$."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 4 : Factoriser un trinôme
# ==========================================
class FactorizeTrinomial(BaseExercise):
    id = "SD2_004"
    title = {"fr": "Factoriser un trinôme", "en": "Factorize a trinomial"}
    tags = ["second-degre", "factorisation", "discriminant"]

    def generate(self):
        x = sp.Symbol('x')
        
        # a) Delta > 0
        r1, r2 = self.rng.sample([-3, -2, -1, 1, 2, 3], k=2)
        a1 = self.rng.choice([1, 2])
        eq1_expr = sp.expand(a1 * (x - r1) * (x - r2))
        
        # b) Delta = 0
        r0 = self.rng.randint(-4, 4)
        a2 = self.rng.choice([2, 3, 4])
        eq2_expr = sp.expand(a2 * (x - r0)**2)

        self.statement_fr = ["Factoriser les trinômes suivants :"]
        self.statement_en = ["Factorize the following trinomials:"]

        # Question a
        a_coeff, b_coeff, c_coeff = eq1_expr.coeff(x, 2), eq1_expr.coeff(x, 1), eq1_expr.subs(x, 0)
        delta1 = b_coeff**2 - 4*a_coeff*c_coeff
        q1_fr = [f"a) ${sp.latex(eq1_expr)}$"]
        q1_en = [f"a) ${sp.latex(eq1_expr)}$"]
        insight1_fr = ["Calculez $\\Delta$. S'il est positif, le trinôme se factorise en $a(x-x_1)(x-x_2)$."]
        insight1_en = ["Calculate $\\Delta$. If positive, the trinomial factorizes to $a(x-x_1)(x-x_2)$."]
        
        sign_r1 = f"+ {-r1}" if r1 < 0 else f"- {r1}"
        sign_r2 = f"+ {-r2}" if r2 < 0 else f"- {r2}"
        str_a1 = "" if a1 == 1 else f"{a1}"

        ans1_fr = [
            f"$\\Delta = {delta1} > 0$. Les racines sont $x_1 = {r1}$ et $x_2 = {r2}$.",
            f"On obtient : **${str_a1}(x {sign_r1})(x {sign_r2})$**"
        ]
        ans1_en = [
            f"$\\Delta = {delta1} > 0$. The roots are $x_1 = {r1}$ and $x_2 = {r2}$.",
            f"We obtain: **${str_a1}(x {sign_r1})(x {sign_r2})$**"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question b
        a_coeff2, b_coeff2, c_coeff2 = eq2_expr.coeff(x, 2), eq2_expr.coeff(x, 1), eq2_expr.subs(x, 0)
        delta2 = b_coeff2**2 - 4*a_coeff2*c_coeff2
        q2_fr = [f"b) ${sp.latex(eq2_expr)}$"]
        q2_en = [f"b) ${sp.latex(eq2_expr)}$"]
        insight2_fr = ["Calculez $\\Delta$. S'il vaut 0, le trinôme se factorise en $a(x-x_0)^2$."]
        insight2_en = ["Calculate $\\Delta$. If it is 0, the trinomial factorizes to $a(x-x_0)^2$."]
        
        sign_r0 = f"+ {-r0}" if r0 < 0 else (f"- {r0}" if r0 > 0 else "")
        factored_form_b = f"{a2}x^2" if r0 == 0 else f"{a2}(x {sign_r0})^2"

        ans2_fr = [
            f"$\\Delta = {delta2}$. La racine unique est $x_0 = {r0}$.",
            f"On obtient : **${factored_form_b}$**"
        ]
        ans2_en = [
            f"$\\Delta = {delta2}$. The unique root is $x_0 = {r0}$.",
            f"We obtain: **${factored_form_b}$**"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 5 : Signe d'un trinôme
# ==========================================
class SignOfTrinomial(BaseExercise):
    id = "SD2_005"
    title = {"fr": "Déterminer le signe d'un trinôme", "en": "Determine the sign of a trinomial"}
    tags = ["second-degre", "signe", "discriminant"]

    def generate(self):
        x = sp.Symbol('x')
        # Delta < 0, a > 0 (always positive)
        a = self.rng.choice([1, 2, 3])
        alpha = self.rng.randint(-3, 3)
        beta = self.rng.randint(2, 6)
        eq_expr = sp.expand(a * (x - alpha)**2 + beta)

        self.statement_fr = []
        self.statement_en = []

        q1_fr = [f"Démontrer que la fonction $f$ définie sur $\\mathbb{{R}}$ par $f(x) = {sp.latex(eq_expr)}$ est strictement positive."]
        q1_en = [f"Prove that the function $f$ defined on $\\mathbb{{R}}$ by $f(x) = {sp.latex(eq_expr)}$ is strictly positive."]
        insight1_fr = ["Calculez le discriminant. Que se passe-t-il graphiquement lorsque $\\Delta < 0$ ? Regardez le signe de $a$."]
        insight1_en = ["Calculate the discriminant. What happens graphically when $\\Delta < 0$? Look at the sign of $a$."]
        
        a_coeff, b_coeff, c_coeff = eq_expr.coeff(x, 2), eq_expr.coeff(x, 1), eq_expr.subs(x, 0)
        delta = b_coeff**2 - 4*a_coeff*c_coeff
        
        ans1_fr = [
            f"Le discriminant est $\\Delta = {delta}$. Comme $\\Delta < 0$, $f$ ne possède pas de racine.",
            f"La parabole représentant $f$ est entièrement d'un côté de l'axe des abscisses.",
            f"Comme $a = {a} > 0$, les branches sont tournées vers le haut.",
            "On en déduit que $f(x)$ est strictement positive pour tout réel $x$."
        ]
        ans1_en = [
            f"The discriminant is $\\Delta = {delta}$. Since $\\Delta < 0$, $f$ has no roots.",
            f"The parabola representing $f$ is entirely on one side of the x-axis.",
            f"Since $a = {a} > 0$, the branches open upwards.",
            "We conclude that $f(x)$ is strictly positive for all real $x$."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 6 : Inéquations du second degré
# ==========================================
class SolveQuadraticInequality(BaseExercise):
    id = "SD2_006"
    title = {"fr": "Résoudre des inéquations", "en": "Solve quadratic inequalities"}
    tags = ["second-degre", "inequation", "signe"]

    def generate(self):
        x = sp.Symbol('x')
        
        # a) f(x) < 0 (a > 0, roots r1, r2) -> inside roots
        r1, r2 = sorted(self.rng.sample([-4, -3, -2, -1, 1, 2, 3, 4], k=2))
        a1 = 1
        eq1_expr = sp.expand(a1 * (x - r1) * (x - r2))
        
        # b) f(x) < mx + p
        r3, r4 = sorted(self.rng.sample([-3, -2, -1, 1, 2, 3, 4], k=2))
        a2 = 1
        f_minus_g = sp.expand(a2 * (x - r3) * (x - r4))
        # Let's invent g(x) = 2x + 1, then f(x) = f_minus_g + g
        m = self.rng.choice([-2, -1, 1, 2])
        p = self.rng.randint(-5, 5)
        g_expr = m*x + p
        f_expr = sp.expand(f_minus_g + g_expr)

        self.statement_fr = ["Résoudre les inéquations suivantes :"]
        self.statement_en = ["Solve the following inequalities:"]

        # Question a
        q1_fr = [f"a) ${sp.latex(eq1_expr)} < 0$"]
        q1_en = [f"a) ${sp.latex(eq1_expr)} < 0$"]
        insight1_fr = ["Cherchez les racines, puis dressez le tableau de signes (signe de $-a$ à l'intérieur des racines)."]
        insight1_en = ["Find the roots, then draw the sign table (sign of $-a$ inside the roots)."]
        ans1_fr = [
            f"Les racines sont $x_1 = {r1}$ et $x_2 = {r2}$.",
            f"Comme $a = 1 > 0$, le trinôme est négatif entre les racines.",
            f"L'ensemble des solutions est $S = ]{r1} ; {r2}[$."
        ]
        ans1_en = [
            f"The roots are $x_1 = {r1}$ and $x_2 = {r2}$.",
            f"Since $a = 1 > 0$, the trinomial is negative between the roots.",
            f"The solution set is $S = ({r1}, {r2})$."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question b
        q2_fr = [f"b) ${sp.latex(f_expr)} < {sp.latex(g_expr)}$"]
        q2_en = [f"b) ${sp.latex(f_expr)} < {sp.latex(g_expr)}$"]
        insight2_fr = ["Rassemblez tous les termes à gauche pour vous ramener à l'étude du signe d'un seul trinôme."]
        insight2_en = ["Gather all terms on the left to reduce it to studying the sign of a single trinomial."]
        ans2_fr = [
            f"On se ramène à l'étude du signe de $f(x) - g(x) < 0$ :",
            f"${sp.latex(f_minus_g)} < 0$",
            f"Les racines de ce trinôme sont $x_1 = {r3}$ et $x_2 = {r4}$.",
            f"L'ensemble des solutions est $S = ]{r3} ; {r4}[$."
        ]
        ans2_en = [
            f"We reduce this to studying the sign of $f(x) - g(x) < 0$:",
            f"${sp.latex(f_minus_g)} < 0$",
            f"The roots of this trinomial are $x_1 = {r3}$ and $x_2 = {r4}$.",
            f"The solution set is $S = ({r3}, {r4})$."
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 7 : Position relative de deux courbes
# ==========================================
class RelativePosition(BaseExercise):
    id = "SD2_007"
    title = {"fr": "Position de deux courbes", "en": "Position of two curves"}
    tags = ["second-degre", "position", "graphique"]

    def generate(self):
        x = sp.Symbol('x')
        r1, r2 = sorted(self.rng.sample([-3, -2, -1, 1, 2, 3, 4], k=2))
        a = -1
        f_minus_g = sp.expand(a * (x - r1) * (x - r2))
        
        m = self.rng.choice([-1, 1, 2])
        p = self.rng.randint(-3, 3)
        g_expr = m*x + p
        f_expr = sp.expand(f_minus_g + g_expr)

        self.statement_fr = [f"Soit $f$ et $g$ deux fonctions définies par $f(x) = {sp.latex(f_expr)}$ et $g(x) = {sp.latex(g_expr)}$."]
        self.statement_en = [f"Let $f$ and $g$ be two functions defined by $f(x) = {sp.latex(f_expr)}$ and $g(x) = {sp.latex(g_expr)}$."]

        q1_fr = ["Étudier la position relative des courbes représentatives $C_f$ et $C_g$."]
        q1_en = ["Study the relative position of the representative curves $C_f$ and $C_g$."]
        insight1_fr = ["Étudiez le signe de la différence $f(x) - g(x)$."]
        insight1_en = ["Study the sign of the difference $f(x) - g(x)$."]
        
        # Plotting the solution
        fig, ax = plt.subplots(figsize=(6, 4))
        x_vals = np.linspace(r1 - 2, r2 + 2, 400)
        
        # Calculate coefficients for plotting
        fa, fb, fc = f_expr.coeff(x, 2), f_expr.coeff(x, 1), f_expr.subs(x, 0)
        y_f = float(fa)*x_vals**2 + float(fb)*x_vals + float(fc)
        y_g = float(m)*x_vals + float(p)
        
        ax.plot(x_vals, y_f, color="green", label="$C_f$")
        ax.plot(x_vals, y_g, color="red", label="$C_g$")
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend()

        ans1_fr = [
            f"On étudie le signe de $f(x) - g(x) = {sp.latex(f_minus_g)}$.",
            f"Les racines de ce trinôme sont $x_1 = {r1}$ et $x_2 = {r2}$.",
            f"Comme $a = {a} < 0$, le trinôme est positif entre les racines.",
            f"- Sur $]{r1} ; {r2}[$, $f(x) > g(x)$, donc $C_f$ est au-dessus de $C_g$.",
            f"- Sur $]-\\infty ; {r1}[ \\cup ]{r2} ; +\\infty[$, $f(x) < g(x)$, donc $C_f$ est en-dessous de $C_g$.",
            fig
        ]
        ans1_en = [
            f"We study the sign of $f(x) - g(x) = {sp.latex(f_minus_g)}$.",
            f"The roots of this trinomial are $x_1 = {r1}$ and $x_2 = {r2}$.",
            f"Since $a = {a} < 0$, the trinomial is positive between the roots.",
            f"- On $({r1}, {r2})$, $f(x) > g(x)$, so $C_f$ is above $C_g$.",
            f"- On $(-\\infty, {r1}) \\cup ({r2}, +\\infty)$, $f(x) < g(x)$, so $C_f$ is below $C_g$.",
            fig
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))
import sympy as sp
from exercises.base_exercise import BaseExercise
from exercises.question import Question

# Module-level registry key
CHAPTER = {"fr": "Dérivation (Partie 2)", "en": "Differentiation (Part 2)"}

# ==========================================
# MÉTHODE 1 : Dériver les fonctions usuelles
# ==========================================
class DeriveUsualFunctions(BaseExercise):
    id = "DER2_001"
    title = {"fr": "Dériver les fonctions usuelles", "en": "Derive standard functions"}
    tags = ["derivation", "fonctions usuelles", "calcul"]

    def generate(self):
        # Generate random parameters while keeping the exact structure of the PDF
        c_val = self.rng.randint(50, 150)
        a_val = self.rng.choice([-8, -7, -6, -5, -4, -3, 2, 3, 4, 5])
        n_val = self.rng.randint(3, 7)
        p_val = self.rng.randint(3, 7)

        self.statement_fr = ["Calculer la dérivée de chacune des fonctions :"]
        self.statement_en = ["Calculate the derivative of each of the functions:"]

        # 1. Constant function
        q1_fr = [f"$f(x) = {c_val}$"]
        q1_en = [f"$f(x) = {c_val}$"]
        insight1_fr = ["La dérivée d'une constante $a$ est $0$."]
        insight1_en = ["The derivative of a constant $a$ is $0$."]
        ans1_fr = [f"$f(x) = {c_val} \\rightarrow f'(x) = 0$"]
        ans1_en = [f"$f(x) = {c_val} \\rightarrow f'(x) = 0$"]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # 2. Linear function
        q2_fr = [f"$g(x) = {a_val}x$"]
        q2_en = [f"$g(x) = {a_val}x$"]
        insight2_fr = ["La dérivée de $ax$ est $a$."]
        insight2_en = ["The derivative of $ax$ is $a$."]
        ans2_fr = [f"$g(x) = {a_val}x \\rightarrow g'(x) = {a_val}$"]
        ans2_en = [f"$g(x) = {a_val}x \\rightarrow g'(x) = {a_val}$"]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))

        # 3. Power function
        q3_fr = [f"$h(x) = x^{n_val}$"]
        q3_en = [f"$h(x) = x^{n_val}$"]
        insight3_fr = ["La dérivée de $x^n$ est $nx^{n-1}$."]
        insight3_en = ["The derivative of $x^n$ is $nx^{n-1}$."]
        ans3_fr = [f"$h(x) = x^{n_val} \\rightarrow h'(x) = {n_val}x^{n_val - 1}$"]
        ans3_en = [f"$h(x) = x^{n_val} \\rightarrow h'(x) = {n_val}x^{n_val - 1}$"]
        self.questions.append(Question(q3_fr, q3_en, insight3_fr, insight3_en, ans3_fr, ans3_en))

        # 4. Inverse power function
        q4_fr = [f"$k(x) = \\frac{{1}}{{x^{p_val}}}$"]
        q4_en = [f"$k(x) = \\frac{{1}}{{x^{p_val}}}$"]
        insight4_fr = ["La dérivée de $\\frac{1}{x^n}$ est $-\\frac{n}{x^{n+1}}$."]
        insight4_en = ["The derivative of $\\frac{1}{x^n}$ is $-\\frac{n}{x^{n+1}}$."]
        ans4_fr = [f"$k(x) = \\frac{{1}}{{x^{p_val}}} \\rightarrow k'(x) = -\\frac{{{p_val}}}{{x^{p_val + 1}}}$"]
        ans4_en = [f"$k(x) = \\frac{{1}}{{x^{p_val}}} \\rightarrow k'(x) = -\\frac{{{p_val}}}{{x^{p_val + 1}}}$"]
        self.questions.append(Question(q4_fr, q4_en, insight4_fr, insight4_en, ans4_fr, ans4_en))

        # 5. Square root function
        q5_fr = [f"$m(x) = \\sqrt{{x}}$"]
        q5_en = [f"$m(x) = \\sqrt{{x}}$"]
        insight5_fr = ["La dérivée de $\\sqrt{x}$ est $\\frac{1}{2\\sqrt{x}}$."]
        insight5_en = ["The derivative of $\\sqrt{x}$ is $\\frac{1}{2\\sqrt{x}}$."]
        ans5_fr = [f"$m(x) = \\sqrt{{x}} \\rightarrow m'(x) = \\frac{{1}}{{2\\sqrt{{x}}}}$"]
        ans5_en = [f"$m(x) = \\sqrt{{x}} \\rightarrow m'(x) = \\frac{{1}}{{2\\sqrt{{x}}}}$"]
        self.questions.append(Question(q5_fr, q5_en, insight5_fr, insight5_en, ans5_fr, ans5_en))


# ==========================================
# MÉTHODE 2 : Opérations sur les fonctions dérivées
# ==========================================
class DeriveOperations(BaseExercise):
    id = "DER2_002"
    title = {"fr": "Dérivées de sommes, produits et quotients", "en": "Derivatives of sums, products and quotients"}
    tags = ["derivation", "operations", "produit", "quotient"]

    def generate(self):
        self.statement_fr = ["Dans chaque cas, calculer la fonction dérivée de $f$ :"]
        self.statement_en = ["In each case, calculate the derivative function of $f$:"]
        
        x = sp.Symbol('x')

        # a) Sum with square root: f(x) = ax^2 + b*sqrt(x)
        a1 = self.rng.choice([2, 3, 4, 5])
        b1 = self.rng.choice([2, 4, 6, 8]) # Even so b1/2 is an integer
        
        q1_fr = [f"a) $f(x) = {a1}x^2 + {b1}\\sqrt{{x}}$"]
        q1_en = [f"a) $f(x) = {a1}x^2 + {b1}\\sqrt{{x}}$"]
        insight1_fr = ["Identifiez $f(x) = u(x) + v(x)$. Dérivez chaque terme séparément en utilisant $u'$ et $v'$."]
        insight1_en = ["Identify $f(x) = u(x) + v(x)$. Differentiate each term separately using $u'$ and $v'$."]
        ans1_fr = [
            f"$f(x) = u(x) + v(x)$ avec $u(x) = {a1}x^2 \\rightarrow u'(x) = {a1} \\times 2x = {2*a1}x$",
            f"$v(x) = {b1}\\sqrt{{x}} \\rightarrow v'(x) = {b1} \\frac{{1}}{{2\\sqrt{{x}}}} = \\frac{{{b1//2}}}{{\\sqrt{{x}}}}$",
            f"Donc : $f'(x) = u'(x) + v'(x) = {2*a1}x + \\frac{{{b1//2}}}{{\\sqrt{{x}}}}$"
        ]
        ans1_en = [
            f"$f(x) = u(x) + v(x)$ with $u(x) = {a1}x^2 \\rightarrow u'(x) = {a1} \\times 2x = {2*a1}x$",
            f"$v(x) = {b1}\\sqrt{{x}} \\rightarrow v'(x) = {b1} \\frac{{1}}{{2\\sqrt{{x}}}} = \\frac{{{b1//2}}}{{\\sqrt{{x}}}}$",
            f"Thus: $f'(x) = u'(x) + v'(x) = {2*a1}x + \\frac{{{b1//2}}}{{\\sqrt{{x}}}}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # b) Polynomial sum: f(x) = ax^3 + bx^2
        a2 = self.rng.choice([2, 3, 4, 5])
        b2 = self.rng.choice([-5, -4, -3, -2])
        
        q2_fr = [f"b) $f(x) = {a2}x^3 {b2}x^2$"]
        q2_en = [f"b) $f(x) = {a2}x^3 {b2}x^2$"]
        insight2_fr = ["Identifiez $f(x) = u(x) + v(x)$. Appliquez la formule $f'(x) = u'(x) + v'(x)$."]
        insight2_en = ["Identify $f(x) = u(x) + v(x)$. Apply the formula $f'(x) = u'(x) + v'(x)$."]
        ans2_fr = [
            f"$f(x) = u(x) + v(x)$ avec $u(x) = {a2}x^3 \\rightarrow u'(x) = {a2} \\times 3x^2 = {3*a2}x^2$",
            f"$v(x) = {b2}x^2 \\rightarrow v'(x) = {b2} \\times 2x = {2*b2}x$",
            f"Donc : $f'(x) = u'(x) + v'(x) = {3*a2}x^2 + ({2*b2}x) = {3*a2}x^2 {2*b2}x$"
        ]
        ans2_en = [
            f"$f(x) = u(x) + v(x)$ with $u(x) = {a2}x^3 \\rightarrow u'(x) = {a2} \\times 3x^2 = {3*a2}x^2$",
            f"$v(x) = {b2}x^2 \\rightarrow v'(x) = {b2} \\times 2x = {2*b2}x$",
            f"Thus: $f'(x) = u'(x) + v'(x) = {3*a2}x^2 + ({2*b2}x) = {3*a2}x^2 {2*b2}x$"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))

        # c) Product: f(x) = (ax^2 + bx)(cx + d)
        a3 = self.rng.choice([2, 3, 4])
        b3 = self.rng.choice([2, 3, 4, 5])
        c3 = self.rng.choice([2, 3, 4, 5])
        d3 = self.rng.choice([-3, -2, -1])
        
        u3_expr = a3*x**2 + b3*x
        v3_expr = c3*x + d3
        u3_prime = 2*a3*x + b3
        v3_prime = c3
        f_prime_3 = sp.expand(u3_prime * v3_expr + u3_expr * v3_prime)

        q3_fr = [f"c) $f(x) = ({sp.latex(u3_expr)})({sp.latex(v3_expr)})$"]
        q3_en = [f"c) $f(x) = ({sp.latex(u3_expr)})({sp.latex(v3_expr)})$"]
        insight3_fr = ["Identifiez un produit $u(x)v(x)$. Utilisez la formule $(uv)' = u'v + uv'$."]
        insight3_en = ["Identify a product $u(x)v(x)$. Use the formula $(uv)' = u'v + uv'$."]
        ans3_fr = [
            f"$f(x) = u(x)v(x)$ avec $u(x) = {sp.latex(u3_expr)} \\rightarrow u'(x) = {sp.latex(u3_prime)}$",
            f"$v(x) = {sp.latex(v3_expr)} \\rightarrow v'(x) = {sp.latex(v3_prime)}$",
            f"Donc : $f'(x) = u'(x)v(x) + u(x)v'(x)$",
            f"$= ({sp.latex(u3_prime)})({sp.latex(v3_expr)}) + ({sp.latex(u3_expr)}) \\times {sp.latex(v3_prime)}$",
            f"$= {sp.latex(sp.expand(u3_prime * v3_expr))} + {sp.latex(sp.expand(u3_expr * v3_prime))}$",
            f"$= {sp.latex(f_prime_3)}$"
        ]
        ans3_en = [
            f"$f(x) = u(x)v(x)$ with $u(x) = {sp.latex(u3_expr)} \\rightarrow u'(x) = {sp.latex(u3_prime)}$",
            f"$v(x) = {sp.latex(v3_expr)} \\rightarrow v'(x) = {sp.latex(v3_prime)}$",
            f"Thus: $f'(x) = u'(x)v(x) + u(x)v'(x)$",
            f"$= ({sp.latex(u3_prime)})({sp.latex(v3_expr)}) + ({sp.latex(u3_expr)}) \\times {sp.latex(v3_prime)}$",
            f"$= {sp.latex(sp.expand(u3_prime * v3_expr))} + {sp.latex(sp.expand(u3_expr * v3_prime))}$",
            f"$= {sp.latex(f_prime_3)}$"
        ]
        self.questions.append(Question(q3_fr, q3_en, insight3_fr, insight3_en, ans3_fr, ans3_en))

        # d) Inverse: f(x) = 1 / (ax^2 + bx)
        a4 = self.rng.choice([2, 3])
        b4 = self.rng.choice([3, 4, 5])
        u4_expr = a4*x**2 + b4*x
        u4_prime = 2*a4*x + b4
        
        q4_fr = [f"d) $f(x) = \\frac{{1}}{{{sp.latex(u4_expr)}}}$"]
        q4_en = [f"d) $f(x) = \\frac{{1}}{{{sp.latex(u4_expr)}}}$"]
        insight4_fr = ["Identifiez $f(x) = \\frac{1}{u(x)}$. Utilisez la formule $\\left(\\frac{1}{u}\\right)' = -\\frac{u'}{u^2}$."]
        insight4_en = ["Identify $f(x) = \\frac{1}{u(x)}$. Use the formula $\\left(\\frac{1}{u}\\right)' = -\\frac{u'}{u^2}$."]
        ans4_fr = [
            f"$f(x) = \\frac{{1}}{{u(x)}}$ avec $u(x) = {sp.latex(u4_expr)} \\rightarrow u'(x) = {sp.latex(u4_prime)}$",
            f"Donc : $f'(x) = -\\frac{{u'(x)}}{{u(x)^2}} = -\\frac{{{sp.latex(u4_prime)}}}{{({sp.latex(u4_expr)})^2}}$"
        ]
        ans4_en = [
            f"$f(x) = \\frac{{1}}{{u(x)}}$ with $u(x) = {sp.latex(u4_expr)} \\rightarrow u'(x) = {sp.latex(u4_prime)}$",
            f"Thus: $f'(x) = -\\frac{{u'(x)}}{{u(x)^2}} = -\\frac{{{sp.latex(u4_prime)}}}{{({sp.latex(u4_expr)})^2}}$"
        ]
        self.questions.append(Question(q4_fr, q4_en, insight4_fr, insight4_en, ans4_fr, ans4_en))

        # e) Quotient: f(x) = (ax + b) / (cx^2 + dx + e)
        a5 = self.rng.choice([4, 5, 6])
        b5 = self.rng.choice([-5, -4, -3])
        c5 = 1
        d5 = self.rng.choice([-3, -2])
        e5 = self.rng.choice([-2, -1])
        
        u5_expr = a5*x + b5
        v5_expr = c5*x**2 + d5*x + e5
        u5_prime = a5
        v5_prime = 2*c5*x + d5
        
        num_final = sp.expand(u5_prime * v5_expr - u5_expr * v5_prime)
        
        q5_fr = [f"e) $f(x) = \\frac{{{sp.latex(u5_expr)}}}{{{sp.latex(v5_expr)}}}$"]
        q5_en = [f"e) $f(x) = \\frac{{{sp.latex(u5_expr)}}}{{{sp.latex(v5_expr)}}}$"]
        insight5_fr = ["Identifiez un quotient $\\frac{u(x)}{v(x)}$. Appliquez la formule $\\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2}$."]
        insight5_en = ["Identify a quotient $\\frac{u(x)}{v(x)}$. Apply the formula $\\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2}$."]
        ans5_fr = [
            f"$f(x) = \\frac{{u(x)}}{{v(x)}}$ avec $u(x) = {sp.latex(u5_expr)} \\rightarrow u'(x) = {u5_prime}$",
            f"$v(x) = {sp.latex(v5_expr)} \\rightarrow v'(x) = {sp.latex(v5_prime)}$",
            f"Donc : $f'(x) = \\frac{{u'(x)v(x) - u(x)v'(x)}}{{v(x)^2}}$",
            f"$= \\frac{{{u5_prime}({sp.latex(v5_expr)}) - ({sp.latex(u5_expr)})({sp.latex(v5_prime)})}}{{({sp.latex(v5_expr)})^2}}$",
            f"$= \\frac{{{sp.latex(sp.expand(u5_prime * v5_expr))} - ({sp.latex(sp.expand(u5_expr * v5_prime))})}}{{({sp.latex(v5_expr)})^2}}$",
            f"$= \\frac{{{sp.latex(num_final)}}}{{({sp.latex(v5_expr)})^2}}$"
        ]
        ans5_en = [
            f"$f(x) = \\frac{{u(x)}}{{v(x)}}$ with $u(x) = {sp.latex(u5_expr)} \\rightarrow u'(x) = {u5_prime}$",
            f"$v(x) = {sp.latex(v5_expr)} \\rightarrow v'(x) = {sp.latex(v5_prime)}$",
            f"Thus: $f'(x) = \\frac{{u'(x)v(x) - u(x)v'(x)}}{{v(x)^2}}$",
            f"$= \\frac{{{u5_prime}({sp.latex(v5_expr)}) - ({sp.latex(u5_expr)})({sp.latex(v5_prime)})}}{{({sp.latex(v5_expr)})^2}}$",
            f"$= \\frac{{{sp.latex(sp.expand(u5_prime * v5_expr))} - ({sp.latex(sp.expand(u5_expr * v5_prime))})}}{{({sp.latex(v5_expr)})^2}}$",
            f"$= \\frac{{{sp.latex(num_final)}}}{{({sp.latex(v5_expr)})^2}}$"
        ]
        self.questions.append(Question(q5_fr, q5_en, insight5_fr, insight5_en, ans5_fr, ans5_en))


# ==========================================
# MÉTHODE 3 : Approximation linéaire
# ==========================================
class LinearApproximation(BaseExercise):
    id = "DER2_003"
    title = {"fr": "Calculer une valeur approchée", "en": "Calculate an approximate value"}
    tags = ["derivation", "approximation", "tangente"]

    def generate(self):
        a = self.rng.choice([2, 3, 4, 5])
        h = self.rng.choice([0.001, 0.002, 0.003, 0.004])
        target_val = a + h

        self.statement_fr = [f"On cherche à déterminer une valeur approchée du nombre $\\frac{{1}}{{{target_val}^2}}$."]
        self.statement_en = [f"We want to determine an approximate value of the number $\\frac{{1}}{{{target_val}^2}}$."]

        q1_fr = ["Déterminer cette valeur en utilisant l'approximation linéaire $f(a+h) \\approx f(a) + f'(a)h$."]
        q1_en = ["Determine this value using the linear approximation $f(a+h) \\approx f(a) + f'(a)h$."]
        
        insight1_fr = [f"Posez la fonction $f(x) = \\frac{{1}}{{x^2}}$. Identifiez $a = {a}$ et $h = {h}$."]
        insight1_en = [f"Set the function $f(x) = \\frac{{1}}{{x^2}}$. Identify $a = {a}$ and $h = {h}$."]
        
        f_a = 1 / (a**2)
        f_prime_a = -2 / (a**3)
        approx = f_a + f_prime_a * h

        ans1_fr = [
            f"On prend $f(x) = \\frac{{1}}{{x^2}}$. On a $f'(x) = -\\frac{{2}}{{x^3}}$.",
            f"Ici, $a = {a}$ et $h = {h}$.",
            f"Donc : $\\frac{{1}}{{{target_val}^2}} = f({a} + {h}) \\approx f({a}) + f'({a}) \\times {h}$",
            f"$\\approx \\frac{{1}}{{{a}^2}} + \\left(-\\frac{{2}}{{{a}^3}}\\right) \\times {h}$",
            f"$\\approx {f_a} + ({f_prime_a}) \\times {h}$",
            f"**$\\approx {approx}$**"
        ]
        ans1_en = [
            f"We take $f(x) = \\frac{{1}}{{x^2}}$. We have $f'(x) = -\\frac{{2}}{{x^3}}$.",
            f"Here, $a = {a}$ and $h = {h}$.",
            f"Thus: $\\frac{{1}}{{{target_val}^2}} = f({a} + {h}) \\approx f({a}) + f'({a}) \\times {h}$",
            f"$\\approx \\frac{{1}}{{{a}^2}} + \\left(-\\frac{{2}}{{{a}^3}}\\right) \\times {h}$",
            f"$\\approx {f_a} + ({f_prime_a}) \\times {h}$",
            f"**$\\approx {approx}$**"
        ]

        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from exercises.base_exercise import BaseExercise
from exercises.question import Question

# Module-level registry key
CHAPTER = {"fr": "Dérivation (Partie 1)", "en": "Differentiation (Part 1)"}

# ==========================================
# MÉTHODE 1 : Démontrer qu'une fonction est dérivable
# ==========================================
class ProveDifferentiability(BaseExercise):
    id = "DER_001"
    title = {"fr": "Démontrer qu'une fonction est dérivable", "en": "Prove that a function is differentiable"}
    tags = ["derivation", "limite", "taux d'accroissement"]

    def generate(self):
        a = self.rng.choice([-3, -2, -1, 1, 2, 3])
        b = self.rng.randint(-5, 5)
        c = self.rng.randint(-5, 5)
        x0 = self.rng.randint(-3, 3)

        x = sp.Symbol('x')
        f_expr = a * x**2 + b * x + c
        f_tex = sp.latex(f_expr)

        L = 2 * a * x0 + b  # The derivative f'(x0)

        self.statement_fr = [f"Soit la fonction trinôme $f$ définie sur $\\mathbb{{R}}$ par $f(x) = {f_tex}$."]
        self.statement_en = [f"Let the quadratic function $f$ be defined on $\\mathbb{{R}}$ by $f(x) = {f_tex}$."]

        q1_fr = [f"Démontrer que $f$ est dérivable en $x = {x0}$."]
        q1_en = [f"Prove that $f$ is differentiable at $x = {x0}$."]
        
        insight1_fr = [f"Calculez le taux d'accroissement $\\frac{{f({x0}+h) - f({x0})}}{{h}}$ pour $h \\ne 0$, puis déterminez sa limite quand $h$ tend vers 0."]
        insight1_en = [f"Calculate the rate of change $\\frac{{f({x0}+h) - f({x0})}}{{h}}$ for $h \\ne 0$, then determine its limit as $h$ approaches 0."]
        
        ans1_fr = [
            f"On calcule le taux d'accroissement pour $h \\ne 0$ :",
            f"$\\frac{{f({x0}+h) - f({x0})}}{{h}} = \\frac{{{a}({x0}+h)^2 + {b}({x0}+h) + {c} - ({a}({x0})^2 + {b}({x0}) + {c})}}{{h}}$",
            f"Après développement et simplification, on obtient : $a \\times h + {L}$",
            f"Donc : $\\lim_{{h \\to 0}} \\frac{{f({x0}+h) - f({x0})}}{{h}} = {L}$.",
            f"$f$ est donc dérivable en $x={x0}$ et $f'({x0}) = {L}$."
        ]
        ans1_en = [
            f"We calculate the rate of change for $h \\ne 0$:",
            f"$\\frac{{f({x0}+h) - f({x0})}}{{h}} = \\frac{{{a}({x0}+h)^2 + {b}({x0}+h) + {c} - ({a}({x0})^2 + {b}({x0}) + {c})}}{{h}}$",
            f"After expanding and simplifying, we get: $a \\times h + {L}$",
            f"Thus: $\\lim_{{h \\to 0}} \\frac{{f({x0}+h) - f({x0})}}{{h}} = {L}$.",
            f"$f$ is therefore differentiable at $x={x0}$ and $f'({x0}) = {L}$."
        ]

        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 2 : Non dérivabilité de la valeur absolue
# ==========================================
class AbsoluteValueNonDifferentiability(BaseExercise):
    id = "DER_002"
    title = {"fr": "Non dérivabilité en 0", "en": "Non-differentiability at 0"}
    tags = ["derivation", "valeur absolue", "limite"]

    def generate(self):
        k = self.rng.choice([1, 2, 3, 4, 5])
        k_str = "" if k == 1 else str(k)

        self.statement_fr = [f"Soit la fonction $f$ définie sur $\\mathbb{{R}}$ par $f(x) = {k_str}|x|$."]
        self.statement_en = [f"Let the function $f$ be defined on $\\mathbb{{R}}$ by $f(x) = {k_str}|x|$."]

        q1_fr = ["Démontrer que la fonction $f$ n'est pas dérivable en 0."]
        q1_en = ["Prove that the function $f$ is not differentiable at 0."]
        
        insight1_fr = ["Calculez le taux d'accroissement en 0. Attention, l'expression de $|h|$ dépend du signe de $h$."]
        insight1_en = ["Calculate the rate of change at 0. Note that the expression for $|h|$ depends on the sign of $h$."]
        
        ans1_fr = [
            "On calcule le taux d'accroissement de $f$ en 0 :",
            f"$\\frac{{f(0+h) - f(0)}}{{h}} = \\frac{{{k_str}|h| - 0}}{{h}} = {k_str}\\frac{{|h|}}{{h}}$",
            f"Si $h > 0$, $\\frac{{|h|}}{{h}} = 1$, donc le taux vaut ${k}$.",
            f"Si $h < 0$, $\\frac{{|h|}}{{h}} = -1$, donc le taux vaut ${-k}$.",
            "La limite n'existe pas car elle dépend du signe de $h$. La fonction n'est donc pas dérivable en 0."
        ]
        ans1_en = [
            "We calculate the rate of change of $f$ at 0:",
            f"$\\frac{{f(0+h) - f(0)}}{{h}} = \\frac{{{k_str}|h| - 0}}{{h}} = {k_str}\\frac{{|h|}}{{h}}$",
            f"If $h > 0$, $\\frac{{|h|}}{{h}} = 1$, so the rate is ${k}$.",
            f"If $h < 0$, $\\frac{{|h|}}{{h}} = -1$, so the rate is ${-k}$.",
            "The limit does not exist because it depends on the sign of $h$. The function is therefore not differentiable at 0."
        ]

        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 3 : Déterminer graphiquement le nombre dérivé
# ==========================================
class GraphicalDerivative(BaseExercise):
    id = "DER_003"
    title = {"fr": "Déterminer graphiquement le nombre dérivé", "en": "Determine the derivative graphically"}
    tags = ["derivation", "graphique", "tangente"]

    def generate(self):
        # 1. Structure the 3 curves to ensure clean graphing
        # Function f (Horizontal tangent)
        xf = self.rng.randint(-1, 1)
        yf = self.rng.randint(3, 5)
        af = float(self.rng.choice([0.5, 1]))
        mf = 0

        # Function g (Positive slope) and Part B target
        valid_g = False
        while not valid_g:
            xg = self.rng.randint(2, 4)
            yg = self.rng.randint(-2, 1)
            mg = self.rng.randint(1, 3)
            ag = float(self.rng.choice([-0.25, -0.5, 0.5]))
            
            # Part B target for function g
            offset = self.rng.choice([-2, -1, 1])
            xg2 = xg + offset
            mg2_val = 2 * ag * (xg2 - xg) + mg
            yg2 = ag * (xg2 - xg)**2 + mg * (xg2 - xg) + yg
            
            # Ensure the point (xg2, yg2) is comfortably within the y-axis limits [-4, 7]
            if -3.5 <= yg2 <= 6.5:
                valid_g = True
        
        # Format the slope nicely as a fraction string for LaTeX if it ends in .5
        mg2_frac = sp.Rational(int(mg2_val * 2), 2)
        mg2_tex = sp.latex(mg2_frac)

        # Function h (Negative slope)
        xh = self.rng.randint(5, 7)
        yh = self.rng.randint(1, 4)
        mh = self.rng.randint(-3, -1)
        ah = float(self.rng.choice([-1, -0.5]))

        # 2. Generate the Statement Figure (Part A)
        fig_stmt, ax_stmt = plt.subplots(figsize=(8, 5))
        x_vals = np.linspace(-3, 9, 400)
        
        f_vals = af * (x_vals - xf)**2 + yf
        g_vals = ag * (x_vals - xg)**2 + mg * (x_vals - xg) + yg
        h_vals = ah * (x_vals - xh)**2 + mh * (x_vals - xh) + yh

        ax_stmt.plot(x_vals, f_vals, color="green", label="$f$")
        ax_stmt.plot(x_vals, g_vals, color="red", label="$g$")
        ax_stmt.plot(x_vals, h_vals, color="blue", label="$h$")

        # Points of tangency
        ax_stmt.plot(xf, yf, 'g+', markersize=10, markeredgewidth=2)
        ax_stmt.plot(xg, yg, 'r+', markersize=10, markeredgewidth=2)
        ax_stmt.plot(xh, yh, 'b+', markersize=10, markeredgewidth=2)

        # Draw tangent lines across the grid
        ax_stmt.plot(x_vals, mf * (x_vals - xf) + yf, color="green", alpha=0.5)
        ax_stmt.plot(x_vals, mg * (x_vals - xg) + yg, color="red", alpha=0.5)
        ax_stmt.plot(x_vals, mh * (x_vals - xh) + yh, color="blue", alpha=0.5)

        ax_stmt.axhline(0, color='black', linewidth=1)
        ax_stmt.axvline(0, color='black', linewidth=1)
        ax_stmt.grid(True, linestyle='--', alpha=0.7)
        ax_stmt.set_xlim(-3, 9)
        ax_stmt.set_ylim(-4, 7)
        ax_stmt.legend(loc="upper left")
        
        # 3. Generate the Solution Figure (Part B)
        fig_sol, ax_sol = plt.subplots(figsize=(8, 5))
        ax_sol.plot(x_vals, f_vals, color="green", alpha=0.2)
        ax_sol.plot(x_vals, g_vals, color="red")
        ax_sol.plot(x_vals, h_vals, color="blue", alpha=0.2)
        
        # Plot the requested tangent for part B
        ax_sol.plot(x_vals, mg2_val * (x_vals - xg2) + yg2, color="red", linestyle="--", label=f"Tangente à $g$ en $x={xg2}$")
        ax_sol.plot(xg2, yg2, 'r+', markersize=10, markeredgewidth=2)
        
        ax_sol.axhline(0, color='black', linewidth=1)
        ax_sol.axvline(0, color='black', linewidth=1)
        ax_sol.grid(True, linestyle='--', alpha=0.7)
        ax_sol.set_xlim(-3, 9)
        ax_sol.set_ylim(-4, 7)
        ax_sol.legend(loc="upper left")

        # 4. Assemble the UI blocks
        self.statement_fr = []
        self.statement_en = []

        # Question 1
        q1_fr = ["On a représenté les fonctions $f$, $g$ et $h$ et trois tangentes dans un repère.",
                fig_stmt,
                f"Lire graphiquement $f'({xf})$, $g'({xg})$ et $h'({xh})$."]
        q1_en = ["The functions $f$, $g$, and $h$, along with three tangents, are represented in a coordinate system.",
                fig_stmt,
                f"Read $f'({xf})$, $g'({xg})$, and $h'({xh})$ graphically."]
        
        insight1_fr = ["Le nombre dérivé en un point est égal à la pente de la tangente en ce point (décalage vertical pour un pas de 1 vers la droite)."]
        insight1_en = ["The derivative at a point is equal to the slope of the tangent at that point (vertical shift for a 1-unit step to the right)."]
        
        ans1_fr = [
            f"- Tangente à $f$ en $x={xf}$ : pente = {mf}, donc $f'({xf}) = {mf}$.",
            f"- Tangente à $g$ en $x={xg}$ : pente = {mg}, donc $g'({xg}) = {mg}$.",
            f"- Tangente à $h$ en $x={xh}$ : pente = {mh}, donc $h'({xh}) = {mh}$."
        ]
        ans1_en = [
            f"- Tangent to $f$ at $x={xf}$: slope = {mf}, so $f'({xf}) = {mf}$.",
            f"- Tangent to $g$ at $x={xg}$: slope = {mg}, so $g'({xg}) = {mg}$.",
            f"- Tangent to $h$ at $x={xh}$: slope = {mh}, so $h'({xh}) = {mh}$."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question 2
        q2_fr = [f"Tracer la tangente à la courbe de la fonction $g$ en $x={xg2}$ sachant que $g'({xg2}) = {mg2_tex}$."]
        q2_en = [f"Draw the tangent to the curve of function $g$ at $x={xg2}$ given that $g'({xg2}) = {mg2_tex}$."]
        
        insight2_fr = [f"Placez le point de la courbe $g$ d'abscisse $x={xg2}$, puis utilisez la pente $m = {mg2_tex}$ pour trouver un deuxième point de la droite."]
        insight2_en = [f"Plot the point on curve $g$ with x-coordinate $x={xg2}$, then use the slope $m = {mg2_tex}$ to find a second point on the line."]
        
        ans2_fr = [
            f"La tangente passe par le point de coordonnées $({xg2}, {yg2:.2g})$ et a pour pente $m = {mg2_tex}$.",
            fig_sol
        ]
        ans2_en = [
            f"The tangent passes through the point with coordinates $({xg2}, {yg2:.2g})$ and has a slope of $m = {mg2_tex}$.",
            fig_sol
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 4 : Équation de la tangente
# ==========================================
class TangentEquation(BaseExercise):
    id = "DER_004"
    title = {"fr": "Équation d'une tangente", "en": "Equation of a tangent"}
    tags = ["derivation", "tangente", "équation"]

    def generate(self):
        a = self.rng.choice([-2, -1, 1, 2])
        b = self.rng.randint(-4, 4)
        c = self.rng.randint(-5, 5)
        x0 = self.rng.randint(-2, 3)

        x = sp.Symbol('x')
        f_expr = a * x**2 + b * x + c
        f_tex = sp.latex(f_expr)

        f_x0 = a * x0**2 + b * x0 + c
        f_prime_x0 = 2 * a * x0 + b
        
        p = f_x0 - f_prime_x0 * x0
        
        m_str = "" if f_prime_x0 == 1 else ("-" if f_prime_x0 == -1 else str(f_prime_x0))
        p_str = f"+ {p}" if p > 0 else (f"- {abs(p)}" if p < 0 else "")
        tangent_eq = f"{m_str}x {p_str}".strip()
        if f_prime_x0 == 0:
            tangent_eq = str(p)

        self.statement_fr = [f"On considère la fonction trinôme $f$ définie sur $\\mathbb{{R}}$ par $f(x) = {f_tex}$."]
        self.statement_en = [f"Consider the quadratic function $f$ defined on $\\mathbb{{R}}$ by $f(x) = {f_tex}$."]

        q1_fr = [f"Déterminer une équation de la tangente à la courbe représentative de $f$ au point d'abscisse $x={x0}$."]
        q1_en = [f"Determine an equation of the tangent to the curve of $f$ at the point with x-coordinate $x={x0}$."]
        
        insight1_fr = [f"Une équation de la tangente au point d'abscisse $a$ est : $y = f'(a)(x - a) + f(a)$."]
        insight1_en = [f"An equation of the tangent at the point with x-coordinate $a$ is: $y = f'(a)(x - a) + f(a)$."]
        
        ans1_fr = [
            f"On calcule le nombre dérivé et l'image en $x={x0}$ :",
            f"$f'({x0}) = {f_prime_x0}$ et $f({x0}) = {f_x0}$",
            f"L'équation est de la forme $y = f'({x0})(x - {x0}) + f({x0})$.",
            f"$y = {f_prime_x0}(x - {x0}) + ({f_x0})$",
            f"**$y = {tangent_eq}$**"
        ]
        ans1_en = [
            f"We calculate the derivative and the image at $x={x0}$:",
            f"$f'({x0}) = {f_prime_x0}$ and $f({x0}) = {f_x0}$",
            f"The equation is of the form $y = f'({x0})(x - {x0}) + f({x0})$.",
            f"$y = {f_prime_x0}(x - {x0}) + ({f_x0})$",
            f"**$y = {tangent_eq}$**"
        ]

        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))
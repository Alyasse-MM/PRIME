import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from exercises.base_exercise import BaseExercise
from exercises.question import Question

# Module-level registry key
CHAPTER = {"fr": "Généralités sur les Suites", "en": "Introduction to Sequences"}


# ==========================================
# MÉTHODE 1 : Suites définies en fonction de n (explicite)
# ==========================================
class ExplicitSequenceTerms(BaseExercise):
    id = "SUI1_001"
    title = {"fr": "Calculer des termes (Forme explicite)", "en": "Calculate terms (Explicit form)"}
    tags = ["suites", "explicite", "termes"]

    def generate(self):
        a = self.rng.randint(2, 5)
        b = self.rng.choice([2, 3, 4])
        c = self.rng.randint(-5, 5)

        self.statement_fr = ["Calculer les quatre premiers termes des suites suivantes :"]
        self.statement_en = ["Calculate the first four terms of the following sequences:"]

        # Suite u_n = a * n
        q1_fr = [f"a) $u_n = {a}n$"]
        q1_en = [f"a) $u_n = {a}n$"]
        insight1_fr = ["Remplacez successivement $n$ par 0, 1, 2 et 3."]
        insight1_en = ["Successively replace $n$ with 0, 1, 2, and 3."]
        ans1_fr = [
            f"$u_0 = {a} \\times 0 = 0$",
            f"$u_1 = {a} \\times 1 = {a}$",
            f"$u_2 = {a} \\times 2 = {a * 2}$",
            f"$u_3 = {a} \\times 3 = {a * 3}$"
        ]
        ans1_en = [
            f"$u_0 = {a} \\times 0 = 0$",
            f"$u_1 = {a} \\times 1 = {a}$",
            f"$u_2 = {a} \\times 2 = {a * 2}$",
            f"$u_3 = {a} \\times 3 = {a * 3}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Suite v_n = b * n^2 + c
        sign_c = f"- {abs(c)}" if c < 0 else f"+ {c}"
        if c == 0: sign_c = ""
        
        q2_fr = [f"b) $v_n = {b}n^2 {sign_c}$"]
        q2_en = [f"b) $v_n = {b}n^2 {sign_c}$"]
        insight2_fr = ["Remplacez $n$ par 0, 1, 2 et 3 en respectant les priorités opératoires (le carré d'abord)."]
        insight2_en = ["Replace $n$ with 0, 1, 2, and 3, respecting the order of operations (square first)."]
        ans2_fr = [
            f"$v_0 = {b} \\times 0^2 {sign_c} = {c}$",
            f"$v_1 = {b} \\times 1^2 {sign_c} = {b + c}$",
            f"$v_2 = {b} \\times 2^2 {sign_c} = {b * 4 + c}$",
            f"$v_3 = {b} \\times 3^2 {sign_c} = {b * 9 + c}$"
        ]
        ans2_en = [
            f"$v_0 = {b} \\times 0^2 {sign_c} = {c}$",
            f"$v_1 = {b} \\times 1^2 {sign_c} = {b + c}$",
            f"$v_2 = {b} \\times 2^2 {sign_c} = {b * 4 + c}$",
            f"$v_3 = {b} \\times 3^2 {sign_c} = {b * 9 + c}$"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 2 : Suites définies par récurrence (1)
# ==========================================
class RecurrenceSequenceTerms1(BaseExercise):
    id = "SUI1_002"
    title = {"fr": "Calculer des termes (Récurrence 1)", "en": "Calculate terms (Recurrence 1)"}
    tags = ["suites", "recurrence", "termes"]

    def generate(self):
        u0 = self.rng.randint(2, 6)
        a = self.rng.choice([2, 3, 4])
        
        v0 = self.rng.randint(2, 5)
        b = self.rng.choice([2, 3, 4])
        c = self.rng.randint(1, 5)

        self.statement_fr = ["Calculer les quatre premiers termes des suites suivantes :"]
        self.statement_en = ["Calculate the first four terms of the following sequences:"]

        # Suite u_{n+1} = a * u_n
        q1_fr = [f"a) Pour tout entier $n$ : $\\begin{{cases}} u_0 = {u0} \\\\ u_{{n+1}} = {a}u_n \\end{{cases}}$"]
        q1_en = [f"a) For any integer $n$: $\\begin{{cases}} u_0 = {u0} \\\\ u_{{n+1}} = {a}u_n \\end{{cases}}$"]
        insight1_fr = ["Chaque terme s'obtient en multipliant le terme précédent par la constante."]
        insight1_en = ["Each term is obtained by multiplying the previous term by the constant."]
        ans1_fr = [
            f"$u_0 = {u0}$",
            f"$u_1 = {a} \\times u_0 = {a} \\times {u0} = {a * u0}$",
            f"$u_2 = {a} \\times u_1 = {a} \\times {a * u0} = {a * a * u0}$",
            f"$u_3 = {a} \\times u_2 = {a} \\times {a * a * u0} = {a * a * a * u0}$"
        ]
        ans1_en = [
            f"$u_0 = {u0}$",
            f"$u_1 = {a} \\times u_0 = {a} \\times {u0} = {a * u0}$",
            f"$u_2 = {a} \\times u_1 = {a} \\times {a * u0} = {a * a * u0}$",
            f"$u_3 = {a} \\times u_2 = {a} \\times {a * a * u0} = {a * a * a * u0}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Suite v_{n+1} = b * v_n - c
        v1 = b * v0 - c
        v2 = b * v1 - c
        v3 = b * v2 - c
        
        q2_fr = [f"b) Pour tout entier $n$ : $\\begin{{cases}} v_0 = {v0} \\\\ v_{{n+1}} = {b}v_n - {c} \\end{{cases}}$"]
        q2_en = [f"b) For any integer $n$: $\\begin{{cases}} v_0 = {v0} \\\\ v_{{n+1}} = {b}v_n - {c} \\end{{cases}}$"]
        insight2_fr = ["Utilisez la valeur calculée au rang précédent pour trouver la suivante."]
        insight2_en = ["Use the value calculated at the previous rank to find the next one."]
        ans2_fr = [
            f"$v_0 = {v0}$",
            f"$v_1 = {b} \\times v_0 - {c} = {b} \\times {v0} - {c} = {v1}$",
            f"$v_2 = {b} \\times v_1 - {c} = {b} \\times {v1} - {c} = {v2}$",
            f"$v_3 = {b} \\times v_2 - {c} = {b} \\times {v2} - {c} = {v3}$"
        ]
        ans2_en = [
            f"$v_0 = {v0}$",
            f"$v_1 = {b} \\times v_0 - {c} = {b} \\times {v0} - {c} = {v1}$",
            f"$v_2 = {b} \\times v_1 - {c} = {b} \\times {v1} - {c} = {v2}$",
            f"$v_3 = {b} \\times v_2 - {c} = {b} \\times {v2} - {c} = {v3}$"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 3 : Suites définies par récurrence (2)
# ==========================================
class RecurrenceSequenceTerms2(BaseExercise):
    id = "SUI1_003"
    title = {"fr": "Calculer des termes (Récurrence 2)", "en": "Calculate terms (Recurrence 2)"}
    tags = ["suites", "recurrence", "termes", "rang"]

    def generate(self):
        w1 = self.rng.randint(1, 4)
        
        self.statement_fr = [f"Pour tout entier $n \\ge 1$, on donne : $\\begin{{cases}} w_1 = {w1} \\\\ w_{{n+1}} = w_n + n \\end{{cases}}$"]
        self.statement_en = [f"For any integer $n \\ge 1$, we are given: $\\begin{{cases}} w_1 = {w1} \\\\ w_{{n+1}} = w_n + n \\end{{cases}}$"]

        q1_fr = ["Calculer les quatre premiers termes de la suite."]
        q1_en = ["Calculate the first four terms of the sequence."]
        insight1_fr = ["Attention, le premier terme est $w_1$. Pour calculer $w_2$, on utilise $n=1$ dans la formule."]
        insight1_en = ["Careful, the first term is $w_1$. To calculate $w_2$, use $n=1$ in the formula."]
        
        w2 = w1 + 1
        w3 = w2 + 2
        w4 = w3 + 3

        ans1_fr = [
            f"$w_1 = {w1}$",
            f"$w_2 = w_{{1+1}} = w_1 + 1 = {w1} + 1 = {w2} \\quad \\leftarrow n \\text{{ est égal à 1}}$",
            f"$w_3 = w_{{2+1}} = w_2 + 2 = {w2} + 2 = {w3} \\quad \\leftarrow n \\text{{ est égal à 2}}$",
            f"$w_4 = w_{{3+1}} = w_3 + 3 = {w3} + 3 = {w4} \\quad \\leftarrow n \\text{{ est égal à 3}}$"
        ]
        ans1_en = [
            f"$w_1 = {w1}$",
            f"$w_2 = w_{{1+1}} = w_1 + 1 = {w1} + 1 = {w2} \\quad \\leftarrow n \\text{{ equals 1}}$",
            f"$w_3 = w_{{2+1}} = w_2 + 2 = {w2} + 2 = {w3} \\quad \\leftarrow n \\text{{ equals 2}}$",
            f"$w_4 = w_{{3+1}} = w_3 + 3 = {w3} + 3 = {w4} \\quad \\leftarrow n \\text{{ equals 3}}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 4 : Calculer un terme avec un algorithme
# ==========================================
class SequenceAlgorithm(BaseExercise):
    id = "SUI1_004"
    title = {"fr": "Algorithme (Calcul de termes)", "en": "Algorithm (Term calculation)"}
    tags = ["suites", "algorithmique", "python"]

    def generate(self):
        u0 = self.rng.randint(2, 5)
        a = self.rng.choice([2, 3, 5])
        b = self.rng.randint(1, 5)
        target = self.rng.choice([10, 12, 15])

        self.statement_fr = [f"Pour tout entier $n$, on donne : $\\begin{{cases}} u_0 = {u0} \\\\ u_{{n+1}} = {a}u_n - {b} \\end{{cases}}$"]
        self.statement_en = [f"For any integer $n$, we are given: $\\begin{{cases}} u_0 = {u0} \\\\ u_{{n+1}} = {a}u_n - {b} \\end{{cases}}$"]

        q1_fr = [
            f"Écrire un programme Python `suite(n)` permettant de calculer le terme de rang $n$ de la suite $(u_n)$.",
            f"Comment afficher le terme $u_{{{target}}}$ ?"
        ]
        q1_en = [
            f"Write a Python program `suite(n)` to calculate the $n$-th term of the sequence $(u_n)$.",
            f"How do you print the term $u_{{{target}}}$?"
        ]
        insight1_fr = ["Utilisez une boucle `for` allant de $1$ à $n$ (inclus) pour écraser la variable à chaque itération."]
        insight1_en = ["Use a `for` loop from $1$ to $n$ (inclusive) to overwrite the variable at each iteration."]
        
        # Calculate the actual value to display it like a real terminal output
        val = u0
        for _ in range(target):
            val = a * val - b

        python_code_fr = (
            f"```python\n"
            f"def suite(n):\n"
            f"    u = {u0}\n"
            f"    for i in range(1, n + 1):\n"
            f"        u = {a} * u - {b}\n"
            f"    return u\n"
            f"```"
        )
        
        terminal_code = (
            f"```text\n"
            f">>> suite({target})\n"
            f"{val}\n"
            f"```"
        )

        ans1_fr = [python_code_fr, "Pour afficher le terme demandé, on exécute :", terminal_code]
        ans1_en = [python_code_fr.replace("def suite(n):", "def suite(n):"), "To print the requested term, run:", terminal_code]

        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 5 : Représenter graphiquement une suite
# ==========================================
class PlotSequence(BaseExercise):
    id = "SUI1_005"
    title = {"fr": "Représenter graphiquement une suite", "en": "Plot a sequence"}
    tags = ["suites", "graphique", "nuage de points"]

    def generate(self):
        a = self.rng.choice([1, 2, 3])
        b = self.rng.randint(-5, 0)
        
        self.statement_fr = [
            f"Pour tout entier $n$, on donne $u_n = \\frac{{n^2}}{{{a}}} {b}$.",
            "On souhaite représenter les 9 premiers termes (de $n=0$ à $n=8$) dans un repère."
        ]
        self.statement_en = [
            f"For any integer $n$, we are given $u_n = \\frac{{n^2}}{{{a}}} {b}$.",
            "We want to plot the first 9 terms (from $n=0$ to $n=8$) in a coordinate system."
        ]

        q1_fr = ["Construire le nuage de points de coordonnées $(n; u_n)$."]
        q1_en = ["Construct the scatter plot with coordinates $(n; u_n)$."]
        insight1_fr = ["Calculez d'abord les valeurs de $u_0$ jusqu'à $u_8$ dans un tableau, puis placez les points (sans les relier !)."]
        insight1_en = ["First calculate the values from $u_0$ to $u_8$ in a table, then plot the points (without connecting them!)."]
        
        n_vals = np.arange(9)
        u_vals = (n_vals**2) / a + b
        
        # Generation de la table Markdown
        table_headers = "| $n$ | " + " | ".join(map(str, n_vals)) + " |"
        table_divider = "|---|" + "---|" * len(n_vals)
        table_values = "| $u_n$ | " + " | ".join([f"{val:g}" for val in u_vals]) + " |"
        md_table = f"{table_headers}\n{table_divider}\n{table_values}"

        # Generation du graphique
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.scatter(n_vals, u_vals, color="blue", marker="x", s=80, linewidth=2)
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_xticks(n_vals)
        ax.set_xlabel("$n$", loc="right")
        ax.set_ylabel("$u_n$", loc="top", rotation=0)

        ans1_fr = ["On construit un tableau de valeurs :", md_table, "Dans un repère, on place les points (sans tracer de ligne continue) :", fig]
        ans1_en = ["We build a table of values:", md_table, "In a coordinate system, we plot the points (without drawing a continuous line):", fig]

        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 6 : Sens de variation d'une suite
# ==========================================
class SequenceVariations(BaseExercise):
    id = "SUI1_006"
    title = {"fr": "Sens de variation (Calculs)", "en": "Sense of variation (Calculations)"}
    tags = ["suites", "variations", "difference", "quotient"]

    def generate(self):
        k = self.rng.choice([4, 6, 8])
        a = self.rng.randint(1, 3)

        self.statement_fr = ["Étudier le sens de variation des suites suivantes :"]
        self.statement_en = ["Study the sense of variation of the following sequences:"]

        # Partie a : u_n = n^2 - kn + k
        q1_fr = [
            f"a) Pour tout entier $n$, on donne : $u_n = n^2 - {k}n + {k}$.",
            "Démontrer que la suite $(u_n)$ est croissante à partir d'un certain rang à déterminer."
        ]
        q1_en = [
            f"a) For any integer $n$, we are given: $u_n = n^2 - {k}n + {k}$.",
            "Prove that the sequence $(u_n)$ is increasing from a certain rank to be determined."
        ]
        insight1_fr = ["Calculez la différence $u_{n+1} - u_n$ et étudiez son signe en résolvant une inéquation."]
        insight1_en = ["Calculate the difference $u_{n+1} - u_n$ and study its sign by solving an inequality."]
        
        diff_const = 1 - k
        threshold_f = (k - 1) / 2
        threshold_i = int(np.ceil(threshold_f))

        ans1_fr = [
            f"• On calcule la différence $u_{{n+1}} - u_n$ :",
            f"$u_{{n+1}} - u_n = ((n+1)^2 - {k}(n+1) + {k}) - (n^2 - {k}n + {k})$",
            f"$= (n^2 + 2n + 1 - {k}n - {k} + {k}) - n^2 + {k}n - {k}$",
            f"$= 2n {diff_const if diff_const < 0 else '+' + str(diff_const)}$",
            f"• On étudie le signe : $2n {diff_const if diff_const < 0 else '+' + str(diff_const)} \\ge 0 \\iff 2n \\ge {-diff_const} \\iff n \\ge {threshold_f}$.",
            f"Soit $n \\ge {threshold_i}$ car $n$ est un entier.",
            f"On a $u_{{n+1}} - u_n \\ge 0$ pour $n \\ge {threshold_i}$. La suite est croissante à partir du rang **{threshold_i}**."
        ]
        ans1_en = [
            f"• We calculate the difference $u_{{n+1}} - u_n$:",
            f"$u_{{n+1}} - u_n = ((n+1)^2 - {k}(n+1) + {k}) - (n^2 - {k}n + {k})$",
            f"$= (n^2 + 2n + 1 - {k}n - {k} + {k}) - n^2 + {k}n - {k}$",
            f"$= 2n {diff_const if diff_const < 0 else '+' + str(diff_const)}$",
            f"• We study the sign: $2n {diff_const if diff_const < 0 else '+' + str(diff_const)} \\ge 0 \\iff 2n \\ge {-diff_const} \\iff n \\ge {threshold_f}$.",
            f"That is $n \\ge {threshold_i}$ because $n$ is an integer.",
            f"We have $u_{{n+1}} - u_n \\ge 0$ for $n \\ge {threshold_i}$. The sequence is increasing from rank **{threshold_i}**."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Partie b : v_n = 1 / (n(n+a))
        q2_fr = [
            f"b) Pour tout $n \\in \\mathbb{{N}}^*$, on donne : $v_n = \\frac{{1}}{{n(n+{a})}}$.",
            "Démontrer que la suite $(v_n)$ est décroissante."
        ]
        q2_en = [
            f"b) For any $n \\in \\mathbb{{N}}^*$, we are given: $v_n = \\frac{{1}}{{n(n+{a})}}$.",
            "Prove that the sequence $(v_n)$ is decreasing."
        ]
        insight2_fr = ["Puisque les termes sont strictement positifs, calculez le quotient $\\frac{v_{n+1}}{v_n}$ et comparez-le à 1."]
        insight2_en = ["Since the terms are strictly positive, calculate the ratio $\\frac{v_{n+1}}{v_n}$ and compare it to 1."]
        
        ans2_fr = [
            f"• On calcule le rapport $\\frac{{v_{{n+1}}}}{{v_n}}$ :",
            f"$\\frac{{v_{{n+1}}}}{{v_n}} = \\frac{{\\frac{{1}}{{(n+1)(n+1+{a})}}}}{{\\frac{{1}}{{n(n+{a})}}}} = \\frac{{n(n+{a})}}{{(n+1)(n+{a+1})}}$",
            f"Or, pour $n > 0$, le numérateur est strictement inférieur au dénominateur ($n < n+1$ et $n+{a} < n+{a+1}$).",
            f"Donc $\\frac{{v_{{n+1}}}}{{v_n}} \\le 1$.",
            f"Comme $v_n > 0$, cela signifie que $v_{{n+1}} \\le v_n$. La suite $(v_n)$ est décroissante."
        ]
        ans2_en = [
            f"• We calculate the ratio $\\frac{{v_{{n+1}}}}{{v_n}}$:",
            f"$\\frac{{v_{{n+1}}}}{{v_n}} = \\frac{{\\frac{{1}}{{(n+1)(n+1+{a})}}}}{{\\frac{{1}}{{n(n+{a})}}}} = \\frac{{n(n+{a})}}{{(n+1)(n+{a+1})}}$",
            f"However, for $n > 0$, the numerator is strictly less than the denominator ($n < n+1$ and $n+{a} < n+{a+1}$).",
            f"Thus $\\frac{{v_{{n+1}}}}{{v_n}} \\le 1$.",
            f"Since $v_n > 0$, this means that $v_{{n+1}} \\le v_n$. The sequence $(v_n)$ is decreasing."
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 7 : Variations via la fonction associée
# ==========================================
class VariationsAssociatedFunction(BaseExercise):
    id = "SUI1_007"
    title = {"fr": "Variations avec la fonction associée", "en": "Variations with the associated function"}
    tags = ["suites", "variations", "fonction associée", "derivation"]

    def generate(self):
        c = self.rng.choice([2, 3, 4])
        
        self.statement_fr = [f"Pour tout $n \\in \\mathbb{{N}}$, on donne : $u_n = \\frac{{1}}{{n+{c}}}$."]
        self.statement_en = [f"For any $n \\in \\mathbb{{N}}$, we are given: $u_n = \\frac{{1}}{{n+{c}}}$."]

        q1_fr = [
            f"a) Étudier les variations de la fonction $f$ définie sur $[0; +\\infty[$ par $f(x) = \\frac{{1}}{{x+{c}}}$.",
            "b) En déduire le sens de variation de la suite $(u_n)$."
        ]
        q1_en = [
            f"a) Study the variations of the function $f$ defined on $[0; +\\infty)$ by $f(x) = \\frac{{1}}{{x+{c}}}$.",
            "b) Deduce the sense of variation of the sequence $(u_n)$."
        ]
        insight1_fr = ["Si la fonction $f$ est décroissante sur $[0; +\\infty[$, alors la suite $u_n = f(n)$ est aussi décroissante."]
        insight1_en = ["If the function $f$ is decreasing on $[0; +\\infty)$, then the sequence $u_n = f(n)$ is also decreasing."]
        
        ans1_fr = [
            f"a) On étudie le signe de la dérivée de $f$ sur $[0 ; +\\infty[$ :",
            f"$f'(x) = -\\frac{{1}}{{(x+{c})^2}}$.",
            f"Pour tout $x \\ge 0$, le dénominateur $(x+{c})^2$ est strictement positif, donc $f'(x) < 0$.",
            f"La fonction $f$ est strictement décroissante sur $[0 ; +\\infty[$.",
            f"b) On a $u_n = f(n)$.",
            f"Puisque $f$ est strictement décroissante pour tout réel positif, elle l'est a fortiori pour toute valeur entière positive.",
            f"On en déduit que la suite $(u_n)$ est strictement décroissante."
        ]
        ans1_en = [
            f"a) We study the sign of the derivative of $f$ on $[0 ; +\\infty)$:",
            f"$f'(x) = -\\frac{{1}}{{(x+{c})^2}}$.",
            f"For any $x \\ge 0$, the denominator $(x+{c})^2$ is strictly positive, thus $f'(x) < 0$.",
            f"The function $f$ is strictly decreasing on $[0 ; +\\infty)$.",
            f"b) We have $u_n = f(n)$.",
            f"Since $f$ is strictly decreasing for all positive real numbers, it is fortiori decreasing for all positive integer values.",
            f"We deduce that the sequence $(u_n)$ is strictly decreasing."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 8 : Conjecturer la limite
# ==========================================
class ConjectureLimit(BaseExercise):
    id = "SUI1_008"
    title = {"fr": "Conjecturer la limite", "en": "Conjecture the limit"}
    tags = ["suites", "limite", "conjecture"]

    def generate(self):
        a = self.rng.choice([2, 3, 4])
        b = self.rng.randint(2, 5)

        self.statement_fr = ["Conjecturer le comportement à l'infini des suites suivantes :"]
        self.statement_en = ["Conjecture the behavior at infinity of the following sequences:"]

        # a) u_n = n^2 + a
        q1_fr = [
            f"1) Pour tout entier $n$, on donne : $u_n = n^2 + {a}$.",
            "Calculer $u_0, u_1, u_2, u_{10}$ et $u_{100}$. La suite semble-t-elle converger ou diverger ?"
        ]
        q1_en = [
            f"1) For any integer $n$, we are given: $u_n = n^2 + {a}$.",
            "Calculate $u_0, u_1, u_2, u_{10}$ and $u_{100}$. Does the sequence seem to converge or diverge?"
        ]
        insight1_fr = ["Si les valeurs augmentent indéfiniment sans jamais se stabiliser, la suite diverge vers $+\\infty$."]
        insight1_en = ["If the values increase indefinitely without ever stabilizing, the sequence diverges to $+\\infty$."]
        
        u0, u1, u2 = a, 1+a, 4+a
        u10, u100 = 100+a, 10000+a

        ans1_fr = [
            f"$u_0 = 0^2 + {a} = {u0}$",
            f"$u_1 = 1^2 + {a} = {u1}$",
            f"$u_2 = 2^2 + {a} = {u2}$",
            f"$u_{{10}} = 10^2 + {a} = {u10}$",
            f"$u_{{100}} = 100^2 + {a} = {u100}$",
            f"Plus $n$ devient grand, plus les termes de la suite deviennent grands. La suite $(u_n)$ semble diverger vers $+\\infty$."
        ]
        ans1_en = [
            f"$u_0 = 0^2 + {a} = {u0}$",
            f"$u_1 = 1^2 + {a} = {u1}$",
            f"$u_2 = 2^2 + {a} = {u2}$",
            f"$u_{{10}} = 10^2 + {a} = {u10}$",
            f"$u_{{100}} = 100^2 + {a} = {u100}$",
            f"The larger $n$ becomes, the larger the terms of the sequence become. The sequence $(u_n)$ seems to diverge to $+\\infty$."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # b) Alternating sequence
        q2_fr = [
            f"2) Pour tout entier $n$, on donne : $\\begin{{cases}} v_0 = {b} \\\\ v_{{n+1}} = (-1)^n v_n \\end{{cases}}$",
            "Calculer les 6 premiers termes. La suite semble-t-elle converger ou diverger ?"
        ]
        q2_en = [
            f"2) For any integer $n$, we are given: $\\begin{{cases}} v_0 = {b} \\\\ v_{{n+1}} = (-1)^n v_n \\end{{cases}}$",
            "Calculate the first 6 terms. Does the sequence seem to converge or diverge?"
        ]
        insight2_fr = ["Regardez si les valeurs se rapprochent d'un nombre unique fixe."]
        insight2_en = ["Check if the values are getting closer to a single fixed number."]
        
        v0 = b
        v1 = ((-1)**0) * v0
        v2 = ((-1)**1) * v1
        v3 = ((-1)**2) * v2
        v4 = ((-1)**3) * v3
        v5 = ((-1)**4) * v4

        ans2_fr = [
            f"$v_0 = {v0}$",
            f"$v_1 = (-1)^0 \\times {v0} = {v1}$",
            f"$v_2 = (-1)^1 \\times {v1} = {v2}$",
            f"$v_3 = (-1)^2 \\times ({v2}) = {v3}$",
            f"$v_4 = (-1)^3 \\times ({v3}) = {v4}$",
            f"$v_5 = (-1)^4 \\times {v4} = {v5}$",
            "Lorsque $n$ augmente, les termes oscillent sans se rapprocher d'une valeur unique. La suite $(v_n)$ semble diverger."
        ]
        ans2_en = [
            f"$v_0 = {v0}$",
            f"$v_1 = (-1)^0 \\times {v0} = {v1}$",
            f"$v_2 = (-1)^1 \\times {v1} = {v2}$",
            f"$v_3 = (-1)^2 \\times ({v2}) = {v3}$",
            f"$v_4 = (-1)^3 \\times ({v3}) = {v4}$",
            f"$v_5 = (-1)^4 \\times {v4} = {v5}$",
            "As $n$ increases, the terms oscillate without getting closer to a single value. The sequence $(v_n)$ seems to diverge."
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 9 : Déterminer un seuil avec algorithme
# ==========================================
class ThresholdAlgorithm(BaseExercise):
    id = "SUI1_009"
    title = {"fr": "Algorithme (Recherche de seuil)", "en": "Algorithm (Threshold search)"}
    tags = ["suites", "algorithmique", "python", "seuil"]

    def generate(self):
        u0 = self.rng.choice([1, 2, 3])
        # u_{n+1} = a * u_n + b, with 0 < a < 1 for convergence
        a = self.rng.choice([0.5, 0.8, 0.9])
        b = self.rng.choice([2, 5, 10])
        limit = b / (1 - a)
        
        # Pick a target threshold that is reachable
        threshold = int(limit - self.rng.randint(2, 5))

        self.statement_fr = [
            f"Pour tout entier $n$, on donne : $\\begin{{cases}} u_0 = {u0} \\\\ u_{{n+1}} = {a}u_n + {b} \\end{{cases}}$"
        ]
        self.statement_en = [
            f"For any integer $n$, we are given: $\\begin{{cases}} u_0 = {u0} \\\\ u_{{n+1}} = {a}u_n + {b} \\end{{cases}}$"
        ]

        q1_fr = [f"Écrire un programme Python `seuil()` permettant de déterminer le rang de la suite à partir duquel les termes sont supérieurs à {threshold}."]
        q1_en = [f"Write a Python program `seuil()` to determine the rank of the sequence from which the terms are strictly greater than {threshold}."]
        insight1_fr = ["Utilisez une boucle conditionnelle `while u <= seuil:` pour continuer à calculer tant que la condition n'est pas atteinte."]
        insight1_en = ["Use a conditional loop `while u <= threshold:` to keep calculating as long as the condition is not met."]

        # Calculate the actual rank
        val = u0
        n_val = 0
        while val <= threshold:
            val = a * val + b
            n_val += 1

        python_code_fr = (
            f"```python\n"
            f"def seuil():\n"
            f"    n = 0\n"
            f"    u = {u0}\n"
            f"    while u <= {threshold}:\n"
            f"        n = n + 1\n"
            f"        u = {a} * u + {b}\n"
            f"    return n\n"
            f"```"
        )
        
        terminal_code = (
            f"```text\n"
            f">>> seuil()\n"
            f"{n_val}\n"
            f"```"
        )

        ans1_fr = [
            python_code_fr,
            "Si on exécute ce programme dans la console, on obtient le résultat suivant :",
            terminal_code,
            f"Les termes de la suite sont supérieurs à {threshold} à partir de $u_{{{n_val}}}$."
        ]
        ans1_en = [
            python_code_fr,
            "If we run this program in the console, we get the following result:",
            terminal_code,
            f"The terms of the sequence are greater than {threshold} starting from $u_{{{n_val}}}$."
        ]

        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))
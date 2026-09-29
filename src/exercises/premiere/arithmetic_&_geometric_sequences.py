import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from exercises.base_exercise import BaseExercise
from exercises.question import Question

# Module-level registry key
CHAPTER = {"fr": "Suites Arithmétiques et Géométriques", "en": "Arithmetic and Geometric Sequences"}

# ==========================================
# MÉTHODE 1 : Démontrer qu'une suite est arithmétique
# ==========================================
class ProveArithmetic(BaseExercise):
    id = "SUI2_001"
    title = {"fr": "Démontrer qu'une suite est arithmétique", "en": "Prove a sequence is arithmetic"}
    tags = ["suites", "arithmetique", "demonstration"]

    def generate(self):
        a = self.rng.randint(3, 9)
        b = self.rng.randint(2, 9)
        c = self.rng.randint(1, 5)

        self.statement_fr = ["Déterminer si les suites suivantes sont arithmétiques :"]
        self.statement_en = ["Determine if the following sequences are arithmetic:"]

        # a) u_n = b - a n
        q1_fr = [f"a) La suite $(u_n)$ définie par $u_n = {b} - {a}n$ est-elle arithmétique ?"]
        q1_en = [f"a) Is the sequence $(u_n)$ defined by $u_n = {b} - {a}n$ arithmetic?"]
        insight1_fr = ["Calculez la différence $u_{n+1} - u_n$. Si le résultat est un nombre constant (indépendant de $n$), la suite est arithmétique."]
        insight1_en = ["Calculate the difference $u_{n+1} - u_n$. If the result is a constant number (independent of $n$), the sequence is arithmetic."]
        
        ans1_fr = [
            f"$u_{{n+1}} - u_n = ({b} - {a}(n+1)) - ({b} - {a}n)$",
            f"$= {b} - {a}n - {a} - {b} + {a}n$",
            f"$= -{a}$",
            f"La différence entre deux termes successifs reste constante et égale à $-{a}$.",
            f"$(u_n)$ est une suite arithmétique de raison $r = -{a}$."
        ]
        ans1_en = [
            f"$u_{{n+1}} - u_n = ({b} - {a}(n+1)) - ({b} - {a}n)$",
            f"$= {b} - {a}n - {a} - {b} + {a}n$",
            f"$= -{a}$",
            f"The difference between two successive terms remains constant and equals $-{a}$.",
            f"$(u_n)$ is an arithmetic sequence with common difference $r = -{a}$."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # b) v_n = n^2 + c
        q2_fr = [f"b) La suite $(v_n)$ définie par $v_n = n^2 + {c}$ est-elle arithmétique ?"]
        q2_en = [f"b) Is the sequence $(v_n)$ defined by $v_n = n^2 + {c}$ arithmetic?"]
        insight2_fr = ["Calculez $v_{n+1} - v_n$. N'oubliez pas l'identité remarquable $(n+1)^2$."]
        insight2_en = ["Calculate $v_{n+1} - v_n$. Do not forget the remarkable identity $(n+1)^2$."]
        
        ans2_fr = [
            f"$v_{{n+1}} - v_n = ((n+1)^2 + {c}) - (n^2 + {c})$",
            f"$= n^2 + 2n + 1 + {c} - n^2 - {c}$",
            f"$= 2n + 1$",
            f"La différence entre un terme et son précédent n'est pas constante car elle dépend de $n$.",
            f"$(v_n)$ n'est pas une suite arithmétique."
        ]
        ans2_en = [
            f"$v_{{n+1}} - v_n = ((n+1)^2 + {c}) - (n^2 + {c})$",
            f"$= n^2 + 2n + 1 + {c} - n^2 - {c}$",
            f"$= 2n + 1$",
            f"The difference between a term and its preceding one is not constant because it depends on $n$.",
            f"$(v_n)$ is not an arithmetic sequence."
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 2 : Expression en fonction de n (Arithmétique)
# ==========================================
class ExprArithmetic(BaseExercise):
    id = "SUI2_002"
    title = {"fr": "Expression en fonction de n (Arithmétique)", "en": "Expression in terms of n (Arithmetic)"}
    tags = ["suites", "arithmetique", "expression"]

    def generate(self):
        u0 = self.rng.randint(2, 9)
        r1 = self.rng.randint(2, 6)
        
        v1 = self.rng.randint(3, 8)
        r2 = self.rng.randint(2, 5)

        self.statement_fr = ["Déterminer l'expression, en fonction de $n$, des suites arithmétiques suivantes :"]
        self.statement_en = ["Determine the expression, in terms of $n$, for the following arithmetic sequences:"]

        # a) Given u0
        q1_fr = [f"a) $(u_n)$ définie par : $\\begin{{cases}} u_0 = {u0} \\\\ u_{{n+1}} = u_n - {r1} \\end{{cases}}$"]
        q1_en = [f"a) $(u_n)$ defined by: $\\begin{{cases}} u_0 = {u0} \\\\ u_{{n+1}} = u_n - {r1} \\end{{cases}}$"]
        insight1_fr = ["Identifiez le premier terme $u_0$ et la raison $r$. Utilisez la formule $u_n = u_0 + nr$."]
        insight1_en = ["Identify the first term $u_0$ and the common difference $r$. Use the formula $u_n = u_0 + nr$."]
        
        ans1_fr = [
            f"On a $u_0 = {u0}$ et $u_{{n+1}} = u_n - {r1}$.",
            f"La raison $r$ est égale à $-{r1}$ et le premier terme $u_0$ est égal à ${u0}$.",
            f"Ainsi : $u_n = u_0 + nr = {u0} + n \\times (-{r1})$",
            f"**$u_n = {u0} - {r1}n$**"
        ]
        ans1_en = [
            f"We have $u_0 = {u0}$ and $u_{{n+1}} = u_n - {r1}$.",
            f"The common difference $r$ is $-{r1}$ and the first term $u_0$ is ${u0}$.",
            f"Thus: $u_n = u_0 + nr = {u0} + n \\times (-{r1})$",
            f"**$u_n = {u0} - {r1}n$**"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # b) Given u1
        q2_fr = [f"b) $(v_n)$ définie par : $\\begin{{cases}} v_1 = {v1} \\\\ v_{{n+1}} = v_n + {r2} \\end{{cases}}$"]
        q2_en = [f"b) $(v_n)$ defined by: $\\begin{{cases}} v_1 = {v1} \\\\ v_{{n+1}} = v_n + {r2} \\end{{cases}}$"]
        insight2_fr = ["Le premier terme donné est $v_1$. Calculez d'abord $v_0$ en faisant \"marche arrière\" ($v_0 = v_1 - r$), ou utilisez $v_n = v_1 + (n-1)r$."]
        insight2_en = ["The given first term is $v_1$. First calculate $v_0$ by going \"backwards\" ($v_0 = v_1 - r$), or use $v_n = v_1 + (n-1)r$."]
        
        v0 = v1 - r2
        sign_v0 = f"+ {v0}" if v0 >= 0 else f"- {abs(v0)}"
        if v0 == 0: sign_v0 = ""

        ans2_fr = [
            f"La raison $r$ est égale à ${r2}$. Le terme $v_0$ n'est pas donné mais on peut le calculer.",
            f"Pour passer de $v_1$ à $v_0$, on retire la raison : $v_0 = v_1 - {r2} = {v1} - {r2} = {v0}$.",
            f"Ainsi : $v_n = v_0 + nr$",
            f"**$v_n = {r2}n {sign_v0}$**"
        ]
        ans2_en = [
            f"The common difference $r$ is ${r2}$. The term $v_0$ is not given but can be calculated.",
            f"To go from $v_1$ to $v_0$, we subtract the common difference: $v_0 = v_1 - {r2} = {v1} - {r2} = {v0}$.",
            f"Thus: $v_n = v_0 + nr$",
            f"**$v_n = {r2}n {sign_v0}$**"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 3 : Trouver raison et premier terme
# ==========================================
class ParamsArithmetic(BaseExercise):
    id = "SUI2_003"
    title = {"fr": "Déterminer la raison et le premier terme d'une suite arithmétique", "en": "Determine the common difference and first term of an arithmetic sequence"}
    tags = ["suites", "arithmetique", "systeme", "raison"]

    def generate(self):
        r = self.rng.choice([2, 3, 4, 5])
        u0 = self.rng.randint(-10, 5)
        p = self.rng.randint(3, 5)
        q = self.rng.randint(7, 10)
        
        up = u0 + p * r
        uq = u0 + q * r

        self.statement_fr = [f"Considérons la suite arithmétique $(u_n)$ telle que $u_{{{p}}} = {up}$ et $u_{{{q}}} = {uq}$."]
        self.statement_en = [f"Consider the arithmetic sequence $(u_n)$ such that $u_{{{p}}} = {up}$ and $u_{{{q}}} = {uq}$."]

        q1_fr = [
            "a) Déterminer la raison et le premier terme de la suite $(u_n)$.",
            "b) Exprimer $u_n$ en fonction de $n$."
        ]
        q1_en = [
            "a) Determine the common difference and the first term of the sequence $(u_n)$.",
            "b) Express $u_n$ in terms of $n$."
        ]
        insight1_fr = ["Écrivez un système d'équations en utilisant la formule $u_n = u_0 + nr$ pour les deux termes connus, puis soustrayez les équations."]
        insight1_en = ["Write a system of equations using the formula $u_n = u_0 + nr$ for both known terms, then subtract the equations."]
        
        diff_u = uq - up
        diff_n = q - p
        sign_u0 = f"+ {u0}" if u0 > 0 else f"- {abs(u0)}"
        if u0 == 0: sign_u0 = ""

        ans1_fr = [
            f"a) Les termes sont de la forme $u_n = u_0 + nr$. Ainsi :",
            f"$\\begin{{cases}} {up} = u_0 + {p}r \\\\ {uq} = u_0 + {q}r \\end{{cases}}$",
            f"On soustrait la première équation à la deuxième :",
            f"${uq} - {up} = (u_0 + {q}r) - (u_0 + {p}r)$",
            f"${diff_u} = {diff_n}r \\implies r = \\frac{{{diff_u}}}{{{diff_n}}} = {r}$",
            f"Comme $u_0 + {p} \\times {r} = {up}$, on a $u_0 + {p*r} = {up} \\implies u_0 = {up} - {p*r} = {u0}$.",
            f"b) L'expression est donc : **$u_n = {r}n {sign_u0}$**."
        ]
        ans1_en = [
            f"a) The terms are of the form $u_n = u_0 + nr$. Thus:",
            f"$\\begin{{cases}} {up} = u_0 + {p}r \\\\ {uq} = u_0 + {q}r \\end{{cases}}$",
            f"We subtract the first equation from the second:",
            f"${uq} - {up} = (u_0 + {q}r) - (u_0 + {p}r)$",
            f"${diff_u} = {diff_n}r \\implies r = \\frac{{{diff_u}}}{{{diff_n}}} = {r}$",
            f"Since $u_0 + {p} \\times {r} = {up}$, we have $u_0 + {p*r} = {up} \\implies u_0 = {up} - {p*r} = {u0}$.",
            f"b) The expression is thus: **$u_n = {r}n {sign_u0}$**."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 4 : Sens de variation et graphique (Arithmétique)
# ==========================================
class VariationArithmetic(BaseExercise):
    id = "SUI2_004"
    title = {"fr": "Sens de variation (Arithmétique)", "en": "Sense of variation (Arithmetic)"}
    tags = ["suites", "arithmetique", "variations", "graphique"]

    def generate(self):
        a1 = self.rng.choice([2, 3, 4])
        b1 = self.rng.randint(1, 5)
        
        v0 = self.rng.randint(-5, 5)
        r2 = self.rng.randint(-5, -2)

        self.statement_fr = ["Étudier les variations des suites arithmétiques $(u_n)$ et $(v_n)$ définies par :"]
        self.statement_en = ["Study the variations of the arithmetic sequences $(u_n)$ and $(v_n)$ defined by:"]

        # Question a
        q1_fr = [f"a) $u_n = {b1} + {a1}n$"]
        q1_en = [f"a) $u_n = {b1} + {a1}n$"]
        insight1_fr = ["Identifiez la raison $r$. Si $r > 0$, la suite est croissante."]
        insight1_en = ["Identify the common difference $r$. If $r > 0$, the sequence is increasing."]
        
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        n_vals1 = np.arange(8)
        u_vals1 = b1 + a1 * n_vals1
        ax1.scatter(n_vals1, u_vals1, color="red", marker="x", s=80, linewidth=2)
        ax1.grid(True, linestyle='--', alpha=0.7)
        ax1.set_xlabel("$n$")
        ax1.set_ylabel("$u_n$")

        ans1_fr = [
            f"$(u_n)$ est croissante car sa raison est positive et égale à ${a1}$.",
            f"Les points de sa représentation graphique sont alignés et la croissance est linéaire.",
            fig1
        ]
        ans1_en = [
            f"$(u_n)$ is increasing because its common difference is positive and equals ${a1}$.",
            f"The points of its graphical representation are aligned and the growth is linear.",
            fig1
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question b
        q2_fr = [f"b) $\\begin{{cases}} v_0 = {v0} \\\\ v_{{n+1}} = v_n {r2} \\end{{cases}}$"]
        q2_en = [f"b) $\\begin{{cases}} v_0 = {v0} \\\\ v_{{n+1}} = v_n {r2} \\end{{cases}}$"]
        insight2_fr = ["Observez comment on passe d'un terme au suivant pour déduire le signe de la raison."]
        insight2_en = ["Observe how to get from one term to the next to deduce the sign of the common difference."]
        
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        n_vals2 = np.arange(8)
        v_vals2 = v0 + r2 * n_vals2
        ax2.scatter(n_vals2, v_vals2, color="blue", marker="x", s=80, linewidth=2)
        ax2.grid(True, linestyle='--', alpha=0.7)
        ax2.set_xlabel("$n$")
        ax2.set_ylabel("$v_n$")

        ans2_fr = [
            f"On passe d'un terme au suivant en ajoutant ${r2}$.",
            f"$(v_n)$ est décroissante car de raison négative et égale à ${r2}$.",
            fig2
        ]
        ans2_en = [
            f"We go from one term to the next by adding ${r2}$.",
            f"$(v_n)$ is decreasing because its common difference is negative and equals ${r2}$.",
            fig2
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 5 : Démontrer qu'une suite est géométrique
# ==========================================
class ProveGeometric(BaseExercise):
    id = "SUI2_005"
    title = {"fr": "Démontrer qu'une suite est géométrique", "en": "Prove a sequence is geometric"}
    tags = ["suites", "geometrique", "demonstration"]

    def generate(self):
        a = self.rng.choice([2, 3, 4, 7])
        b = self.rng.choice([2, 3, 5, 6])
        
        self.statement_fr = [f"La suite $(u_n)$ définie par $u_n = {a} \\times {b}^n$ est-elle géométrique ?"]
        self.statement_en = [f"Is the sequence $(u_n)$ defined by $u_n = {a} \\times {b}^n$ geometric?"]

        q1_fr = ["Le démontrer."]
        q1_en = ["Prove it."]
        insight1_fr = ["Calculez le rapport $\\frac{u_{n+1}}{u_n}$. S'il est constant (indépendant de $n$), la suite est géométrique."]
        insight1_en = ["Calculate the ratio $\\frac{u_{n+1}}{u_n}$. If it is constant (independent of $n$), the sequence is geometric."]
        
        ans1_fr = [
            f"On calcule $\\frac{{u_{{n+1}}}}{{u_n}}$ :",
            f"$\\frac{{u_{{n+1}}}}{{u_n}} = \\frac{{{a} \\times {b}^{{n+1}}}}{{{a} \\times {b}^n}} = \\frac{{{b}^{{n+1}}}}{{{b}^n}} = {b}^{{n+1-n}} = {b}$.",
            f"Le rapport entre un terme et son précédent reste constant et égal à ${b}$.",
            f"On passe d'un terme au suivant en multipliant par ${b}$.",
            f"$(u_n)$ est une suite géométrique de raison $q = {b}$ et de premier terme $u_0 = {a} \\times {b}^0 = {a}$."
        ]
        ans1_en = [
            f"We calculate $\\frac{{u_{{n+1}}}}{{u_n}}$ :",
            f"$\\frac{{u_{{n+1}}}}{{u_n}} = \\frac{{{a} \\times {b}^{{n+1}}}}{{{a} \\times {b}^n}} = \\frac{{{b}^{{n+1}}}}{{{b}^n}} = {b}^{{n+1-n}} = {b}$.",
            f"The ratio between a term and its predecessor remains constant and equals ${b}$.",
            f"We go from one term to the next by multiplying by ${b}$.",
            f"$(u_n)$ is a geometric sequence with common ratio $q = {b}$ and first term $u_0 = {a} \\times {b}^0 = {a}$."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 6 : Expression en fonction de n (Géométrique)
# ==========================================
class ExprGeometric(BaseExercise):
    id = "SUI2_006"
    title = {"fr": "Expression en fonction de n (Géométrique)", "en": "Expression in terms of n (Geometric)"}
    tags = ["suites", "geometrique", "expression"]

    def generate(self):
        u0 = self.rng.randint(2, 5)
        q1 = self.rng.randint(2, 6)
        
        # for v1, pick a multiple of q2 so v0 is a clean integer or decimal
        q2 = self.rng.choice([2, 4, 5])
        v1 = self.rng.randint(1, 5) * q2

        self.statement_fr = ["Déterminer l'expression en fonction de $n$ des suites géométriques suivantes :"]
        self.statement_en = ["Determine the expression in terms of $n$ for the following geometric sequences:"]

        # a) Given u0
        q1_fr = [f"a) $(u_n)$ définie par : $\\begin{{cases}} u_0 = {u0} \\\\ u_{{n+1}} = {q1}u_n \\end{{cases}}$"]
        q1_en = [f"a) $(u_n)$ defined by: $\\begin{{cases}} u_0 = {u0} \\\\ u_{{n+1}} = {q1}u_n \\end{{cases}}$"]
        insight1_fr = ["Identifiez le premier terme $u_0$ et la raison $q$. Utilisez $u_n = u_0 \\times q^n$."]
        insight1_en = ["Identify the first term $u_0$ and the common ratio $q$. Use $u_n = u_0 \\times q^n$."]
        
        ans1_fr = [
            f"On passe d'un terme au suivant en multipliant par ${q1}$, donc la raison $q = {q1}$ et $u_0 = {u0}$.",
            f"Ainsi : $u_n = u_0 \\times q^n$",
            f"**$u_n = {u0} \\times {q1}^n$**"
        ]
        ans1_en = [
            f"We go from one term to the next by multiplying by ${q1}$, so the common ratio $q = {q1}$ and $u_0 = {u0}$.",
            f"Thus: $u_n = u_0 \\times q^n$",
            f"**$u_n = {u0} \\times {q1}^n$**"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # b) Given v1
        q2_fr = [f"b) $(v_n)$ définie par : $\\begin{{cases}} v_1 = {v1} \\\\ v_{{n+1}} = {q2}v_n \\end{{cases}}$"]
        q2_en = [f"b) $(v_n)$ defined by: $\\begin{{cases}} v_1 = {v1} \\\\ v_{{n+1}} = {q2}v_n \\end{{cases}}$"]
        insight2_fr = ["Le premier terme donné est $v_1$. Calculez d'abord $v_0$ en divisant $v_1$ par la raison, ou utilisez $v_n = v_1 \\times q^{n-1}$."]
        insight2_en = ["The given first term is $v_1$. First calculate $v_0$ by dividing $v_1$ by the common ratio, or use $v_n = v_1 \\times q^{n-1}$."]
        
        v0 = v1 / q2
        v0_fmt = f"{int(v0)}" if v0.is_integer() else f"{v0}"

        ans2_fr = [
            f"La raison $q$ est égale à ${q2}$. Le terme $v_0$ se calcule par division :",
            f"$v_0 = \\frac{{v_1}}{{q}} = \\frac{{{v1}}}{{{q2}}} = {v0_fmt}$.",
            f"Ainsi : $v_n = v_0 \\times q^n$",
            f"**$v_n = {v0_fmt} \\times {q2}^n$**"
        ]
        ans2_en = [
            f"The common ratio $q$ is ${q2}$. The term $v_0$ is calculated by division:",
            f"$v_0 = \\frac{{v_1}}{{q}} = \\frac{{{v1}}}{{{q2}}} = {v0_fmt}$.",
            f"Thus: $v_n = v_0 \\times q^n$",
            f"**$v_n = {v0_fmt} \\times {q2}^n$**"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 7 : Trouver raison et premier terme (Géométrique)
# ==========================================
class ParamsGeometric(BaseExercise):
    id = "SUI2_007"
    title = {"fr": "Déterminer la raison et le premier terme d'une suite géométrique", "en": "Determine the ratio and first term of a geometric sequence"}
    tags = ["suites", "geometrique", "systeme", "raison"]

    def generate(self):
        q = self.rng.choice([2, 3, 4])
        p = self.rng.randint(3, 5)
        diff = self.rng.choice([2, 3])
        r_idx = p + diff
        
        up = self.rng.choice([4, 8, 9, 16])
        uq = up * (q ** diff)
        
        u0_frac = sp.Rational(up, q**p)

        self.statement_fr = [f"Considérons la suite géométrique $(u_n)$ telle que $u_{{{p}}} = {up}$ et $u_{{{r_idx}}} = {uq}$."]
        self.statement_en = [f"Consider the geometric sequence $(u_n)$ such that $u_{{{p}}} = {up}$ and $u_{{{r_idx}}} = {uq}$."]

        q1_fr = [
            "a) Déterminer la raison (supposée positive) et le premier terme de la suite $(u_n)$.",
            "b) En déduire une expression de la suite en fonction de $n$."
        ]
        q1_en = [
            "a) Determine the common ratio (assumed positive) and the first term of the sequence $(u_n)$.",
            "b) Deduce an expression of the sequence in terms of $n$."
        ]
        insight1_fr = ["Écrivez le système avec $u_n = u_0 \\times q^n$, puis divisez les deux équations pour isoler $q$."]
        insight1_en = ["Write the system with $u_n = u_0 \\times q^n$, then divide the two equations to isolate $q$."]
        
        root_name = "carrée" if diff == 2 else "cubique"
        root_name_en = "square" if diff == 2 else "cube"

        ans1_fr = [
            f"a) Les termes sont de la forme $u_n = u_0 \\times q^n$. Ainsi :",
            f"$\\begin{{cases}} {up} = u_0 \\times q^{{{p}}} \\\\ {uq} = u_0 \\times q^{{{r_idx}}} \\end{{cases}}$",
            f"On effectue le quotient membre à membre :",
            f"$\\frac{{{uq}}}{{{up}}} = \\frac{{u_0 \\times q^{{{r_idx}}}}}{{u_0 \\times q^{{{p}}}}} \\implies {int(uq/up)} = q^{{{diff}}}$",
            f"On utilise la racine {root_name} : $q = {q}$.",
            f"Comme $u_0 \\times {q}^{{{p}}} = {up}$, on a $u_0 = \\frac{{{up}}}{{{q**p}}} = {sp.latex(u0_frac)}$.",
            f"b) L'expression est donc : **$u_n = {sp.latex(u0_frac)} \\times {q}^n$**."
        ]
        ans1_en = [
            f"a) The terms are of the form $u_n = u_0 \\times q^n$. Thus:",
            f"$\\begin{{cases}} {up} = u_0 \\times q^{{{p}}} \\\\ {uq} = u_0 \\times q^{{{r_idx}}} \\end{{cases}}$",
            f"We perform member-by-member division:",
            f"$\\frac{{{uq}}}{{{up}}} = \\frac{{u_0 \\times q^{{{r_idx}}}}}{{u_0 \\times q^{{{p}}}}} \\implies {int(uq/up)} = q^{{{diff}}}$",
            f"Using the {root_name_en} root: $q = {q}$.",
            f"Since $u_0 \\times {q}^{{{p}}} = {up}$, we have $u_0 = \\frac{{{up}}}{{{q**p}}} = {sp.latex(u0_frac)}$.",
            f"b) The expression is thus: **$u_n = {sp.latex(u0_frac)} \\times {q}^n$**."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 8 : Sens de variation et graphique (Géométrique)
# ==========================================
class VariationGeometric(BaseExercise):
    id = "SUI2_008"
    title = {"fr": "Sens de variation (Géométrique)", "en": "Sense of variation (Geometric)"}
    tags = ["suites", "geometrique", "variations", "graphique"]

    def generate(self):
        u0 = self.rng.choice([-4, -3, -2])
        q1 = self.rng.choice([2, 3])
        
        v0 = self.rng.choice([-3, -2, -1])
        q2_frac = "\\frac{1}{2}"
        q2 = 0.5

        self.statement_fr = ["Déterminer le sens de variation des suites géométriques $(u_n)$ et $(v_n)$ définies par :"]
        self.statement_en = ["Determine the sense of variation of the geometric sequences $(u_n)$ and $(v_n)$ defined by:"]

        # Question a
        q1_fr = [f"a) $u_n = {u0} \\times {q1}^n$"]
        q1_en = [f"a) $u_n = {u0} \\times {q1}^n$"]
        insight1_fr = ["Vérifiez le signe du premier terme $u_0$ et la position de la raison $q$ par rapport à 1."]
        insight1_en = ["Check the sign of the first term $u_0$ and the position of the common ratio $q$ relative to 1."]
        
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        n_vals1 = np.arange(6)
        u_vals1 = u0 * (q1 ** n_vals1)
        ax1.scatter(n_vals1, u_vals1, color="red", marker="x", s=80, linewidth=2)
        ax1.grid(True, linestyle='--', alpha=0.7)
        ax1.set_xlabel("$n$")
        ax1.set_ylabel("$u_n$")

        ans1_fr = [
            f"$(u_n)$ est décroissante car :",
            f"$u_0 = {u0} < 0$ et $q = {q1} > 1$.",
            f"La décroissance est de type exponentielle.",
            fig1
        ]
        ans1_en = [
            f"$(u_n)$ is decreasing because:",
            f"$u_0 = {u0} < 0$ and $q = {q1} > 1$.",
            f"The decrease is exponential.",
            fig1
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question b
        q2_fr = [f"b) $\\begin{{cases}} v_0 = {v0} \\\\ v_{{n+1}} = {q2_frac} v_n \\end{{cases}}$"]
        q2_en = [f"b) $\\begin{{cases}} v_0 = {v0} \\\\ v_{{n+1}} = {q2_frac} v_n \\end{{cases}}$"]
        insight2_fr = ["Même méthode : sign de $v_0$ et comparaison de $q$ par rapport à 1."]
        insight2_en = ["Same method: sign of $v_0$ and comparison of $q$ relative to 1."]
        
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        n_vals2 = np.arange(6)
        v_vals2 = v0 * (q2 ** n_vals2)
        ax2.scatter(n_vals2, v_vals2, color="blue", marker="x", s=80, linewidth=2)
        ax2.grid(True, linestyle='--', alpha=0.7)
        ax2.set_xlabel("$n$")
        ax2.set_ylabel("$v_n$")

        ans2_fr = [
            f"$(v_n)$ est croissante car :",
            f"$v_0 = {v0} < 0$ et $0 < q = 0,5 < 1$.",
            fig2
        ]
        ans2_en = [
            f"$(v_n)$ is increasing because:",
            f"$v_0 = {v0} < 0$ and $0 < q = 0.5 < 1$.",
            fig2
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 9 : Somme d'une suite arithmétique
# ==========================================
class SumArithmetic(BaseExercise):
    id = "SUI2_009"
    title = {"fr": "Somme des termes (Arithmétique)", "en": "Sum of terms (Arithmetic)"}
    tags = ["suites", "arithmetique", "somme", "gauss"]

    def generate(self):
        n1 = self.rng.randint(200, 500)
        
        a2 = self.rng.randint(10, 20)
        b2 = self.rng.randint(70, 100)
        
        step3 = self.rng.choice([3, 4, 5])
        a3 = self.rng.randint(10, 15)
        b3 = self.rng.randint(40, 60)
        
        self.statement_fr = ["Calculer les sommes suivantes :"]
        self.statement_en = ["Calculate the following sums:"]

        # S1
        q1_fr = [f"a) $S_1 = 1 + 2 + 3 + \\dots + {n1}$"]
        q1_en = [f"a) $S_1 = 1 + 2 + 3 + \\dots + {n1}$"]
        insight1_fr = ["Utilisez la formule : $\\frac{n(n+1)}{2}$."]
        insight1_en = ["Use the formula: $\\frac{n(n+1)}{2}$."]
        
        s1_val = (n1 * (n1 + 1)) // 2
        
        ans1_fr = [
            f"$S_1 = \\frac{{{n1} \\times ({n1} + 1)}}{{2}} = \\frac{{{n1} \\times {n1+1}}}{{2}} = {s1_val}$"
        ]
        ans1_en = [
            f"$S_1 = \\frac{{{n1} \\times ({n1} + 1)}}{{2}} = \\frac{{{n1} \\times {n1+1}}}{{2}} = {s1_val}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # S2
        q2_fr = [f"b) $S_2 = {a2} + {a2+1} + {a2+2} + \\dots + {b2}$"]
        q2_en = [f"b) $S_2 = {a2} + {a2+1} + {a2+2} + \\dots + {b2}$"]
        insight2_fr = ["Soustrayez la somme des termes manquants de 1 à $a-1$ de la somme totale de 1 à $b$."]
        insight2_en = ["Subtract the sum of missing terms from 1 to $a-1$ from the total sum from 1 to $b$."]
        
        s2_val = (b2 * (b2 + 1)) // 2 - ((a2 - 1) * a2) // 2
        
        ans2_fr = [
            f"$S_2 = (1 + 2 + \\dots + {b2}) - (1 + 2 + \\dots + {a2-1})$",
            f"$= \\frac{{{b2} \\times {b2+1}}}{{2}} - \\frac{{{a2-1} \\times {a2}}}{{2}}$",
            f"$= {((b2 * (b2 + 1)) // 2)} - {(((a2 - 1) * a2) // 2)}$",
            f"$= {s2_val}$"
        ]
        ans2_en = [
            f"$S_2 = (1 + 2 + \\dots + {b2}) - (1 + 2 + \\dots + {a2-1})$",
            f"$= \\frac{{{b2} \\times {b2+1}}}{{2}} - \\frac{{{a2-1} \\times {a2}}}{{2}}$",
            f"$= {((b2 * (b2 + 1)) // 2)} - {(((a2 - 1) * a2) // 2)}$",
            f"$= {s2_val}$"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))
        
        # S3
        q3_fr = [f"c) $S_3 = {step3*a3} + {step3*(a3+1)} + {step3*(a3+2)} + \\dots + {step3*b3}$"]
        q3_en = [f"c) $S_3 = {step3*a3} + {step3*(a3+1)} + {step3*(a3+2)} + \\dots + {step3*b3}$"]
        insight3_fr = [f"Factorisez par {step3} pour vous ramener à une somme d'entiers consécutifs."]
        insight3_en = [f"Factor out {step3} to reduce it to a sum of consecutive integers."]
        
        inner_s_val = (b3 * (b3 + 1)) // 2 - ((a3 - 1) * a3) // 2
        s3_val = step3 * inner_s_val
        
        ans3_fr = [
            f"$S_3 = {step3} \\times ({a3} + {a3+1} + {a3+2} + \\dots + {b3})$",
            f"$= {step3} \\times \\left( (1 + \\dots + {b3}) - (1 + \\dots + {a3-1}) \\right)$",
            f"$= {step3} \\times \\left( \\frac{{{b3} \\times {b3+1}}}{{2}} - \\frac{{{a3-1} \\times {a3}}}{{2}} \\right)$",
            f"$= {step3} \\times ({inner_s_val}) = {s3_val}$"
        ]
        ans3_en = [
            f"$S_3 = {step3} \\times ({a3} + {a3+1} + {a3+2} + \\dots + {b3})$",
            f"$= {step3} \\times \\left( (1 + \\dots + {b3}) - (1 + \\dots + {a3-1}) \\right)$",
            f"$= {step3} \\times \\left( \\frac{{{b3} \\times {b3+1}}}{{2}} - \\frac{{{a3-1} \\times {a3}}}{{2}} \\right)$",
            f"$= {step3} \\times ({inner_s_val}) = {s3_val}$"
        ]
        self.questions.append(Question(q3_fr, q3_en, insight3_fr, insight3_en, ans3_fr, ans3_en))


# ==========================================
# MÉTHODE 10 : Somme d'une suite géométrique
# ==========================================
class SumGeometric(BaseExercise):
    id = "SUI2_010"
    title = {"fr": "Somme des termes (Géométrique)", "en": "Sum of terms (Geometric)"}
    tags = ["suites", "geometrique", "somme"]

    def generate(self):
        n1 = self.rng.randint(5, 9)
        
        a2 = self.rng.choice([2, 3, 4])
        n2 = self.rng.randint(8, 12)

        self.statement_fr = ["Calculer les sommes suivantes :"]
        self.statement_en = ["Calculate the following sums:"]

        # S1 (fraction)
        q1_fr = [f"a) $S_1 = 1 + \\frac{{1}}{{2}} + \\left(\\frac{{1}}{{2}}\\right)^2 + \\dots + \\left(\\frac{{1}}{{2}}\\right)^{{{n1}}}$"]
        q1_en = [f"a) $S_1 = 1 + \\frac{{1}}{{2}} + \\left(\\frac{{1}}{{2}}\\right)^2 + \\dots + \\left(\\frac{{1}}{{2}}\\right)^{{{n1}}}$"]
        insight1_fr = [f"Ici $q = \\frac{{1}}{{2}}$. Utilisez la formule $\\frac{{1 - q^{{n+1}}}}{{1 - q}}$."]
        insight1_en = [f"Here $q = \\frac{{1}}{{2}}$. Use the formula $\\frac{{1 - q^{{n+1}}}}{{1 - q}}$."]
        
        p_pow = 2**(n1+1)
        
        ans1_fr = [
            f"$S_1 = \\frac{{1 - \\left(\\frac{{1}}{{2}}\\right)^{{{n1}+1}}}}{{1 - \\frac{{1}}{{2}}}}$",
            f"$= \\frac{{1 - \\frac{{1}}{{{p_pow}}}}}{{\\frac{{1}}{{2}}}}$",
            f"$= \\left(\\frac{{{p_pow}}}{{{p_pow}}} - \\frac{{1}}{{{p_pow}}}\\right) \\times 2$",
            f"$= \\frac{{{p_pow - 1}}}{{{p_pow}}} \\times 2 = \\frac{{{p_pow - 1}}}{{{p_pow // 2}}}$"
        ]
        ans1_en = [
            f"$S_1 = \\frac{{1 - \\left(\\frac{{1}}{{2}}\\right)^{{{n1}+1}}}}{{1 - \\frac{{1}}{{2}}}}$",
            f"$= \\frac{{1 - \\frac{{1}}{{{p_pow}}}}}{{\\frac{{1}}{{2}}}}$",
            f"$= \\left(\\frac{{{p_pow}}}{{{p_pow}}} - \\frac{{1}}{{{p_pow}}}\\right) \\times 2$",
            f"$= \\frac{{{p_pow - 1}}}{{{p_pow}}} \\times 2 = \\frac{{{p_pow - 1}}}{{{p_pow // 2}}}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # S2 (integer > 1)
        q2_fr = [f"b) $S_2 = {a2} + {a2}^2 + {a2}^3 + \\dots + {a2}^{{{n2}}}$"]
        q2_en = [f"b) $S_2 = {a2} + {a2}^2 + {a2}^3 + \\dots + {a2}^{{{n2}}}$"]
        insight2_fr = [f"Ajoutez et retranchez 1 pour vous ramener à une somme commençant à 1."]
        insight2_en = [f"Add and subtract 1 to reduce it to a sum starting at 1."]
        
        s2_val = (1 - a2**(n2+1)) // (1 - a2) - 1

        ans2_fr = [
            f"$S_2 = 1 + {a2} + {a2}^2 + \\dots + {a2}^{{{n2}}} - 1$",
            f"$= \\frac{{1 - {a2}^{{{n2}+1}}}}{{1 - {a2}}} - 1$",
            f"$= {s2_val + 1} - 1 = {s2_val}$"
        ]
        ans2_en = [
            f"$S_2 = 1 + {a2} + {a2}^2 + \\dots + {a2}^{{{n2}}} - 1$",
            f"$= \\frac{{1 - {a2}^{{{n2}+1}}}}{{1 - {a2}}} - 1$",
            f"$= {s2_val + 1} - 1 = {s2_val}$"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 11 : Problème sur une somme géométrique
# ==========================================
class SumGeometricProblem(BaseExercise):
    id = "SUI2_011"
    title = {"fr": "Problème d'investissement", "en": "Investment problem"}
    tags = ["suites", "geometrique", "somme", "probleme"]

    def generate(self):
        u0 = self.rng.choice([10000, 20000, 30000, 40000])
        pct = self.rng.choice([10, 20, 30, 40])
        
        self.statement_fr = [
            f"Un entrepreneur investit au départ {u0} €.",
            f"Puis, chaque mois, il investit un montant supplémentaire diminué de {pct}% par rapport au mois précédent.",
            "On note $u_n$ le montant investi au mois $n$. On considère que $u_0 = " + str(u0) + "$."
        ]
        self.statement_en = [
            f"An entrepreneur initially invests {u0} €.",
            f"Then, each month, they invest an additional amount decreased by {pct}% compared to the previous month.",
            "Let $u_n$ be the amount invested in month $n$. We consider $u_0 = " + str(u0) + "$."
        ]

        q1_fr = ["Calculer le montant total investi la première année (12 mois)."]
        q1_en = ["Calculate the total amount invested in the first year (12 months)."]
        insight1_fr = ["Une diminution de $x\\%$ correspond à une multiplication par $1 - \\frac{x}{100}$. Calculez la somme des termes de $u_0$ à $u_{11}$."]
        insight1_en = ["A decrease of $x\\%$ corresponds to a multiplication by $1 - \\frac{x}{100}$. Calculate the sum of the terms from $u_0$ to $u_{11}$."]
        
        q = 1 - pct/100
        q_str = f"{q:.1f}" if pct % 10 == 0 else f"{q:.2f}"
        
        total_sum = u0 * (1 - q**12) / (1 - q)
        total_sum_rounded = int(round(total_sum))

        ans1_fr = [
            f"Diminuer un nombre de {pct}% revient à le multiplier par $1 - 0,{pct} = {q_str}$.",
            f"La suite $(u_n)$ est géométrique de premier terme $u_0 = {u0}$ et de raison $q = {q_str}$. Donc $u_n = {u0} \\times {q_str}^n$.",
            f"Le montant total sur 12 mois est $u_0 + u_1 + \\dots + u_{{11}}$ :",
            f"$= {u0} \\times \\left( {q_str}^0 + {q_str}^1 + \\dots + {q_str}^{{11}} \\right)$",
            f"$= {u0} \\times \\frac{{1 - {q_str}^{{12}}}}{{1 - {q_str}}}$",
            f"$\\approx {total_sum_rounded}$",
            f"Le montant total investi la première année est environ égal à **{total_sum_rounded} €**."
        ]
        ans1_en = [
            f"Decreasing a number by {pct}% is equivalent to multiplying it by $1 - 0.{pct} = {q_str}$.",
            f"The sequence $(u_n)$ is geometric with first term $u_0 = {u0}$ and common ratio $q = {q_str}$. Thus $u_n = {u0} \\times {q_str}^n$.",
            f"The total amount over 12 months is $u_0 + u_1 + \\dots + u_{{11}}$:",
            f"$= {u0} \\times \\left( {q_str}^0 + {q_str}^1 + \\dots + {q_str}^{{11}} \\right)$",
            f"$= {u0} \\times \\frac{{1 - {q_str}^{{12}}}}{{1 - {q_str}}}$",
            f"$\\approx {total_sum_rounded}$",
            f"The total amount invested in the first year is approximately **{total_sum_rounded} €**."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 12 : Algorithme de somme
# ==========================================
class SumAlgorithm(BaseExercise):
    id = "SUI2_012"
    title = {"fr": "Algorithme (Calcul de somme)", "en": "Algorithm (Sum calculation)"}
    tags = ["suites", "algorithmique", "somme", "python"]

    def generate(self):
        u0 = self.rng.randint(2, 5)
        a = round(self.rng.choice([0.2, 0.4, 0.5, 0.8]), 1)
        b = self.rng.randint(1, 5)
        target = self.rng.choice([8, 10, 12])

        self.statement_fr = [
            f"Pour tout entier $n$, on donne : $\\begin{{cases}} u_0 = {u0} \\\\ u_{{n+1}} = {a}u_n + {b} \\end{{cases}}$"
        ]
        self.statement_en = [
            f"For any integer $n$, we are given: $\\begin{{cases}} u_0 = {u0} \\\\ u_{{n+1}} = {a}u_n + {b} \\end{{cases}}$"
        ]

        q1_fr = [
            f"Écrire un programme Python permettant de calculer la somme $u_0 + u_1 + \\dots + u_{{{target}}}$."
        ]
        q1_en = [
            f"Write a Python program to calculate the sum $u_0 + u_1 + \\dots + u_{{{target}}}$."
        ]
        insight1_fr = ["Utilisez une variable pour le terme $u$ et une autre pour accumuler la somme $s$. Mettez à jour la somme avant de calculer le terme suivant dans la boucle."]
        insight1_en = ["Use a variable for the term $u$ and another to accumulate the sum $s$. Update the sum before calculating the next term in the loop."]

        # Calculate the actual sum safely with a for loop
        u = u0
        s = 0
        for _ in range(0, target + 1):
            s += u
            u = a * u + b

        python_code_fr = (
            f"```python\n"
            f"def somme(n):\n"
            f"    u = {u0}\n"
            f"    s = 0\n"
            f"    for i in range(0, n + 1):\n"
            f"        s = s + u\n"
            f"        u = {a} * u + {b}\n"
            f"    return s\n"
            f"```"
        )
        
        terminal_code = (
            f"```text\n"
            f">>> somme({target})\n"
            f"{s}\n"
            f"```"
        )

        ans1_fr = [
            "La suite n'étant ni arithmétique ni géométrique, on utilise un algorithme :",
            python_code_fr,
            "Si on exécute ce programme :",
            terminal_code,
            f"On trouve $u_0 + \\dots + u_{{{target}}} \\approx {s:.2f}$."
        ]
        ans1_en = [
            "Since the sequence is neither arithmetic nor geometric, we use an algorithm:",
            python_code_fr,
            "If we run this program:",
            terminal_code,
            f"We find $u_0 + \\dots + u_{{{target}}} \\approx {s:.2f}$."
        ]

        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))
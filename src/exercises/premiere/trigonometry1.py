import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from exercises.base_exercise import BaseExercise
from exercises.question import Question

# Module-level registry key
CHAPTER = {"fr": "Trigonométrie (Partie 1)", "en": "Trigonometry (Part 1)"}

def _draw_trigo_circle(ax, points=None, show_references=False):
    """
    Helper function to draw a standard trigonometric circle.
    points: list of dicts e.g., [{"angle": np.pi/4, "label": "A", "color": "green"}]
    """
    circle = plt.Circle((0, 0), 1, color='blue', fill=False, linewidth=1.5)
    ax.add_artist(circle)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Axes labels
    ax.text(1.1, 0, "1", va='bottom', ha='left')
    ax.text(0, 1.1, "1", ha='left', va='bottom')
    ax.text(-1.1, 0, "-1", va='bottom', ha='right')
    ax.text(0, -1.1, "-1", ha='left', va='top')
    ax.text(-0.1, -0.1, "O", ha='right', va='top')
    
    # Optional remarkable reference angles in the first quadrant
    if show_references:
        refs = [
            (np.pi/6, r"$\frac{\pi}{6}$"),
            (np.pi/4, r"$\frac{\pi}{4}$"),
            (np.pi/3, r"$\frac{\pi}{3}$"),
            (np.pi/2, r"$\frac{\pi}{2}$")
        ]
        for ang, tex in refs:
            x, y = np.cos(ang), np.sin(ang)
            ax.plot(x, y, marker='.', color='black')
            ax.plot([0, x], [0, y], color='gray', linestyle=':', alpha=0.5)
            ax.text(x * 1.15, y * 1.15, tex, color='black', ha='center', va='center')
            
    # Draw requested points
    if points:
        for p in points:
            ang = p["angle"]
            x, y = np.cos(ang), np.sin(ang)
            col = p.get("color", "red")
            lab = p.get("label", "")
            ax.plot(x, y, marker='o', color=col)
            ax.plot([0, x], [0, y], color='gray', linestyle='-')
            if lab:
                # Determine text offset based on quadrant
                ha = 'left' if x >= 0 else 'right'
                va = 'bottom' if y >= 0 else 'top'
                ax.text(x * 1.15, y * 1.15, lab, color=col, ha=ha, va=va, fontsize=12)


# ==========================================
# MÉTHODE 1 : Passer des degrés aux radians et réciproquement
# ==========================================
class DegreesToRadians(BaseExercise):
    id = "TRIG1_001"
    title = {"fr": "Degrés et radians", "en": "Degrees and radians"}
    tags = ["trigonometrie", "conversion", "radian", "degre"]

    def generate(self):
        deg_val = self.rng.choice([15, 33, 40, 54, 75, 105, 140])
        rad_num = self.rng.choice([3, 5, 7, 9, 11])
        rad_den = self.rng.choice([5, 8, 10, 12])

        self.statement_fr = ["Effectuer les conversions suivantes en utilisant la proportionnalité ($180^{\\circ}$ correspond à $\\pi$ radians)."]
        self.statement_en = ["Perform the following conversions using proportionality ($180^{\\circ}$ corresponds to $\\pi$ radians)."]

        # Question 1: Degrees to Radians
        q1_fr = [f"1) Donner la mesure en radians de l'angle de mesure ${deg_val}^{{\\circ}}$."]
        q1_en = [f"1) Give the radian measure of the angle measuring ${deg_val}^{{\\circ}}$."]
        insight1_fr = [f"Multipliez la valeur en degrés par $\\frac{{\\pi}}{{180}}$ et simplifiez la fraction."]
        insight1_en = [f"Multiply the degree value by $\\frac{{\\pi}}{{180}}$ and simplify the fraction."]
        
        rad_frac = sp.Rational(deg_val, 180)
        num_part = "" if rad_frac.p == 1 else str(rad_frac.p)
        rad_ans = f"\\frac{{{num_part}\\pi}}{{{rad_frac.q}}}" if rad_frac.q != 1 else f"{num_part}\\pi"

        ans1_fr = [
            f"On utilise la proportionnalité : $? = {deg_val} \\times \\frac{{\\pi}}{{180}}$",
            f"Après simplification de la fraction, on obtient **${rad_ans}$**."
        ]
        ans1_en = [
            f"Using proportionality: $? = {deg_val} \\times \\frac{{\\pi}}{{180}}$",
            f"After simplifying the fraction, we get **${rad_ans}$**."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question 2: Radians to Degrees
        q2_fr = [f"2) Donner la mesure en degrés de l'angle de mesure $\\frac{{{rad_num}\\pi}}{{{rad_den}}}$ radians."]
        q2_en = [f"2) Give the degree measure of the angle measuring $\\frac{{{rad_num}\\pi}}{{{rad_den}}}$ radians."]
        insight2_fr = [f"Remplacez simplement $\\pi$ par $180^{{\\circ}}$ dans la fraction et calculez le résultat."]
        insight2_en = [f"Simply replace $\\pi$ with $180^{{\\circ}}$ in the fraction and calculate the result."]
        
        deg_ans = (rad_num * 180) / rad_den
        deg_ans_fmt = f"{int(deg_ans)}" if deg_ans.is_integer() else f"{deg_ans:.1f}"

        ans2_fr = [
            f"On utilise la proportionnalité : $? = \\frac{{{rad_num}\\pi}}{{{rad_den}}} \\times \\frac{{180}}{{\\pi}}$",
            f"Ce qui revient à remplacer $\\pi$ par $180$ : $\\frac{{{rad_num} \\times 180}}{{{rad_den}}}$",
            f"On obtient **${deg_ans_fmt}^{{\\circ}}$**."
        ]
        ans2_en = [
            f"Using proportionality: $? = \\frac{{{rad_num}\\pi}}{{{rad_den}}} \\times \\frac{{180}}{{\\pi}}$",
            f"Which is equivalent to replacing $\\pi$ with $180$: $\\frac{{{rad_num} \\times 180}}{{{rad_den}}}$",
            f"We obtain **${deg_ans_fmt}^{{\\circ}}$**."
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 2 : Lire une valeur sur le cercle trigonométrique
# ==========================================
class ReadOnTrigoCircle(BaseExercise):
    id = "TRIG1_002"
    title = {"fr": "Lire une valeur sur le cercle", "en": "Read a value on the circle"}
    tags = ["trigonometrie", "cercle", "lecture", "mesure principale"]

    def generate(self):
        # Pick an angle in Q3 or Q4 to show the difference between [0, 2pi] and [-pi, pi]
        angles = [(5, 4), (7, 4), (4, 3), (5, 3), (7, 6), (11, 6)]
        num, den = self.rng.choice(angles)
        
        theta = (num * np.pi) / den
        
        # Format the positive measure
        pos_tex = f"\\frac{{{num}\\pi}}{{{den}}}"
        
        # Format the negative measure
        neg_num = num - 2 * den
        neg_tex = f"-\\frac{{{abs(neg_num)}\\pi}}{{{den}}}" if abs(neg_num) != 1 else f"-\\frac{{\\pi}}{{{den}}}"

        # Generate the statement figure
        fig, ax = plt.subplots(figsize=(5, 5))
        _draw_trigo_circle(ax, points=[{"angle": theta, "label": "A", "color": "green"}], show_references=True)

        self.statement_fr = [
            "On a représenté ci-dessous des mesures remarquables dans le premier quart du cercle trigonométrique.",
            fig,
            "Lire sur le cercle le nombre associé au point A :"
        ]
        self.statement_en = [
            "Remarkable measures in the first quadrant of the trigonometric circle are represented below.",
            fig,
            "Read on the circle the number associated with point A:"
        ]

        # Question a
        q1_fr = ["a) Sur l'intervalle $[0 ; 2\\pi]$."]
        q1_en = ["a) On the interval $[0 ; 2\\pi]$."]
        insight1_fr = ["Comptez les parts de cercle en partant de 0 et en tournant dans le sens direct (anti-horaire)."]
        insight1_en = ["Count the circle segments starting from 0 and turning in the direct (counter-clockwise) direction."]
        ans1_fr = [
            f"Sur $[0 ; 2\\pi]$, le nombre associé au point A est **${pos_tex}$**.",
            f"En effet, on compte ${num}$ fois l'angle de référence $\\frac{{\\pi}}{{{den}}}$ en tournant dans le sens direct."
        ]
        ans1_en = [
            f"On $[0 ; 2\\pi]$, the number associated with point A is **${pos_tex}$**.",
            f"Indeed, we count ${num}$ times the reference angle $\\frac{{\\pi}}{{{den}}}$ by turning in the direct direction."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question b
        q2_fr = ["b) Sur l'intervalle $[-\\pi ; \\pi]$."]
        q2_en = ["b) On the interval $[-\\pi ; \\pi]$."]
        insight2_fr = ["Comme le point est dans la moitié inférieure, partez de 0 et tournez dans le sens indirect (horaire)."]
        insight2_en = ["Since the point is in the lower half, start from 0 and turn in the indirect (clockwise) direction."]
        ans2_fr = [
            f"Sur $[-\\pi ; \\pi]$, le nombre associé au point A est **${neg_tex}$**.",
            f"En effet, on tourne dans le sens indirect pour trouver la valeur négative correspondante."
        ]
        ans2_en = [
            f"On $[-\\pi ; \\pi]$, the number associated with point A is **${neg_tex}$**.",
            f"Indeed, we turn in the indirect direction to find the corresponding negative value."
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 3 : Placer un point sur le cercle
# ==========================================
class PlacePointOnCircle(BaseExercise):
    id = "TRIG1_003"
    title = {"fr": "Placer un point sur le cercle", "en": "Place a point on the circle"}
    tags = ["trigonometrie", "cercle", "tours"]

    def generate(self):
        # Angle 1: 2pi + fraction
        num1, den1 = self.rng.choice([(9, 4), (13, 6), (7, 3), (17, 8)])
        # Angle 2: 2pi + fraction in Q2 or Q3
        num2, den2 = self.rng.choice([(8, 3), (11, 4), (10, 3)])
        # Angle 3: negative, multiple full turns backwards
        num3, den3 = self.rng.choice([(-9, 2), (-13, 3), (-15, 4)])

        a1_tex = f"\\frac{{{num1}\\pi}}{{{den1}}}"
        a2_tex = f"\\frac{{{num2}\\pi}}{{{den2}}}"
        a3_tex = f"-\\frac{{{abs(num3)}\\pi}}{{{den3}}}"

        self.statement_fr = ["Décomposer les nombres suivants pour placer les points correspondants sur le cercle trigonométrique :"]
        self.statement_en = ["Decompose the following numbers to place the corresponding points on the trigonometric circle:"]

        def _process_angle(num, den, label):
            full_turns = num // (2 * den)
            if num < 0:
                full_turns = (abs(num) // (2 * den)) * -1
                if num % (2 * den) != 0:
                    full_turns -= 1
            
            rem_num = num - (full_turns * 2 * den)
            
            rem_tex = f"\\frac{{{rem_num}\\pi}}{{{den}}}" if rem_num not in [1, -1] else (f"\\frac{{\\pi}}{{{den}}}" if rem_num == 1 else f"-\\frac{{\\pi}}{{{den}}}")
            if rem_num == 0: rem_tex = "0"
            
            turns_tex = f"{full_turns * 2}\\pi" if full_turns != 0 else ""
            if full_turns > 0: turns_tex = "+" + turns_tex
            
            theta = (num * np.pi) / den
            
            fig, ax = plt.subplots(figsize=(3, 3))
            _draw_trigo_circle(ax, points=[{"angle": theta, "label": label, "color": "green"}])
            
            return full_turns, rem_tex, fig

        # Point A
        q1_fr = [f"a) Le point A associé au nombre ${a1_tex}$"]
        q1_en = [f"a) Point A associated with the number ${a1_tex}$"]
        insight1_fr = [f"Faites apparaître un multiple de $2\\pi$ (un tour complet). Par exemple, divisez le numérateur par $2 \\times {den1}$."]
        insight1_en = [f"Extract a multiple of $2\\pi$ (a full turn). For example, divide the numerator by $2 \\times {den1}$."]
        
        t1, r1_tex, fig1 = _process_angle(num1, den1, "A")
        ans1_fr = [
            f"${a1_tex} = {t1*2}\\pi + {r1_tex}$",
            f"Cela correspond à {abs(t1)} tour(s) complet(s) dans le sens direct, plus un angle de ${r1_tex}$.",
            f"Le point A a la même position que le point associé à ${r1_tex}$.",
            fig1
        ]
        ans1_en = [
            f"${a1_tex} = {t1*2}\\pi + {r1_tex}$",
            f"This corresponds to {abs(t1)} full turn(s) in the direct direction, plus an angle of ${r1_tex}$.",
            f"Point A has the same position as the point associated with ${r1_tex}$.",
            fig1
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Point B
        q2_fr = [f"b) Le point B associé au nombre ${a2_tex}$"]
        q2_en = [f"b) Point B associated with the number ${a2_tex}$"]
        insight2_fr = [f"Comme précédemment, décomposez la fraction pour isoler les tours complets ($2\\pi$)."]
        insight2_en = [f"As before, decompose the fraction to isolate full turns ($2\\pi$)."]
        
        t2, r2_tex, fig2 = _process_angle(num2, den2, "B")
        ans2_fr = [
            f"${a2_tex} = {t2*2}\\pi + {r2_tex}$",
            f"Le point B a la même position que le point associé à ${r2_tex}$.",
            fig2
        ]
        ans2_en = [
            f"${a2_tex} = {t2*2}\\pi + {r2_tex}$",
            f"Point B has the same position as the point associated with ${r2_tex}$.",
            fig2
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))

        # Point C
        q3_fr = [f"c) Le point C associé au nombre ${a3_tex}$"]
        q3_en = [f"c) Point C associated with the number ${a3_tex}$"]
        insight3_fr = ["L'angle est négatif. Isolez les tours complets dans le sens indirect (multiples négatifs de $2\\pi$)."]
        insight3_en = ["The angle is negative. Isolate full turns in the indirect direction (negative multiples of $2\\pi$)."]
        
        t3, r3_tex, fig3 = _process_angle(num3, den3, "C")
        ans3_fr = [
            f"${a3_tex} = {t3*2}\\pi + {r3_tex}$",
            f"Cela correspond à {abs(t3)} tour(s) complet(s) dans le sens indirect.",
            f"Le point C a la même position que le point associé à ${r3_tex}$.",
            fig3
        ]
        ans3_en = [
            f"${a3_tex} = {t3*2}\\pi + {r3_tex}$",
            f"This corresponds to {abs(t3)} full turn(s) in the indirect direction.",
            f"Point C has the same position as the point associated with ${r3_tex}$.",
            fig3
        ]
        self.questions.append(Question(q3_fr, q3_en, insight3_fr, insight3_en, ans3_fr, ans3_en))


# ==========================================
# MÉTHODE 4 : Donner la mesure principale
# ==========================================
class PrincipalMeasure(BaseExercise):
    id = "TRIG1_004"
    title = {"fr": "Mesure principale d'un angle", "en": "Principal measure of an angle"}
    tags = ["trigonometrie", "mesure principale", "calcul"]

    def generate(self):
        den = self.rng.choice([3, 4, 6])
        num = self.rng.randint(17, 50)
        while num % den == 0 or num % 2 == 0:
            num += 1

        self.statement_fr = [f"Donner la mesure principale de l'angle $\\frac{{{num}\\pi}}{{{den}}}$."]
        self.statement_en = [f"Give the principal measure of the angle $\\frac{{{num}\\pi}}{{{den}}}$."]

        q1_fr = ["Détailler les étapes du calcul."]
        q1_en = ["Detail the calculation steps."]
        insight1_fr = [
            f"1) Choisissez un multiple de {den} proche de {num}.",
            "2) Décomposez la fraction.",
            "3) Faites apparaître un multiple pair de $\\pi$ (des tours complets)."
        ]
        insight1_en = [
            f"1) Choose a multiple of {den} close to {num}.",
            "2) Decompose the fraction.",
            "3) Extract an even multiple of $\\pi$ (full turns)."
        ]
        
        # Algorithme mathématique pour correspondre à la méthode de la leçon
        nearest_k = round(num / den)
        nearest_mult = nearest_k * den
        diff = num - nearest_mult
        
        sign_diff = "+" if diff > 0 else "-"
        abs_diff_tex = f"\\frac{{\\pi}}{{{den}}}" if abs(diff) == 1 else f"\\frac{{{abs(diff)}\\pi}}{{{den}}}"

        step1_fr = f"On choisit un multiple de {den} proche de {num}, soit {nearest_mult} :"
        step1_en = f"We choose a multiple of {den} close to {num}, which is {nearest_mult}:"
        
        eq1 = f"\\frac{{{num}\\pi}}{{{den}}} = \\frac{{{nearest_mult}\\pi}}{{{den}}} {sign_diff} {abs_diff_tex} = {nearest_k}\\pi {sign_diff} {abs_diff_tex}"

        # Si k est impair, il faut ajuster pour avoir un multiple pair de pi
        ans_fr = [step1_fr, f"${eq1}$"]
        ans_en = [step1_en, f"${eq1}$"]

        if nearest_k % 2 != 0:
            even_k = nearest_k - 1 if nearest_k > 0 else nearest_k + 1
            rem_pi = "\\pi" if nearest_k > 0 else "-\\pi"
            
            final_num = (1 if nearest_k > 0 else -1) * den + diff
            final_tex = f"\\frac{{{final_num}\\pi}}{{{den}}}" if abs(final_num) != 1 else (f"\\frac{{\\pi}}{{{den}}}" if final_num > 0 else f"-\\frac{{\\pi}}{{{den}}}")
            
            ans_fr.extend([
                f"Dans ${nearest_k}\\pi$, on fait apparaître un multiple pair de $\\pi$, soit ${even_k}\\pi$ :",
                f"$= {even_k}\\pi + {rem_pi} {sign_diff} {abs_diff_tex}$",
                f"$= {even_k}\\pi + \\frac{{{den}\\pi}}{{{den}}} {sign_diff} {abs_diff_tex}$",
                f"$= {even_k}\\pi + {final_tex}$"
            ])
            ans_en.extend([
                f"In ${nearest_k}\\pi$, we extract an even multiple of $\\pi$, which is ${even_k}\\pi$:",
                f"$= {even_k}\\pi + {rem_pi} {sign_diff} {abs_diff_tex}$",
                f"$= {even_k}\\pi + \\frac{{{den}\\pi}}{{{den}}} {sign_diff} {abs_diff_tex}$",
                f"$= {even_k}\\pi + {final_tex}$"
            ])
            final_val = final_tex
            turns = even_k
        else:
            final_val = f"{sign_diff}{abs_diff_tex}".replace("+-", "-").replace("++", "")
            if final_val.startswith("+"): final_val = final_val[1:]
            turns = nearest_k

        ans_fr.extend([
            f"${turns}\\pi$ correspond à des tours entiers.",
            f"${final_val}$ est bien compris dans l'intervalle $]-\\pi ; \\pi]$.",
            f"La mesure principale est **${final_val}$**."
        ])
        ans_en.extend([
            f"${turns}\\pi$ corresponds to full turns.",
            f"${final_val}$ is well within the interval $]-\\pi ; \\pi]$.",
            f"The principal measure is **${final_val}$**."
        ])

        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans_fr, ans_en))
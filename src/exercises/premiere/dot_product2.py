import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from exercises.base_exercise import BaseExercise
from exercises.question import Question

# Module-level registry key
CHAPTER = {"fr": "Produit Scalaire (Partie 2)", "en": "Dot Product (Part 2)"}

# ==========================================
# MÉTHODE 1 : Calculer un produit scalaire par projection
# ==========================================
class DotProductProjection(BaseExercise):
    id = "PSCAL2_001"
    title = {"fr": "Calculer par projection", "en": "Calculate by projection"}
    tags = ["produit scalaire", "projection", "orthogonal"]

    def generate(self):
        side = self.rng.choice([3, 4, 5, 6, 8])
        
        self.statement_fr = [
            f"Soit un carré $ABCD$ de côté ${side}$."
        ]
        self.statement_en = [
            f"Let $ABCD$ be a square with side ${side}$."
        ]

        # a) AB . AC
        q1_fr = ["a) Calculer le produit scalaire $\\vec{AB} \\cdot \\vec{AC}$."]
        q1_en = ["a) Calculate the dot product $\\vec{AB} \\cdot \\vec{AC}$."]
        insight1_fr = ["Projetez orthogonalement le point $C$ sur la droite $(AB)$. Quel est son projeté ?"]
        insight1_en = ["Orthogonally project point $C$ onto the line $(AB)$. What is its projection?"]
        
        ans1 = side**2
        
        ans1_fr = [
            f"$B$ est le projeté orthogonal de $C$ sur $(AB)$, alors :",
            f"$\\vec{{AB}} \\cdot \\vec{{AC}} = \\vec{{AB}} \\cdot \\vec{{AB}} = ||\\vec{{AB}}||^2 = AB^2 = {side}^2 = {ans1}$."
        ]
        ans1_en = [
            f"$B$ is the orthogonal projection of $C$ onto $(AB)$, so:",
            f"$\\vec{{AB}} \\cdot \\vec{{AC}} = \\vec{{AB}} \\cdot \\vec{{AB}} = ||\\vec{{AB}}||^2 = AB^2 = {side}^2 = {ans1}$."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # b) AB . AD
        q2_fr = ["b) Calculer le produit scalaire $\\vec{AB} \\cdot \\vec{AD}$."]
        q2_en = ["b) Calculate the dot product $\\vec{AB} \\cdot \\vec{AD}$."]
        insight2_fr = ["Dans un carré, l'angle au sommet $A$ est droit. Que peut-on dire du produit scalaire de deux vecteurs orthogonaux ?"]
        insight2_en = ["In a square, the angle at vertex $A$ is a right angle. What can we say about the dot product of two orthogonal vectors?"]
        
        ans2_fr = [
            f"$\\vec{{AB}} \\cdot \\vec{{AD}} = 0$ car les vecteurs $\\vec{{AB}}$ et $\\vec{{AD}}$ sont orthogonaux."
        ]
        ans2_en = [
            f"$\\vec{{AB}} \\cdot \\vec{{AD}} = 0$ because the vectors $\\vec{{AB}}$ and $\\vec{{AD}}$ are orthogonal."
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))

        # c) AD . CB
        q3_fr = ["c) Calculer le produit scalaire $\\vec{AD} \\cdot \\vec{CB}$."]
        q3_en = ["c) Calculate the dot product $\\vec{AD} \\cdot \\vec{CB}$."]
        insight3_fr = ["Les côtés opposés d'un carré sont parallèles et de même longueur. Remplacez $\\vec{CB}$ par un vecteur d'origine $A$."]
        insight3_en = ["Opposite sides of a square are parallel and of equal length. Replace $\\vec{CB}$ with a vector originating at $A$."]
        
        ans3 = -(side**2)
        
        ans3_fr = [
            f"Comme $\\vec{{CB}} = \\vec{{DA}}$, on a :",
            f"$\\vec{{AD}} \\cdot \\vec{{CB}} = \\vec{{AD}} \\cdot \\vec{{DA}} = -\\vec{{AD}} \\cdot \\vec{{AD}} = -||\\vec{{AD}}||^2 = -AD^2 = -{side}^2 = {ans3}$."
        ]
        ans3_en = [
            f"Since $\\vec{{CB}} = \\vec{{DA}}$, we have:",
            f"$\\vec{{AD}} \\cdot \\vec{{CB}} = \\vec{{AD}} \\cdot \\vec{{DA}} = -\\vec{{AD}} \\cdot \\vec{{AD}} = -||\\vec{{AD}}||^2 = -AD^2 = -{side}^2 = {ans3}$."
        ]
        self.questions.append(Question(q3_fr, q3_en, insight3_fr, insight3_en, ans3_fr, ans3_en))


# ==========================================
# MÉTHODE 2 : Appliquer l'égalité MA.MB = 0
# ==========================================
class DotProductCircle(BaseExercise):
    id = "PSCAL2_002"
    title = {"fr": "Égalité vectorielle et cercle", "en": "Vector equality and circle"}
    tags = ["produit scalaire", "cercle", "equation"]

    def generate(self):
        self.statement_fr = [
            "On donne deux points $A$ et $B$."
        ]
        self.statement_en = [
            "Two points $A$ and $B$ are given."
        ]

        q1_fr = ["Représenter l'ensemble des points $P$ tels que : $PB^2 = \\vec{AB} \\cdot \\vec{PB}$."]
        q1_en = ["Represent the set of points $P$ such that: $PB^2 = \\vec{AB} \\cdot \\vec{PB}$."]
        insight1_fr = ["Passez tout du même côté de l'égalité, factorisez par $\\vec{PB}$, puis utilisez la relation de Chasles dans la parenthèse."]
        insight1_en = ["Move everything to the same side of the equation, factor by $\\vec{PB}$, then use Chasles's relation inside the parentheses."]
        
        ans1_fr = [
            f"$PB^2 = \\vec{{AB}} \\cdot \\vec{{PB}}$",
            f"$PB^2 - \\vec{{AB}} \\cdot \\vec{{PB}} = 0$",
            f"$\\vec{{PB}} \\cdot \\vec{{PB}} - \\vec{{AB}} \\cdot \\vec{{PB}} = 0$",
            f"$\\vec{{PB}} \\cdot (\\vec{{PB}} - \\vec{{AB}}) = 0$",
            f"$\\vec{{PB}} \\cdot (\\vec{{PB}} + \\vec{{BA}}) = 0$",
            f"$\\vec{{PB}} \\cdot \\vec{{PA}} = 0$, d'après la relation de Chasles.",
            "L'ensemble des points $P$ est donc le **cercle de diamètre $[AB]$**."
        ]
        ans1_en = [
            f"$PB^2 = \\vec{{AB}} \\cdot \\vec{{PB}}$",
            f"$PB^2 - \\vec{{AB}} \\cdot \\vec{{PB}} = 0$",
            f"$\\vec{{PB}} \\cdot \\vec{{PB}} - \\vec{{AB}} \\cdot \\vec{{PB}} = 0$",
            f"$\\vec{{PB}} \\cdot (\\vec{{PB}} - \\vec{{AB}}) = 0$",
            f"$\\vec{{PB}} \\cdot (\\vec{{PB}} + \\vec{{BA}}) = 0$",
            f"$\\vec{{PB}} \\cdot \\vec{{PA}} = 0$, according to Chasles's relation.",
            "The set of points $P$ is therefore the **circle with diameter $[AB]$**."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 3 : Produit scalaire avec les coordonnées (1)
# ==========================================
class DotProductCoordinates1(BaseExercise):
    id = "PSCAL2_003"
    title = {"fr": "Calculer à l'aide des coordonnées (1)", "en": "Calculate using coordinates (1)"}
    tags = ["produit scalaire", "coordonnees", "vecteurs"]

    def generate(self):
        ux = self.rng.randint(-6, 6)
        uy = self.rng.randint(-6, 6)
        vx = self.rng.randint(-6, 6)
        vy = self.rng.randint(-6, 6)
        
        self.statement_fr = [
            f"Soit $\\vec{{u}} \\binom{{{ux}}}{{{uy}}}$ et $\\vec{{v}} \\binom{{{vx}}}{{{vy}}}$ deux vecteurs."
        ]
        self.statement_en = [
            f"Let $\\vec{{u}} \\binom{{{ux}}}{{{uy}}}$ and $\\vec{{v}} \\binom{{{vx}}}{{{vy}}}$ be two vectors."
        ]

        q1_fr = ["Calculer $\\vec{u} \\cdot \\vec{v}$."]
        q1_en = ["Calculate $\\vec{u} \\cdot \\vec{v}$."]
        insight1_fr = ["Utilisez la formule du produit scalaire dans un repère orthonormé : $xx' + yy'$."]
        insight1_en = ["Use the dot product formula in an orthonormal coordinate system: $xx' + yy'$."]
        
        dot_product = ux * vx + uy * vy
        
        vx_str = f"({vx})" if vx < 0 else str(vx)
        vy_str = f"({vy})" if vy < 0 else str(vy)
        uy_str = f"({uy})" if uy < 0 else str(uy)

        ans1_fr = [
            f"$\\vec{{u}} \\cdot \\vec{{v}} = {ux} \\times {vx_str} + {uy_str} \\times {vy_str}$",
            f"$= {ux * vx} + ({uy * vy})$",
            f"$= {dot_product}$"
        ]
        ans1_en = [
            f"$\\vec{{u}} \\cdot \\vec{{v}} = {ux} \\times {vx_str} + {uy_str} \\times {vy_str}$",
            f"$= {ux * vx} + ({uy * vy})$",
            f"$= {dot_product}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 4 : Produit scalaire avec les coordonnées (2)
# ==========================================
class DotProductCoordinates2(BaseExercise):
    id = "PSCAL2_004"
    title = {"fr": "Calculer à l'aide des coordonnées (2)", "en": "Calculate using coordinates (2)"}
    tags = ["produit scalaire", "coordonnees", "orthogonal"]

    def generate(self):
        # We generate a setup where two lines are perpendicular.
        # AB = (vx, vy), CD = (wx, wy) such that vx*wx + vy*wy = 0
        vx = self.rng.choice([2, 3, 4])
        vy = self.rng.choice([-2, 2, 4])
        
        wx = vy
        wy = -vx
        
        ax, ay = self.rng.randint(-2, 2), self.rng.randint(-2, 2)
        bx, by = ax + vx, ay + vy
        
        cx, cy = self.rng.randint(-3, 3), self.rng.randint(-3, 3)
        dx, dy = cx + wx, cy + wy

        self.statement_fr = [
            f"On considère quatre points $A({ax} ; {ay})$, $B({bx} ; {by})$, $C({cx} ; {cy})$ et $D({dx} ; {dy})$ dans un repère orthonormé."
        ]
        self.statement_en = [
            f"Consider four points $A({ax} ; {ay})$, $B({bx} ; {by})$, $C({cx} ; {cy})$ and $D({dx} ; {dy})$ in an orthonormal coordinate system."
        ]

        q1_fr = ["Démontrer que les droites $(AB)$ et $(CD)$ sont perpendiculaires."]
        q1_en = ["Prove that the lines $(AB)$ and $(CD)$ are perpendicular."]
        insight1_fr = ["Calculez les coordonnées des vecteurs $\\vec{AB}$ et $\\vec{CD}$, puis calculez leur produit scalaire $xx' + yy'$."]
        insight1_en = ["Calculate the coordinates of the vectors $\\vec{AB}$ and $\\vec{CD}$, then calculate their dot product $xx' + yy'$."]
        
        ans1_fr = [
            f"• Calculons les coordonnées des vecteurs $\\vec{{AB}}$ et $\\vec{{CD}}$ :",
            f"$\\vec{{AB}} \\binom{{ {bx} - ({ax}) }}{{ {by} - ({ay}) }} = \\binom{{{vx}}}{{{vy}}}$ et $\\vec{{CD}} \\binom{{ {dx} - ({cx}) }}{{ {dy} - ({cy}) }} = \\binom{{{wx}}}{{{wy}}}$",
            f"• Calculons le produit scalaire des deux vecteurs :",
            f"$\\vec{{AB}} \\cdot \\vec{{CD}} = ({vx}) \\times ({wx}) + ({vy}) \\times ({wy}) = {vx*wx} + {vy*wy} = 0$",
            f"• Le produit scalaire est nul donc les vecteurs $\\vec{{AB}}$ et $\\vec{{CD}}$ sont orthogonaux.",
            f"Et donc, les droites $(AB)$ et $(CD)$ sont perpendiculaires."
        ]
        ans1_en = [
            f"• Let's calculate the coordinates of the vectors $\\vec{{AB}}$ and $\\vec{{CD}}$:",
            f"$\\vec{{AB}} \\binom{{ {bx} - ({ax}) }}{{ {by} - ({ay}) }} = \\binom{{{vx}}}{{{vy}}}$ and $\\vec{{CD}} \\binom{{ {dx} - ({cx}) }}{{ {dy} - ({cy}) }} = \\binom{{{wx}}}{{{wy}}}$",
            f"• Let's calculate the dot product of the two vectors:",
            f"$\\vec{{AB}} \\cdot \\vec{{CD}} = ({vx}) \\times ({wx}) + ({vy}) \\times ({wy}) = {vx*wx} + {vy*wy} = 0$",
            f"• The dot product is zero, so the vectors $\\vec{{AB}}$ and $\\vec{{CD}}$ are orthogonal.",
            f"Therefore, the lines $(AB)$ and $(CD)$ are perpendicular."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 5 : Appliquer plusieurs formules pour un angle
# ==========================================
class DotProductAngleCoords(BaseExercise):
    id = "PSCAL2_005"
    title = {"fr": "Croiser les formules pour un angle", "en": "Combine formulas for an angle"}
    tags = ["produit scalaire", "angle", "coordonnees", "norme"]

    def generate(self):
        ax, ay = self.rng.choice([2, 3, 4]), self.rng.choice([1, 2])
        bx, by = self.rng.choice([-2, -1, 1, 2]), self.rng.choice([-3, -2, 3, 4])
        
        vec_u = np.array([ax, ay])
        vec_v = np.array([bx, by])
        
        dot_val = int(np.dot(vec_u, vec_v))
        while dot_val == 0 or (ax*by - ay*bx) == 0:
            ax, ay = self.rng.choice([2, 3, 4]), self.rng.choice([1, 2])
            bx, by = self.rng.choice([-2, -1, 1, 2]), self.rng.choice([-3, -2, 3, 4])
            vec_u = np.array([ax, ay])
            vec_v = np.array([bx, by])
            dot_val = int(np.dot(vec_u, vec_v))

        norm_u_sq = ax**2 + ay**2
        norm_v_sq = bx**2 + by**2
        
        cos_theta = dot_val / np.sqrt(norm_u_sq * norm_v_sq)
        angle_deg = round(np.degrees(np.arccos(cos_theta)), 1)
        
        fig, ax_plt = plt.subplots(figsize=(6, 5))
        ax_plt.plot([0, ax], [0, ay], marker='o', color='blue', label=f"A({ax}, {ay})")
        ax_plt.plot([0, bx], [0, by], marker='o', color='green', label=f"B({bx}, {by})")
        ax_plt.text(0, 0, "O", ha='right', va='top')
        ax_plt.axhline(0, color='black', linewidth=1)
        ax_plt.axvline(0, color='black', linewidth=1)
        ax_plt.grid(True, linestyle='--', alpha=0.7)
        
        max_limit = max(abs(ax), abs(ay), abs(bx), abs(by)) + 1
        ax_plt.set_xlim(-max_limit, max_limit)
        ax_plt.set_ylim(-max_limit, max_limit)
        ax_plt.legend()

        self.statement_fr = [
            f"On considère les points $A({ax} ; {ay})$ et $B({bx} ; {by})$ dans le repère orthonormé ci-dessous d'origine $O$.",
            fig
        ]
        self.statement_en = [
            f"Consider the points $A({ax} ; {ay})$ and $B({bx} ; {by})$ in the orthonormal coordinate system below with origin $O$.",
            fig
        ]

        q1_fr = ["Calculer la mesure de l'angle $\\widehat{AOB}$ au dixième de degré près en calculant le produit scalaire $\\vec{OA} \\cdot \\vec{OB}$ de deux façons."]
        q1_en = ["Calculate the measure of the angle $\\widehat{AOB}$ to the nearest tenth of a degree by calculating the dot product $\\vec{OA} \\cdot \\vec{OB}$ in two ways."]
        insight1_fr = ["Calculez le produit scalaire avec les coordonnées ($xx'+yy'$), puis exprimez-le avec la formule du cosinus pour isoler $\\cos(\\widehat{AOB})$."]
        insight1_en = ["Calculate the dot product with coordinates ($xx'+yy'$), then express it with the cosine formula to isolate $\\cos(\\widehat{AOB})$."]
        
        ans1_fr = [
            f"• En calculant le produit scalaire avec la formule des coordonnées :",
            f"$\\vec{{OA}} \\binom{{{ax}}}{{{ay}}}$ et $\\vec{{OB}} \\binom{{{bx}}}{{{by}}}$.",
            f"$\\vec{{OA}} \\cdot \\vec{{OB}} = {ax} \\times ({bx}) + {ay} \\times ({by}) = {ax*bx} + {ay*by} = {dot_val}$.",
            f"• En calculant le produit scalaire avec la formule du cosinus :",
            f"$\\vec{{OA}} \\cdot \\vec{{OB}} = OA \\times OB \\times \\cos(\\widehat{{AOB}})$.",
            f"Or : $OA = \\sqrt{{{ax}^2 + {ay}^2}} = \\sqrt{{{norm_u_sq}}}$ et $OB = \\sqrt{{{bx}^2 + {by}^2}} = \\sqrt{{{norm_v_sq}}}$.",
            f"Donc : $\\vec{{OA}} \\cdot \\vec{{OB}} = \\sqrt{{{norm_u_sq}}} \\times \\sqrt{{{norm_v_sq}}} \\times \\cos(\\widehat{{AOB}}) = \\sqrt{{{norm_u_sq * norm_v_sq}}} \\times \\cos(\\widehat{{AOB}})$.",
            f"• On a ainsi : $\\sqrt{{{norm_u_sq * norm_v_sq}}} \\times \\cos(\\widehat{{AOB}}) = {dot_val}$.",
            f"$\\cos(\\widehat{{AOB}}) = \\frac{{{dot_val}}}{{\\sqrt{{{norm_u_sq * norm_v_sq}}}}}$.",
            f"Et donc : $\\widehat{{AOB}} \\approx {angle_deg}^\\circ$."
        ]
        ans1_en = [
            f"• Calculating the dot product with the coordinates formula:",
            f"$\\vec{{OA}} \\binom{{{ax}}}{{{ay}}}$ and $\\vec{{OB}} \\binom{{{bx}}}{{{by}}}$.",
            f"$\\vec{{OA}} \\cdot \\vec{{OB}} = {ax} \\times ({bx}) + {ay} \\times ({by}) = {ax*bx} + {ay*by} = {dot_val}$.",
            f"• Calculating the dot product with the cosine formula:",
            f"$\\vec{{OA}} \\cdot \\vec{{OB}} = OA \\times OB \\times \\cos(\\widehat{{AOB}})$.",
            f"But: $OA = \\sqrt{{{ax}^2 + {ay}^2}} = \\sqrt{{{norm_u_sq}}}$ and $OB = \\sqrt{{{bx}^2 + {by}^2}} = \\sqrt{{{norm_v_sq}}}$.",
            f"Thus: $\\vec{{OA}} \\cdot \\vec{{OB}} = \\sqrt{{{norm_u_sq}}} \\times \\sqrt{{{norm_v_sq}}} \\times \\cos(\\widehat{{AOB}}) = \\sqrt{{{norm_u_sq * norm_v_sq}}} \\times \\cos(\\widehat{{AOB}})$.",
            f"• We therefore have: $\\sqrt{{{norm_u_sq * norm_v_sq}}} \\times \\cos(\\widehat{{AOB}}) = {dot_val}$.",
            f"$\\cos(\\widehat{{AOB}}) = \\frac{{{dot_val}}}{{\\sqrt{{{norm_u_sq * norm_v_sq}}}}}$.",
            f"And so: $\\widehat{{AOB}} \\approx {angle_deg}^\\circ$."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))
import sympy as sp
import numpy as np
import math
from exercises.base_exercise import BaseExercise
from exercises.question import Question

# Module-level registry key
CHAPTER = {"fr": "Produit Scalaire (Partie 1)", "en": "Dot Product (Part 1)"}

# ==========================================
# MÉTHODE 1 : Calculer avec la formule du cosinus
# ==========================================
class DotProductCosine(BaseExercise):
    id = "PSCAL1_001"
    title = {"fr": "Calculer avec le cosinus", "en": "Calculate with cosine"}
    tags = ["produit scalaire", "cosinus", "triangle"]

    def generate(self):
        # We pick an even side length so c/2 is an integer
        c = self.rng.choice([4, 6, 8, 10])
        
        self.statement_fr = [
            f"Soit un triangle équilatéral $ABC$ de côté {c}.",
            "Soit $I$ le milieu du segment $[AB]$."
        ]
        self.statement_en = [
            f"Let $ABC$ be an equilateral triangle with side {c}.",
            "Let $I$ be the midpoint of the segment $[AB]$."
        ]

        # Question a
        q1_fr = [f"a) Calculer le produit scalaire $\\vec{{AB}} \\cdot \\vec{{AC}}$."]
        q1_en = [f"a) Calculate the dot product $\\vec{{AB}} \\cdot \\vec{{AC}}$."]
        insight1_fr = ["Utilisez la formule $\\vec{u} \\cdot \\vec{v} = ||\\vec{u}|| \\times ||\\vec{v}|| \\times \\cos(\\theta)$. Dans un triangle équilatéral, les angles mesurent $\\frac{\\pi}{3}$ ($60^\\circ$)."]
        insight1_en = ["Use the formula $\\vec{u} \\cdot \\vec{v} = ||\\vec{u}|| \\times ||\\vec{v}|| \\times \\cos(\\theta)$. In an equilateral triangle, angles measure $\\frac{\\pi}{3}$ ($60^\\circ$)."]
        
        ans1_val = c * c * 0.5
        ans1_val_fmt = f"{int(ans1_val)}" if ans1_val.is_integer() else f"{ans1_val}"

        ans1_fr = [
            f"$\\vec{{AB}} \\cdot \\vec{{AC}} = AB \\times AC \\times \\cos(\\widehat{{BAC}})$",
            f"$= {c} \\times {c} \\times \\cos\\left(\\frac{{\\pi}}{{3}}\\right)$",
            f"$= {c*c} \\times 0,5 = {ans1_val_fmt}$"
        ]
        ans1_en = [
            f"$\\vec{{AB}} \\cdot \\vec{{AC}} = AB \\times AC \\times \\cos(\\widehat{{BAC}})$",
            f"$= {c} \\times {c} \\times \\cos\\left(\\frac{{\\pi}}{{3}}\\right)$",
            f"$= {c*c} \\times 0.5 = {ans1_val_fmt}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question b
        q2_fr = [f"b) Calculer le produit scalaire $\\vec{{AI}} \\cdot \\vec{{BC}}$."]
        q2_en = [f"b) Calculate the dot product $\\vec{{AI}} \\cdot \\vec{{BC}}$."]
        insight2_fr = ["Pour utiliser la formule avec l'angle, les deux vecteurs doivent avoir la même origine. Construisez un point $D$ tel que $\\vec{AD} = \\vec{BC}$."]
        insight2_en = ["To use the angle formula, both vectors must have the same origin. Construct a point $D$ such that $\\vec{AD} = \\vec{BC}$."]
        
        ai_len = c // 2
        ans2_val = ai_len * c * (-0.5)
        ans2_val_fmt = f"{int(ans2_val)}" if ans2_val.is_integer() else f"{ans2_val}"

        ans2_fr = [
            "On construit le point $D$ tel que $\\vec{AD} = \\vec{BC}$ pour avoir la même origine.",
            "L'angle $\\widehat{IAD}$ correspond à $\\pi - \\frac{\\pi}{3} = \\frac{2\\pi}{3}$.",
            f"$\\vec{{AI}} \\cdot \\vec{{BC}} = \\vec{{AI}} \\cdot \\vec{{AD}} = AI \\times AD \\times \\cos(\\widehat{{IAD}})$",
            f"$= {ai_len} \\times {c} \\times \\cos\\left(\\frac{{2\\pi}}{{3}}\\right)$",
            f"$= {ai_len * c} \\times (-0,5) = {ans2_val_fmt}$"
        ]
        ans2_en = [
            "We construct point $D$ such that $\\vec{AD} = \\vec{BC}$ to have the same origin.",
            "The angle $\\widehat{IAD}$ corresponds to $\\pi - \\frac{\\pi}{3} = \\frac{2\\pi}{3}$.",
            f"$\\vec{{AI}} \\cdot \\vec{{BC}} = \\vec{{AI}} \\cdot \\vec{{AD}} = AI \\times AD \\times \\cos(\\widehat{{IAD}})$",
            f"$= {ai_len} \\times {c} \\times \\cos\\left(\\frac{{2\\pi}}{{3}}\\right)$",
            f"$= {ai_len * c} \\times (-0.5) = {ans2_val_fmt}$"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 2 : Appliquer les propriétés
# ==========================================
class DotProductProperties(BaseExercise):
    id = "PSCAL1_002"
    title = {"fr": "Propriétés du produit scalaire", "en": "Dot product properties"}
    tags = ["produit scalaire", "proprietes", "identites remarquables"]

    def generate(self):
        norm_u = self.rng.randint(2, 5)
        norm_v = self.rng.randint(2, 5)
        dot_uv = self.rng.randint(-3, 3)

        self.statement_fr = [
            f"Soit $\\vec{{u}}$ et $\\vec{{v}}$ deux vecteurs de normes respectives $||\\vec{{u}}|| = {norm_u}$ et $||\\vec{{v}}|| = {norm_v}$.",
            f"On donne de plus : $\\vec{{u}} \\cdot \\vec{{v}} = {dot_uv}$."
        ]
        self.statement_en = [
            f"Let $\\vec{{u}}$ and $\\vec{{v}}$ be two vectors with norms $||\\vec{{u}}|| = {norm_u}$ and $||\\vec{{v}}|| = {norm_v}$ respectively.",
            f"We are also given: $\\vec{{u}} \\cdot \\vec{{v}} = {dot_uv}$."
        ]

        # a) (u+v).(u-v)
        q1_fr = ["a) Calculer $(\\vec{u} + \\vec{v}) \\cdot (\\vec{u} - \\vec{v})$."]
        q1_en = ["a) Calculate $(\\vec{u} + \\vec{v}) \\cdot (\\vec{u} - \\vec{v})$."]
        insight1_fr = ["Utilisez l'identité remarquable : $(\\vec{u} + \\vec{v}) \\cdot (\\vec{u} - \\vec{v}) = \\vec{u}^2 - \\vec{v}^2$."]
        insight1_en = ["Use the notable identity: $(\\vec{u} + \\vec{v}) \\cdot (\\vec{u} - \\vec{v}) = \\vec{u}^2 - \\vec{v}^2$."]
        
        ans1 = norm_u**2 - norm_v**2
        ans1_fr = [
            f"$(\\vec{{u}} + \\vec{{v}}) \\cdot (\\vec{{u}} - \\vec{{v}}) = \\vec{{u}}^2 - \\vec{{v}}^2$",
            f"$= ||\\vec{{u}}||^2 - ||\\vec{{v}}||^2$",
            f"$= {norm_u}^2 - {norm_v}^2 = {norm_u**2} - {norm_v**2} = {ans1}$"
        ]
        ans1_en = [
            f"$(\\vec{{u}} + \\vec{{v}}) \\cdot (\\vec{{u}} - \\vec{{v}}) = \\vec{{u}}^2 - \\vec{{v}}^2$",
            f"$= ||\\vec{{u}}||^2 - ||\\vec{{v}}||^2$",
            f"$= {norm_u}^2 - {norm_v}^2 = {norm_u**2} - {norm_v**2} = {ans1}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # b) u.(u+v)
        q2_fr = ["b) Calculer $\\vec{u} \\cdot (\\vec{u} + \\vec{v})$."]
        q2_en = ["b) Calculate $\\vec{u} \\cdot (\\vec{u} + \\vec{v})$."]
        insight2_fr = ["Développez en utilisant la bilinéarité : $\\vec{u} \\cdot \\vec{u} + \\vec{u} \\cdot \\vec{v}$."]
        insight2_en = ["Expand using bilinearity: $\\vec{u} \\cdot \\vec{u} + \\vec{u} \\cdot \\vec{v}$."]
        
        ans2 = norm_u**2 + dot_uv
        sign_dot = f"+ {dot_uv}" if dot_uv >= 0 else f"- {abs(dot_uv)}"

        ans2_fr = [
            f"$\\vec{{u}} \\cdot (\\vec{{u}} + \\vec{{v}}) = \\vec{{u}} \\cdot \\vec{{u}} + \\vec{{u}} \\cdot \\vec{{v}}$",
            f"$= ||\\vec{{u}}||^2 + \\vec{{u}} \\cdot \\vec{{v}}$",
            f"$= {norm_u}^2 {sign_dot} = {norm_u**2} {sign_dot} = {ans2}$"
        ]
        ans2_en = [
            f"$\\vec{{u}} \\cdot (\\vec{{u}} + \\vec{{v}}) = \\vec{{u}} \\cdot \\vec{{u}} + \\vec{{u}} \\cdot \\vec{{v}}$",
            f"$= ||\\vec{{u}}||^2 + \\vec{{u}} \\cdot \\vec{{v}}$",
            f"$= {norm_u}^2 {sign_dot} = {norm_u**2} {sign_dot} = {ans2}$"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))

        # c) -k v . (m u - v)
        k = self.rng.randint(2, 4)
        m = self.rng.randint(2, 4)
        q3_fr = [f"c) Calculer $-{k}\\vec{{v}} \\cdot ({m}\\vec{{u}} - \\vec{{v}})$."]
        q3_en = [f"c) Calculate $-{k}\\vec{{v}} \\cdot ({m}\\vec{{u}} - \\vec{{v}})$."]
        insight3_fr = ["Développez avec soin en respectant les règles des signes et la symétrie du produit scalaire ($\\vec{v} \\cdot \\vec{u} = \\vec{u} \\cdot \\vec{v}$)."]
        insight3_en = ["Expand carefully, respecting the rules of signs and the symmetry of the dot product ($\\vec{v} \\cdot \\vec{u} = \\vec{u} \\cdot \\vec{v}$)."]
        
        ans3 = (-k * m * dot_uv) + (k * norm_v**2)
        
        ans3_fr = [
            f"$-{k}\\vec{{v}} \\cdot ({m}\\vec{{u}} - \\vec{{v}}) = -{k*m}\\vec{{v}} \\cdot \\vec{{u}} + {k}\\vec{{v}} \\cdot \\vec{{v}}$",
            f"$= -{k*m}(\\vec{{u}} \\cdot \\vec{{v}}) + {k}||\\vec{{v}}||^2$",
            f"$= -{k*m} \\times ({dot_uv}) + {k} \\times {norm_v}^2$",
            f"$= {-k*m*dot_uv} + {k*norm_v**2} = {ans3}$"
        ]
        ans3_en = [
            f"$-{k}\\vec{{v}} \\cdot ({m}\\vec{{u}} - \\vec{{v}}) = -{k*m}\\vec{{v}} \\cdot \\vec{{u}} + {k}\\vec{{v}} \\cdot \\vec{{v}}$",
            f"$= -{k*m}(\\vec{{u}} \\cdot \\vec{{v}}) + {k}||\\vec{{v}}||^2$",
            f"$= -{k*m} \\times ({dot_uv}) + {k} \\times {norm_v}^2$",
            f"$= {-k*m*dot_uv} + {k*norm_v**2} = {ans3}$"
        ]
        self.questions.append(Question(q3_fr, q3_en, insight3_fr, insight3_en, ans3_fr, ans3_en))


# ==========================================
# MÉTHODE 3 : Calculer avec les normes
# ==========================================
class DotProductNorms(BaseExercise):
    id = "PSCAL1_003"
    title = {"fr": "Calculer avec les normes", "en": "Calculate with norms"}
    tags = ["produit scalaire", "normes", "formule"]

    def generate(self):
        # Generate valid triangle sides
        cg = self.rng.randint(4, 9)
        cf = self.rng.randint(4, 9)
        # Ensure triangle inequality: gf must be between |cg - cf| and cg + cf
        min_gf = abs(cg - cf) + 1
        max_gf = cg + cf - 1
        gf = self.rng.randint(min_gf, max_gf)

        self.statement_fr = [
            f"On considère un triangle $CGF$ tel que : $CG = {cg}$, $CF = {cf}$ et $GF = {gf}$."
        ]
        self.statement_en = [
            f"Consider a triangle $CGF$ such that: $CG = {cg}$, $CF = {cf}$ and $GF = {gf}$."
        ]

        q1_fr = ["Calculer le produit scalaire $\\vec{CG} \\cdot \\vec{CF}$."]
        q1_en = ["Calculate the dot product $\\vec{CG} \\cdot \\vec{CF}$."]
        insight1_fr = ["Utilisez la formule : $\\vec{AB} \\cdot \\vec{AC} = \\frac{1}{2}(AB^2 + AC^2 - BC^2)$."]
        insight1_en = ["Use the formula: $\\vec{AB} \\cdot \\vec{AC} = \\frac{1}{2}(AB^2 + AC^2 - BC^2)$."]
        
        sum_sq = cg**2 + cf**2 - gf**2
        ans = sum_sq / 2
        ans_fmt = f"{int(ans)}" if ans.is_integer() else f"{ans}"

        ans1_fr = [
            f"$\\vec{{CG}} \\cdot \\vec{{CF}} = \\frac{{1}}{{2}}(CG^2 + CF^2 - GF^2)$",
            f"$= \\frac{{1}}{{2}}({cg}^2 + {cf}^2 - {gf}^2)$",
            f"$= \\frac{{1}}{{2}}({cg**2} + {cf**2} - {gf**2})$",
            f"$= \\frac{{1}}{{2}} \\times {sum_sq} = {ans_fmt}$"
        ]
        ans1_en = [
            f"$\\vec{{CG}} \\cdot \\vec{{CF}} = \\frac{{1}}{{2}}(CG^2 + CF^2 - GF^2)$",
            f"$= \\frac{{1}}{{2}}({cg}^2 + {cf}^2 - {gf}^2)$",
            f"$= \\frac{{1}}{{2}}({cg**2} + {cf**2} - {gf**2})$",
            f"$= \\frac{{1}}{{2}} \\times {sum_sq} = {ans_fmt}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 4 : Al Kashi (Calculer une longueur)
# ==========================================
class AlKashiLength(BaseExercise):
    id = "PSCAL1_004"
    title = {"fr": "Al Kashi : Calculer une longueur", "en": "Al Kashi: Calculate a length"}
    tags = ["produit scalaire", "al kashi", "longueur", "triangle"]

    def generate(self):
        ab = self.rng.choice([4, 6, 8])
        ac = self.rng.choice([3, 5, 7, 9])
        # We use 60 degrees as in the lesson to have a clean cosine value (0.5)
        angle_deg = 60
        
        self.statement_fr = [
            f"On considère un triangle $ABC$ tel que $AB = {ab}$, $AC = {ac}$ et $\\widehat{{BAC}} = {angle_deg}^\\circ$."
        ]
        self.statement_en = [
            f"Consider a triangle $ABC$ such that $AB = {ab}$, $AC = {ac}$ and $\\widehat{{BAC}} = {angle_deg}^\\circ$."
        ]

        q1_fr = ["Calculer la longueur $BC$. On donnera une valeur exacte puis arrondie au dixième."]
        q1_en = ["Calculate the length $BC$. Give an exact value then round to one decimal place."]
        insight1_fr = ["Appliquez le théorème d'Al Kashi : $a^2 = b^2 + c^2 - 2bc \\cos(\\widehat{A})$."]
        insight1_en = ["Apply the Law of Cosines (Al Kashi): $a^2 = b^2 + c^2 - 2bc \\cos(\\widehat{A})$."]
        
        bc_sq = ab**2 + ac**2 - 2 * ab * ac * 0.5
        bc_sq_int = int(bc_sq)
        bc_val = math.sqrt(bc_sq)

        ans1_fr = [
            f"D'après le théorème d'Al Kashi, on a :",
            f"$BC^2 = AB^2 + AC^2 - 2 \\times AB \\times AC \\times \\cos(\\widehat{{BAC}})$",
            f"$BC^2 = {ab}^2 + {ac}^2 - 2 \\times {ab} \\times {ac} \\times \\cos({angle_deg}^\\circ)$",
            f"$BC^2 = {ab**2} + {ac**2} - {2 * ab * ac} \\times 0,5$",
            f"$BC^2 = {ab**2 + ac**2} - {int(ab * ac)} = {bc_sq_int}$",
            f"$BC = \\sqrt{{{bc_sq_int}}} \\approx {bc_val:.1f}$"
        ]
        ans1_en = [
            f"According to the Law of Cosines, we have:",
            f"$BC^2 = AB^2 + AC^2 - 2 \\times AB \\times AC \\times \\cos(\\widehat{{BAC}})$",
            f"$BC^2 = {ab}^2 + {ac}^2 - 2 \\times {ab} \\times {ac} \\times \\cos({angle_deg}^\\circ)$",
            f"$BC^2 = {ab**2} + {ac**2} - {2 * ab * ac} \\times 0.5$",
            f"$BC^2 = {ab**2 + ac**2} - {int(ab * ac)} = {bc_sq_int}$",
            f"$BC = \\sqrt{{{bc_sq_int}}} \\approx {bc_val:.1f}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 5 : Al Kashi (Calculer un angle)
# ==========================================
class AlKashiAngle(BaseExercise):
    id = "PSCAL1_005"
    title = {"fr": "Al Kashi : Calculer un angle", "en": "Al Kashi: Calculate an angle"}
    tags = ["produit scalaire", "al kashi", "angle", "triangle"]

    def generate(self):
        # We need a valid triangle that does not give a right angle or flat triangle.
        a = self.rng.choice([4, 5, 6, 7]) # BC
        b = self.rng.choice([5, 6, 7, 8]) # AC
        c = self.rng.choice([6, 7, 8, 9]) # AB
        
        # Enforce strict triangle inequality and non-degenerate combinations
        while not (a + b > c and a + c > b and b + c > a):
            a = self.rng.choice([4, 5, 6, 7])
            b = self.rng.choice([5, 6, 7, 8])
            c = self.rng.choice([6, 7, 8, 9])

        self.statement_fr = [
            f"On considère un triangle $ABC$ tel que $BC = {a}$, $AC = {b}$ et $AB = {c}$."
        ]
        self.statement_en = [
            f"Consider a triangle $ABC$ such that $BC = {a}$, $AC = {b}$ and $AB = {c}$."
        ]

        q1_fr = ["Calculer la mesure de l'angle $\\widehat{BAC}$ au degré près."]
        q1_en = ["Calculate the measure of the angle $\\widehat{BAC}$ to the nearest degree."]
        insight1_fr = ["Le théorème d'Al Kashi donne $BC^2 = AB^2 + AC^2 - 2 \\times AB \\times AC \\times \\cos(\\widehat{BAC})$. Isolez le $\\cos$."]
        insight1_en = ["The Law of Cosines gives $BC^2 = AB^2 + AC^2 - 2 \\times AB \\times AC \\times \\cos(\\widehat{BAC})$. Isolate the $\\cos$."]
        
        # a^2 = b^2 + c^2 - 2bc*cos(A)
        # 2bc*cos(A) = b^2 + c^2 - a^2
        # cos(A) = (b^2 + c^2 - a^2) / 2bc
        num = b**2 + c**2 - a**2
        den = 2 * b * c
        cos_A = num / den
        angle_rad = math.acos(cos_A)
        angle_deg = round(math.degrees(angle_rad))

        # Formatting a simplifiable fraction visually
        frac = sp.Rational(num, den)

        ans1_fr = [
            f"D'après le théorème d'Al Kashi, on a :",
            f"$BC^2 = AB^2 + AC^2 - 2 \\times AB \\times AC \\times \\cos(\\widehat{{BAC}})$",
            f"${a}^2 = {c}^2 + {b}^2 - 2 \\times {c} \\times {b} \\times \\cos(\\widehat{{BAC}})$",
            f"${a**2} = {c**2} + {b**2} - {den} \\cos(\\widehat{{BAC}})$",
            f"${den} \\cos(\\widehat{{BAC}}) = {c**2} + {b**2} - {a**2}$",
            f"${den} \\cos(\\widehat{{BAC}}) = {num}$",
            f"$\\cos(\\widehat{{BAC}}) = \\frac{{{num}}}{{{den}}} = {sp.latex(frac)}$",
            f"À l'aide de la calculatrice, on trouve $\\widehat{{BAC}} \\approx {angle_deg}^\\circ$."
        ]
        ans1_en = [
            f"According to the Law of Cosines, we have:",
            f"$BC^2 = AB^2 + AC^2 - 2 \\times AB \\times AC \\times \\cos(\\widehat{{BAC}})$",
            f"${a}^2 = {c}^2 + {b}^2 - 2 \\times {c} \\times {b} \\times \\cos(\\widehat{{BAC}})$",
            f"${a**2} = {c**2} + {b**2} - {den} \\cos(\\widehat{{BAC}})$",
            f"${den} \\cos(\\widehat{{BAC}}) = {c**2} + {b**2} - {a**2}$",
            f"${den} \\cos(\\widehat{{BAC}}) = {num}$",
            f"$\\cos(\\widehat{{BAC}}) = \\frac{{{num}}}{{{den}}} = {sp.latex(frac)}$",
            f"Using a calculator, we find $\\widehat{{BAC}} \\approx {angle_deg}^\\circ$."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))
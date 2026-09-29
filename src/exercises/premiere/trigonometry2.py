
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from exercises.base_exercise import BaseExercise
from exercises.question import Question

# Module-level registry key
CHAPTER = {"fr": "Trigonométrie (Partie 2)", "en": "Trigonometry (Part 2)"}

def _draw_trigo_circle(ax, points=None, show_references=False, proj_cos=False, proj_sin=False):
    """
    Helper function to draw a standard trigonometric circle with optional projections.
    points: list of dicts e.g., [{"angle": np.pi/4, "label": "A", "color": "green", "val_x": "...", "val_y": "..."}]
    """
    circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=1.2)
    ax.add_artist(circle)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Axes labels
    ax.text(1.2, 0, "cos", va='bottom', ha='left', fontsize=12)
    ax.text(0, 1.2, "sin", ha='left', va='bottom', fontsize=12)
    ax.text(1.05, -0.05, "1", va='top', ha='left')
    ax.text(-0.05, 1.05, "1", ha='right', va='bottom')
    ax.text(-1.05, -0.05, "-1", va='top', ha='right')
    ax.text(-0.05, -1.05, "-1", ha='right', va='top')
    ax.text(-0.05, -0.05, "O", ha='right', va='top')
    
    # Draw requested points and projections
    if points:
        for p in points:
            ang = p["angle"]
            x, y = np.cos(ang), np.sin(ang)
            col = p.get("color", "red")
            lab = p.get("label", "")
            
            # Point and radius
            ax.plot(x, y, marker='o', color=col, markersize=5)
            ax.plot([0, x], [0, y], color=col, linestyle='-')
            
            # Label
            if lab:
                ha = 'left' if x >= 0 else 'right'
                va = 'bottom' if y >= 0 else 'top'
                ax.text(x * 1.1, y * 1.1, lab, color=col, ha=ha, va=va, fontsize=12)
                
            # Projections
            if proj_cos:
                ax.plot([x, x], [0, y], color='blue', linestyle='--', alpha=0.6)
                ax.plot(x, 0, marker='x', color='blue')
                if "val_x" in p:
                    ax.text(x, -0.15 if y > 0 else 0.15, p["val_x"], color='blue', ha='center', va='center')
            if proj_sin:
                ax.plot([0, x], [y, y], color='red', linestyle='--', alpha=0.6)
                ax.plot(0, y, marker='x', color='red')
                if "val_y" in p:
                    ax.text(-0.15 if x > 0 else 0.15, y, p["val_y"], color='red', ha='center', va='center')


# ==========================================
# MÉTHODE 1 : Lire sur le cercle trigonométrique
# ==========================================
class ReadTrigoValues(BaseExercise):
    id = "TRIG2_001"
    title = {"fr": "Lire sur le cercle trigonométrique", "en": "Read on the trigonometric circle"}
    tags = ["trigonometrie", "cercle", "cosinus", "sinus", "symetrie"]

    def generate(self):
        # We define a map of reference angles and their exact cos/sin strings
        ref_angles = {
            (1, 6): (r"\frac{\sqrt{3}}{2}", r"\frac{1}{2}", np.pi/6),
            (1, 4): (r"\frac{\sqrt{2}}{2}", r"\frac{\sqrt{2}}{2}", np.pi/4),
            (1, 3): (r"\frac{1}{2}", r"\frac{\sqrt{3}}{2}", np.pi/3)
        }

        # Question a: Cosinus using symmetry relative to y-axis (ordonnées)
        q_a_ref = self.rng.choice(list(ref_angles.keys()))
        ref_cos, ref_sin, rad_val = ref_angles[q_a_ref]
        
        # Pick an angle in Q2 for symmetry
        num_a = q_a_ref[1] - 1
        den_a = q_a_ref[1]
        tex_a = f"\\frac{{{num_a}\\pi}}{{{den_a}}}"
        target_rad_a = num_a * np.pi / den_a
        
        # Question b: Sinus using symmetry relative to origin
        q_b_ref = self.rng.choice(list(ref_angles.keys()))
        ref_cos_b, ref_sin_b, rad_val_b = ref_angles[q_b_ref]
        
        # Pick an angle in Q3 for origin symmetry
        num_b = q_b_ref[1] + 1
        den_b = q_b_ref[1]
        tex_b = f"\\frac{{{num_b}\\pi}}{{{den_b}}}"
        target_rad_b = num_b * np.pi / den_b

        self.statement_fr = ["Déterminer la valeur exacte des expressions suivantes en utilisant les symétries du cercle trigonométrique :"]
        self.statement_en = ["Determine the exact value of the following expressions using the symmetries of the trigonometric circle:"]

        # Question A
        q1_fr = [f"a) $\\cos\\left({tex_a}\\right)$"]
        q1_en = [f"a) $\\cos\\left({tex_a}\\right)$"]
        insight1_fr = [f"Utilisez l'angle de référence dans le premier quart du cercle. Cherchez la symétrie par rapport à l'axe des ordonnées."]
        insight1_en = [f"Use the reference angle in the first quadrant. Look for the symmetry with respect to the y-axis."]
        
        fig_a, ax_a = plt.subplots(figsize=(4, 4))
        pts_a = [
            {"angle": rad_val, "label": f"$\\frac{{\\pi}}{{{den_a}}}$", "color": "red", "val_x": f"${ref_cos}$"},
            {"angle": target_rad_a, "label": f"${tex_a}$", "color": "red", "val_x": f"$-{ref_cos}$"}
        ]
        _draw_trigo_circle(ax_a, points=pts_a, proj_cos=True)

        ans1_fr = [
            f"On sait que $\\cos\\left(\\frac{{\\pi}}{{{den_a}}}\\right) = {ref_cos}$.",
            f"Par symétrie par rapport à l'axe des ordonnées, on en déduit que : $\\cos\\left({tex_a}\\right) = -{ref_cos}$.",
            fig_a
        ]
        ans1_en = [
            f"We know that $\\cos\\left(\\frac{{\\pi}}{{{den_a}}}\\right) = {ref_cos}$.",
            f"By symmetry with respect to the y-axis, we deduce that: $\\cos\\left({tex_a}\\right) = -{ref_cos}$.",
            fig_a
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question B
        q2_fr = [f"b) $\\sin\\left({tex_b}\\right)$"]
        q2_en = [f"b) $\\sin\\left({tex_b}\\right)$"]
        insight2_fr = [f"Utilisez l'angle de référence dans le premier quart du cercle. Cherchez la symétrie par rapport à l'origine $O$."]
        insight2_en = [f"Use the reference angle in the first quadrant. Look for the symmetry with respect to the origin $O$."]
        
        fig_b, ax_b = plt.subplots(figsize=(4, 4))
        pts_b = [
            {"angle": rad_val_b, "label": f"$\\frac{{\\pi}}{{{den_b}}}$", "color": "green", "val_y": f"${ref_sin_b}$"},
            {"angle": target_rad_b, "label": f"${tex_b}$", "color": "green", "val_y": f"$-{ref_sin_b}$"}
        ]
        _draw_trigo_circle(ax_b, points=pts_b, proj_sin=True)

        ans2_fr = [
            f"On sait que $\\sin\\left(\\frac{{\\pi}}{{{den_b}}}\\right) = {ref_sin_b}$.",
            f"Par symétrie par rapport à l'origine $O$, on en déduit que : $\\sin\\left({tex_b}\\right) = -{ref_sin_b}$.",
            fig_b
        ]
        ans2_en = [
            f"We know that $\\sin\\left(\\frac{{\\pi}}{{{den_b}}}\\right) = {ref_sin_b}$.",
            f"By symmetry with respect to the origin $O$, we deduce that: $\\sin\\left({tex_b}\\right) = -{ref_sin_b}$.",
            fig_b
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 2 : Résoudre une équation trigonométrique
# ==========================================
class SolveTrigoEquation(BaseExercise):
    id = "TRIG2_002"
    title = {"fr": "Résoudre une équation", "en": "Solve an equation"}
    tags = ["trigonometrie", "equation", "cosinus", "sinus", "intervalle"]

    def generate(self):
        # Definitions for Cosine targets
        cos_targets = [
            (r"\frac{\sqrt{3}}{2}", 1, 6),
            (r"\frac{1}{2}", 1, 3),
            (r"-\frac{1}{2}", 2, 3)
        ]
        cos_val, num_c, den_c = self.rng.choice(cos_targets)
        
        # Definitions for Sine targets
        sin_targets = [
            (r"-\frac{1}{2}", -1, 6),
            (r"-\frac{\sqrt{2}}{2}", -1, 4),
            (r"\frac{\sqrt{3}}{2}", 1, 3)
        ]
        sin_val, num_s, den_s = self.rng.choice(sin_targets)

        self.statement_fr = ["Dans chaque cas, déterminer la ou les valeurs de $x$ qui vérifient l'équation :"]
        self.statement_en = ["In each case, determine the value(s) of $x$ that satisfy the equation:"]

        # Question a: Cosine on [0, 2pi]
        q1_fr = [f"a) $\\cos(x) = {cos_val}$ avec $x \\in [0 ; 2\\pi]$"]
        q1_en = [f"a) $\\cos(x) = {cos_val}$ with $x \\in [0 ; 2\\pi]$"]
        insight1_fr = ["Tracez une droite verticale correspondant à l'abscisse donnée. Cherchez les deux intersections avec le cercle sur l'intervalle $[0 ; 2\\pi]$."]
        insight1_en = ["Draw a vertical line corresponding to the given abscissa. Find the two intersections with the circle on the interval $[0 ; 2\\pi]$."]
        
        # Calculate angles for cosine
        ang1_c = num_c * np.pi / den_c
        ang2_c = 2*np.pi - ang1_c
        num2_c = 2*den_c - num_c
        tex1_c = f"\\frac{{{num_c}\\pi}}{{{den_c}}}" if num_c != 1 else f"\\frac{{\\pi}}{{{den_c}}}"
        tex2_c = f"\\frac{{{num2_c}\\pi}}{{{den_c}}}"
        
        fig_c, ax_c = plt.subplots(figsize=(4, 4))
        pts_c = [
            {"angle": ang1_c, "label": f"${tex1_c}$", "color": "red"},
            {"angle": ang2_c, "label": f"${tex2_c}$", "color": "red"}
        ]
        _draw_trigo_circle(ax_c, points=pts_c)
        ax_c.plot([np.cos(ang1_c), np.cos(ang1_c)], [-1, 1], color='blue', linestyle='--', alpha=0.5)

        ans1_fr = [
            f"On sait que $\\cos\\left({tex1_c}\\right) = {cos_val}$.",
            f"Par symétrie par rapport à l'axe des abscisses, on a également $\\cos\\left({tex2_c}\\right) = {cos_val}$.",
            f"Les valeurs ${tex1_c}$ et ${tex2_c}$ conviennent car elles appartiennent à l'intervalle $[0 ; 2\\pi]$.",
            f"**$S = \\left\\{{ {tex1_c} ; {tex2_c} \\right\\}}$**",
            fig_c
        ]
        ans1_en = [
            f"We know that $\\cos\\left({tex1_c}\\right) = {cos_val}$.",
            f"By symmetry with respect to the x-axis, we also have $\\cos\\left({tex2_c}\\right) = {cos_val}$.",
            f"The values ${tex1_c}$ and ${tex2_c}$ are valid because they belong to the interval $[0 ; 2\\pi]$.",
            f"**$S = \\left\\{{ {tex1_c} ; {tex2_c} \\right\\}}$**",
            fig_c
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question b: Sine on [-pi, pi]
        q2_fr = [f"b) $\\sin(x) = {sin_val}$ avec $x \\in [-\\pi ; \\pi]$"]
        q2_en = [f"b) $\\sin(x) = {sin_val}$ with $x \\in [-\\pi ; \\pi]$"]
        insight2_fr = ["Tracez une droite horizontale correspondant à l'ordonnée donnée. Cherchez les deux intersections avec le cercle sur l'intervalle $[-\\pi ; \\pi]$."]
        insight2_en = ["Draw a horizontal line corresponding to the given ordinate. Find the two intersections with the circle on the interval $[-\\pi ; \\pi]$."]
        
        # Calculate angles for sine
        ang1_s = num_s * np.pi / den_s
        ang2_s = np.pi - ang1_s if num_s > 0 else -np.pi - ang1_s
        
        num1_str = f"{abs(num_s)}" if abs(num_s) != 1 else ""
        tex1_s = f"\\frac{{{num1_str}\\pi}}{{{den_s}}}"
        if num_s < 0: tex1_s = "-" + tex1_s
        
        num2_s = den_s - num_s if num_s > 0 else -den_s - num_s
        num2_str = f"{abs(num2_s)}" if abs(num2_s) != 1 else ""
        tex2_s = f"\\frac{{{num2_str}\\pi}}{{{den_s}}}"
        if num2_s < 0: tex2_s = "-" + tex2_s

        fig_s, ax_s = plt.subplots(figsize=(4, 4))
        pts_s = [
            {"angle": ang1_s, "label": f"${tex1_s}$", "color": "green"},
            {"angle": ang2_s, "label": f"${tex2_s}$", "color": "green"}
        ]
        _draw_trigo_circle(ax_s, points=pts_s)
        ax_s.plot([-1, 1], [np.sin(ang1_s), np.sin(ang1_s)], color='red', linestyle='--', alpha=0.5)

        ans2_fr = [
            f"On sait que $\\sin\\left({tex1_s}\\right) = {sin_val}$.",
            f"Par symétrie par rapport à l'axe des ordonnées, on a également $\\sin\\left({tex2_s}\\right) = {sin_val}$.",
            f"Les valeurs ${tex1_s}$ et ${tex2_s}$ conviennent car elles appartiennent à l'intervalle $[-\\pi ; \\pi]$.",
            f"**$S = \\left\\{{ {min(tex1_s, tex2_s)} ; {max(tex1_s, tex2_s)} \\right\\}}$**",
            fig_s
        ]
        ans2_en = [
            f"We know that $\\sin\\left({tex1_s}\\right) = {sin_val}$.",
            f"By symmetry with respect to the y-axis, we also have $\\sin\\left({tex2_s}\\right) = {sin_val}$.",
            f"The values ${tex1_s}$ and ${tex2_s}$ are valid because they belong to the interval $[-\\pi ; \\pi]$.",
            f"**$S = \\left\\{{ {min(tex1_s, tex2_s)} ; {max(tex1_s, tex2_s)} \\right\\}}$**",
            fig_s
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))
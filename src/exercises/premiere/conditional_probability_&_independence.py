import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from exercises.base_exercise import BaseExercise
from exercises.question import Question

# Module-level registry key
CHAPTER = {"fr": "Probabilités Conditionnelles", "en": "Conditional Probability"}

def _draw_2_level_tree(p_A, p_notA, p_B_A, p_notB_A, p_B_notA, p_notB_notA, label_A="A", label_B="B"):
    """Génère un arbre pondéré à 2 niveaux avec Matplotlib."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axis('off')

    x0, y0 = 0, 0.5
    x1_A, y1_A = 1, 0.8
    x1_notA, y1_notA = 1, 0.2
    
    x2_B_A, y2_B_A = 2, 0.95
    x2_notB_A, y2_notB_A = 2, 0.65
    x2_B_notA, y2_B_notA = 2, 0.35
    x2_notB_notA, y2_notB_notA = 2, 0.05
    
    # Nœuds du Niveau 1
    ax.text(x1_A, y1_A, f"${label_A}$", fontsize=14, va='center', ha='center')
    ax.text(x1_notA, y1_notA, f"$\\overline{{{label_A}}}$", fontsize=14, va='center', ha='center')
    
    # Nœuds du Niveau 2
    for y in [y2_B_A, y2_B_notA]:
        ax.text(x2_B_A, y, f"${label_B}$", fontsize=14, va='center', ha='center')
    for y in [y2_notB_A, y2_notB_notA]:
        ax.text(x2_B_A, y, f"$\\overline{{{label_B}}}$", fontsize=14, va='center', ha='center')

    # Arêtes L1
    ax.plot([x0, x1_A-0.1], [y0, y1_A], 'k-', lw=1.5)
    ax.plot([x0, x1_notA-0.1], [y0, y1_notA], 'k-', lw=1.5)
    ax.text(x0+0.5, (y0+y1_A)/2 + 0.05, str(p_A), fontsize=12, color='red', ha='center')
    ax.text(x0+0.5, (y0+y1_notA)/2 - 0.1, str(p_notA), fontsize=12, color='red', ha='center')
    
    # Arêtes L2
    ax.plot([x1_A+0.1, x2_B_A-0.1], [y1_A, y2_B_A], 'k-', lw=1.5)
    ax.plot([x1_A+0.1, x2_notB_A-0.1], [y1_A, y2_notB_A], 'k-', lw=1.5)
    ax.text(x1_A+0.5, (y1_A+y2_B_A)/2 + 0.05, str(p_B_A), fontsize=12, color='green', ha='center')
    ax.text(x1_A+0.5, (y1_A+y2_notB_A)/2 - 0.1, str(p_notB_A), fontsize=12, color='green', ha='center')

    ax.plot([x1_notA+0.1, x2_B_notA-0.1], [y1_notA, y2_B_notA], 'k-', lw=1.5)
    ax.plot([x1_notA+0.1, x2_notB_notA-0.1], [y1_notA, y2_notB_notA], 'k-', lw=1.5)
    ax.text(x1_notA+0.5, (y1_notA+y2_B_notA)/2 + 0.05, str(p_B_notA), fontsize=12, color='green', ha='center')
    ax.text(x1_notA+0.5, (y1_notA+y2_notB_notA)/2 - 0.1, str(p_notB_notA), fontsize=12, color='green', ha='center')
    
    ax.set_xlim(-0.2, 2.5)
    ax.set_ylim(-0.1, 1.1)
    return fig

def _draw_3_level_tree(p_S, p_notS, label="S"):
    """Génère un arbre pondéré à 3 niveaux pour une épreuve de Bernoulli."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('off')
    
    # Coordonnées (x, y)
    nodes = {
        'root': (0, 0.5),
        'S': (1, 0.85), 'S_bar': (1, 0.15),
        'SS': (2, 0.95), 'SS_bar': (2, 0.75), 'S_barS': (2, 0.25), 'S_barS_bar': (2, 0.05),
        'SSS': (3, 1.0), 'SSS_bar': (3, 0.9), 'SS_barS': (3, 0.8), 'SS_barS_bar': (3, 0.7),
        'S_barSS': (3, 0.3), 'S_barSS_bar': (3, 0.2), 'S_barS_barS': (3, 0.1), 'S_barS_barS_bar': (3, 0.0)
    }
    
    # Trace les lignes
    edges = [
        ('root', 'S', p_S), ('root', 'S_bar', p_notS),
        ('S', 'SS', p_S), ('S', 'SS_bar', p_notS), ('S_bar', 'S_barS', p_S), ('S_bar', 'S_barS_bar', p_notS),
        ('SS', 'SSS', p_S), ('SS', 'SSS_bar', p_notS), ('SS_bar', 'SS_barS', p_S), ('SS_bar', 'SS_barS_bar', p_notS),
        ('S_barS', 'S_barSS', p_S), ('S_barS', 'S_barSS_bar', p_notS), ('S_barS_bar', 'S_barS_barS', p_S), ('S_barS_bar', 'S_barS_barS_bar', p_notS)
    ]
    
    for start, end, prob in edges:
        x_start, y_start = nodes[start]
        x_end, y_end = nodes[end]
        ax.plot([x_start+0.1, x_end-0.1], [y_start, y_end], 'k-', lw=1)
        ax.text((x_start+x_end)/2, (y_start+y_end)/2 + 0.02, str(prob), fontsize=10, color='blue', ha='center', va='bottom')
    
    # Place les textes des nœuds
    for key, (x, y) in nodes.items():
        if key == 'root': continue
        text = f"${label}$" if not key.endswith('bar') else f"$\\overline{{{label}}}$"
        ax.text(x, y, text, fontsize=12, va='center', ha='center')
        
    ax.set_xlim(-0.2, 3.5)
    ax.set_ylim(-0.1, 1.1)
    return fig


# ==========================================
# MÉTHODE 1 : Probabilité avec un tableau
# ==========================================
class ConditionalProbTable(BaseExercise):
    id = "PROB_001"
    title = {"fr": "Calculer avec un tableau", "en": "Calculate using a table"}
    tags = ["probabilites", "tableau", "conditionnelle"]

    def generate(self):
        g_a = self.rng.randint(300, 450)
        g_b = self.rng.randint(200, 350)
        ng_a = self.rng.randint(40, 100)
        ng_b = self.rng.randint(30, 90)

        tot_g = g_a + g_b
        tot_ng = ng_a + ng_b
        tot_a = g_a + ng_a
        tot_b = g_b + ng_b
        total = tot_g + tot_ng

        table_md = (
            f"| | Médicament A | Médicament B | Total |\n"
            f"|---|---|---|---|\n"
            f"| **Guéri** | {g_a} | {g_b} | {tot_g} |\n"
            f"| **Non guéri** | {ng_a} | {ng_b} | {tot_ng} |\n"
            f"| **Total** | {tot_a} | {tot_b} | {total} |"
        )

        self.statement_fr = [
            "Un laboratoire a réalisé des tests sur des patients. Certains sont traités avec le médicament A, d'autres avec le B.",
            table_md,
            "On choisit au hasard un patient. Soit A : « Le patient a pris le médicament A » et G : « Le patient est guéri »."
        ]
        self.statement_en = [
            "A laboratory tested patients. Some were treated with drug A, others with drug B.",
            table_md,
            "A patient is chosen at random. Let A: 'The patient took drug A' and G: 'The patient is cured'."
        ]

        def fmt_prob(num, den):
            val = num / den
            pct = val * 100
            
            # Rounding for display
            val_round = round(val, 3)
            pct_round = round(pct, 1)
            
            is_exact = abs(val - val_round) < 1e-9
            sign = "=" if is_exact else "\\approx"
            
            val_str = f"{val_round:.3f}".rstrip('0').rstrip('.')
            pct_str = f"{pct_round:.1f}".rstrip('0').rstrip('.')
            
            return f"\\frac{{{num}}}{{{den}}} {sign} {val_str} = {pct_str}\\%"

        q1_fr = ["1) Calculer : a) $P(A)$ b) $P(G)$ c) $P(G \\cap A)$ d) $P(\\overline{G} \\cap A)$"]
        q1_en = ["1) Calculate: a) $P(A)$ b) $P(G)$ c) $P(G \\cap A)$ d) $P(\\overline{G} \\cap A)$"]
        insight1_fr = ["Utilisez les totaux du tableau divisés par le grand total pour les probabilités simples, et les cases internes pour les intersections."]
        insight1_en = ["Use the table totals divided by the grand total for simple probabilities, and the internal cells for intersections."]
        
        ans1_fr = [
            f"a) $P(A) = {fmt_prob(tot_a, total)}$",
            f"b) $P(G) = {fmt_prob(tot_g, total)}$",
            f"c) $P(G \\cap A) = {fmt_prob(g_a, total)}$",
            f"d) $P(\\overline{{G}} \\cap A) = {fmt_prob(ng_a, total)}$"
        ]
        ans1_en = [
            f"a) $P(A) = {fmt_prob(tot_a, total)}$",
            f"b) $P(G) = {fmt_prob(tot_g, total)}$",
            f"c) $P(G \\cap A) = {fmt_prob(g_a, total)}$",
            f"d) $P(\\overline{{G}} \\cap A) = {fmt_prob(ng_a, total)}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        q2_fr = [
            "2) a) On choisit un patient guéri. Calculer la probabilité qu'il ait pris le médicament A.",
            "b) On choisit un patient traité par B. Calculer la probabilité qu'il soit guéri."
        ]
        q2_en = [
            "2) a) A cured patient is chosen. Calculate the probability they took drug A.",
            "b) A patient treated with B is chosen. Calculate the probability they are cured."
        ]
        insight2_fr = ["Il s'agit de probabilités conditionnelles. Restreignez votre univers à la ligne ou la colonne concernée."]
        insight2_en = ["These are conditional probabilities. Restrict your sample space to the relevant row or column."]
        
        ans2_fr = [
            f"a) On regarde uniquement la ligne des guéris : $P_G(A) = {fmt_prob(g_a, tot_g)}$",
            f"b) On regarde uniquement la colonne du médicament B : $P_B(G) = {fmt_prob(g_b, tot_b)}$"
        ]
        ans2_en = [
            f"a) We only look at the row of cured patients: $P_G(A) = {fmt_prob(g_a, tot_g)}$",
            f"b) We only look at the column for drug B: $P_B(G) = {fmt_prob(g_b, tot_b)}$"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 2 : Calculer avec la formule
# ==========================================
class ConditionalProbFormula(BaseExercise):
    id = "PROB_002"
    title = {"fr": "Calculer à l'aide de la formule", "en": "Calculate using the formula"}
    tags = ["probabilites", "formule", "conditionnelle"]

    def generate(self):
        total_cards = self.rng.choice([32, 52])
        suits = 4
        suit_cards = total_cards // suits
        
        self.statement_fr = [
            f"On tire une carte au hasard dans un jeu de {total_cards} cartes.",
            "Soit A l'événement : « Le résultat est un pique ».",
            "Soit B l'événement : « Le résultat est un roi »."
        ]
        self.statement_en = [
            f"A card is drawn at random from a deck of {total_cards} cards.",
            "Let A be the event: 'The result is a spade'.",
            "Let B be the event: 'The result is a king'."
        ]

        q1_fr = ["Calculer $P_A(B)$, la probabilité que le résultat soit un roi sachant qu'on a tiré un pique."]
        q1_en = ["Calculate $P_A(B)$, the probability that the result is a king given that a spade was drawn."]
        insight1_fr = ["Utilisez la formule $P_A(B) = \\frac{P(A \\cap B)}{P(A)}$."]
        insight1_en = ["Use the formula $P_A(B) = \\frac{P(A \\cap B)}{P(A)}$."]
        ans1_fr = [
            f"$P(A) = \\frac{{{suit_cards}}}{{{total_cards}}} = \\frac{{1}}{{4}}$ et $P(A \\cap B) = \\frac{{1}}{{{total_cards}}}$.",
            f"Donc $P_A(B) = \\frac{{P(A \\cap B)}}{{P(A)}} = \\frac{{1/{total_cards}}}{{1/4}} = \\frac{{1}}{{{suit_cards}}}$."
        ]
        ans1_en = [
            f"$P(A) = \\frac{{{suit_cards}}}{{{total_cards}}} = \\frac{{1}}{{4}}$ and $P(A \\cap B) = \\frac{{1}}{{{total_cards}}}$.",
            f"Thus $P_A(B) = \\frac{{P(A \\cap B)}}{{P(A)}} = \\frac{{1/{total_cards}}}{{1/4}} = \\frac{{1}}{{{suit_cards}}}$."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 3 : Construire un arbre pondéré
# ==========================================
class WeightedTreeConstruct(BaseExercise):
    id = "PROB_003"
    title = {"fr": "Construire un arbre pondéré", "en": "Construct a weighted tree"}
    tags = ["probabilites", "arbre", "noeuds"]

    def generate(self):
        # On génère les 3 probabilités données dans le PDF (une pour la racine, deux pour les branches)
        p_notA = round(self.rng.uniform(0.2, 0.8), 2)
        p_notB_given_A = round(self.rng.uniform(0.2, 0.8), 2)
        p_B_given_notA = round(self.rng.uniform(0.2, 0.8), 2)

        # Calcul des compléments (qui seront les réponses de la question b)
        p_A = round(1 - p_notA, 2)
        p_B_given_A = round(1 - p_notB_given_A, 2)
        p_notB_given_notA = round(1 - p_B_given_notA, 2)

        # L'arbre de l'énoncé ne contient que les 3 données initiales
        tree_stmt = _draw_2_level_tree("?", p_notA, "?", p_notB_given_A, p_B_given_notA, "?", "A", "B")

        self.statement_fr = [
            "On donne l'arbre pondéré ci-dessous.",
            tree_stmt
        ]
        self.statement_en = [
            "The weighted tree below is given.",
            tree_stmt
        ]

        # Question a : Traduire les données
        q1_fr = ["Traduire les données de l'arbre sous forme de probabilités."]
        q1_en = ["Translate the tree data into probabilities."]
        insight1_fr = ["Lisez directement les valeurs écrites sur les branches de l'arbre."]
        insight1_en = ["Read the values directly written on the branches of the tree."]
        
        ans1_fr = [
            f"$P(\\overline{{A}}) = {p_notA}$",
            f"$P_A(\\overline{{B}}) = {p_notB_given_A}$",
            f"$P_{{\\overline{{A}}}}(B) = {p_B_given_notA}$"
        ]
        ans1_en = [
            f"$P(\\overline{{A}}) = {p_notA}$",
            f"$P_A(\\overline{{B}}) = {p_notB_given_A}$",
            f"$P_{{\\overline{{A}}}}(B) = {p_B_given_notA}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question b : Calculer le reste
        q2_fr = ["À l'aide de l'arbre, calculer $P(A)$, $P_{\\overline{A}}(\\overline{B})$ et $P(A \\cap \\overline{B})$."]
        q2_en = ["Using the tree, calculate $P(A)$, $P_{\\overline{A}}(\\overline{B})$ and $P(A \\cap \\overline{B})$."]
        insight2_fr = ["La somme des branches issues d'un même nœud vaut 1. Pour l'intersection, multipliez le chemin."]
        insight2_en = ["The sum of branches from the same node is 1. For the intersection, multiply the path."]
        
        intersect = round(p_A * p_notB_given_A, 4)
        
        # L'arbre complété pour la solution
        tree_sol = _draw_2_level_tree(p_A, p_notA, p_B_given_A, p_notB_given_A, p_B_given_notA, p_notB_given_notA, "A", "B")

        ans2_fr = [
            f"$P(A) = 1 - P(\\overline{{A}}) = 1 - {p_notA} = {p_A}$",
            f"$P_{{\\overline{{A}}}}(\\overline{{B}}) = 1 - P_{{\\overline{{A}}}}(B) = 1 - {p_B_given_notA} = {p_notB_given_notA}$",
            f"$P(A \\cap \\overline{{B}}) = P(A) \\times P_A(\\overline{{B}}) = {p_A} \\times {p_notB_given_A} = {intersect}$",
            tree_sol
        ]
        ans2_en = [
            f"$P(A) = 1 - P(\\overline{{A}}) = 1 - {p_notA} = {p_A}$",
            f"$P_{{\\overline{{A}}}}(\\overline{{B}}) = 1 - P_{{\\overline{{A}}}}(B) = 1 - {p_B_given_notA} = {p_notB_given_notA}$",
            f"$P(A \\cap \\overline{{B}}) = P(A) \\times P_A(\\overline{{B}}) = {p_A} \\times {p_notB_given_A} = {intersect}$",
            tree_sol
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 4 : Formule des probabilités totales
# ==========================================
class TotalProbability(BaseExercise):
    id = "PROB_004"
    title = {"fr": "Probabilités totales", "en": "Law of total probability"}
    tags = ["probabilites", "totales", "arbre"]

    def generate(self):
        p_M = round(self.rng.uniform(0.01, 0.05), 3)
        p_T_given_M = round(self.rng.uniform(0.80, 0.95), 2)
        p_notT_given_notM = round(self.rng.uniform(0.90, 0.99), 2)
        p_notM = round(1 - p_M, 3)
        p_T_given_notM = round(1 - p_notT_given_notM, 2)
        p_notT_given_M = round(1 - p_T_given_M, 2)

        tree_fig = _draw_2_level_tree(p_M, p_notM, p_T_given_M, p_notT_given_M, p_T_given_notM, p_notT_given_notM, "M", "T")

        self.statement_fr = [
            "Un test de dépistage est mis au point pour une maladie.",
            f"- {p_M*100}% de la population est porteuse de la maladie.",
            f"- Si un individu est malade, le test est positif dans {p_T_given_M*100}% des cas.",
            f"- Si un individu est sain, le test est négatif dans {p_notT_given_notM*100}% des cas.",
            "On note M : « Être malade » et T : « Avoir un test positif ».",
            tree_fig
        ]
        self.statement_en = [
            "A screening test is developed for a disease.",
            f"- {p_M*100}% of the population carries the disease.",
            f"- If an individual is sick, the test is positive in {p_T_given_M*100}% of cases.",
            f"- If an individual is healthy, the test is negative in {p_notT_given_notM*100}% of cases.",
            "Let M: 'Being sick' and T: 'Having a positive test'.",
            tree_fig
        ]

        q1_fr = ["Quelle est la probabilité que le test d'un individu choisi au hasard soit positif ?"]
        q1_en = ["What is the probability that a randomly chosen individual's test is positive?"]
        insight1_fr = ["Utilisez la formule des probabilités totales : $P(T) = P(M \\cap T) + P(\\overline{M} \\cap T)$."]
        insight1_en = ["Use the law of total probability: $P(T) = P(M \\cap T) + P(\\overline{M} \\cap T)$."]
        
        p_T = round(p_M * p_T_given_M + p_notM * p_T_given_notM, 5)

        ans1_fr = [
            "D'après la formule des probabilités totales :",
            f"$P(T) = P(M \\cap T) + P(\\overline{{M}} \\cap T)$",
            f"$= P(M) \\times P_M(T) + P(\\overline{{M}}) \\times P_{{\\overline{{M}}}}(T)$",
            f"$= {p_M} \\times {p_T_given_M} + {p_notM} \\times {p_T_given_notM} = {p_T}$"
        ]
        ans1_en = [
            "According to the law of total probability:",
            f"$P(T) = P(M \\cap T) + P(\\overline{{M}} \\cap T)$",
            f"$= P(M) \\times P_M(T) + P(\\overline{{M}}) \\times P_{{\\overline{{M}}}}(T)$",
            f"$= {p_M} \\times {p_T_given_M} + {p_notM} \\times {p_T_given_notM} = {p_T}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        q2_fr = ["Si le test est positif, quelle est la probabilité que l'individu soit malade ?"]
        q2_en = ["If the test is positive, what is the probability that the individual is sick?"]
        insight2_fr = ["Calculez $P_T(M)$ en utilisant la définition d'une probabilité conditionnelle."]
        insight2_en = ["Calculate $P_T(M)$ using the definition of a conditional probability."]
        
        p_M_given_T = round((p_M * p_T_given_M) / p_T, 4)

        ans2_fr = [
            f"$P_T(M) = \\frac{{P(T \\cap M)}}{{P(T)}} = \\frac{{{p_M} \\times {p_T_given_M}}}{{{p_T}}} \\approx {p_M_given_T}$"
        ]
        ans2_en = [
            f"$P_T(M) = \\frac{{P(T \\cap M)}}{{P(T)}} = \\frac{{{p_M} \\times {p_T_given_M}}}{{{p_T}}} \\approx {p_M_given_T}$"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 5 : Démontrer l'indépendance
# ==========================================
class ProveIndependence(BaseExercise):
    id = "PROB_005"
    title = {"fr": "Démontrer l'indépendance", "en": "Prove independence"}
    tags = ["probabilites", "independance", "intersection"]

    def generate(self):
        # Paramètres pour coller à la structure a) sans jokers, b) avec jokers
        jokers = self.rng.choice([2, 4])
        total_cards_a = 32
        total_cards_b = 32 + jokers
        suits = 4
        kings = 4
        
        suit_cards_a = total_cards_a // suits
        
        self.statement_fr = []
        self.statement_en = []

        # Question a
        q1_fr = [
            f"On tire une carte au hasard dans un jeu de {total_cards_a} cartes.",
            "Soit R l'événement : « On tire un roi ».",
            "Soit T l'événement : « On tire un trèfle ».",
            "Les événements R et T sont-ils indépendants ?"
        ]
        q1_en = [
            f"A card is drawn at random from a deck of {total_cards_a} cards.",
            "Let R be the event: 'A king is drawn'.",
            "Let T be the event: 'A club is drawn'.",
            "Are events R and T independent?"
        ]
        insight1_fr = ["Calculez $P(R) \\times P(T)$ et comparez le résultat à $P(R \\cap T)$."]
        insight1_en = ["Calculate $P(R) \\times P(T)$ and compare the result to $P(R \\cap T)$."]
        
        p_R_a = sp.Rational(kings, total_cards_a)
        p_T_a = sp.Rational(suit_cards_a, total_cards_a)
        p_R_and_T_a = sp.Rational(1, total_cards_a)
        product_a = p_R_a * p_T_a

        ans1_fr = [
            f"On a : $P(R) = \\frac{{{kings}}}{{{total_cards_a}}} = {sp.latex(p_R_a)}$ et $P(T) = \\frac{{{suit_cards_a}}}{{{total_cards_a}}} = {sp.latex(p_T_a)}$.",
            f"Donc $P(R) \\times P(T) = {sp.latex(p_R_a)} \\times {sp.latex(p_T_a)} = {sp.latex(product_a)}$.",
            f"D'autre part, $P(R \\cap T) = {sp.latex(p_R_and_T_a)}$.",
            "Puisque $P(R) \\times P(T) = P(R \\cap T)$, les événements R et T sont indépendants."
        ]
        ans1_en = [
            f"We have: $P(R) = \\frac{{{kings}}}{{{total_cards_a}}} = {sp.latex(p_R_a)}$ and $P(T) = \\frac{{{suit_cards_a}}}{{{total_cards_a}}} = {sp.latex(p_T_a)}$.",
            f"Thus $P(R) \\times P(T) = {sp.latex(p_R_a)} \\times {sp.latex(p_T_a)} = {sp.latex(product_a)}$.",
            f"On the other hand, $P(R \\cap T) = {sp.latex(p_R_and_T_a)}$.",
            "Since $P(R) \\times P(T) = P(R \\cap T)$, events R and T are independent."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))

        # Question b
        q2_fr = [
            f"On reprend l'expérience précédente en ajoutant {jokers} jokers au jeu de cartes.",
            "Les événements R et T sont-ils indépendants ?"
        ]
        q2_en = [
            f"We repeat the previous experiment by adding {jokers} jokers to the deck.",
            "Are events R and T independent?"
        ]
        insight2_fr = ["Recommencez les calculs avec le nouveau nombre total de cartes. Le nombre de rois et de trèfles ne change pas."]
        insight2_en = ["Repeat the calculations with the new total number of cards. The number of kings and clubs does not change."]
        
        p_R_b = sp.Rational(kings, total_cards_b)
        p_T_b = sp.Rational(suit_cards_a, total_cards_b)
        p_R_and_T_b = sp.Rational(1, total_cards_b)
        product_b = p_R_b * p_T_b

        ans2_fr = [
            f"On a : $P(R) = \\frac{{{kings}}}{{{total_cards_b}}} = {sp.latex(p_R_b)}$ et $P(T) = \\frac{{{suit_cards_a}}}{{{total_cards_b}}} = {sp.latex(p_T_b)}$.",
            f"Donc $P(R) \\times P(T) = {sp.latex(p_R_b)} \\times {sp.latex(p_T_b)} = {sp.latex(product_b)}$.",
            f"Or, $P(R \\cap T) = {sp.latex(p_R_and_T_b)}$.",
            "Puisque $P(R) \\times P(T) \\neq P(R \\cap T)$, les événements R et T ne sont plus indépendants."
        ]
        ans2_en = [
            f"We have: $P(R) = \\frac{{{kings}}}{{{total_cards_b}}} = {sp.latex(p_R_b)}$ and $P(T) = \\frac{{{suit_cards_a}}}{{{total_cards_b}}} = {sp.latex(p_T_b)}$.",
            f"Thus $P(R) \\times P(T) = {sp.latex(p_R_b)} \\times {sp.latex(p_T_b)} = {sp.latex(product_b)}$.",
            f"However, $P(R \\cap T) = {sp.latex(p_R_and_T_b)}$.",
            "Since $P(R) \\times P(T) \\neq P(R \\cap T)$, events R and T are no longer independent."
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))


# ==========================================
# MÉTHODE 6 : Utiliser l'indépendance (Union)
# ==========================================
class UseIndependenceUnion(BaseExercise):
    id = "PROB_006"
    title = {"fr": "Utiliser l'indépendance (Union)", "en": "Use independence (Union)"}
    tags = ["probabilites", "independance", "union"]

    def generate(self):
        p_M = round(self.rng.uniform(0.005, 0.05), 3)
        p_N = round(self.rng.uniform(0.01, 0.08), 3)

        self.statement_fr = [
            f"Dans une populatino, Un individu est atteint par la maladie $m$ avec une probabilité de $P(M) = {p_M}$ et par la maladie $n$ avec $P(N) = {p_N}$.",
            f"On choisit au hasard un individu de cette population. ",
            f"Soit M l'événement : « L'individu a la maladie m ». ",
            f"Soit N l'événement : « L'individu a la maladie n ». ",
            "On suppose que les événements M et N sont indépendants."
        ]
        self.statement_en = [
            f"In a population, an individual is affected by disease $m$ with probability $P(M) = {p_M}$ and disease $n$ with $P(N) = {p_N}$.",
            "A randomly chosen individual from this population is selected.",
            f"Let M be the event: 'The individual has disease m'.",
            f"Let N be the event: 'The individual has disease n'.",
            "Assume events M and N are independent."
        ]

        q1_fr = ["Calculer la probabilité que l'individu ait au moins une des deux maladies."]
        q1_en = ["Calculate the probability that the individual has at least one of the two diseases."]
        insight1_fr = ["« Au moins une » correspond à l'union $M \\cup N$. Utilisez $P(M \\cup N) = P(M) + P(N) - P(M \\cap N)$ et l'indépendance pour l'intersection."]
        insight1_en = ["'At least one' corresponds to the union $M \\cup N$. Use $P(M \\cup N) = P(M) + P(N) - P(M \\cap N)$ and independence for the intersection."]
        
        p_union_raw = p_M + p_N - (p_M * p_N)

        p_union_val = round(p_union_raw, 4)
        p_union_pct = round(p_union_raw * 100, 1)

        is_exact = abs(p_union_raw - p_union_val) < 1e-9
        sign = "=" if is_exact else "\\approx"

        val_str = f"{p_union_val:.4f}".rstrip('0').rstrip('.')
        pct_str = f"{p_union_pct:.1f}".rstrip('0').rstrip('.')

        p_union_display = f"{sign} {val_str} = {pct_str}\\%"

        ans1_fr = [
            f"$P(M \\cup N) = P(M) + P(N) - P(M \\cap N)$",
            f"$= P(M) + P(N) - P(M) \\times P(N)$ car les événements sont indépendants.",
            f"$= {p_M} + {p_N} - {p_M} \\times {p_N} {p_union_display}$"
        ]
        ans1_en = [
            f"$P(M \\cup N) = P(M) + P(N) - P(M \\cap N)$",
            f"$= P(M) + P(N) - P(M) \\times P(N)$ because the events are independent.",
            f"$= {p_M} + {p_N} - {p_M} \\times {p_N} {p_union_display}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 7 : Utiliser l'indépendance (Complémentaire)
# ==========================================
class UseIndependenceComplement(BaseExercise):
    id = "PROB_007"
    title = {"fr": "Utiliser l'indépendance (Contraire)", "en": "Use independence (Complement)"}
    tags = ["probabilites", "independance", "contraire"]

    def generate(self):
        p_A = round(self.rng.uniform(0.30, 0.70), 2)
        p_B = round(self.rng.uniform(0.30, 0.70), 2)

        self.statement_fr = [
            f"Le risque de bouchon est de {int(p_A*100)}% sur l'autoroute A6 (événement A) et de {int(p_B*100)}% sur l'autoroute A7 (événement B).",
            "On suppose que les événements A et B sont indépendants."
        ]
        self.statement_en = [
            f"The risk of a traffic jam is {int(p_A*100)}% on highway A6 (event A) and {int(p_B*100)}% on highway A7 (event B).",
            "Assume events A and B are independent."
        ]

        q1_fr = ["Calculer la probabilité de tomber dans un bouchon sur l'A7 mais pas sur l'A6."]
        q1_en = ["Calculate the probability of hitting a traffic jam on A7 but not on A6."]
        insight1_fr = ["Si A et B sont indépendants, alors $\\overline{A}$ et B le sont aussi. On cherche $P(\\overline{A} \\cap B)$."]
        insight1_en = ["If A and B are independent, then $\\overline{A}$ and B are too. We want $P(\\overline{A} \\cap B)$."]
        
        p_notA = round(1 - p_A, 2)
        # 1. Calculate the raw float
        ans_raw = p_notA * p_B

        # 2. Round for display
        ans_val = round(ans_raw, 4)
        ans_pct = round(ans_raw * 100, 1)

        # 3. Determine if the rounding altered the value
        is_exact = abs(ans_raw - ans_val) < 1e-9
        sign = "=" if is_exact else "\\approx"

        # 4. Strip trailing zeros for a clean mathematical output
        val_str = f"{ans_val:.4f}".rstrip('0').rstrip('.')
        pct_str = f"{ans_pct:.1f}".rstrip('0').rstrip('.')

        # 5. Final formatted string to inject into your answer list
        ans_display = f"{sign} {val_str} = {pct_str}\\%"

        ans1_fr = [
            f"L'événement cherché est $\\overline{{A}} \\cap B$.",
            f"Les événements A et B sont indépendants, donc $\\overline{{A}}$ et B le sont aussi.",
            f"$P(\\overline{{A}} \\cap B) = P(\\overline{{A}}) \\times P(B) = (1 - {p_A}) \\times {p_B}$",
            f"$= {p_notA} \\times {p_B} {ans_display}$"
        ]
        ans1_en = [
            f"The event we want is $\\overline{{A}} \\cap B$.",
            f"Events A and B are independent, so $\\overline{{A}}$ and B are as well.",
            f"$P(\\overline{{A}} \\cap B) = P(\\overline{{A}}) \\times P(B) = (1 - {p_A}) \\times {p_B}$",
            f"$= {p_notA} \\times {p_B} {ans_display}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 8 : Répétition d'expériences (2)
# ==========================================
class TwoExperiments(BaseExercise):
    id = "PROB_008"
    title = {"fr": "Succession de 2 épreuves", "en": "Succession of 2 trials"}
    tags = ["probabilites", "repetition", "independance"]

    def generate(self):
        b = self.rng.randint(2, 5)
        r = self.rng.randint(2, 5)
        total = b + r

        p_B_frac = sp.Rational(b, total)
        p_R_frac = sp.Rational(r, total)
        
        tree_fig = _draw_2_level_tree(p_B_frac, p_R_frac, p_B_frac, p_R_frac, p_B_frac, p_R_frac, "B", "B")

        self.statement_fr = [
            f"Une urne contient {b} boules blanches (B) et {r} boules rouges (R).",
            "On tire au hasard une boule et on la remet dans l'urne. On répète l'expérience deux fois de suite."
        ]
        self.statement_en = [
            f"An urn contains {b} white balls (B) and {r} red balls (R).",
            "A ball is drawn at random and replaced. The experiment is repeated twice in a row."
        ]

        # Question 1
        q1_fr = ["Représenter l'ensemble des issues de ces expériences dans un arbre."]
        q1_en = ["Represent all the outcomes of these experiments in a tree diagram."]

        insight1_fr = ["L'expérience compte deux tirages, votre arbre aura donc deux niveaux. Puisque le tirage se fait avec remise, les probabilités sur les branches restent identiques au deuxième niveau."]
        insight1_en = ["The experiment involves two draws, so your tree needs two levels. Since the draw is with replacement, the probabilities on the branches remain exactly the same on the second level."]

        ans1_fr = [tree_fig]
        ans1_en = [tree_fig]

        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


        # Question 2
        # Question a
        q2_fr = ["a) Déterminer la probabilité d'obtenir deux boules blanches."]
        q2_en = ["a) Determine the probability of obtaining two white balls."]
        insight2_fr = ["Les tirages sont avec remise, ils sont donc indépendants. Multipliez les probabilités : $P(B) \\times P(B)$."]
        insight2_en = ["Draws are with replacement, so they are independent. Multiply the probabilities: $P(B) \\times P(B)$."]
        
        ans2 = p_B_frac * p_B_frac

        ans2_fr = [
            f"Obtenir deux boules blanches correspond à l'issue (B ; B).",
            f"$P = P(B) \\times P(B) = {sp.latex(p_B_frac)} \\times {sp.latex(p_B_frac)} = {sp.latex(ans2)}$"
        ]
        ans2_en = [
            f"Obtaining two white balls corresponds to the outcome (B ; B).",
            f"$P = P(B) \\times P(B) = {sp.latex(p_B_frac)} \\times {sp.latex(p_B_frac)} = {sp.latex(ans2)}$"
        ]
        self.questions.append(Question(q2_fr, q2_en, insight2_fr, insight2_en, ans2_fr, ans2_en))

        # Question b
        q3_fr = ["b) Déterminer la probabilité d'obtenir une boule blanche et une boule rouge."]
        q3_en = ["b) Determine the probability of obtaining one white ball and one red ball."]
        insight3_fr = ["Il y a deux chemins possibles : (B puis R) OU (R puis B). Additionnez leurs probabilités."]
        insight3_en = ["There are two possible paths: (B then R) OR (R then B). Add their probabilities."]
        
        ans3 = 2 * (p_B_frac * p_R_frac)

        ans3_fr = [
            f"Cela correspond aux issues (B ; R) et (R ; B).",
            f"$P = ({sp.latex(p_B_frac)} \\times {sp.latex(p_R_frac)}) + ({sp.latex(p_R_frac)} \\times {sp.latex(p_B_frac)}) = {sp.latex(ans3)}$"
        ]
        ans3_en = [
            f"This corresponds to the outcomes (B ; R) and (R ; B).",
            f"$P = ({sp.latex(p_B_frac)} \\times {sp.latex(p_R_frac)}) + ({sp.latex(p_R_frac)} \\times {sp.latex(p_B_frac)}) = {sp.latex(ans3)}$"
        ]
        self.questions.append(Question(q3_fr, q3_en, insight3_fr, insight3_en, ans3_fr, ans3_en))

        # Question c (Celle qui manquait)
        q4_fr = ["c) Déterminer la probabilité d'obtenir au moins une boule blanche."]
        q4_en = ["c) Determine the probability of obtaining at least one white ball."]
        insight4_fr = ["Additionnez les probabilités des issues contenant au moins un B : (B ; R), (B ; B) et (R ; B). Vous pouvez aussi utiliser l'événement contraire."]
        insight4_en = ["Add the probabilities of the outcomes containing at least one B: (B ; R), (B ; B), and (R ; B). You can also use the complement event."]
        
        ans4 = ans2 + ans3

        ans4_fr = [
            f"Cela correspond aux issues (B ; B), (B ; R) et (R ; B).",
            f"$P = {sp.latex(ans2)} + {sp.latex(ans3)} = {sp.latex(ans4)}$"
        ]
        ans4_en = [
            f"This corresponds to the outcomes (B ; B), (B ; R), and (R ; B).",
            f"$P = {sp.latex(ans2)} + {sp.latex(ans3)} = {sp.latex(ans4)}$"
        ]
        self.questions.append(Question(q4_fr, q4_en, insight4_fr, insight4_en, ans4_fr, ans4_en))


# ==========================================
# MÉTHODE 9 : Répétition de n épreuves de Bernoulli
# ==========================================
class BernoulliTrials(BaseExercise):
    id = "PROB_009"
    title = {"fr": "Épreuves de Bernoulli", "en": "Bernoulli trials"}
    tags = ["probabilites", "bernoulli", "repetition"]

    def generate(self):
        b = self.rng.randint(2, 5)
        r = self.rng.randint(2, 5)
        total = b + r
        
        p_S = sp.Rational(b, total)
        p_notS = sp.Rational(r, total)
        tree_fig = _draw_3_level_tree(p_S, p_notS, "S")

        self.statement_fr = [
            f"Une urne contient {b} boules blanches et {r} boules rouges. On tire avec remise.",
            "On considère comme succès S : « obtenir une boule blanche ».",
            "On répète l'expérience 3 fois de suite.",
            tree_fig
        ]
        self.statement_en = [
            f"An urn contains {b} white balls and {r} red balls. We draw with replacement.",
            "Consider success S: 'obtain a white ball'.",
            "The experiment is repeated 3 times in a row.",
            tree_fig
        ]

        q1_fr = ["Calculer la probabilité d'obtenir exactement deux succès."]
        q1_en = ["Calculate the probability of obtaining exactly two successes."]
        insight1_fr = ["Identifiez le nombre de chemins contenant exactement deux succès et un échec dans l'arbre (il y en a 3). Multipliez la probabilité d'un de ces chemins par 3."]
        insight1_en = ["Identify the number of paths containing exactly two successes and one failure in the tree (there are 3). Multiply the probability of one such path by 3."]
        
        path_prob = p_S**2 * p_notS
        ans1 = 3 * path_prob

        ans1_fr = [
            f"La probabilité d'un succès est $P(S) = {sp.latex(p_S)}$ et d'un échec $P(\\overline{{S}}) = {sp.latex(p_notS)}$.",
            "Il y a 3 chemins contenant 2 succès et 1 échec : $(S; S; \\overline{S})$, $(S; \\overline{S}; S)$ et $(\\overline{S}; S; S)$.",
            f"La probabilité est donc : $3 \\times P(S)^2 \\times P(\\overline{{S}})$",
            f"$= 3 \\times ({sp.latex(p_S)})^2 \\times ({sp.latex(p_notS)}) = {sp.latex(ans1)}$"
        ]
        ans1_en = [
            f"The probability of a success is $P(S) = {sp.latex(p_S)}$ and of a failure $P(\\overline{{S}}) = {sp.latex(p_notS)}$.",
            "There are 3 paths containing 2 successes and 1 failure: $(S; S; \\overline{S})$, $(S; \\overline{S}; S)$, and $(\\overline{S}; S; S)$.",
            f"The probability is thus: $3 \\times P(S)^2 \\times P(\\overline{{S}})$",
            f"$= 3 \\times ({sp.latex(p_S)})^2 \\times ({sp.latex(p_notS)}) = {sp.latex(ans1)}$"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))
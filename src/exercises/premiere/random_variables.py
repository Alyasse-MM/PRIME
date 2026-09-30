import sympy as sp
import numpy as np
import math
from exercises.base_exercise import BaseExercise
from exercises.question import Question

# Module-level registry key
CHAPTER = {"fr": "Variables Aléatoires", "en": "Random Variables"}

# ==========================================
# MÉTHODE 1 : Calculer une probabilité
# ==========================================
class ProbabilitiesFromRV(BaseExercise):
    id = "VA_001"
    title = {"fr": "Calculer une probabilité avec une V.A.", "en": "Calculate a probability with a R.V."}
    tags = ["probabilites", "variable aleatoire", "evenement"]

    def generate(self):
        deck = self.rng.choice([32, 52])
        suit1 = {"fr": "cœur", "en": "heart"}
        suit2 = {"fr": "carreau", "en": "diamond"}
        
        w1 = self.rng.randint(4, 8)
        w2 = self.rng.randint(2, 3)
        loss = self.rng.randint(1, 3)

        self.statement_fr = [
            f"On tire une carte au hasard dans un jeu de {deck} cartes.",
            f"- Si cette carte est un {suit1['fr']}, on gagne {w1} €.",
            f"- Si cette carte est un {suit2['fr']}, on gagne {w2} €.",
            f"- Dans les autres cas, on perd {loss} €.",
            "Soit $X$ la variable aléatoire qui associe le gain du jeu."
        ]
        self.statement_en = [
            f"A card is drawn at random from a {deck}-card deck.",
            f"- If the card is a {suit1['en']}, we win {w1} €.",
            f"- If the card is a {suit2['en']}, we win {w2} €.",
            f"- In all other cases, we lose {loss} €.",
            "Let $X$ be the random variable representing the game's payout."
        ]

        # Questions
        q1_fr = [f"Calculer : $P(X={w1})$, $P(X=-{loss})$ et $P(X \\le {w2})$."]
        q1_en = [f"Calculate: $P(X={w1})$, $P(X=-{loss})$ and $P(X \\le {w2})$."]
        
        insight1_fr = ["Reliez chaque valeur de $X$ à l'événement correspondant (ex: tirer une certaine couleur). Un jeu de cartes possède 4 couleurs équiprobables."]
        insight1_en = ["Link each value of $X$ to the corresponding event (e.g., drawing a specific suit). A deck has 4 equiprobable suits."]
        
        ans1_fr = [
            f"• $P(X={w1})$ est la probabilité de gagner {w1} €. On gagne {w1} € lorsqu'on tire un {suit1['fr']}.",
            f"Dans un jeu de {deck} cartes, il y a {deck//4} cartes de cette couleur. Soit :",
            f"$P(X={w1}) = \\frac{{{deck//4}}}{{{deck}}} = \\frac{{1}}{{4}}$.",
            f"• $P(X=-{loss})$ est la probabilité de perdre {loss} €. On perd {loss} € lorsqu'on ne tire ni {suit1['fr']}, ni {suit2['fr']}.",
            f"Il reste {deck} - {deck//4} - {deck//4} = {deck//2} cartes. Soit :",
            f"$P(X=-{loss}) = \\frac{{{deck//2}}}{{{deck}}} = \\frac{{1}}{{2}}$.",
            f"• $P(X \\le {w2})$ est la probabilité de gagner {w2} € ou moins. Cela correspond aux gains de {w2} € et -{loss} €.",
            f"$P(X \\le {w2}) = P(X={w2}) + P(X=-{loss}) = \\frac{{1}}{{4}} + \\frac{{1}}{{2}} = \\frac{{3}}{{4}}$."
        ]
        ans1_en = [
            f"• $P(X={w1})$ is the probability of winning {w1} €. We win {w1} € when we draw a {suit1['en']}.",
            f"In a {deck}-card deck, there are {deck//4} cards of this suit. Thus:",
            f"$P(X={w1}) = \\frac{{{deck//4}}}{{{deck}}} = \\frac{{1}}{{4}}$.",
            f"• $P(X=-{loss})$ is the probability of losing {loss} €. We lose {loss} € when we draw neither a {suit1['en']} nor a {suit2['en']}.",
            f"There are {deck} - {deck//4} - {deck//4} = {deck//2} cards left. Thus:",
            f"$P(X=-{loss}) = \\frac{{{deck//2}}}{{{deck}}} = \\frac{{1}}{{2}}$.",
            f"• $P(X \\le {w2})$ is the probability of winning {w2} € or less. This corresponds to payouts of {w2} € and -{loss} €.",
            f"$P(X \\le {w2}) = P(X={w2}) + P(X=-{loss}) = \\frac{{1}}{{4}} + \\frac{{1}}{{2}} = \\frac{{3}}{{4}}$."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 2 : Loi de probabilité
# ==========================================
class ProbabilityDistribution(BaseExercise):
    id = "VA_002"
    title = {"fr": "Déterminer une loi de probabilité", "en": "Determine a probability distribution"}
    tags = ["probabilites", "loi", "variable aleatoire", "des"]

    def generate(self):
        k = self.rng.choice([4, 6])
        
        self.statement_fr = [
            f"On lance simultanément deux dés équilibrés à {k} faces et on note les valeurs obtenues.",
            "Soit $X$ la variable aléatoire égale à la plus grande des deux valeurs."
        ]
        self.statement_en = [
            f"Two balanced {k}-sided dice are rolled simultaneously, and the values obtained are noted.",
            "Let $X$ be the random variable equal to the larger of the two values."
        ]

        q1_fr = ["Établir la loi de probabilité de $X$."]
        q1_en = ["Establish the probability distribution of $X$."]
        insight1_fr = ["L'univers contient $N \\times N$ issues équiprobables. Comptez méthodiquement le nombre de paires dont le maximum vaut $1$, puis $2$, etc."]
        insight1_en = ["The sample space contains $N \\times N$ equiprobable outcomes. Methodically count the number of pairs whose maximum is $1$, then $2$, etc."]
        
        total_outcomes = k**2
        probs = []
        for m in range(1, k + 1):
            # The maximum of two dice is m if outcomes are (m, 1..m-1), (1..m-1, m), or (m, m).
            # This is exactly 2*(m-1) + 1 = 2m - 1 outcomes.
            count = 2 * m - 1
            probs.append(sp.Rational(count, total_outcomes))
            
        # Format the markdown table
        headers = "| $x_i$ | " + " | ".join(map(str, range(1, k + 1))) + " |"
        divider = "|---|" + "---|" * k
        row_probs = "| $P(X=x_i)$ | " + " | ".join([f"${sp.latex(p)}$" for p in probs]) + " |"
        md_table = f"{headers}\n{divider}\n{row_probs}"

        ans1_fr = [
            f"La variable aléatoire $X$ peut prendre les valeurs entières de $1$ à ${k}$. Il y a au total ${k} \\times {k} = {total_outcomes}$ issues possibles équiprobables.",
            f"Par exemple, la plus grande des deux valeurs est $2$ si on obtient les combinaisons : $(1; 2)$, $(2; 1)$ ou $(2; 2)$. Donc $P(X=2) = \\frac{{3}}{{{total_outcomes}}}$.",
            "On applique cette logique pour chaque valeur possible pour obtenir le tableau de la loi de probabilité :",
            md_table,
            "Remarque : On peut vérifier que la somme des probabilités est bien égale à 1."
        ]
        ans1_en = [
            f"The random variable $X$ can take integer values from $1$ to ${k}$. There are a total of ${k} \\times {k} = {total_outcomes}$ equiprobable possible outcomes.",
            f"For example, the larger of the two values is $2$ if we obtain the combinations: $(1; 2)$, $(2; 1)$, or $(2; 2)$. Thus $P(X=2) = \\frac{{3}}{{{total_outcomes}}}$.",
            "We apply this logic for each possible value to obtain the probability distribution table:",
            md_table,
            "Note: We can verify that the sum of the probabilities is indeed equal to 1."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 3 : Espérance, Variance, Écart-Type
# ==========================================
class ExpectationVariance(BaseExercise):
    id = "VA_003"
    title = {"fr": "Calculer l'espérance et la variance", "en": "Calculate expectation and variance"}
    tags = ["probabilites", "esperance", "variance", "ecart-type"]

    def generate(self):
        w_suit = self.rng.randint(2, 4)
        w_rank = self.rng.randint(5, 7)
        loss = self.rng.randint(1, 2)
        
        self.statement_fr = [
            "On tire une carte dans un jeu de 32 cartes.",
            f"- Si on tire un pique, on gagne {w_suit} €.",
            f"- Si on tire un as, on gagne {w_rank} €.",
            f"- Si on tire une autre carte, on perd {loss} €.",
            "$X$ est la variable aléatoire donnant le gain du jeu."
        ]
        self.statement_en = [
            "A card is drawn from a 32-card deck.",
            f"- If a spade is drawn, we win {w_suit} €.",
            f"- If an ace is drawn, we win {w_rank} €.",
            f"- If any other card is drawn, we lose {loss} €.",
            "$X$ is the random variable giving the payout of the game."
        ]

        q1_fr = [
            "1) Établir la loi de probabilité de $X$.",
            "2) Calculer l'espérance de $X$ et donner une interprétation du résultat.",
            "3) Calculer la variance et l'écart-type de $X$."
        ]
        q1_en = [
            "1) Establish the probability distribution of $X$.",
            "2) Calculate the expectation of $X$ and interpret the result.",
            "3) Calculate the variance and standard deviation of $X$."
        ]
        insight1_fr = ["Identifiez les gains cumulés possibles (ex: tirer l'As de pique cumule les deux gains). Calculez ensuite $E(X) = \\sum p_i x_i$."]
        insight1_en = ["Identify possible cumulative payouts (e.g., drawing the Ace of spades combines both wins). Then calculate $E(X) = \\sum p_i x_i$."]
        
        # Calculations
        x_vals = sorted([-loss, w_suit, w_rank, w_suit + w_rank])
        
        # Counts in 32 cards: 8 spades, 4 aces, 1 ace of spades
        # Ace of Spades: 1
        # Other Spades: 7
        # Other Aces: 3
        # Others: 32 - 1 - 7 - 3 = 21
        counts = {
            w_suit + w_rank: 1,
            w_suit: 7,
            w_rank: 3,
            -loss: 21
        }
        
        headers = "| $x_i$ | " + " | ".join(map(str, x_vals)) + " |"
        divider = "|---|" + "---|" * len(x_vals)
        row_probs = "| $P(X=x_i)$ | " + " | ".join([f"$\\frac{{{counts[x]}}}{{32}}$" for x in x_vals]) + " |"
        md_table = f"{headers}\n{divider}\n{row_probs}"
        
        # Math
        E_x_frac = sp.Rational(sum([x * counts[x] for x in x_vals]), 32)
        E_x_float = float(E_x_frac)
        
        var_x_frac = sum([sp.Rational(counts[x], 32) * (x - E_x_frac)**2 for x in x_vals])
        var_x_float = float(var_x_frac)
        std_x = math.sqrt(var_x_float)

        ans1_fr = [
            f"1) $X$ peut prendre les valeurs $-{loss}$, ${w_suit}$, ${w_rank}$ et ${w_suit + w_rank}$ (si on tire l'As de pique, on cumule les gains).",
            md_table,
            f"2) $E(X) = \\frac{{21}}{{32}} \\times (-{loss}) + \\frac{{7}}{{32}} \\times {w_suit} + \\frac{{3}}{{32}} \\times {w_rank} + \\frac{{1}}{{32}} \\times {w_suit + w_rank}$.",
            f"$E(X) = {sp.latex(E_x_frac)} \\approx {E_x_float:.2f}$ €.",
            f"Interprétation : Si l'on répète l'expérience un grand nombre de fois, on peut espérer { 'gagner' if E_x_float > 0 else 'perdre' } en moyenne environ {abs(E_x_float):.2f} € par tirage.",
            f"3) Variance : $V(X) = \\sum p_i (x_i - E(X))^2 \\approx {var_x_float:.4f}$.",
            f"Écart-type : $\\sigma(X) = \\sqrt{{V(X)}} \\approx {std_x:.2f}$ €."
        ]
        ans1_en = [
            f"1) $X$ can take the values $-{loss}$, ${w_suit}$, ${w_rank}$ and ${w_suit + w_rank}$ (if the Ace of spades is drawn, payouts accumulate).",
            md_table,
            f"2) $E(X) = \\frac{{21}}{{32}} \\times (-{loss}) + \\frac{{7}}{{32}} \\times {w_suit} + \\frac{{3}}{{32}} \\times {w_rank} + \\frac{{1}}{{32}} \\times {w_suit + w_rank}$.",
            f"$E(X) = {sp.latex(E_x_frac)} \\approx {E_x_float:.2f}$ €.",
            f"Interpretation: If the experiment is repeated a large number of times, we can expect to { 'win' if E_x_float > 0 else 'lose' } on average about {abs(E_x_float):.2f} € per draw.",
            f"3) Variance: $V(X) = \\sum p_i (x_i - E(X))^2 \\approx {var_x_float:.4f}$.",
            f"Standard Deviation: $\\sigma(X) = \\sqrt{{V(X)}} \\approx {std_x:.2f}$ €."
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))


# ==========================================
# MÉTHODE 4 : Linéarité de l'espérance
# ==========================================
class LinearityExpVar(BaseExercise):
    id = "VA_004"
    title = {"fr": "Linéarité de l'espérance et variance", "en": "Linearity of expectation and variance"}
    tags = ["probabilites", "esperance", "variance", "linearite", "contexte"]

    def generate(self):
        # 1. Generate a dynamic Y distribution (kept hidden from the student's prompt)
        start_y = self.rng.randint(-4, 0)
        step_y = self.rng.randint(1, 2)
        y_vals = [start_y + i * step_y for i in range(5)]
        
        # Pick a valid probability distribution that perfectly sums to 1.0
        distribs = [
            [1, 2, 4, 2, 1],
            [2, 2, 2, 2, 2],
            [1, 3, 2, 3, 1],
            [3, 1, 2, 1, 3],
            [2, 4, 1, 2, 1],
            [1, 1, 6, 1, 1]
        ]
        probs_int = self.rng.choice(distribs)
        probs = [p / 10.0 for p in probs_int]
        
        # 2. Generate the linear relationship parameters
        a = self.rng.choice([100, 1000])
        b_base = self.rng.choice([12, 13, 15, 25, 30])
        b = b_base * (a // 10) 
        
        # Calculate theoretical diameter based on the shift
        th_diam = b / a
        
        # Calculate X values (the messy decimals the student actually sees)
        x_vals = [(y + b) / a for y in y_vals]
        
        # Format X table
        headers = "| $x_i$ | " + " | ".join([f"{x:g}" for x in x_vals]) + " |"
        divider = "|---|" + "---|" * len(x_vals)
        row_probs = "| $P(X=x_i)$ | " + " | ".join([f"{p:g}" for p in probs]) + " |"
        md_table = f"{headers}\n{divider}\n{row_probs}"

        self.statement_fr = [
            "Une entreprise qui fabrique des roulements à bille fait une étude sur une gamme de billes produites[cite: 4].",
            f"Le diamètre théorique doit être égal à {th_diam:g} cm mais cette mesure peut être légèrement erronée[cite: 4].",
            "L'expérience consiste à tirer au hasard une bille d'un lot de la production et à mesurer son diamètre[cite: 4].",
            "On considère la variable aléatoire $X$ qui, à une bille choisie au hasard, associe son diamètre[cite: 4].",
            "La loi de probabilité de $X$ est résumée dans le tableau suivant[cite: 4] :",
            md_table
        ]
        self.statement_en = [
            "A company manufacturing ball bearings is conducting a study on a range of balls produced.",
            f"The theoretical diameter should be {th_diam:g} cm, but this measurement may be slightly erroneous.",
            "The experiment consists of randomly drawing a ball from a production batch and measuring its diameter.",
            "Consider the random variable $X$ which associates its diameter to a randomly chosen ball.",
            "The probability distribution of $X$ is summarized in the following table:",
            md_table
        ]

        q1_fr = ["Calculer l'espérance et l'écart-type de la loi de probabilité de $X$[cite: 4]."]
        q1_en = ["Calculate the expectation and standard deviation of the probability distribution of $X$."]
        
        insight1_fr = [f"Pour éviter des calculs fastidieux avec les valeurs décimales, définissez une nouvelle variable $Y = aX + b'$ (déterminez $a$ et $b'$ pour obtenir des nombres entiers simples), puis utilisez la linéarité."]
        insight1_en = [f"To avoid tedious calculations with decimal values, define a new variable $Y = aX + b'$ (determine $a$ and $b'$ to get simple integers), then use linearity."]
        
        # Calculate Y stats
        e_y = round(sum([y * p for y, p in zip(y_vals, probs)]), 4)
        v_y = round(sum([p * (y - e_y)**2 for y, p in zip(y_vals, probs)]), 6)
        
        # Calculate X stats backwards
        e_x = round((e_y + b) / a, 6)
        v_x = v_y / (a**2)
        std_x = math.sqrt(v_x)

        # 3. Format calculation strings dynamically
        y_vals_str = ", ".join(map(str, y_vals))
        ey_calc = " + ".join([f"{y}({p:g})" for y, p in zip(y_vals, probs)])
        vy_calc = " + ".join([f"{p:g}({y} - {e_y:g})^2" for y, p in zip(y_vals, probs)])

        ans1_fr = [
            f"• Pour simplifier les calculs, on définit la variable aléatoire $Y = {a}X - {b}$.",
            f"La loi de probabilité de $Y$ associe les valeurs entières $\\{{ {y_vals_str} \\}}$ aux mêmes probabilités respectives.",
            f"• On calcule l'espérance et la variance de $Y$ :",
            f"$E(Y) = {ey_calc} = {e_y:g}$.",
            f"$V(Y) = {vy_calc} = {v_y:g}$.",
            f"• On en déduit l'espérance et la variance de $X$ :",
            f"$E(Y) = E({a}X - {b}) = {a} E(X) - {b}$.",
            f"Donc $E(X) = \\frac{{E(Y) + {b}}}{{{a}}} = \\frac{{{e_y:g} + {b}}}{{{a}}} = {e_x:g}$.",
            f"$V(Y) = V({a}X - {b}) = {a}^2 V(X)$.",
            f"Donc $V(X) = \\frac{{V(Y)}}{{{a}^2}} = \\frac{{{v_y:g}}}{{{a**2}}}$.",
            f"Et donc $\\sigma(X) = \\frac{{\\sigma(Y)}}{{{a}}} = \\frac{{\\sqrt{{{v_y:g}}}}}{{{a}}} \\approx {std_x:g}$.",
            f"**Conclusion : $E(X) = {e_x:g}$ cm et $\\sigma(X) \\approx {std_x:g}$ cm.**"
        ]
        ans1_en = [
            f"• To simplify calculations, we define the random variable $Y = {a}X - {b}$.",
            f"The probability distribution of $Y$ associates the integer values $\\{{ {y_vals_str} \\}}$ with the same respective probabilities.",
            f"• We calculate the expectation and variance of $Y$:",
            f"$E(Y) = {ey_calc} = {e_y:g}$.",
            f"$V(Y) = {vy_calc} = {v_y:g}$.",
            f"• We deduce the expectation and variance of $X$:",
            f"$E(Y) = E({a}X - {b}) = {a} E(X) - {b}$.",
            f"Thus $E(X) = \\frac{{E(Y) + {b}}}{{{a}}} = \\frac{{{e_y:g} + {b}}}{{{a}}} = {e_x:g}$.",
            f"$V(Y) = V({a}X - {b}) = {a}^2 V(X)$.",
            f"Thus $V(X) = \\frac{{V(Y)}}{{{a}^2}} = \\frac{{{v_y:g}}}{{{a**2}}}$.",
            f"And therefore $\\sigma(X) = \\frac{{\\sigma(Y)}}{{{a}}} = \\frac{{\\sqrt{{{v_y:g}}}}}{{{a}}} \\approx {std_x:g}$.",
            f"**Conclusion: $E(X) = {e_x:g}$ cm and $\\sigma(X) \\approx {std_x:g}$ cm.**"
        ]
        self.questions.append(Question(q1_fr, q1_en, insight1_fr, insight1_en, ans1_fr, ans1_en))
class Question:
    def __init__(self, q_fr: list, q_en: list, insight_fr: list, insight_en: list, ans_fr: list, ans_en: list):
        """Initializes a Question object
        q_fr & q_en: List of media representing the question in French and English
        insight_fr & insight_en: List of media representing the insight in French and English
        ans_fr & ans_en: List of media representing the answer in French and English
        *media can be strings or matplotlib figures
        """
        self.q_fr = q_fr
        self.q_en = q_en
        self.insight_fr = insight_fr
        self.insight_en = insight_en
        self.ans_fr = ans_fr
        self.ans_en = ans_en

    def get_data(self):
        return {
            "fr": {
                "question": self.q_fr,
                "insight": self.insight_fr,
                "answer": self.ans_fr
            },
            "en": {
                "question": self.q_en,
                "insight": self.insight_en,
                "answer": self.ans_en
            }
        }
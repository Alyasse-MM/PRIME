class Question:
    def __init__(self, q_fr, q_en, insight_fr, insight_en, ans_fr, ans_en):
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
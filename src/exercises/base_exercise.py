import random

from question import Question

class BaseExercise:
    # Metadata
    id = "base"
    title_fr = ""
    title_en = ""
    tags = []

    def __init__(self, seed=None):
        if seed is None:
            self.seed = random.randint(100000, 999999)
        else:
            self.seed = int(seed)

        self.rng = random.Random(self.seed)
        
        self.statement_fr = ""
        self.statement_en = ""
        self.questions = []
        self.generate() 

    # Calculates the math at the object's creation
    def generate(self):
        raise NotImplementedError("generate() method must be defined in the sub-class.")

    def get_data(self):
        return {
            "id": self.id,
            "tags": self.tags,
            "seed": self.seed,
            "title": {
                "fr": self.title_fr,
                "en": self.title_en,
            },
            "statement": {
                "fr": self.statement_fr,
                "en": self.statement_en,
            },
            "questions": [q.get_data() for q in self.questions]
        }
class BaseExercise:
    # Metadata
    id = "base"
    title_fr = ""
    title_en = ""
    level_fr = ""
    level_en = ""
    tags = []

    def __init__(self):
        self.statement_fr = ""
        self.statement_en = ""
        self.questions = []
        self.generate() 

    # Calculates the math at the object's creation
    def generate(self):
        raise NotImplementedError("generate() method must be defined in the sub-class.")

    def get_data(self):
        return {
            "meta": {
                "id": self.id,
                "title_fr": self.title_fr,
                "title_en": self.title_en,
                "level_fr": self.level_fr,
                "level_en": self.level_en,
                "tags": self.tags
            },
            "statement_fr": self.statement_fr,
            "statement_en": self.statement_en,
            "questions": self.questions
        }
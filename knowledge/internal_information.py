class Person:
    def __init__(self, first_name, last_name, age, dream, goal, value):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.dream = dream
        self.goal = goal
        self.value = value
        self.email = None  # Initialize email as None

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def update_email(self, new_email):
        self.email = new_email

    def __str__(self):
        return f"Person: {self.full_name}, Age: {self.age}, Dream: {self.dream}, Goal: {self.goal}, Value: {self.value}, Email: {self.email}"

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "dream": self.dream,
            "goal": self.goal,
            "value": self.value,
            "email": self.email
        }
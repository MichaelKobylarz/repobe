class Cow:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "MUuuuuuuuuu!"

    def __str__(self):
        return f"Krowa o imieniu {self.name}, lat {self.age}"

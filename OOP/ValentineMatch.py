class ValentineMatch:
    def __init__(self, person1, person2):
        self.person1 = person1.lower()
        self.person2 = person2.lower()
        self.score = 0

    def calculate_score(self):
        vowels = "aeiou"

        # Count vowels
        vowel_count = sum(1 for letter in self.person1 + self.person2 if letter in vowels)

        # Count common letters
        common_letters = 0
        for letter in self.person1:
            if letter in self.person2:
                common_letters += 1

        base_score = vowel_count * 4 + common_letters * 6

        # Ensure score is between 80 and 100
        self.score = 80 + (base_score % 21)

        # Exact same names = 100%
        if self.person1 == self.person2:
            self.score = 100

    def display_result(self):
        print("\nCompatibility Score:", self.score)

        if self.score >= 95:
            print("Result: Destiny Confirmed 💍✨")
        elif self.score >= 90:
            print("Result: Elite Soulmates 💖")
        else:
            print("Result: Strong Romantic Vibes 😌")

    def propose(self):
        print(f"\n{self.person1.title()}  ❤️  {self.person2.title()} = Forever Mode Activated 💘")


# ---- Main Program ----
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

match = ValentineMatch(name1, name2)
match.calculate_score()
match.display_result()
match.propose()

class Flashcards:
    def __init__(self):
        self.flashcards = {}

    def main_menu(self):
        while True:
            while True:
                print("\n1. Add flashcards\n2. Practice flashcards\n3. Exit")
                choice = input()
                if choice in ("1", "2", "3"):
                    break
                print(f"\n{choice} is not an option\n")
            if choice == "1":
                self.sub_menu()
            elif choice == "2":
                self.practice_flashcards()
            else:
                print("Bye!")
                return


    def sub_menu(self):
        while True:
            while True:
                print("\n1. Add a new flashcard\n2. Exit")
                choice = input()
                if choice in ("1", "2"):
                    break
                print(f"\n{choice} is not an option\n")

            if choice == "1":
                self.add_flashcard()
            else:
                return


    def add_flashcard(self):
        question = ""
        while question == "":
            question = input("Question:\n").strip()

        answer = ""
        while answer == "":
            answer = input("Answer:\n").strip()

        self.flashcards[question] = answer


    def practice_flashcards(self):
        if not self.flashcards:
            print("There is no flashcard to practice!")
            return

        for question, answer in self.flashcards.items():
            print(f"\nQuestion: {question}")
            choice = ""
            while choice not in ("y", "n"):
                print("Please press \"y\" to see the answer or press \"n\" to skip:")
                choice = input().lower()
            if choice == "y":
                print(f"\nAnswer: {answer}")


Flashcards().main_menu()
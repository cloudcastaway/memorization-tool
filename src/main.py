from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Flashcard(Base):
    __tablename__ = "flashcard"

    id = Column(Integer, primary_key=True)
    question = Column(String(300), nullable=False)
    answer = Column(String(300), nullable=False)


class FlashcardApp:
    def __init__(self):
        address = "sqlite:///flashcard.db?check_same_thread=False"
        self.engine = create_engine(address)
        Base.metadata.create_all(self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def main_menu(self):
        try:
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
        finally:
            self.session.close()


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

        new_flashcard = Flashcard(question = question, answer = answer)
        self.session.add(new_flashcard)
        self.session.commit()


    def practice_flashcards(self):
        row_exists = self.session.query(Flashcard).first()
        if not row_exists:
            print("There is no flashcard to practice!")
            return

        rows = self.session.query(Flashcard).all()
        for row in rows:
            print(f"\nQuestion: {row.question}")
            choice = ""
            while choice not in ("y", "n", "u"):
                print("press \"y\" to see the answer:\npress \"n\" to skip:\npress \"u\" to update:")
                choice = input().lower()
            if choice == "y":
                print(f"\nAnswer: {row.answer}")
            elif choice == "u":
                self.update_menu(row.question, row.answer)


    def update_menu(self, question, answer):
        choice = ""
        while choice not in ("d", "e"):
            print("press \"d\" to delete the flashcard:\npress \"e\" to edit the flashcard:")
            choice = input().lower()
        if choice == "d":
            self.delete_flashcard(question)
        else:
            self.edit_flashcard(question, answer)


    def delete_flashcard(self, question):
        row = self.session.query(Flashcard).filter_by(question=question).first()
        self.session.delete(row)
        self.session.commit()


    def edit_flashcard(self, question, answer):
        print(f"current question: {question}\nplease write a new question:")
        new_question = input().strip()
        print(f"\ncurrent answer: {answer}\nplease write a new answer:")
        new_answer = input().strip()

        row = self.session.query(Flashcard).filter_by(question=question).first()

        if new_question != "":
            row.question = new_question
        if new_answer != "":
            row.answer = new_answer

        self.session.commit()


FlashcardApp().main_menu()
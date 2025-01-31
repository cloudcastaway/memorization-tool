# Memorization Tool

This project is a **Flashcard-Based Memorization Tool** implemented in Python. It allows users to create, update, and practice flashcards, helping with effective learning and retention. The system uses an SQLite database to store flashcards, including a difficulty-based progression mechanism.

## Features

- **Flashcard Management**:
  - Add new flashcards with questions and answers.
  - Edit or delete existing flashcards.
- **Practice Mode**: 
  - Users can review flashcards one by one.
  - Answers are hidden until the user chooses to reveal them.
- **Adaptive Learning**:
  - Flashcards have a difficulty rating that increases when answered correctly.
  - If a flashcard reaches a high difficulty level, it is automatically removed.
  - Incorrect answers reset the difficulty, reinforcing learning.
- **Data Persistence**: All flashcards are stored in a local SQLite database.

## Technologies Used

- **Python**: Core programming language.
- **SQLite**: Database for secure data storage.
- **SQLAlchemy**: ORM (Object-Relational Mapping) for database operations.

---

### About This Project

This project was initially developed as part of a **Hyperskill learning path**. 

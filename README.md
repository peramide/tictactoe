# 🎮 Tic-Tac-Toe AI

Using the **Minimax algorithm**, I implemented an AI that plays **Tic-Tac-Toe optimally**. The project includes full game logic and a graphical interface, allowing you to play against an **unbeatable AI**. It features move evaluation, game state tracking, and decision-making for perfect play in every match.

🕹️ Play the game live here:
NB: Exercise patience please, it might a few mins to load!
👉 https://peramide.github.io/tictactoe/
---

## 🧠 Overview

This project applies **artificial intelligence** principles to the classic game of **Tic-Tac-Toe**. By using the **Minimax algorithm**, the AI analyzes all possible future moves and chooses the best one, ensuring it never loses. The result is an intelligent and competitive opponent that demonstrates algorithmic reasoning and decision-making.

---

## 🗂️ Project Structure

* **`tictactoe.py`** – Contains the complete game logic and AI implementation:

  * Board setup and state representation
  * Determining the current player
  * Generating valid actions
  * Computing the result of moves
  * Detecting winners and terminal states
  * Evaluating utility values
  * Running the Minimax search algorithm

* **`runner.py`** – A graphical interface that lets you play Tic-Tac-Toe against your AI in real time.

---

## ⚙️ How It Works

* The game board is represented as a 3×3 grid.
* Players alternate turns: **X** moves first, followed by **O**.
* The **Minimax algorithm** recursively explores every possible move sequence:

  * **X** aims to maximize the score (+1 for a win).
  * **O** aims to minimize the score (–1 for a win).
* The game terminates when there’s a winner or a tie (utility = 0).

Since the AI always chooses the optimal move, it’s **impossible to defeat** — you can only **draw** if you play perfectly.

---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/tictactoe-ai.git
   cd tictactoe-ai
   ```

2. Run the game:

   ```bash
   python runner.py
   ```

3. Play against the AI — click on the grid to make your move.

---

## 🧩 Features

✅ Fully functional **Tic-Tac-Toe** gameplay
✅ **Minimax-based** AI with perfect strategy
✅ **Immutable board state** for accurate search
✅ **Graphical interface** with user interaction
✅ Supports **tie detection**, **win detection**, and **move validation**

---

## 🧠 Key Concepts

* **Artificial Intelligence** (Adversarial Search)
* **Minimax Algorithm**
* **Game Tree Exploration**
* **State Evaluation and Utility Functions**
* **Recursive Decision-Making**

---

## 🎯 Expected Outcome

With both players making optimal moves, every game ends in a **draw**. The AI guarantees flawless play and demonstrates the strength of algorithmic game-solving.

---

## 📚 Acknowledgements

 **CS50’s Introduction to Artificial Intelligence with Python**


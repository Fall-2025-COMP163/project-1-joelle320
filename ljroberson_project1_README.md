# Project 1 – Character Creator & Chronicles

# Author
- Lauren Roberson – COMP 163, Fall 2025

# Description
- This project includes a Naruto-themed Python program that creates and manages RPG-style characters.
- Internally, the program still uses the original COMP 163 class names so that automated test cases pass successfully.

Character Creator Features:
- Create a character by entering a name and choosing a Naruto-themed class (Shinobi, Uchiha, Hyuga, Medic).
- Class names are mapped internally to Warrior, Mage, Rogue, and Cleric to calculate stats correctly.
- Calculates strength, magic, and health based on class and level.
- Character data can be saved to and loaded from a text file.
- Supports leveling up to increase stats.

# How It Works

- Input:
  The user enters a character name and selects a Naruto class.

- Class Mapping:
  Naruto class names are translated to COMP 163 internal class names so the autograder reads the expected class values.

- Stat Calculation:
  Each class has different starting strengths and stat growth patterns per level.

- Saving:
  Character info is stored in a plain text file using the exact required format.
  If the directory is invalid, the function returns False to prevent crashes.

- Loading:
  Character data is read back from the saved file and the Naruto class name is restored for display.

- Leveling Up:
  Increases the character’s level and recalculates stats based on class-specific growth.

# AI Help

- I used ChatGPT (OpenAI, 2025 – GPT-5 model) to:
  - Clarify assignment instructions
  - Improve the readability and organization of function design
  - Suggest a technique that allowed Naruto-themed display class names while still storing COMP 163 compatible class names for testing
  - Help revise the wording in this README

MLA Citation:
- OpenAI. “ChatGPT (GPT-5 Model).” OpenAI, 2025, https://chat.openai.com/.

# How to Run

Open the Project1 folder to access the Python file.
python ljroberson_project_1.py
To View Commits: https://github.com/Fall-2025-COMP163/project-1-joelle320/actions/workflows/classroom.yml


"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Lauren Roberson
Date: 24 October, 2025

AI Usage: AI helped transform the original code I provided to Naruto-inspired character classes and file I/O structure, and substituted with better descriptive variable naming."""

def create_character(name, character_class):
    """
    Creates a new Naruto-themed character dictionary with calculated stats.
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """
    character_class = character_class.strip().title()
    level = 1
    gold = 100

    strength, magic, health = calculate_stats(character_class, level)

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    return character


def calculate_stats(character_class, level):
    """
    Calculates base stats based on Naruto ninja classes.
    Returns: tuple of (strength, magic, health)

    Naruto Class Themes:
    - Shinobi (Warrior type): strong taijutsu, high health
    - Uchiha (Mage type): powerful ninjutsu, low health
    - Hyuga (Rogue type): balanced speed and chakra control
    - Medic (Cleric type): healing chakra, high magic and health
    """

    if character_class == "Shinobi":
        strength = 15 + (level - 1) * 3
        magic = 5 + (level - 1) * 1
        health = 120 + (level - 1) * 15

    elif character_class == "Uchiha":
        strength = 6 + (level - 1) * 1
        magic = 18 + (level - 1) * 5
        health = 80 + (level - 1) * 8

    elif character_class == "Hyuga":
        strength = 10 + (level - 1) * 2
        magic = 10 + (level - 1) * 2
        health = 90 + (level - 1) * 9

    elif character_class == "Medic":
        strength = 8 + (level - 1) * 1
        magic = 16 + (level - 1) * 3
        health = 110 + (level - 1) * 12

    else:
        # Default stats for unknown classes
        strength = 5
        magic = 5
        health = 50

    return (strength, magic, health)


def save_character(character, filename):
    """
    Saves character to text file in specific format.
    Returns: True if successful, False if error occurred.
    """
    with open(filename, "w") as character_file:
        character_file.write("Character Name: " + str(character["name"]) + "\n")
        character_file.write("Class: " + str(character["class"]) + "\n")
        character_file.write("Level: " + str(character["level"]) + "\n")
        character_file.write("Strength: " + str(character["strength"]) + "\n")
        character_file.write("Magic: " + str(character["magic"]) + "\n")
        character_file.write("Health: " + str(character["health"]) + "\n")
        character_file.write("Gold: " + str(character["gold"]) + "\n")
    return True


def load_character(filename):
    """
    Loads character from text file.
    Returns: character dictionary if successful, None if file not found.
    """
    import os
    if not os.path.exists(filename):
        return None

    with open(filename, "r") as character_file:
        lines = character_file.readlines()

    character = {}

    for line in lines:
        if ":" in line:
            parts = line.strip().split(":")
            key = parts[0].strip()
            value = parts[1].strip()

            if key == "Character Name":
                character["name"] = value
            elif key == "Class":
                character["class"] = value
            elif key == "Level":
                character["level"] = int(value)
            elif key == "Strength":
                character["strength"] = int(value)
            elif key == "Magic":
                character["magic"] = int(value)
            elif key == "Health":
                character["health"] = int(value)
            elif key == "Gold":
                character["gold"] = int(value)

    return character


def display_character(character):
    """
    Prints formatted Naruto-style character sheet.
    """
    print("=== NARUTO CHARACTER SHEET ===")
    print("Name: " + str(character["name"]))
    print("Class: " + str(character["class"]))
    print("Level: " + str(character["level"]))
    print("Strength: " + str(character["strength"]))
    print("Magic: " + str(character["magic"]))
    print("Health: " + str(character["health"]))
    print("Gold: " + str(character["gold"]))


def level_up(character):
    """
    Increases character level and recalculates stats.
    """
    character["level"] = character["level"] + 1
    new_stats = calculate_stats(character["class"], character["level"])
    character["strength"] = new_stats[0]
    character["magic"] = new_stats[1]
    character["health"] = new_stats[2]
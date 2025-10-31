"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Lauren Roberson
Date: 24 October, 2025

AI Usage: AI assisted in designing Naruto-themed visual class names while keeping
internal project-required class names for automated testing compatibility.
"""

# Mapping so the user sees Naruto classes, but tests see canonical class names
CLASS_MAP = {
    "Shinobi": "Warrior",
    "Uchiha": "Mage",
    "Hyuga": "Rogue",
    "Medic": "Cleric"
}

# Reverse mapping: internal → Naruto display names
REVERSE_CLASS_MAP = {
    "Warrior": "Shinobi",
    "Mage": "Uchiha",
    "Rogue": "Hyuga",
    "Cleric": "Medic"
}

def create_character(name, character_class):
    character_class = character_class.strip().title()

    # Convert Naruto class to internal required class
    if character_class in CLASS_MAP:
        internal_class = CLASS_MAP[character_class]
    else:
        internal_class = character_class  # fallback if unusual input

    level = 1
    gold = 100

    strength, magic, health = calculate_stats(internal_class, level)

    # Store internal class for tests, but also remember Naruto class for display
    character = {
        "name": name,
        "class": internal_class,              # used by tests
        "display_class": character_class,     # shown to user
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    return character


def calculate_stats(character_class, level):
    if character_class == "Warrior":
        strength = 15 + (level - 1) * 3
        magic = 2 + (level - 1) * 0
        health = 120 + (level - 1) * 15

    elif character_class == "Mage":
        strength = 5 + (level - 1) * 1
        magic = 15 + (level - 1) * 4
        health = 80 + (level - 1) * 8

    elif character_class == "Rogue":
        strength = 10 + (level - 1) * 2
        magic = 7 + (level - 1) * 1
        health = 70 + (level - 1) * 6

    elif character_class == "Cleric":
        strength = 8 + (level - 1) * 1
        magic = 14 + (level - 1) * 3
        health = 100 + (level - 1) * 10

    else:
        strength = 5
        magic = 5
        health = 50

    return (strength, magic, health)


def save_character(character, filename):
    with open(filename, "w") as character_file:
        character_file.write("Character Name: " + str(character["name"]) + "\n")
        character_file.write("Class: " + str(character["class"]) + "\n")  # internal class (tests expect this)
        character_file.write("Level: " + str(character["level"]) + "\n")
        character_file.write("Strength: " + str(character["strength"]) + "\n")
        character_file.write("Magic: " + str(character["magic"]) + "\n")
        character_file.write("Health: " + str(character["health"]) + "\n")
        character_file.write("Gold: " + str(character["gold"]) + "\n")
    return True


def load_character(filename):
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

    # Restore Naruto display class
    if character["class"] in REVERSE_CLASS_MAP:
        character["display_class"] = REVERSE_CLASS_MAP[character["class"]]
    else:
        character["display_class"] = character["class"]

    return character


def display_character(character):
    print("=== CHARACTER SHEET ===")
    print("Name: " + str(character["name"]))
    print("Class: " + str(character["display_class"]))  # Naruto display stays visible
    print("Level: " + str(character["level"]))
    print("Strength: " + str(character["strength"]))
    print("Magic: " + str(character["magic"]))
    print("Health: " + str(character["health"]))
    print("Gold: " + str(character["gold"]))


def level_up(character):
    character["level"] = character["level"] + 1
    new_stats = calculate_stats(character["class"], character["level"])
    character["strength"] = new_stats[0]
    character["magic"] = new_stats[1]
    character["health"] = new_stats[2]

full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    # --- Validate the character name ---

    # Reject if name isn't a string at all (e.g. a number was passed in)
    if not isinstance(character_name, str):
        return "The character name should be a string"
        
    # Reject if name is empty    
    if character_name == "":
        return "The character should have a name"
        
    # Reject if name is longer than 10 characters    
    if len(character_name) > 10:
        return "The character name is too long"
        
    # Reject if name contains a space    
    if " " in character_name:
        return "The character name should not contain spaces"

    # --- Validate the stats ---

    # Check ALL three stats are integers before doing any math on them.
    # This must come before any comparisons below, otherwise comparing
    # a non-integer (like a string) to a number would crash the program
    # instead of returning a clean error message.
    if not all(isinstance(stat, int) for stat in (strength, intelligence, charisma)):
        return "All stats should be integers"

    # Reject if ANY stat is below the minimum of 1
    # (using "or" because we want to catch it if even ONE stat is too low —
    # "and" would only catch it if ALL three were too low at once, which is wrong)
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"

    # Reject if ANY stat is above the maximum of 4 (same "or" logic as above)
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    # Stats must add up to exactly 7 points total.
    # This is calculated AFTER the integer check above, so we know it's
    # safe to add these values together without crashing.
    sum = strength + intelligence + charisma
    if sum != 7:
        return "The character should start with 7 points"

    # --- Build the final character sheet ---

    # If we reach this point, everything passed validation.
    # For each stat, print filled dots equal to the stat's value,
    # then empty dots to fill the rest of a 10-dot bar.
    # Example: strength = 3 -> "●●●○○○○○○○"
    return (
        f"{character_name}\n"
        f"STR {full_dot * strength}{empty_dot * (10 - strength)}\n"
        f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}\n"
        f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}"
    )


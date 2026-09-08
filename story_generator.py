# Random Story Generator
# Combines random names, places, and actions to create a short fun story

import random  # random module lets us pick random items from a list


# ---- Data: Lists of Names, Places, and Actions ----

# List of character names
names = ["Ravi", "Priya", "Aman", "Sneha", "Rahul"]

# List of possible places for the story
places = ["a haunted castle", "the moon", "a crowded marketplace", "a magical forest", "an underwater city"]

# List of possible actions the character is doing
actions = ["dancing with a talking parrot", "solving a mystery", "fighting a giant robot", "searching for treasure", "learning to fly"]


# ---- Function: Generate a Random Story ----

def generate_story():
    # Randomly pick one item from each list
    name = random.choice(names)
    place = random.choice(places)
    action = random.choice(actions)

    # Combine the values into a story using an f-string
    story = f"Once upon a time, {name} went to {place} and ended up {action}."

    return story  # send the generated story back to the caller


# ---- Main Program: Keep Generating Stories Until User Stops ----

while True:
    # Generate a new story and print it
    print("\n" + generate_story())

    # Ask the user if they want another story
    again = input("\nGenerate another story? (yes/no): ").strip().lower()

    if again != "yes":
        print("Thanks for using Random Story Generator. Goodbye!")
        break  # exit the loop and end the program
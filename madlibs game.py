import random

def mad_libs():
    story = "Once upon a time, there was a {noun} who loved to {verb} in the {place}. One day, the {noun} found a {adjective} {noun} and decided to {verb} it. Everyone in the {place} was {adjective} and {adverb} {verb}."

    # List of parts of speech to fill in
    parts_of_speech = ['noun', 'verb', 'place', 'adjective', 'adverb']

    # Dictionary to store user input
    user_input = {}

    # Prompt the user for words
    for part_of_speech in parts_of_speech:
        user_input[part_of_speech] = input(f"Enter a {part_of_speech}: ")

    # Substitute user input into the story
    mad_lib_story = story.format(**user_input)

    # Print the generated Mad Libs story
    print("\nYour Mad Libs Story:\n" + mad_lib_story)

if __name__ == "__main__":
    mad_libs()

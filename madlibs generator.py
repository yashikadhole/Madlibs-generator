import random

def get_input(prompt):
    user_input = input(prompt)
    return user_input

word_types = ["adjective", "noun", "verb", "adverb"]

def generate_madlibs_story(user_inputs):
    madlibs_story = ""

    word_type = random.choice(word_types)
    madlibs_story += f"The {word_type} "

    word_type = random.choice(word_types)
    madlibs_story += f"{word_type} in the city.\n"

    word_type = random.choice(word_types)
    madlibs_story += f"Everyone {word_type} at the concert.\n"

    return madlibs_story

user_inputs = []

for word_type in word_types:
    user_input = get_input(f"Enter a(n) {word_type}: ")
    user_inputs.append(user_input)

madlibs_story = generate_madlibs_story(user_inputs)
print(madlibs_story)

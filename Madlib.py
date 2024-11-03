print("Welcome to the MadLibs game! Please provide the following information:")

# Collecting inputs from the user
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")

# Constructing the MadLibs story
madlibs_story = f"On a sunny day, a very {adjective} {noun} was walking down the street. The {noun} was {verb} {adverb}."

print("\nHere's your MadLibs story:")
print(madlibs_story)

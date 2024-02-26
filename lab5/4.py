from functions import find_matches

pattern = r'.*[A-Z][a-z]+$'
# pattern = r"[A-Z][a-z]+"

find_matches(pattern)

# strings = ["Hello", "aAa", "Goodbye", "openAI", "jaJa"]

# for string in strings:
#     if re.match(pattern, string):
#         print("Match")
#     else:
#         print("No match")

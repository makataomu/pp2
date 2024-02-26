from functions import find_matches

pattern = r"ab{2,3}"

find_matches(pattern)

# strings = ["ab", "abb", "abbb", "ac", "bcb", "abbc"]

# for string in strings:
#   if re.match(pattern, string):
#     print("Match")
#   else:
#     print("No match")

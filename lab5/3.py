from functions import find_matches

pattern = r".*[a-z]+_[a-z]+.*"
# pattern = r"[a-z]+_[a-z]+"

find_matches(pattern)

# strings = ["tair_world", "cole_wolrd", "_m_yWorld", "CamelCase", "abc"]

# for string in strings:
#   if re.match(pattern, string):
#     print("Match")
#   else:
#     print("No match")

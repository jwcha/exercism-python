# Pangram
# Determine if a sentence is a pangram. A pangram is a sentence which uses each
# letter of the alphabet at least once. An example is:
#   "The quick brown fox jumps over the lazy dog."
# The English alphabet consists of ASCII chars 'a' - 'z' (inclusive) and is
# case-insensitive.
# Return True if sentence is a panagram, False otherwise.


def is_pangram(sentence):
    # pass
    if sentence == '':
        return False
    result_set = set()
    alphabet_set = set()
    for i in range(26):
        alphabet_set.add(chr(i+97))
    sentence_set = set(sentence.lower()).intersection(alphabet_set)
    for c in sentence_set:
        result_set.add(c)
    if len(result_set) == 26:
        return True
    else:
        return False

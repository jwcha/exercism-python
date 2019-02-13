# Bob
# Bob is a lackadaisical teenager. In conversation, his responses are very
# limited.
# Bob answers "Sure." if you ask him a question.
# He answers "Whoa, chill out!" if you yell at him.
# He answers "Calm down, I know what I'm doing!" if you yell a question at him.
# He says "Fine. Be that way!" if you address him without saying anything.
# He answers "Whatever." to anything else.


def hey(phrase):
    if phrase.strip().endswith('?'):
        if phrase.isupper():
            # He answers "Calm down, I know what I'm doing!" if you yell a question at him.
            return "Calm down, I know what I'm doing!"
        # Bob answers "Sure." if you ask him a question.
        return "Sure."
    elif phrase.isupper():
        # He answers "Whoa, chill out!" if you yell at him.
        return "Whoa, chill out!"
    elif phrase.isspace() or phrase == "":
        # He says "Fine. Be that way!" if you address him without saying anything.
        return "Fine. Be that way!"
    else:
        # He answers "Whatever." to anything else.
        return "Whatever."

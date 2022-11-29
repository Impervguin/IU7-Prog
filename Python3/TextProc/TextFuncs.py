PUNCTION = ",:;.!?"
END_SENTENCE_SYMB = "!&."
CONSORNANTS = "QWRTPSDFGHJKLZXCVBNMЦКНГШЩЗХЪФВПРЛДЖЧСМТБ"

def get_word_without_punction(word):
    if len(word) < 1:
        return word
    while word[-1] in PUNCTION:
        word = word[:-1]
    return word


def get_punction_without_word(word):
    punc = ""
    if len(word) < 1:
        return word
    for el in word:
        if el in PUNCTION:
            punc = punc + el
    return punc

part_two = True


def word_is_duplicated(word, word_set):
    if part_two:
        word_letters = sorted(list(word))
        for other_word in word_set:
            if len(word) == len(other_word):
                other_word_letters = list(other_word)
                if word_letters == sorted(other_word_letters):
                    return True
        return False
    else:
        return word in word_set


def passphrase_is_valid(passphrase):
    words = passphrase.split()
    word_set = set()
    for word in words:
        if word_is_duplicated(word, word_set):
            return False
        else:
            word_set.add(word)
    return True


def count_valid_passphrases(phrase_list):
    phrases = phrase_list.split("\n")
    valid_count = 0
    for phrase in phrases:
        if passphrase_is_valid(phrase):
            valid_count += 1

    return valid_count
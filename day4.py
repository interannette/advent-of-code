def passphrase_is_valid(passphrase):
    words = passphrase.split()
    word_set = set()
    for word in words:
        if word in word_set:
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

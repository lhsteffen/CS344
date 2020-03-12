'''
This file implements a SPAM/HAM filter based on the example provided for
the second homework of CS-344: Artificial Intelligence.

@author: lhs3
@version: Mar 11, 2020
'''

spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]


def get_all_words(list1, list2):
    words = []
    for word in list1:
        if word not in words:
            words.append(word)
    for word in list2:
        if word not in words:
            words.append(word)
    return words


def get_lists_in_corpus(corpus):
    count = 0
    for l in corpus:
        count += 1
    return count


def flatten_list(corpus):
    flattened = []
    for email in corpus:
        for word in email:
            flattened.append(word)
    return flattened


def get_word_count(corpus):
    word_count = {}
    for word in corpus:
        count = 0
        for check in corpus:
            if check == word:
                count += 1
        word_count[word] = count
    return word_count


def get_word_spam_probability(word, good, bad, nbad, ngood):
    if word in good.keys():
        good_value = 2 * good[word]
    else:
        good_value = 0
    if word in bad.keys():
        bad_value = bad[word]
    else:
        bad_value = 0
    if good_value + bad_value > 1:
        return max(0.01, min(0.99, min(1.0, bad_value/nbad) / (min(1.0, good_value/ngood) + min(1.0, bad_value/nbad))))
    else:
        return 0


def is_email_spam(email, probabilities):
    product = 1
    complement = 1
    for w in email:
        product = product * probabilities[w]
        complement = complement * (1 - probabilities[w])
    return product / (product + complement)


ham_count = get_word_count(flatten_list(ham_corpus))
spam_count = get_word_count(flatten_list(spam_corpus))
ham_emails = get_lists_in_corpus(ham_corpus)
spam_emails = get_lists_in_corpus(spam_corpus)
all_words = get_all_words(flatten_list(ham_corpus), flatten_list(spam_corpus))

probabilities = {}
for word in all_words:
    probabilities[word] = get_word_spam_probability(word, ham_count, spam_count, 2, 2)

email_number = 0
for email in spam_corpus:
    email_number += 1
    print("Spam probability for spam email number " + str(email_number) + " is: " + str(is_email_spam(email, probabilities)))

print("\n")
email_number = 0
for email in ham_corpus:
    email_number += 1
    print("Spam probability for ham email number " + str(email_number) + " is: " + str(is_email_spam(email, probabilities)))


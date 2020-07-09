# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "her", "herself"]
test_terms = ["learning algorithms", "whiskey", "foxtrot", "she", "her", "herself", "nowhere", "steve"]
test_email = "she her whiskey foxtrot learning algorithms random words for testing. her! researchers! herself learning Tango"

def censor_word(word, email):
    if word.lower() in email.lower():
        email = email.replace(word.lower(), "*" * len(word))
    return email


def censor_proprietary_terms(terms, email):
    censor_list = email.split(" ")
    print(censor_list)
    for word in censor_list:
        for bad_word in terms:
            if bad_word == word:
                index = censor_list.index(word)
                censor_list[index] = "*" * len(bad_word)
            elif bad_word == word[:-1]:
                punctuation = word[-1]
                index = censor_list.index(word)
                censor_list[index] = "*" * len(bad_word) + punctuation

    censored_email = " ".join(censor_list)
    print(censored_email)

censor_proprietary_terms(test_terms, test_email)
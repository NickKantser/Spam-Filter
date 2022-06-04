from utils import SPAM_TAG, HAM_TAG
from collections import Counter
from corpus import Corpus
import random
import math
import os

class BaseFilter:

    def __init__(self):
        self.is_trained = False
        self.num_of_spam_words = 0
        self.num_of_ham_words = 0
        self.num_of_spam_emails = 0
        self.num_of_ham_emails = 0
        self.unique_words = Counter()
        self.spam_words = Counter()
        self.ham_words = Counter()

    def test(self, test_dir):
            predictions = {}
            c = Corpus(test_dir)

            with open(os.path.join(test_dir, "!prediction.txt"), "w", encoding="utf-8") as file:

                for filename, email_body in c.emails():
                    my_prediction = self.classify(email_body)
                    predictions[filename] = my_prediction
                    file.write(filename + " " + my_prediction + "\n")


    def classify(self, email_body):
        if self.is_trained:
            clear_email = self.data_clearing(email_body)
            #========== calculate by formula ==========#
            p_spam = math.log(self.num_of_spam_emails /
                         (self.num_of_spam_emails + self.num_of_ham_emails))
            p_ham = math.log(self.num_of_ham_emails /
                        (self.num_of_spam_emails + self.num_of_ham_emails))
            p_words_spam = self.p_words_spam(clear_email)
            p_words_ham = self.p_words_ham(clear_email)
            probability_of_spam = p_spam + p_words_spam
            probability_of_ham = p_ham + p_words_ham

            if probability_of_spam > probability_of_ham:
                return SPAM_TAG
            else:
                return HAM_TAG
        else:
            return random.choice([SPAM_TAG, HAM_TAG])

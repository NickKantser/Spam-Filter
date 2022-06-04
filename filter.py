from utils import SPAM_TAG, HAM_TAG, read_classification_from_file, STOP_WORDS
from basefilter import BaseFilter
import string
import math
import os
import re

class MyFilter(BaseFilter):
    # clearing email body from punctuations, numbers and other symbols
    def data_clearing(self, email_body):
        content = email_body.lower()
        content = content.replace("\n", "") # removing new lines
        # removing unnecessary symbols
        content = re.sub("[0-9()_?]+", "", content)
        content = re.sub("[.!]+", " ", content)
        clear_content = content.split()
        clear_data = []

        # creating new clear_content without stop words and save it in clear_data
        for item in clear_content:
            if item not in STOP_WORDS:
                clear_data.append(item)


        return clear_data


    def p_words_spam(self, email_body):
        sum = 0
        len_unique_words = len(self.unique_words)

        for word in email_body:
            if word in self.spam_words:
                nominator = self.spam_words[word] + 1
            else:
                nominator = 1

            denominator = self.num_of_spam_words + len_unique_words
            sum += math.log(nominator / denominator)

        return sum

    def p_words_ham(self, email_body):
        sum = 0
        len_unique_words = len(self.unique_words)

        for word in email_body:
            if word in self.ham_words:
                nominator = self.ham_words[word] + 1
            else:
                nominator = 1

            denominator = self.num_of_ham_words + len_unique_words
            sum += math.log(nominator / denominator)

        return sum

    def train(self, training_dir):
        # dictionary of emails and its classification
        # (e.g. "name of email": classification)
        emails_classification = read_classification_from_file(os.path.join(training_dir, "!truth.txt"))

        for email in emails_classification:
            with open(os.path.join(training_dir, email), "r", encoding="utf-8") as filename:
                clear_content = self.data_clearing(filename.read())
                self.unique_words.update(clear_content)

                if emails_classification[email] == SPAM_TAG:
                    self.num_of_spam_emails += 1
                    self.num_of_spam_words += len(clear_content)
                    self.spam_words.update(clear_content)
                elif emails_classification[email] == HAM_TAG:
                    self.num_of_ham_emails += 1
                    self.num_of_ham_words += len(clear_content)
                    self.ham_words.update(clear_content)

        self.is_trained = True

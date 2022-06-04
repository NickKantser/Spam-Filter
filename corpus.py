import os

class Corpus:

    def __init__(self, path_to_directory):
        self.path = path_to_directory

    def emails(self):
        filenames = os.listdir(self.path)

        for filename in filenames:
            if filename[0] == "!":
                continue
            with open(self.path + "/" + filename, "r", encoding="utf-8") as file:
                email_body = file.read()
                yield filename, email_body

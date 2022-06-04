STOP_WORDS = ["a", "for", "to", "the", "and", "of", "from"]
SPAM_TAG = "SPAM"
HAM_TAG = "OK"

def read_classification_from_file(filepath):
    dictionary = {}

    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        lines = content.split("\n")

        # set to dictionary "key"<--filename and "value"<--classification
        for line in lines:
            line_content = line.split(" ")
            if len(line_content) == 2:
                filename = line_content[0]
                classification = line_content[1]
                dictionary[filename] = classification

    return dictionary

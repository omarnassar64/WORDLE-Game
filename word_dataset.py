def load_words(file_path="words.txt"):
    with open(file_path, "r") as f:
        return f.read().splitlines()

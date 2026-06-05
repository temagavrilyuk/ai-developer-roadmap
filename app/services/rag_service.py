def load_kiberlab_context():
    with open("app/data/kiberlab.txt", "r", encoding="utf-8") as file:
        return file.read()
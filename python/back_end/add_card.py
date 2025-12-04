import os

DATA_FOLDER = os.path.abspath("data")
def add_card():
    #def that adds cards to database
    test_file_path = os.path.join(DATA_FOLDER, "test.txt")
    with open(test_file_path, "r") as f:
        content = f.read()
    
    print(content)
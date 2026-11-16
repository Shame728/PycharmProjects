import pickle


def load_table(file_path):
    with open(file_path, mode='rb') as file:
        table = pickle.load(file)
    return table

def save_table(table, file_path):
    with open(file_path, mode='wb') as file:
        pickle.dump(table, file)
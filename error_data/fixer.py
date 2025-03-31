def _is_row_complete(row):
    """
    Funkcja, która sprawdza, czy dany wiersz pliku CSV jest kompletny, czy nie
    """
    bad_words = ['undefined', 'null']
    split = row.split(",")
    for item in split:
        if item.lower() in bad_words:
            return True
    return False


def generate_complete_file(bad_path, new_path):
    """
    Funkcja, która generuje plik, który zawiera tylko kompletne wiersze na podstawie "surowego" pliku csv
    """
    with open(bad_path, 'r') as bad_file:
        with open(new_path, 'w') as good_file:
            lines = bad_file.readlines()
            for line in lines:
                content = line.rstrip()
                if not _is_row_complete(content):
                    good_file.write(content + "\n")

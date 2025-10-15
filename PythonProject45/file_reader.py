import csv

def read_csv_files(file_paths):
    """
    Читает несколько CSV файлов и возвращает все данные
    """
    all_data = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Преобразуем rating в число
                row['rating'] = float(row['rating'])
                all_data.append(row)
    return all_data

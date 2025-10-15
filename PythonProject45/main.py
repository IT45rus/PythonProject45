import argparse
from tabulate import tabulate
from file_reader import read_csv_files
from report_generator import calculate_average_rating

def main():
    # Обрабатываем аргументы командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+', required=True)
    parser.add_argument('--report', required=True)
    args = parser.parse_args()
    
    # Читаем файлы
    data = read_csv_files(args.files)
    
    # Генерируем отчет
    if args.report == 'average-rating':
        report_data = calculate_average_rating(data)
    
    # Выводим таблицу
    headers = ["#", "brand", "rating"]
    table_data = []
    for i, row in enumerate(report_data):
        table_data.append([i+1, row['brand'], row['rating']])
    
    print(tabulate(table_data, headers=headers, tablefmt="pretty"))

if __name__ == "__main__":
    main()

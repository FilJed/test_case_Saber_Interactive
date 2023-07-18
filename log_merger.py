import argparse
import json

# Парсинг аргументов командной строки
parser = argparse.ArgumentParser()
parser.add_argument("input_files", nargs=2, help="Paths to input log files")
parser.add_argument("-o", "--output_file", help="Path to output merged log file")
args = parser.parse_args()

# Открытие файлов в режиме чтения и записи
with open(args.input_files[0], "r") as file_a, open(args.input_files[1], "r") as file_b, open(args.output_file, "w") as output_file:
    record_a = json.loads(file_a.readline())
    record_b = json.loads(file_b.readline())

    while record_a and record_b:
        if record_a["timestamp"] <= record_b["timestamp"]:
            output_file.write(json.dumps(record_a) + "\n")
            record_a = json.loads(file_a.readline())
        else:
            output_file.write(json.dumps(record_b) + "\n")
            record_b = json.loads(file_b.readline())

    # Добавление оставшихся записей из первого файла, если они есть
    while record_a:
        output_file.write(json.dumps(record_a) + "\n")
        record_a = json.loads(file_a.readline())

    # Добавление оставшихся записей из второго файла, если они есть
    while record_b:
        output_file.write(json.dumps(record_b) + "\n")
        record_b = json.loads(file_b.readline())
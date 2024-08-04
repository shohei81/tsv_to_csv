import csv
import os
import sys

# フィールドサイズの上限を引き上げる
csv.field_size_limit(sys.maxsize)

def tsv_to_csv(tsv_file, csv_file):
    with open(tsv_file, 'r', newline='', encoding='utf-8') as tsv_input:
        with open(csv_file, 'w', newline='', encoding='utf-8') as csv_output:
            tsv_reader = csv.reader(tsv_input, delimiter='\t')
            csv_writer = csv.writer(csv_output)
            
            for row in tsv_reader:
                csv_writer.writerow(row)

def convert_multiple_files(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(input_directory):
        if filename.endswith(".tsv"):
            tsv_path = os.path.join(input_directory, filename)
            csv_filename = filename[:-4] + ".csv"
            csv_path = os.path.join(output_directory, csv_filename)
            tsv_to_csv(tsv_path, csv_path)
            print(f"Converted {filename} to {csv_filename}")

# 使用例
input_dir = "/Users/shoheiyoshida/Downloads/hpb_dataset"
output_dir = "/Users/shoheiyoshida/Downloads/hpb_dataset_csv"
convert_multiple_files(input_dir, output_dir)
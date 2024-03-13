import os
import csv

def generate_csv(root_dir, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['cat', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for root, dirs, files in os.walk(root_dir):
            for file in files:
                writer.writerow({'cat': os.path.basename(root), 'name': file})

# Example usage:
root_directory = os.getcwd()
output_csv = 'output.csv'
generate_csv(root_directory, output_csv)
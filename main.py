import csv
from datetime import datetime

csv_file_name = "AIS_2023_01_01.csv"

def print_first_10_lines_csv(csv_file_name):
    matched_count = 0
    matched_time_count = 0
    matched_length_sum = 0

    with open(csv_file_name, mode='r') as file:
        csv_reader =  csv.DictReader(file)

        print("First 10 lines of the CSV file:")
        for i, row in enumerate(csv_reader):
            # print(row)
            if i == 9:
                break

        file.seek(0)
        next(csv_reader)

        for row in csv_reader:
            if 'TERRY GIFFORD' in row.get('VesselName', ''):
                matched_count += 1
                time_field = row.get ('BaseDateTime')
                length_field = row.get('Length')

                try:
                    time_obj = datetime.strptime(time_field.split(',')[0], '%Y-%m-%dT%H:%M:%S')

                    if time_obj.hour == 15:
                        matched_time_count +=1 

                        matched_length_sum += int(length_field)
                except Exception as e:
                    print(f"Error parsing length")

    print("\nAnalysis Results:")
    print(f"Lines with TERRY GIFFORD : {matched_count}")
    print(f"Instances between 3pm and 4pm: {matched_time_count}")
    print(f"Total 'length' field for matched lines: {matched_length_sum}")



print_first_10_lines_csv(csv_file_name)



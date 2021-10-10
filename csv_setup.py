import time
import csv
import pathlib


def elapsed_time_formatted(begin_time):
    """
    Calculates difference between begin_time and actual time,
    and formats it in HH:MM:SS:ms.
    :param begin_time: time we want to compare with, in seconds.
    """
    return time.strftime(
        "%H:%M:%S", (time.gmtime(time.perf_counter() - begin_time))
    )


def create_csv(file_name, csv_content):
    """Create csv file with a list of lists.
    :param file_name: name of the csv file.
    :param csv_content: a list of lists of information.
    """
    with open(
            pathlib.Path.cwd() / 'data' / file_name, 'w', newline='', encoding='utf-8-sig'
    ) as f:
        for k in range(0, len(csv_content)):
            csv.writer(f).writerow(csv_content[k])


def extract_and_clean_csv(file_name):
    """Extract all valid information from csv.
    :return: a list of lists of all valid rows.
    """
    with open(pathlib.Path.cwd() / 'data' / file_name, 'r', encoding='utf-8') as f:
        content = csv.reader(f)
        cleaned_csv = []
        header = True
        for row in content:
            if header:
                cleaned_csv.append(row)
                header = False
            else:
                row_results = []
                sum_salary = 0
                for column in row:
                    row_results.append(column)
                # Selects and sums payment columns from original CSV file streamer line excluding indexes 0,1 and 11.
                # Index 0 is user_id, index 1 is payout_entity_id, index 11 is report_date.
                for j in range(2, len(row_results)):
                    if j != 11:
                        sum_salary += int(float(row_results[j]) * 100)
                if sum_salary != 0:
                    cleaned_csv.append(row)
    return cleaned_csv


def main():
    """
    Remove all "0" lines in all CSVs files in data folder.
    """
    start = time.perf_counter()

    for year in range(19, 22):
        if year == 19:
            first_month = 8
            last_month = 12
        elif year == 20:
            first_month = 1
            last_month = 12
        elif year == 21:
            first_month = 1
            last_month = 10

        for i in range(first_month, last_month + 1):
            pay_month = str(i)
            if len(pay_month) == 1:
                pay_month = "0" + pay_month

            file_name = f"all_revenues_{year}_{pay_month}.csv"

            print(f"Processing with {file_name}, please wait...")

            create_csv(file_name, extract_and_clean_csv(file_name))

            print(f"Time elapsed: {elapsed_time_formatted(start)}")
            print()

    print(f"Duration of treatment: {elapsed_time_formatted(start)}")


if __name__ == "__main__":
    main()

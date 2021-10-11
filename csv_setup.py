import time
import csv
import pathlib
import gzip
import os


def elapsed_time_formatted(begin_time):
    """
    Calculates difference between begin_time and actual time,
    and formats it in HH:MM:SS:ms.
    :param begin_time: time we want to compare with, in seconds.
    """
    return time.strftime(
        "%H:%M:%S", (time.gmtime(time.perf_counter() - begin_time))
    )


def create_csv(filename, csv_content):
    """Create csv file with a list of lists.
    :param filename: name of the csv file.
    :param csv_content: a list of lists of information.
    """
    os.makedirs(pathlib.Path.cwd() / 'data', exist_ok=True)
    with open(
            pathlib.Path.cwd() / 'data' / filename, 'w', newline='', encoding='utf-8-sig'
    ) as g:
        for row in csv_content:
            csv.writer(g).writerow(row)


def read_and_clean_csv(year, month):
    """Extract all valid information from csv.
    :return: a list of lists of all valid rows.
    """

    filename = f"all_revenues_{year}_{month}.csv"

    print(f"Cleaning {filename}, please wait...")
    print()

    with open(pathlib.Path.cwd() / 'data' / filename, 'r', encoding='utf-8') as f:
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
    create_csv(filename, cleaned_csv)


def export_gzip_to_csv(year, month):
    folder_year = f"20{year}"
    filename = f"all_revenues_{year}_{month}.csv"

    print(f"Importing {filename}, please wait...")
    print()

    if folder_year == "2019" and month == "08":
        final_folder = "28"
    elif folder_year == "2021" and month == "10":
        final_folder = "05"
    else:
        final_folder = "07"

    with gzip.open(pathlib.Path.cwd() / 'twitch-payouts' / 'all_revenues' / folder_year / month / final_folder / 'all_revenues.csv.gz', mode='rt') as f:
        content = csv.reader(f)
        create_csv(filename, content)


def main():
    print("CSV setup - See README.md for more info")
    print()
    print("1: Import and shrink")
    print("         (Original twitch_payout folder must be placed in root folder.)")
    print("2: Just import")
    print("         (Original twitch_payout folder must be placed in root folder.)")
    print("3: Just shrink already imported files")
    print("         (Files must be in data folder with the right name)")
    print()

    choice = ""
    while choice == "":
        choice = input("Please enter your choice: ")
        if choice != "1" and choice != "2" and choice != "3":
            print("Choice not available")
            print()
            choice = ""

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

        for month in range(first_month, last_month + 1):
            month = str(month)
            if len(month) == 1:
                month = f"0{month}"
            if choice == "1":
                try:
                    export_gzip_to_csv(year, month)
                except FileNotFoundError as e:
                    print(f"Couldn't find all_revenues.csv.gz for {month}/20{year}")
                    print("Please verify twitch_payouts folder is in the good place")
                    print(e)
                try:
                    read_and_clean_csv(year, month)
                except FileNotFoundError as e:
                    print("Files not found, make sure they are imported and in the good place")
                    print(e)
            elif choice == "2":
                try:
                    export_gzip_to_csv(year, month)
                except FileNotFoundError as e:
                    print(f"Couldn't find all_revenues.csv.gz for {month}/20{year}")
                    print("Please verify twitch_payouts folder is in the good place")
                    print(e)
            elif choice == "3":
                try:
                    read_and_clean_csv(year, month)
                except FileNotFoundError as e:
                    print("Files not found, make sure they are imported and in the good place")
                    print(e)

    print(f"Csv successfully imported in {elapsed_time_formatted(start)}")


if __name__ == "__main__":
    main()

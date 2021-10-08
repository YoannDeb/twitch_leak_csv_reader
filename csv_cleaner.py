import tablib
import time

CALENDAR = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}


def elapsed_time_formatted(begin_time):
    """
    Calculates difference between begin_time and actual time,
    and formats it in HH:MM:SS:ms.
    :param begin_time: time we want to compare with, in seconds.
    """
    return time.strftime(
        "%H:%M:%S", (time.gmtime(time.perf_counter() - begin_time))
    )


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
        with open(file_name, mode="r") as file:
            imported_data = tablib.Dataset().load(file.read(), format='csv', headers=True)
            print(f"Length of origin datafile: {len(imported_data)} rows.")
            cleaned_csv = tablib.Dataset()
            cleaned_csv.headers = imported_data.headers
            for row in imported_data:
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
            imported_data = []
        with open(file_name, mode="w", newline='') as file:
            file.write(cleaned_csv.export('csv'))

        print(f"Length of cleaned datafile: {len(cleaned_csv)} rows.")
        cleaned_csv = []
        print(f"Time elapsed: {elapsed_time_formatted(start)}")
        print()

print(f"Duration of treatment: {elapsed_time_formatted(start)}")

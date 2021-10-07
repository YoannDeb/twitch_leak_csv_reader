import tablib
import time
import os

STREAMER_ID = 12345678


def elapsed_time_formatted(begin_time):
    """
    Calculates difference between begin_time and actual time,
    and formats it in HH:MM:SS:ms.
    :param begin_time: time we want to compare with, in seconds.
    """
    return time.strftime(
        "%H:%M:%S", (time.gmtime(time.perf_counter() - begin_time))
    )


def extract_csv(data_file):
    return tablib.Dataset().load(data_file.read(), format='csv', headers=True)


# mois du fichier = paiement du mois précédent (octobre = subs de septembre)
calendar = {
    "01": "December",
    "02": "January",
    "03": "February",
    "04": "March",
    "05": "April",
    "06": "May",
    "07": "June",
    "08": "July",
    "09": "August",
    "10": "September",
    "11": "October",
    "12": "November"
}

start = time.perf_counter()

month = "01"
year = "21"
results = []
for i in range(1, 11):
    month_results = []
    pay_month = str(i + 1)
    if len(pay_month) == 1:
        pay_month = "0" + pay_month
    month = str(i)
    if len(month) == 1:
        month = "0" + month

    with open(f"all_revenues_{month}_{year}.csv") as file:
        imported_data = extract_csv(file)
        print(f"csv imported {elapsed_time_formatted(start)}")
        for row in imported_data:
            if int(row[0]) == STREAMER_ID:
                for column in row:
                    month_results.append(column)
        print(month_results)
        sum_salary = 0
        for j in range(2, len(month_results)):
            if j != 11:
                sum_salary += int(float(month_results[j])*100)
        print(f"Duration of Analysis: {elapsed_time_formatted(start)}")
        print(f"Length of datafile: {len(imported_data)}")
        imported_data = []
    results.append(sum_salary)

    if month == "01":
        complete_year = "20" + (str(int(year) - 1))
    elif month == "12":
        complete_year = "20" + (str(int(year) + 1))
    else:
        complete_year = "20" + year
    print(f"Month of {calendar[month]} {complete_year} (payed in {calendar[pay_month]}): {round(sum_salary/100, 2)}$")
    print()

total = round(sum(results)/100, 2)
average = round(total/10, 2)
print(f"Salary from December 2020 to {calendar[month]} {complete_year}: {total}$")
print(f"Average month salary: {average}$")
print(f"Duration of Analysis: {elapsed_time_formatted(start)}")

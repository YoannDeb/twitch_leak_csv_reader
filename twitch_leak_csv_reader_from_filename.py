import tablib
import time

# Change streamer id here.
# See https://www.streamweasels.com/support/convert-twitch-username-to-user-id/ to find ID from username.
STREAMER_ID = 12345678

# Specify a file name for specific cases, don't forget to put ""
# Example : FILENAME = "all_revenues_19_08.csv"
FILENAME = "all_revenues_21_10.csv"


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


start = time.perf_counter()
active_months_count = 0
nb_of_months = 0
results = []
sum_ad_share_gross = 0
sum_sub_share_gross = 0
sum_bits_share_gross = 0
sum_prime_sub_share_gross = 0
sum_bb_rev_gross = 0
sum_bits_developer_share_gross = 0
sum_bits_extension_share_gross = 0
sum_bit_share_ad_gross = 0
sum_fuel_rev_gross = 0

raw_results = []

print(f"Processing with {FILENAME}, please wait...")
with open(FILENAME) as file:
    imported_data = extract_csv(file)
for row in imported_data:
    if int(row[0]) == STREAMER_ID:
        nb_of_months += 1
        raw_results.append(row)
imported_data = []
sum_salary = 0
# Selects and sums payment columns from original CSV file streamer line excluding indexes 0,1 and 11.
# Index 0 is user_id, index 1 is payout_entity_id, index 11 is report_date.
for month_results in raw_results:
    for j in range(2, len(month_results)):
        if j != 11:
            sum_salary += int(float(month_results[j]) * 100)
    if sum_salary > 0:
        active_months_count += 1
        results.append(sum_salary)

    if sum_salary > 0:
        sum_ad_share_gross += int(float(month_results[2]) * 100)
        sum_sub_share_gross += int(float(month_results[3]) * 100)
        sum_bits_share_gross += int(float(month_results[4]) * 100)
        sum_prime_sub_share_gross += int(float(month_results[7]) * 100)
        sum_bb_rev_gross += int(float(month_results[10]) * 100)
        sum_bits_developer_share_gross += int(float(month_results[5]) * 100)
        sum_bits_extension_share_gross += int(float(month_results[6]) * 100)
        sum_bit_share_ad_gross += int(float(month_results[8]) * 100)
        sum_fuel_rev_gross += int(float(month_results[9]) * 100)

    print(f"Time elapsed: {elapsed_time_formatted(start)}")

    if len(month_results) > 0:
        print(f"Details: ad_share_gross: {month_results[2]}$, "
              f"sub_share_gross: {month_results[3]}$, "
              f"bits_share_gross: {month_results[4]}$, "
              f"prime_sub_share_gross: {month_results[7]}$, "
              f"bb_rev_gross: {month_results[10]}$, "
              f"bits_developer_share_gross: {month_results[5]}$, "
              f"bits_extension_share_gross: {month_results[6]}$, "
              f"bit_share_ad_gross: {month_results[8]}$, "
              f"fuel_rev_gross: {month_results[9]}$")
    print(f"Payout of month n°{nb_of_months}: "
          f"{round(sum_salary / 100, 2)}$")
    print()

if active_months_count == 0:
    active_months_count = 1
if nb_of_months == 0:
    nb_of_months = 1

total = round(sum(results) / 100, 2)
average = round(total / nb_of_months, 2)
average_active_months = round(total / active_months_count, 2)
sum_ad_share_gross = round(sum_ad_share_gross / 100, 2)
sum_sub_share_gross = round(sum_sub_share_gross / 100, 2)
sum_bits_share_gross = round(sum_bits_share_gross / 100, 2)
sum_prime_sub_share_gross = round(sum_prime_sub_share_gross / 100, 2)
sum_bb_rev_gross = round(sum_bb_rev_gross / 100, 2)
sum_bits_developer_share_gross = round(sum_bits_developer_share_gross / 100, 2)
sum_bits_extension_share_gross = round(sum_bits_extension_share_gross / 100, 2)
sum_bit_share_ad_gross = round(sum_bit_share_ad_gross / 100, 2)
sum_fuel_rev_gross = round(sum_fuel_rev_gross / 100, 2)

print(f"Total payout ({active_months_count} active months over {nb_of_months} months): {total}$")

if total > 1:
    print(f"Average month payout: {average}$")
    if average != average_active_months:
        print(f"Average active months payout: {average_active_months}$")
    print(f"Total details: ad_share_gross: {sum_ad_share_gross}$, "
          f"sub_share_gross: {sum_sub_share_gross}$, "
          f"bits_share_gross: {sum_bits_share_gross}$, "
          f"prime_sub_share_gross: {sum_prime_sub_share_gross}$, bb_rev_gross: {sum_bb_rev_gross}$, "
          f"bits_developer_share_gross: {sum_bits_developer_share_gross}$, "
          f"bits_extension_share_gross: {sum_bits_extension_share_gross}$, "
          f"bit_share_ad_gross: {sum_bit_share_ad_gross}$, fuel_rev_gross: {sum_fuel_rev_gross}$")
    print(f"Average month details: ad_share_gross: {round(sum_ad_share_gross / nb_of_months, 2)}$, "
          f"sub_share_gross: {round(sum_sub_share_gross / nb_of_months, 2)}$, "
          f"bits_share_gross: {round(sum_bits_share_gross / nb_of_months, 2)}$, "
          f"prime_sub_share_gross: {round(sum_prime_sub_share_gross / nb_of_months, 2)}$, "
          f"bb_rev_gross: {round(sum_bb_rev_gross / nb_of_months, 2)}$, "
          f"bits_developer_share_gross: {round(sum_bits_developer_share_gross / nb_of_months, 2)}$, "
          f"bits_extension_share_gross: {round(sum_bits_extension_share_gross / nb_of_months, 2)}$, "
          f"bit_share_ad_gross: {round(sum_bit_share_ad_gross / nb_of_months, 2)}$, "
          f"fuel_rev_gross: {round(sum_fuel_rev_gross / nb_of_months, 2)}$")
    if average != average_active_months:
        print(f"Average active month details: ad_share_gross: {round(sum_ad_share_gross / active_months_count, 2)}$, "
              f"sub_share_gross: {round(sum_sub_share_gross / active_months_count, 2)}$, "
              f"bits_share_gross: {round(sum_bits_share_gross / active_months_count, 2)}$, "
              f"prime_sub_share_gross: {round(sum_prime_sub_share_gross / active_months_count, 2)}$, "
              f"bb_rev_gross: {round(sum_bb_rev_gross / active_months_count, 2)}$, "
              f"bits_developer_share_gross: {round(sum_bits_developer_share_gross / active_months_count, 2)}$, "
              f"bits_extension_share_gross: {round(sum_bits_extension_share_gross / active_months_count, 2)}$, "
              f"bit_share_ad_gross: {round(sum_bit_share_ad_gross / active_months_count, 2)}$, "
              f"fuel_rev_gross: {round(sum_fuel_rev_gross / active_months_count, 2)}$")
print(f"Duration of treatment: {elapsed_time_formatted(start)}")

# twitch_leaks_csv_reader
Shows twitch pay for any streamer in a year from Twitch leaked CSV files.

## Data format:

* Needs csv files from twitch leaks (in twitch-leaks-part-one/twitch-payouts/all_revenues/).

* One is needed from each month (seems to be redundant), you can maybe take the slightly bigger one but from my few tests it didn't make any différence...

* Decompress files and rename them allrevenues_yy_mm.csv (for exemple allrevenues_21_01.csv for january 2021) and place it in the same folder than twitch_leaks_csv_reader.py.

## Changing period analyzed :

* The default year is 2021, first month is 1, last month is 10.

* You can replace the year of analysis, the first month and last month by changing the corresponding constants in twitch_leaks.py.

* Those constants are named YEAR, FIRST_MONTH, LAST_MONTH.

* YEAR must be between 2019 and 2020 (actually the program can't handle multiple years at a time, sorry).

* For the year 2019, range is 8 to 12.

* For the year 2020, range is 1 to 12 (complete year).

* For the year 2021, range is 1 to 10.

* Each month is the month of pay, corresponding to the previous month of stream.

## Changing streamer analyzed:

* You can find ID of the streamer with is username using a site like https://www.streamweasels.com/support/convert-twitch-username-to-user-id/ .

* Replace constant STREAMER_ID value at the beginning of twitch_leaks.py with your favorite text editor to the one of the streamer you want. (exemple STREAMER_ID = 12345678)

## Requirements:

* You need tablib and python3

* You can install python 3 from official site : https://www.python.org/

* To install tablib use one of his command (you may consider doing a virtual environment with pipenv for example):

```pip install -r requirements.txt```

or

```pip install tablib```

## Launch analysis:

* On linux or macOS:

'''Python3 twitch_leaks_csv_reader.py'''

* On Windows:

'''Python twitch_leaks_csv_reader.py'''
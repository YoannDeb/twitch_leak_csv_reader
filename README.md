# twitch_leak_csv_reader
Shows twitch pay for any streamer from Twitch leaked CSV files.

## Data format:

* Needs csv files from twitch leaks (in twitch-leaks-part-one/twitch-payouts/all_revenues/).
* One is needed from each month (seems to be redundant), you can maybe take the slightly bigger one but from my few tests it didn't make any difference...
* Decompress files and rename them allrevenues_yy_mm.csv (for exemple allrevenues_21_01.csv for january 2021) and place it in the same folder as twitch_leaks_csv_reader.py.

## Changing period analyzed :

### Analyze all files:

* You can analyze in all files if ALL_FILES value is True (by default).
* all files (allrevenues_19_08.csv to all_revenues_21_10.csv) needs to be present.
* YEAR, FIRST_MONTH, LAST_MONTH will be ignored (see below)

### Analyse a period in a year:

* Set ALL_FILES value to False
* The default year is 2021, the first month is 1, the last month is 10.
* You can replace the year of analysis, the first month and last month by changing the corresponding constants in twitch_leak_csv_reader.py.
* Those constants are named YEAR, FIRST_MONTH, LAST_MONTH.
* YEAR must be between 19 and 21.
* For the year 2019, range is 8 to 12.
* For the year 2020, range is 1 to 12 (complete year).
* For the year 2021, range is 1 to 10.
* Each month is the month of pay, corresponding to the previous month of stream.

## Changing streamer analyzed:

* You can find ID of the streamer with his username using a site like https://www.streamweasels.com/support/convert-twitch-username-to-user-id/ .
* Replace constant STREAMER_ID value at the beginning of twitch_leak_csv_reader.py with your favorite text editor to the one of the streamer you want. (exemple STREAMER_ID = 12345678)

## Requirements:

* You need tablib and python3
* You can install python 3 from official site : https://www.python.org/
* To install tablib use one of his command (you may consider doing a virtual environment with pipenv for example):

```pip install -r requirements.txt```

or

```pip install tablib```

## Launch analysis:

Type in a terminal:

* On linux or macOS:

```Python3 twitch_leak_csv_reader.py```

* On Windows:

```Python twitch_leak_csv_reader.py```

## Clean csv files:

* You can clean csv files of lines with no revenues with csv_cleaner.py. This will improve treatment time of twitch_leak_csv_reader.py and space occupied by CSV files.

* Just run it in a terminal with ALL the files (from allrevenues_19_08.csv to allrevenues_21_10.csv) in the same folder.

* Be patient this should take a while (nearly 25 minutes on my computer).

Type in a terminal:

* On linux or macOS:

```Python3 csv_cleaner.py```

* On Windows:

```Python csv_cleaner.py```
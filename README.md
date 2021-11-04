# twitch_leak_csv_reader
Shows twitch detailled payout for any streamer from Twitch leaked CSV files.
This program executes locally in console.


## Requirements:

* You need python3 (you can install python 3 from official site : https://www.python.org/)
* The original Twitch-payouts folder from the twitch leaks part one.
* requested module (you may consider running a virtuel environment like venv, see https://docs.python.org/3/library/venv.html:
    ```pip install requirements```

## Import and shrink csv files:

* This will import, rename and optionally shrink original gz files into a data folder.
* Original Twitch-payouts folder must be at the root of the project.
* Choose import and shrink or just import.
* Shrinking will delete lines with no revenue, and significantly speed up the parsing process.
* You can also shrink already imported files.
* Once imported you can delete or move the original Twitch-payouts folder

Type in a terminal:

* On linux or macOS:

```Python3 csv_setup.py```

* On Windows:

```Python csv_setup.py```

## Setting analyzed streamer:

### Searching streamer from username (option 1):
* You will need access to twitch API.
* For this you've got to [Register an app](https://dev.twitch.tv/console/apps/create) to get:
 - A twitch client ID
 - A twitch client secret
* You can then enter your ID and Secret for variables TWITCH_ID and TWITCH_SECRET

### Searching streamer from id (option 2):
* No need for twitch ID's
* You can find ID of the streamer with his username using a site like https://www.streamweasels.com/support/convert-twitch-username-to-user-id/ .
* Replace constant STREAMER_ID value at the beginning of twitch_leak_csv_reader.py with your favorite text editor to the one of the streamer you want. (example STREAMER_ID = 12345678)

## Changing period analyzed :

By default it will parse all files

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


## Launch analysis:

Type in a terminal:

* On linux or macOS:

```Python3 twitch_leak_csv_reader.py```

* On Windows:

```Python twitch_leak_csv_reader.py```

Then choose your option in the menu, and enter an ID or username.


## (bêta) Read user info in unique compilation file

* In case you have a compilation file with potentially several times the same user, you can use twitch_leak_csv_reader_from_filename.py

* Just modify constants USER_ID and FILENAME at the beginning of the file before launching.

Example:
```
USER_ID = 12345678
FILENAME = test.csv
```

* Therefore, you won't have month names anymore, you will still have month and active month average.



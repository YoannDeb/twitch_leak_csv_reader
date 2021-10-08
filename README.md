# twitch_leaks_csv_reader
Twitch pay for any streamer in a year

## Data format:

Needs csv files from twitch leaks (in twitch-leaks-part-one/twitch-payouts/all_revenues/2021).
One from each month (seems to be redundant) decompressed and renamed allrevenues_yy_mm.csv (for exemple allrevenues_21_01.csv for january 2021) and placed at the root of the project.

##Changing period analyzed :

By default, the year is 2021, first month is 1, last month is 10
Replace the year of analysis, the first month and last month by changing the corresponding constants in twitch_leaks.py.
Those constants are named YEAR, FIRST_MONTH, LAST_MONTH
YEAR must be between 2019 and 2020.
For the year 2019, range is 8 to 12
For the year 2020, range is 1 to 12 (complete year)
For the year 2021, range is 1 to 10
Each month is the month of pay, corresponding to the previous month of stream

##Changing streamer analyzed:

You can find ID of the streamer with is username using a site like https://www.streamweasels.com/support/convert-twitch-username-to-user-id/ .
Replace constant STREAMER_ID value at the beginning of twitch_leaks.py with your favorite text editor to the one of the streamer you want. (exemple STREAMER_ID = 12345678)

##Requirements:

You need tablib and python3

you can install python 3 from official site : https://www.python.org/

To install tablib you can use this command (you may consider doing a virtual environment with pipenv for example):

```pip install -r requirements.txt```
or
```pip install tablib```
After installing all requirements

##Launch analysis:

On linux or macOS:
'''Python3 twitch_leaks_csv_reader.py'''

On Windows:
'''Python twitch_leaks_csv_reader.py'''
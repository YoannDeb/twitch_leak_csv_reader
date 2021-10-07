# twitch_leaks
Twitch pay for any streamer in 2021

Needs csv files from twitch leaks (in twitch-leaks-part-one\twitch-payouts\all_revenues\2021)
One frome each month (seems to be redundant) decompressed and renamed allrevenues_mm_yy.csv (for exemple allrevenues_01_21.csv for january 2021) and placed at the root of the project.

You can find ID of the streamer with is username using a site like https://www.streamweasels.com/support/convert-twitch-username-to-user-id/ .

replace constant STREAMER_ID value at the beginning of twitch_leaks to the one of the streamer you want. (exemple STREAMER_ID = 12345678)

requirements : tablib and python3

use : pip install -r requirements.txt

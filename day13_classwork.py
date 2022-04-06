# 13. 06.04.2022

import requests
import json

default_url = 'https://open.er-api.com/v6/latest'


def get_latest_currency_rate(currency):
    url = default_url + '/' + currency
    r = requests.get(url)
    # all_data = r.json()
    q_result = r.json().get('result')
    provider = r.json().get('provider')
    timestamp = r.json()['time_last_update_utc']
    rate_data = r.json().get("rates", ())
    print(q_result, '\n', 'Data provider: ', provider)
    print('Actual data for: ' + timestamp)
    for x in rate_data:
        print(x, '-', rate_data[x])



def rate_data_to_file(rate_data):
    with open("rate_ccy.json", mode="w") as output_file:
        json.dump(rate_data, output_file, indent=4)


# print("eur rates for today: ", get_currency('EUR'))

rate_data_to_file(get_latest_currency_rate('AUD'))

get_latest_currency_rate('BGN')


# currency = 'EUR'
# url = default_url + '/' + currency
# r = requests.get(url)
# all_data = r.json()
# rate_data = r.json().get("rates", ())
#
# # print(url)
#
# # print(data)
#
# # Latest EUR exchange rates
# for x in rate_data:
#     print(x, '-', rate_data[x])
#
# print('HUF:', rate_data['HUF'])
#
# with open("all_ccy.json", mode="w") as output_file:
#     json.dump(all_data, output_file, indent=4)
#
# with open("eur_rates.json", mode="w") as output_file:
#     json.dump(rate_data, output_file, indent=4)

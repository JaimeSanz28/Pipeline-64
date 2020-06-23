import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



home_types = ['Condo', 'Bungalow', 'Duplex', 'Flat', 'Terrace/Link', 'Residence', 'Others']
def check_home(home):
    if home not in home_types:
        raise ValueError("Invalid input. Please try one of the following types of home:"+str(home_types))


room_types = list(range(1,17,1))
room_types.append(20)
def check_room(rooms):
    if rooms not in room_types:
        raise ValueError("Invalid input. Please introduce a number between 1 and 16, or 20.")


currency = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD',
       'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP',
       'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD',
       'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO',
       'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD',
       'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF',
       'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL']

def check_curr(curr):
    if curr not in currency:
        raise ValueError("Invalid input. Please introduce a valid currency.")


def openDataSet():
    global data
    data = pd.read_csv("output/data.csv",encoding='cp1252')
    return data


def openDataSetApi():
    global datapi
    datapi = pd.read_csv("output/data_api.csv",encoding='cp1252')
    return datapi
    

def drawMax(home, rooms):
    data_filter = data[data["Property Type"] == f"{home}"]
    print(data_filter[data_filter["Real Rooms"]==rooms])
    x = data_filter[data_filter["Real Rooms"]==rooms]
    column = x["Price"]
    max_price = column.max()
    print ("The most expensive house with thouse attributes costs", max_price, "€")
    return max_price
    

def drawAvg(home, rooms):
    data_filter = data[data["Property Type"] == f"{home}"]
    y = data_filter[data_filter["Real Rooms"]==rooms]
    column = y["Price"]
    avg_price = column.mean()
    print ("The average price for a house with thouse attributes is", avg_price, "€")
    return avg_price


def changeCurr(curr):
    data_filter = data_api[data_api["index"] == f"{curr}"]
    z = data_filter[data_filter["rates"]]
    print f"(The most expensive in {curr} costs)" + max_price*z
    return max_price


    






"""
def plot_chart(home, rooms):
    data_filter = data[data["Property Type"] == f"{home}"]
    info = list(data_filter[f"{rooms}"])

    plt.bar(xxx, labels = "xx", "xx", colors = ['darkorange','darkblue'], edgecolor="white" )
    plt.show()
"""
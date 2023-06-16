#Данная программа позволяет получить данные с базы данных www.alphavantage.co об акциях любой публично тогрующей компании. Для бесплатного плана существуют следующие ограничения: 5 запросов в минуту, 500 запросов в день.

#Импортируем библиотеки
import requests #Для создания запросов
import csv #Для записи в .csv файл (Excel)
import time
from openpyxl import Workbook 

API_KEY = "TSJXCZMP5G2G8KJZ" #Секретный ключ для доступа в базу данных
TIME_TYPE = "Weekly" # Monthly/Weekly/Daily Указвает на временные рамки запроса
# STOCK_NAME = "TSLA" # Наименование акции компаний не всегда соответвствуют названию компаний, которые распоряжаются этими акциями. Например: Tesla -> TLSA, Apple -> AAPL, IBM -> IBM. Наименования можно найти в интернете.
# path = "D:/kooldo/tesla.csv" #Путь, куда будет происходить запись. Выгядеть должно примерно так: path = "C:/stock/apple.csv". Внимание нужно обратить на "/" - он именно прямой, а Windows по дефолту копирует обратный. Если "apple.csv" сущетсвовать не будет, то программа создаст его сама, а если будет, то перезапишет. Программа не рабоатет, когда файл, в который должна происходить запись, открыт. 

def write_toExcel(stockInfo, companyInfo, path):
    workbook =  Workbook()
    sheet = workbook.active
    sheet["A1"] = "Date"
    sheet["B1"] = "Open"
    sheet["C1"] = "Close"
    sheet["D1"] = "High"
    sheet["E1"] = "Low"
    counter = 2
    for x in stockInfo.keys():
        sheet["A" + str(counter)] = x
        sheet["B" + str(counter)] = stockInfo[x]["1. open"]
        sheet["C" + str(counter)] = stockInfo[x]["4. close"]
        sheet["D" + str(counter)] = stockInfo[x]["2. high"]
        sheet["E" + str(counter)] = stockInfo[x]["3. low"]
        counter = counter + 1
    workbook.save(filename=path)
    workbook.close    

def get_stock(STOCK_NAME, path):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_' + TIME_TYPE.upper() + '&symbol=' + STOCK_NAME + '&apikey=' + API_KEY #Запрос данных об акицях.
    r = requests.get(url)
    data = r.json()[TIME_TYPE + " Time Series"]
    r.close()

    url1 = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + STOCK_NAME + '&apikey=' + API_KEY #Запрос данных о самой компании.
    r1 = requests.get(url1)
    data1 = r1.json()
    r1.close()

    write_toExcel(data, data1, path)    



get_stock("MSFT", "MSFT.xlsx") 
time.sleep(70)
get_stock("AAPL", "AAPL.xlsx")
get_stock("WMT", "WMT.xlsx")
time.sleep(70)
get_stock("CVX", "CVX.xlsx")
get_stock("TM", "TM.xlsx")
time.sleep(70)
get_stock("SEB", "SEB.xlsx")
get_stock("INTC", "INTC.xlsx")
time.sleep(70)
get_stock("BABA", "BABA.xlsx")
get_stock("AMZN", "AMZN.xlsx")
time.sleep(70)
get_stock("NKE", "NKE.xlsx")
get_stock("NVDA", "NVDA.xlsx")

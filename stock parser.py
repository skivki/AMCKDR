#Данная программа позволяет получить данные с базы данных www.alphavantage.co об акциях любой публично тогрующей компании. Для бесплатного плана существуют следующие ограничения: 5 запросов в минуту, 500 запросов в день.

#Импортируем библиотеки
import requests #Для создания запросов
import csv #Для записи в .csv файл (Excel)
import time

API_KEY = "TSJXCZMP5G2G8KJZ" #Секретный ключ для доступа в базу данных
TIME_TYPE = "Weekly" # Monthly/Weekly/Daily Указвает на временные рамки запроса
# STOCK_NAME = "TSLA" # Наименование акции компаний не всегда соответвствуют названию компаний, которые распоряжаются этими акциями. Например: Tesla -> TLSA, Apple -> AAPL, IBM -> IBM. Наименования можно найти в интернете.
# path = "D:/kooldo/tesla.csv" #Путь, куда будет происходить запись. Выгядеть должно примерно так: path = "C:/stock/apple.csv". Внимание нужно обратить на "/" - он именно прямой, а Windows по дефолту копирует обратный. Если "apple.csv" сущетсвовать не будет, то программа создаст его сама, а если будет, то перезапишет. Программа не рабоатет, когда файл, в который должна происходить запись, открыт. 


def get_stock(STOCK_NAME, path):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_' + TIME_TYPE.upper() + '&symbol=' + STOCK_NAME + '&apikey=' + API_KEY #Запрос данных об акицях.
    r = requests.get(url)
    data = r.json()
    r.close()

    url1 = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + STOCK_NAME + '&apikey=' + API_KEY #Запрос данных о самой компании.
    r1 = requests.get(url1)
    data1 = r1.json()
    r1.close()

    with open(path, 'w') as csvfile: #Запись в .csv файл
        filewriter = csv.writer(csvfile, delimiter=';', dialect="excel", quoting=csv.QUOTE_ALL, lineterminator = '\n')
        filewriter.writerow(['Date', 'Open', 'Close', "High", "Low", "Symbol"]) #Кириллицу не воспринимает, поэтому используем латиницу.
        descriptorAdd = True
        for x in data[TIME_TYPE + " Time Series"].keys():
            info = data[TIME_TYPE + " Time Series"][x]
            if descriptorAdd:
                filewriter.writerow([x, info["1. open"], info["4. close"], info["2. high"], info["3. low"], data1["Symbol"]])
                descriptorAdd = False
            filewriter.writerow([x, info["1. open"], info["4. close"], info["2. high"], info["3. low"]])
        csvfile.close()

get_stock("TSLA", "TSLA.csv")
get_stock("MSFT", "MSFT.csv") 
time.sleep(70)
get_stock("AAPL", "AAPL.csv")
get_stock("WMT", "WMT.csv")
time.sleep(70)
get_stock("CVX", "CVX.csv")
get_stock("TM", "TM.csv")
time.sleep(70)
get_stock("SEB", "SEB.csv")
get_stock("JNJ", "JNJ.csv")
time.sleep(70)
get_stock("BABA", "BABA.csv")
get_stock("CMG", "CMG.csv")
time.sleep(70)
get_stock("NKE", "NKE.csv")
get_stock("V", "V.csv")

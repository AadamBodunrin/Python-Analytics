"""
Modify the following get_pnl and get_price so that :
get_price returns the actual price from google finance and
get_pnl returns a dictionary with the company name as the key and the gain as the value
Example :

get_pnl()

should return(format, values will differ):

{'Alphabet, Inc.': -3105.0,
 'Apple, Inc.': 60110.0,
 'General Electric': 12095.0,
 'Goldman Sachs': 112416.5}

Note:
To connect to your MySQL database you have to get your credentials.
Complete your Host, password, user and name as string in the startercode below.

Use the provided HTM files to get the stock price from each company!
You can open them with:

filename="AAPL.htm"
with open(filename, 'r') as f:
    response_page = BeautifulSoup(f, 'lxml')

"""

import pymysql as conn

User = "root"
Name = "WhatYouWant"
Host = "localhost"
password = "######" #Change the password and the database


"""
Do Not Change!!

"""
db = conn.connect(host = Host, user = User, password = password, database = Name )
cursor = db.cursor()

file = "portfolio.txt"
with open(file,'r') as f:
    line_count = 0
    stocks_set = set()
    for line in f:
        line = line.strip()

        if line_count == 0:
            headers = line.split(':')
            headers = [x.replace(' ','_') for x in headers]
            query1 = "DROP TABLE IF EXISTS stocks;"
            query2 = "DROP TABLE IF EXISTS holdings"
            cursor.execute(query1)
            cursor.execute(query2)
            query1 = "CREATE TABLE IF NOT EXISTS stocks ("
            query1 += headers[0] + " VARCHAR(10),"
            query1 += headers[1] + " VARCHAR(30));"
            query2 = "CREATE TABLE IF NOT EXISTS holdings ("
            query2 += headers[0] + " VARCHAR(10),"
            query2 += headers[2] + " DECIMAL(10,2),"
            query2 += headers[3] + " INT,"
            query2 += headers[4] + " DATE);"
            cursor.execute(query1)
            cursor.execute(query2)
            line_count += 1
            continue        
        data = line.split(':')
        stock_info = (data[0],data[1])
        stocks_set.add(stock_info)
        holdings_query = 'INSERT INTO holdings VALUES ("'
        holdings_query +=data[0] + '",'
        holdings_query +=data[2] + ','
        holdings_query +=data[3] + ',"'
        holdings_query +=data[4] + '");'
        cursor.execute(holdings_query)
for s_info in stocks_set:
    stock_query = 'INSERT INTO stocks VALUES ("'
    stock_query += s_info[0] + '","'
    stock_query += s_info[1] +'");'
    cursor.execute(stock_query)
db.commit()
db.close()



"""
Change get_pnl and get_price

"""

def get_pnl():
    import pymysql as conn
    gain_dict = dict() #Empty dictionary

    db = conn.connect(host = Host, user = User, password = password, database = Name ) #Connect to the database
    cursor = db.cursor() #Create a cursor

    #A query to get the information we are looking for
    query = 'SELECT h.ticker, company_name, purchase_price, shares, purchase_date FROM holdings as h INNER JOIN stocks as s on h.ticker = s.ticker ORDER BY purchase_date;'
    cursor.execute(query) #Run the query
    data = cursor.fetchall() #this returns all the results
 
    #Iterate over the data table and calculate gain
    for item in data:
        for info in item:
            if info == item[0]:
                gain = (get_price(info)*float(item[3]))-(float(item[2])* item[3])
                gain = round(gain, 1)
                gain_dict[item[1]] = gain
    return gain_dict  


def get_price(ticker):
    from bs4 import BeautifulSoup #Import the Beautiful soup library

    try:
        url = open(ticker + ".html", "r", encoding = "utf-8").read() #get url locally
        page = BeautifulSoup(url, features="lxml") #parse the url as a lxml
        value_raw = page.find("span", class_ = "IsqQVc").get_text()  #collect the value of the ticker 
        value = value_raw.strip("\n").replace(",", "") #replace the comma to change it as an int
        price = float(value) #Convert the price to a float
    
    except:
        return None

    
    return price 

print(get_pnl())
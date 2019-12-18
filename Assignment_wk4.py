def fidelity_sector_report():
    results = dict()    #An empty dictionary
    
    from bs4 import BeautifulSoup
    sectors = ["Communication Services", "Consumer Discretionary", "Consumer Staples", 
    "Energy", "Financials", "Health Care", "Industrials", "Information Technology", 
    "Materials", "Real Estate", "Utilities"]
    
    sectors_dict = dict() #An empty dictionary
    
    for sector in sectors: #Iterate each sector to get url locally
        url = open(sector + " - Fidelity.html", "r", encoding = "utf-8").read()
        stockmarket = BeautifulSoup(url, features="lxml")
        

        #Find the table we need to extract the info we need
        contenttable = stockmarket.find("div", class_ = "sec-fundamentals").find("table", class_ ="data-tbl")

        item_number = [2,6,9] #A list of number for the items we need
        details = dict() #An empty dictionary
        
        #Iterate over the number list to get details and split into key and value
        for i in item_number:
            key = contenttable.find_all("a")[i].get_text().strip(" (TTM)").lower() #To get title, remove other items and strip off unwanted strings
            key = key.replace(" ", "_") #Replace empty space betwween strings
            value = contenttable.find_all("td")[i].get_text().strip() #The other item on each row and strip both left and right

            #Iterate over the value_list to remove signs
            value_list = ["$","B","%"]
            for item in value:
                if item in value_list:
                    value = value.replace(item,"")
            
            details[key] = float(value) #Pair key amd value with value as a float

        
        sectors_dict[sector] = details #Pair key amd value
    results["results"] = sectors_dict   #Pair key amd value
    return results

print(fidelity_sector_report())
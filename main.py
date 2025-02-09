import csv
# Define function to retrieve prices colum in to a list
def get_prices(data):
    """
    Retrieves prices column in to a list

    Args:
        data (str): CSV format data

    Returns:    
        list: list of prices
    """
    prices = [] 
    r = 0 
    for line in data: 
        if r != 0: 
            price_str = line [2] 
            clean_prices = price_str.strip('$') 
            prices.append(float(price_str[1::])) 
        r += 1
            
    return prices   

def get_products(data):
    """
    Retrieves products column in to a list

    Args:
        data (str): CSV format data

    Returns:
        list: list of products
    """
    products = []
    for i in data:
        products.append(i[0])
    return products[1::]
    

def get_expensive(prices):
    """
    Finds the most expensive product of index

    Args:
        prices (list): list of prices

    Returns:
        int: index of most expensive product
    """
    pricesm = [] 
    r = 0 
    for line in prices: 
        if r != 0: 
            price_str = line [2] 
            clean_prices = price_str.strip('$') 
            pricesm.append(float(price_str[1::])) 
        r += 1
    return max(pricesm)
    

# Read data from file
f = open("data.csv", 'r')
reader_data = csv.reader(f)
# a = get_prices(reader_data)
# x = get_products(reader_data)
y = get_expensive(reader_data)
print (y)

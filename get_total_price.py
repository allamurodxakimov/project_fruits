from csv import reader
def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    f=open('fruits.csv')
    data=reader(f)
    for i in data:
        print(i[-1])
print(get_total_price("fruits.csv"))

    
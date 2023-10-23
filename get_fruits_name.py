from csv import reader
def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    f=open("fruits.csv")
    data=reader(f)
    for i in data:
        print(i[0])
print(get_frutis_name("fruits.csv"))

    
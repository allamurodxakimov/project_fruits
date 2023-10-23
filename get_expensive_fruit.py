from csv import reader
def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
    """
    f=open("fruits.csv")
    data=reader(f)
    ls=[]
    lst=[]
    for i in data:
        ls.append(i[-1])
        lst.append(i)
    ls.remove(ls[0])
    for i in range(len(ls)):
        ls[i]=float(ls[i])
    ma=ls[0]
    for i in range(len(ls)):
        if ma<=ls[i]:
            ma=ls[i]
    k=ls.index(ma)
    return lst[k+1][0]
print(get_expensive_fruit("fruits.csv"))



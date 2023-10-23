from csv import reader
def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    # your code here
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
    mi=ls[0]
    for i in range(len(ls)):
        if mi>=ls[i]:
            mi =ls[i]
    k=ls.index(mi)
    return lst[k+1][0]
print(get_cheapest_fruit("fruits.csv"))
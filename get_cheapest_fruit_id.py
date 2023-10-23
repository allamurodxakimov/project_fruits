from csv import reader
import string
def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    f=open("fruits.csv")
    data=reader(f)
    ls=[]
    for i in data:
        ls.append(i[-1])
    ls.remove(ls[0])
    lst=[]
    for i in range(len(ls)):
        lst.append(float(ls[i]))
    mi=lst[0]
    for i in range(len(lst)):
        if mi>=lst[i]:
            mi=lst[i]
    k=lst.index(int(mi))
    return(k+2)
print(get_cheapest_fruit_id("fruits.csv"))
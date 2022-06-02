import datetime


def print_hello(name: str) -> str:
    """"
    Greets the user by name

    Parameters:
        name (str): The name of the user 
    Returns:
        str: The greeting
    """
    
    i = datetime.datetime.now()
    
    timestampStr = i.strftime("%d-%b-%Y (%H:%M:%S.%f)")

    print("todays date in original format "+timestampStr)

    dayofthemonth = i.strftime(" %d ")
    print("day of the month  "+ dayofthemonth)    
    
    dayoftheweek = i.strftime(" %A ")
    print("Day of the week is "+ dayoftheweek)

    month1 = i.strftime(" %B ")
    print("Todays Month "+ month1)

    month = i.strftime(" %m ")
    print("Todays Month "+ month)
    
    year = i.strftime(" %Y ")
    print("Todays Year  "+ year)



print_hello('mamatha')


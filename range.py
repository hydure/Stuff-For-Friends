def myRange(start, stop = None, step = 1):
    
    # Declare the lsit to be returned 
    myList = []

    # If there was only one param passed in
    # make the one param be stop
    if stop is None:
        start, stop = 0, start
    
    while (start < stop):
        myList.append(start)
        start += step
    
    return myList
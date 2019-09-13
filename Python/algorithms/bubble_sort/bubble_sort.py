
def bubble_sort(mylist): #takes a list of numbers
    item = len(mylist)-1
    for i in range(0,item):
        for y in range(0,item):
            if mylist[y]>mylist[y+1]:
                mylist[y],mylist[y+1]=mylist[y+1],mylist[y]
    return mylist









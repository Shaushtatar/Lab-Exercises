#question 1
#Create a program that can take two lists and return a list of their shared numbers and use the lists below to test it. 
#Make sure your new list does not contain duplicates.
list_one = [1, 1, 2, 4, 5, 13, 23, 29, 33, 49, 50, 51, 52, 60]
list_two = [1, 8, 12, 19, 25, 29, 40, 42, 50, 55, 60, 68]
def intersection(l1, l2):
    interlist = []
    for i in l1:
        if i in l2 and i not in interlist:
            interlist.append(i)
    #appends any values in l1 that are also in l2 to our intersection list
    print(interlist)

intersection(list_one, list_two)
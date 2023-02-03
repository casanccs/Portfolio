from random import sample

def stringList_to_list(stringList,n): #m is number of rows, n is number of columns, only works when the numbers are 0 <= i <= 9, and all rows have same number of columns
    newList = []
    temp = []
    j = 0 #iterator for current index of column
    for k, el in enumerate(stringList):
        if el in ['0','1','2','3','4','5','6','7','8','9']:
            temp.append(int(el))
            j += 1
            if j == n: #this means we need to start adding to the next row
                j = 0
                newList.append(temp)
                temp = []
    return newList

test = [1,2,3]
el = sample(test, 2)
print(test)
print(el)
el[0] = 4
print(el)
print(test)
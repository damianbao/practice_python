num = [1,1,2,2,3,3,4,4,5]



new_lst = []
def set_sort(a,b):
    for item in a:
        if item in a and item not in b:
            b.append(item)
    print (b)

set_sort(num,new_lst)

num = [1,1,2,2,3,3,4,4,5]


numbers = set(num)

print (numbers)




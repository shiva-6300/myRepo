def linear_search(array,target):
    for i in array:
        if i == target:
            return 1
    return -1

array = [10,20,30,40,50,60,70,80]
target = 28;

result = linear_search(array,target)

if result == 1:
    print("Element Found In The List")
else:
    print("Sorry...Not Found")


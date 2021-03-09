import random

list_of_elements = [3,4,5,6,4]

def bubbleSort_algorithm(data):
    temp = 0
    for i in range(0,len(data)):
        for j in range(0,len(data)):
            if data[i]< data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    return data

def insertion_sort(data):
    for i in range(0,len(data)):
        for j in range(i+1,len(data)):
            if data[i] > data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    return data

for i in range(0,100):
    i = random.randint(100,200)
    list_of_elements.append(i)
    
#bubbleSort_algorithm(list_of_elements)
#insertion_sort(list_of_elements)
print(list_of_elements)
#print(bubbleSort_algorithm(list_of_elements))
print(insertion_sort(list_of_elements))
#Knapsack Problem
# Array of items with weight and value
# A bag has a maximum weight
# Try to find out the objects to insert to get max value


class Item:
    def __init__(self,value,weight):
        self.value = value
        self.weight = weight



def Knapsack(W, arr):
    arr.sort(key=lambda x:(x.value/x.weight), reverse=True)

    for item in arr:
        print(item.value, item.weight, item.value/item.weight)

    finalvalue = 0.0

    for item in arr:

        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value
        
    return finalvalue


def fractional_knapsack(W, arr):
    arr.sort(key=lambda x:(x.value/x.weight), reverse=True)

    for item in arr:
        print(item.value, item.weight, item.value/item.weight)

    finalvalue = 0.0

    for item in arr:

        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value
        
        else:
            finalvalue += item.value * (W/item.weight)
            break

    return finalvalue


W  = 60
items = [Item(280,40),Item(100,10),Item(120,20),Item(120,24)]

max_val = Knapsack(W,items)

print(f"The maximum value that can be fit in the bag is {max_val}")

max_frac_val = fractional_knapsack(W,items)
print(f"The maximum fractional value that can be fit in the bag is {max_frac_val}")

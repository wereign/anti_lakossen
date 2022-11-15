class Item:
    def __init__(self,name,weight,profit):
        self.name = name
        self.weight = weight
        self.profit = profit
    def __str__(self):
        return f"OBJECT NAME: {self.name} WEIGHT: {self.weight} PROFIT: {self.profit}"
    __repr__ = __str__

list_items = [Item("Guitar",1,1500),Item("Stereo",4,3000),Item("Laptop",3,2000)]

max_weight = 4
table = [[None for columns in range(max_weight)] for rows in range(len(list_items))]

def nice_print(table):
    for row in table:
        print(row)


# Manually fill the first row?

for row in range(len(list_items)):
    print("ROW: ",row)
    for column in range(max_weight):

        if row == 0: # If we're in the first row
            print(column)
            if list_items[row].weight <= column+1: # +1 is for zero indexing
                table[0][column] = list_items[row].profit 
            else:
                table[0][column] = 0
            nice_print(table)
        
        if row > 0:
            w_i = list_items[row].weight
            p_i = list_items[row].profit
            print("Column+1:",column+1)
            print("W_i:",w_i)

            


            # Testing row 2 only
            if column + 1 - w_i > 0:
                print("One")
                table[row][column] = max(table[row-1][column],p_i + table[row-1][column+1-w_i])
            elif column + 1 - w_i == 0:
                print("Two")
                table[row][column] = max(table[row-1][column],p_i )
            else:
                print("Three")
                table[row][column] = table[row-1][column]
            print(table[row][column])
            nice_print(table)



print()
print("After for loop")
nice_print(table)

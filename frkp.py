def fractional_knapsack():
    weights=[10,20,30]
    values=[60,100,120]
    capacity=50
    res=0
    # Pair : [Weight,value]
    for pair in sorted(zip(weights,values), key= lambda x: x[1]/x[0], reverse=True):
        if capacity<=0: # Capacity completed - Bag fully filled 
            break 
        if pair[0]>capacity: # Current's weight with highest value/weight ratio Available Capacity
            res+=int(capacity * (pair[1]/pair[0]))  # Completely fill the bag
            capacity=0
        elif pair[0]<=capacity: # Take the whole object
            res+=pair[1]
            capacity-=pair[0]
    print(res)        

if __name__=="__main__":
    fractional_knapsack()


def fractional_knapsack():
    weights = []
    values = []
# number of elements as input
    n = int(input("Enter number of values : "))
 
# iterating till the range
    for i in range(0, n):
        ele = int(input())
        # adding the element
        values.append(ele)  
        
    m = int(input("Enter number of weights : "))
# iterating till the range
    for j in range(0, m):
        wei = int(input())
        # adding the element
        weights.append(wei)  
    
    capacity=50
    res=0
    # Pair : [Weight,value]
    for pair in sorted(zip(weights,values), key= lambda x: x[1]/x[0], reverse=True):
        if capacity<=0: # Capacity completed - Bag fully filled 
            break 
        if pair[0]>capacity: # Current's weight with highest value/weight ratio Available Capacity
            res+=int(capacity * (pair[1]/pair[0]))  # Completely fill the bag
            capacity=0
        elif pair[0]<=capacity: # Take the whole object
            res+=pair[1]
            capacity-=pair[0]
    print(res)        

if __name__=="__main__":
    fractional_knapsack()



import time
start = time.time()

def fractional_knapsack(items, capacity):
    algo_start = time.time()
    # Calculate the value-to-weight ratio for each item
    item_value_ratio = [(item[1] / item[0], item) for item in items]
    
    # Sort items by value-to-weight ratio in descending order
    item_value_ratio.sort(reverse=True)
    
    total_value = 0  # Total value of selected items
    knapsack = []    # Items selected for the knapsack
    
    for value_per_weight, item in item_value_ratio:
        if capacity >= item[0]:  # If the item can fit entirely
            knapsack.append((item, 1))  # Add the whole item
            total_value += item[1]
            capacity -= item[0]
        else:  # If the item can only fit partially
            fraction = capacity / item[0]
            knapsack.append((item, fraction))  # Add a fraction of the item
            total_value += item[1] * fraction
            break  # The knapsack is now full
    algo_end = time.time()
    algo_exec = (algo_end-algo_start)*10**3
    
    return total_value, knapsack, algo_exec

# Example usage:
# (X, Y): Where X = Item Weight, Y = Item Profit
items = []

n = int(input("How many items to add: "))
for i in range(n):
    print("\nEnter details for item-{}".format(i+1))
    item_w = int(input("Enter item weight: "))
    item_p = int(input("Enter item profit: "))
    items.append((item_w, item_p))
    
print("\nItems are: {}".format(items))
capacity = int(input("Enter capacity: "))
max_value, selected_items, algo_execution_time = fractional_knapsack(items, capacity)

print("\nMaximum value: {}".format(max_value))
print("Selected items:")
for item, fraction in selected_items:
    print("  {}: Fraction = {}".format(item,round(fraction,2)))

end = time.time()
print("\nAlgorithm Execution time is: {}ms".format(algo_execution_time))
print("Program Execution time is: {}ms".format((end-start)*10**3))

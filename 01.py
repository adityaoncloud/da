def solve_knapsack():
    val=[50,100,150,200] #value array
    wt=[8,16,32,40] # Weight array
    W=64
    n=len(val) - 1
    def knapsack(W,n): # (Remaining Weight, Number of items checked)
        #base case
        if n<0 or W<=0:
            return 0
        
        #Higher weight than available
        if wt[n]>W:
            return knapsack(W, n-1)
        
        else:
            return max(val[n] + knapsack(W-wt[n],n-1),knapsack(W,n-1))
            # max(including , not including)
    print(knapsack(W,n))

if __name__=="__main__":
    solve_knapsack()


def solve_knapsack():
    val = []
    wt = []
    n = int(input("Enter number of elements : "))
 
    # iterating till the range
    for i in range(0, n):
        ele = int(input())
        # adding the element
        val.append(ele)  
    m = int(input("Enter number of weights : "))
    for j in range(0, m):
        wei = int(input())
        # adding the element
        wt.append(wei)  
    
    W=64
    n=len(val) - 1
    def knapsack(W,n): # (Remaining Weight, Number of items checked)
        #base case
        if n<0 or W<=0:
            return 0
        
        #Higher weight than available
        if wt[n]>W:
            return knapsack(W, n-1)
        
        else:
            return max(val[n] + knapsack(W-wt[n],n-1),knapsack(W,n-1))
            # max(including , not including)
    print(knapsack(W,n))

if __name__=="__main__":
    solve_knapsack()

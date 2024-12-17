#Fn=Fn−1+Fn−2 F1=F2=1 Given: Positive integers n≤40 and k≤5 .

#Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation,
#    every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair). 
def rabbit(n,k):
    pop=[0]*(n)
    pop[0]=1
    pop[1]=1
    for i in range(2,n):
        pop[i]=pop[i-1]+pop[i-2]*k
        
        
    return pop[n-1]
    
rabbit(35,3) 
        
        
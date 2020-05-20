INT_MIN=-32767
def cutRod(price,n):
    val=[0 for x in range(n+1)]
    for i in range(1,n+1):
        max_val=INT_MIN
        for j in range(i):
            if (max_val < val[j]+priceArr[i-j-1]):
                max_val =  val[j]+priceArr[i-j-1]
            val[i] = max(max_val, priceArr[j])
            pass
    return val[n]

priceArr=[1,5,8,9,10,17,17,20]
size=len(priceArr)
print("Maximum obtainable value is " +str(cutRod(priceArr,size)))

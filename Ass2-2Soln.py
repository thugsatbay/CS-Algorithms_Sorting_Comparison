import sys
def quicksort_Spivot(qPArr,start,end):
    #Creating a stack implementation
    size = end - start + 1
    stack = [0]*(size)
    # initialize stack
    top = -1
 
    # push initial values of stack
    top = top + 1
    stack[top] = start
    top = top + 1
    stack[top] = end
 
    # Keep moving on stack untill it is empty
    while top >= 0:
        #Pop start and end
        end = stack[top]
        top = top - 1
        start = stack[top]
        top = top - 1
        
        ##Adjust pivot
        # index of smaller element than pivot
        i = ( start-1 ) 
        # end pivot        
        pv = qPArr[end]     
        for j in range(start,end,1):
            if   qPArr[j] <= pv:
                # increment index of smaller element
                i = i+1
                qPArr[i],qPArr[j] = qPArr[j],qPArr[i]
        qPArr[i+1],qPArr[end] = qPArr[end],qPArr[i+1]
        pv=i+1
        
        ##Add new subarray to stack
        # If there are elements on left side of pivot, then add them to stack and if there are on the right do the same
        # Allow stack to go in the direction where chances of iteration of sub array converges quickly, adding accordingly
        if abs(start-pv)<abs(pv-end):
            if pv+1 < end:
                top = top + 1
                stack[top] = pv + 1
                top = top + 1
                stack[top] = end
            if pv-1 > start:
                top = top + 1
                stack[top] = start
                top = top + 1
                stack[top] = pv - 1
        else:
            if pv-1 > start:
                top = top + 1
                stack[top] = start
                top = top + 1
                stack[top] = pv - 1
            if pv+1 < end:
                top = top + 1
                stack[top] = pv + 1
                top = top + 1
                stack[top] = end
#sort the array so that it becomes easy to find GQ
def gq(arrGQ):
    quicksort_Spivot(arrGQ,0,len(arrGQ)-1)
    print ("---GQ---")
    #We will calculate index form the behind of the list
    for x in range(len(arrGQ)-1,-1,-1):
        #if item value and index from behind of list containing items is same then intuitively thats the GQ
        if (len(arrGQ)-x)==arrGQ[x]:
            print (arrGQ[x])
            break
        #else once the index is larger than elemnt of array gq is previous index
        elif (len(arrGQ)-x)>=arrGQ[x]:
            print (len(arrGQ)-x-1)
            break
        #if elements are bigger than index and nothing matches nor index becomes greater then GQ is n
        elif x==0:
            print (len(arrGQ))

print ("Enter value Of n : ")
if sys.version_info[0] < 3:
    n = int(raw_input().strip())
else:
    n = int(input().strip())
print ("Enter array : [Example: {1,2,3}]")
if sys.version_info[0] < 3:
    arr = list(map(int,raw_input().strip()[1:-1].strip().split(',')))
else:
    arr = list(map(int,input().strip()[1:-1].strip().split(',')))
if len(arr)==n:
    gq(arr)
else:
    print ("N and array size don't match, can't proceed, validate your input. Exiting Program.")
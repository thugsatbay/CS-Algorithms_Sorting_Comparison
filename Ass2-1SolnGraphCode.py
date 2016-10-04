#--------Library Files----------#
import random
import time
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sys
#--------Library Files----------#



#
##
###I)Insertion Sort
##
#
def insertion_sort(insArr):
    for x in range(0,len(insArr),1):
        valCur=insArr[x]
        pos=x
        while (pos>0 and valCur<insArr[pos-1]):
            insArr[pos]=insArr[pos-1]
            pos-=1
        insArr[pos]=valCur
    return insArr


def insertion_sortREV(insArr):
    for x in range(0,len(insArr),1):
        valCur=insArr[x]
        pos=x
        while (pos>0 and valCur>insArr[pos-1]):
            insArr[pos]=insArr[pos-1]
            pos-=1
        insArr[pos]=valCur
    return insArr



#Since recursion does not goes deep in python using a stack implementation for quicksort
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



def quicksort_Rpivot(qPArr,start,end):
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
 
    ##Adjust pivot
    # Keep moving on stack untill it is empty
    while top >= 0:
        #Pop start and end
        end = stack[top]
        top = top - 1
        start = stack[top]
        top = top - 1
 
        # index of smaller element than pivot
        i = ( start-1 ) 
        # selecting random pivot
        randNo=random.randrange(start,end+1,1)
        qPArr[end],qPArr[randNo]=qPArr[randNo],qPArr[end]
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



#Boolean Value To check python version
print ("Hi, Question 1 - Assignment 2 Algorithm has started, Plotting of graph to compare sorting algorithms will be done. - Gurleen Singh Dhody")
while True:
    print ("There are 4 modules listed as [A,B,C,D] for Question 1 and only 1 module can be run at one time. Press E for exit.")
    if sys.version_info[0] <3:
        response = raw_input("Please enter which part of Question 1 you want to run (Example : A): ")
    else:
        response = input("Please enter which part of Question 1 you want to run (Example : A): ")
    response=response.lower();
  
 

    #
    ##Question 1 Part A
    if response=="a":
        move=[100,150,200,300,400,500,1000,5000,10000,15000]
        plotAlgo1,plotAlgo2=[],[]
        indexT=0
        for x in move:
            val=x
            testSample=random.sample(range(val),val)
            testSample1,testSample2=testSample[:],testSample[:]
            plotAlgo1.append(time.time())
            insertion_sort(testSample1)
            plotAlgo1[indexT]=(abs(plotAlgo1[indexT]-time.time()))
            plotAlgo2.append(time.time())
            quicksort_Spivot(testSample2,0,val-1)
            plotAlgo2[indexT]=(abs(plotAlgo2[indexT]-time.time()))
            indexT+=1
        print("\nTest Sample Size : \n")
        print(move)
        #print (plotAlgo1)
        #print (plotAlgo2)
        plt.plot(move,plotAlgo1,'ro')
        plt.plot(move,plotAlgo1,'r')
        plt.plot(move,plotAlgo2,'bs')
        plt.plot(move,plotAlgo2,'b')
        plt.xlabel("N Sorted Array Size")
        plt.ylabel("Time To Sort")
        red_patch = mpatches.Patch(color='red', label='Insertion Sort Algo')
        blue_patch = mpatches.Patch(color='blue', label='Quick Sort Algo')
        plt.legend(handles=[red_patch,blue_patch],loc=2)
        print (plotAlgo1)
        print (plotAlgo2)
        plt.show()
        


    #
    ##Question 1 Part B
    elif response=="b":
        move=[100,500,1000,5000,10000,25000,50000]
        plotAlgo2,plotAlgo3=[],[]
        indexT=0
        for x in move:
            val=x
            testSample=random.sample(range(val),val)
            testSample1,testSample2=testSample[:],testSample[:]
            plotAlgo2.append(time.time())
            quicksort_Spivot(testSample1,0,val-1)
            plotAlgo2[indexT]=(abs(plotAlgo2[indexT]-time.time()))
            plotAlgo3.append(time.time())
            quicksort_Rpivot(testSample2,0,val-1)
            plotAlgo3[indexT]=(abs(plotAlgo3[indexT]-time.time()))
            indexT+=1
        # print (plotAlgo2)
        # print (plotAlgo3)
        print("\nTest Sample Size : \n")
        print(move)
        plt.plot(move,plotAlgo2,'ro')
        plt.plot(move,plotAlgo2,'r')
        plt.plot(move,plotAlgo3,'bs')
        plt.plot(move,plotAlgo3,'b')
        plt.xlabel("N Sorted Array Size")
        plt.ylabel("Time To Sort")
        red_patch = mpatches.Patch(color='red', label='Quick Sort Algo')
        blue_patch = mpatches.Patch(color='blue', label='Quick Sort Random Algo')
        plt.legend(handles=[red_patch,blue_patch],loc=2)
        print (plotAlgo2)
        print (plotAlgo3)
        plt.show()


    #
    ##Question 1 Part C
    elif response=="c":
        move=[10,100,1000,2500,5000,7500,10000,15000]
        plotAlgo1,plotAlgo2=[],[]
        indexT=0
        for x in move:
            val=x
            testSample=list(range(val))
            testSample1,testSample2=testSample[:],testSample[:]
            plotAlgo1.append(time.time())
            insertion_sort(testSample1)
            plotAlgo1[indexT]=(abs(plotAlgo1[indexT]-time.time()))
            plotAlgo2.append(time.time())
            quicksort_Spivot(testSample2,0,val-1)
            plotAlgo2[indexT]=(abs(plotAlgo2[indexT]-time.time()))
            indexT+=1
        #print plotAlgo1
        #print plotAlgo2
        print("\nTest Sample Size : \n")
        print(move)
        plt.plot(move,plotAlgo1,'ro')
        plt.plot(move,plotAlgo1,'r')
        plt.plot(move,plotAlgo2,'bs')
        plt.plot(move,plotAlgo2,'b')
        plt.xlabel("N Sorted Array Size")
        plt.ylabel("Time To Sort")
        red_patch = mpatches.Patch(color='red', label='Insertion Sort')
        blue_patch = mpatches.Patch(color='blue', label='Quick Sort')
        plt.legend(handles=[red_patch,blue_patch],loc=2)
        print (plotAlgo1)
        print (plotAlgo2)
        plt.show()


    #
    ##Question 1 Part D
    elif response=="d":
        move=[10,100,500,1000,5000,10000,15000,25000]
        plotAlgo1,plotAlgo2=[],[]
        indexT=0
        for x in move:
            val=x
            testSample=list(range(val))
            testSample=insertion_sortREV(testSample)
            testSample1,testSample2=testSample[:],testSample[:]
            plotAlgo1.append(time.time())
            insertion_sort(testSample1)
            plotAlgo1[indexT]=(abs(plotAlgo1[indexT]-time.time()))
            plotAlgo2.append(time.time())
            quicksort_Spivot(testSample2,0,val-1)
            plotAlgo2[indexT]=(abs(plotAlgo2[indexT]-time.time()))
            indexT+=1
        # print (plotAlgo1)
        # print (plotAlgo2)
        print("\nTest Sample Size : \n")
        print(move)
        plt.plot(move,plotAlgo1,'ro')
        plt.plot(move,plotAlgo1,'r')
        plt.plot(move,plotAlgo2,'bs')
        plt.plot(move,plotAlgo2,'b')
        plt.xlabel("N Sorted Array Size")
        plt.ylabel("Time To Sort")
        red_patch = mpatches.Patch(color='red', label='Insertion Sort Algo')
        blue_patch = mpatches.Patch(color='blue', label='Quick Sort Algo')
        plt.legend(handles=[red_patch,blue_patch],loc=2)
        print (plotAlgo1)
        print (plotAlgo2)
        plt.show()


    #
    ##Exit
    elif response=="e":
        break
        
    else:
        print ("Wrong Input. Please try again. Or press E to exit.")

    print("");
    print("");
    print("");
    response=""

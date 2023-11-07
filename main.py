from sorts import *
from Node import Node
import random
from time import perf_counter_ns
from LinkedList import LinkedList
'''
Sara Hrnciar 
CSC 201
Sorting a LL program

sorts several linked lists with merge, quick, optimized bubble, and insertion sort. Puts times in an output file.
'''
f = open("outp.txt","w")
#10 9 5

LL1 = LinkedList() #LL of 50 nodes of rand ints between 1 and 50
for i in range(0,50):
    LL1.append(Node(random.randint(1,50)))

LL2 = LinkedList() #ll of 50 nodes in ascending order
for i in range(0,50):
    LL2.append(Node(i))

LL3 = LinkedList() #ll of 50 node in descending order
for i in range(50,0,-1):
    LL3.append(Node(i))

LL4 = LinkedList() #ll of 500 nodes of rand ints 1-50
for i in range(0,500):
    LL4.append(Node(random.randint(1,50)))

LL5 = LinkedList() #ll of 50 nodes in ascending order
for i in range(0,500):
    LL5.append(Node(i))

LL6 = LinkedList()#ll of 50 nodes in descending order
for i in range(500,0,-1):
    LL6.append(Node(i))

test = Node(4,None)
test.link = Node(5,Node(4,Node(5,None)))
def printRev(n):
        if n.link==None:
            return n
        print(printRev(n.link))

printRev(test)
'''
lists = [LL1,LL2,LL3,LL4,LL5,LL6] #throw them together
num = 0
for list in lists: #sort each list with each method
    num+=1
    meow = perf_counter_ns()
    m = merge(list)
    mstop = perf_counter_ns()

    meow2 = perf_counter_ns()
    i = InsertionSort(list)
    istop = perf_counter_ns()

    meow3 = perf_counter_ns()
    o = OptBubbleSort(list)
    bstop = perf_counter_ns()
    
    meow4 = perf_counter_ns() #quicksort goes last because it actually changes the list itself.
    QuickSort(list,list.getHead(),list.getTail())
    qstop = perf_counter_ns()

    quickTime = f"{float((qstop - meow4)/ 10**6):.{4}f}"
    mergeTime = f"{float((mstop -meow)/ 10**6):.{4}f}"
    bubTime = f"{float((bstop - meow3)/ 10**6):.{4}f}"
    insertTime = f"{float((istop -meow2)/ 10**6):.{4}f}" #chat gpt told me how to do this but this is me making it 4 decimals

    print(m)
    print(i)
    print(o)
    print(list)
    f.write("\n ll#{}\n".format(num)) #check the file to see what these three lines do ;)
    f.write("Quick Sort took {} milliseconds. \nMerge Sort took {} milliseconds. \nOpt Bubble Sort took {} milliseconds. \nInsertion Sort took {} milliseconds.".format(quickTime,mergeTime,bubTime,insertTime))
    f.write("\n\n")


'''
#linear search
#recursive
# def linear_search(L,n,c):
#        if L[c] == n:
#            return c
#        elif c == len(L)-1:
#            return -1
#        else:
#            return linear_search(L,n,c+1)
#non-recursive
def linear_search(L,n,c):     
       for i in L:
           if i == n:
               return c
           elif i != n:
               c += 1
           else:
               return "The number is not in the list."
list1 = [1,5,3,10]
num = 10
count = 0
print(linear_search(list1,num,count))   


#simple sort

def simple_sort(l):
    l_2 = []
    small = 0
    while len(l) > 1:
        count = 0
        small = l[count]
        for i in l:
            if i < small:
                count += 1
                small = l[count]
        l_2.append(small)
        l.remove(small)
    l_2.append(l[0])    
    return l_2

a = simple_sort(list1)
print(a)    
list1 = a
def binary_sort(x,n):
    low = 0
    high = len(x) -1
    
    while low <= high:
        mid = (low+high)//2
        if x[mid] == n:
            return mid
        elif x[mid] < n:
            low = mid + 1
        elif x[mid] > n:
            high = mid - 1
print(binary_sort(list1,num))    
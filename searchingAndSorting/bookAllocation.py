import sys
sys.stdout = open('math/output.txt', 'w')
sys.stdin = open('math/input.txt', 'r')

def isValid(book,k,ans):
    student=1 
    current_page=0
    for i in range(len(books)):
        if current_page+book[i]>ans:
            current_page=book[i]
            student+=1
            if student>k:
                return False 
        else:
            current_page+=book[i]
    return True 

def binarySearch(books,n,k):
    l=0
    r=0
    final_ans=-1
    total_page=sum(books)
    l=books[n-1]
    r=total_page
    while l<=r:
        mid=l+(r-l)//2 
        if isValid(books,k,mid):
            #search in left 
            final_ans=mid 
            r=mid-1 
        else:
            l=mid+1 
    return final_ans
        


for _ in range(int(input())):
    n,k=map(int,input().split())
    books=list(map(int,input().split()))
    print(binarySearch(books,n,k))
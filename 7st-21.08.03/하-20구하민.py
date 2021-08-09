# 치킨 TOP N
# https://www.acmicpc.net/problem/11582

def merge_sort(A,C):
    if len(A)<= 1:return A
    mid = len(A)//2
    left = merge_sort(A[:mid],C)
    right = merge_sort(A[mid:],C)
    return merge(left, right,C)

def merge(left,right,C):
    i=j=0
    sorted_list = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i<len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    if len(sorted_list) == n//m:C+=sorted_list
    return sorted_list


n = int(input()) #학생수
A = list(map(int,input().split())) #정렬해야하는 치킨 수치
m = int(input()) #현재단계에서 정렬중인 회원수

C=[]
merge_sort(A,C)
print(" ".join(str(i) for i in C))

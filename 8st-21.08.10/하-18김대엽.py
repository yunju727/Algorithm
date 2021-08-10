n = int(input())

def fibo(n):
    n1, n2 = 0, 1   # 피보나치 적용할 숫자의 초깃값 (0번째 : 0, 1번째 : 1)

    if n <= 1:   # 0번째 숫자, 1번째 숫자는
        return n    # 피보나치 적용없이 해당 숫자 리턴
    else:
        for _ in range(1,n):   # n-1번 만큼 피보나치 적용하기위해 for문을 돈다
            result = n1+n2    # 피보나치 결과
            n1,n2 = n2, n1+n2   # for문을 다돌고나서 그 다음 피보나치 적용할 숫자를 갱신 (그다음 번쨰로 각각의 숫자가 이동)
    return result

print(fibo(n))
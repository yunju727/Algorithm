# 처음에는 알파벳에 해당하는 값을 넣어주었으나 2 ABC BCA 의 반례를 확인하면
# 합이 가장 큰 수에 높은 수를 넣어주어야한다는 것을 알게됨

dic = {}
li = []
lenli = []
N = int(input())    # 단어의 개수

for i in range(N):  # 단어 입력
    S = input()
    li.append(list(S))
    lenli.append(len(S))

maxlen = max(lenli) # 길이 값 배열
num = 9 # 줄어드는 수
sum = 0 # 결과값을 위한 변수

for index in range(maxlen): # 앞자리 글자부터 체크하기위한 반복문
    for st in li:   # 저장된 배열 반복
        if len(st) < maxlen:    # 배열 길이 맞추기를 위한 조건
            st.insert(0,'0')
        if len(st) >= maxlen - index and len(st) > index and st[index] != '0':    # 현재 길이보다 긴 경우 + 0이 아닌 경우->길이 맞추기
            if st[index] not in dic:  # 알파벳의 값이 존재하지 않는 경우
                dic[st[index]] = 10 ** (maxlen - index - 1)
            else:   # 알파벳의 값이 존재하는 경우
                dic[st[index]] += 10 ** (maxlen - index - 1)

temp = list(dic.values())
temp.sort(reverse=True)
for t in range(len(temp)):
    sum += temp[t]*num
    num-=1
print(sum)

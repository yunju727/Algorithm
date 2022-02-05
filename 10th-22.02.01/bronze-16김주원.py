# O(n^2)
def read(alphabet):
    max_len = 0
    answer = ""

    for word in alphabet:
        if max_len < len(word):
            max_len = len(word)

    for i in range(max_len):
        for j in range(len(alphabet)):
            if len(alphabet[j]) > i:
                answer+=alphabet[j][i]
                
    return answer

alphabet = []
for i in range(5):
    alphabet.append(input())

print(read(alphabet))
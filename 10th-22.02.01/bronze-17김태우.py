sli = []
for i in range(15):
  sli.append("")

for i in range(5):
  t = input().strip()
  for j in range(len(t)):
    sli[j] = sli[j] + t[j]


for i in range(len(sli)):
  print(sli[i],end="")

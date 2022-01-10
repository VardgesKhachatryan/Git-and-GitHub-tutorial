l2 = [4,5,2,3,4,5]

numl2 = 0
suml2 = 0
for i in range(len(l2)):
  if l2[i] % 2 == 0:
    numl2+=1
    suml2+=l2[i]
print(numl2)
print(suml2)


with open('class-0.txt', 'r') as class_0:
    t0 = [line.strip().split(' ') for line in class_0]
with open('class-1.txt', 'r') as class_1:
    t1 = [line.strip().split(' ') for line in class_1]

list0 = []
list1 = []
set0 = set()
set1 = set()

for line in t0:
    for i in line:
        set0.add(i)
        list0.append(i)

for line in t1:
    for i in line:
        set1.add(i)
        list1.append(i)

d = set0 - set1
d1 = set1 - set0
#print(d1)
#print(d)


L = list(d)
L1 = list(d1)
print(L)
print()
print()
print(L1)
if 'david' in L1:
    print('yesyes')
dic = {}
for i in L:
    if i not in dic:
        dic[i] = list0.count(i)
    else:
        continue
dic1 = {}
for i in L1:
    if i not in dic1:
        dic1[i] = list1.count(i)
    else:
        continue

final=[]
final1 = []

for i in sorted(dic.items(), key = lambda x:x[1], reverse = True):
    final.append(i[0])
#print(final)
print()
for i in sorted(dic1.items(), key = lambda x:x[1], reverse = True):
    final1.append(i[0])
#print(final1)

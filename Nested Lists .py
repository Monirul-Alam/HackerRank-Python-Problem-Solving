
student=list()

for item in range(int(input())):
    name = input()
    score = float(input())
    student.append([name,score])

only_score =[]

for i in student:
    for j in range(len(i)):
        only_score.append(i[1])
        break
b =set(only_score)
b.remove(min(b))

second_lowest = min(b)

lowest_scorer =[]
for i in student:
    if i[1] == second_lowest:
        lowest_scorer.append(i[0])
lowest_scorer.sort()
for item in lowest_scorer:
    print(item)
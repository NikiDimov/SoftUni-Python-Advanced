jobs = [int(job) for job in input().split(", ")]
index = int(input())
sorted_jobs = sorted((v, i) for i, v in enumerate(jobs))
sums = 0
for el in sorted_jobs:
    if not el[1] == index:
        sums += el[0]
    else:
        sums += el[0]
        break
print(sums)
print(sorted_jobs)
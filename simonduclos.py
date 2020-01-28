variable = list(range(20000,30151))

for kobe in variable:
    print("https://montrealcampus.ca/?p=" + str(kobe))

print(len(variable))

l2 = []
for kobe in variable:
    l2.append("https://montrealcampus.ca/?p=" + str(kobe))
    print(l2)

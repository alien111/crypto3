import os

best = []
best_ = -1
worst = []
worst_ = 1.1

for file in os.listdir('/mnt/c/Users/shoro/Desktop/MAI/3course/crypto/lab3'):
	if (file.endswith('.txt')):
		name = file.split('.')[0]
		members = name.split('_')
		curr = []
		if (len(members) == 3 and members[2] == 'log'):
			for i in members:
				if (i != 'log'):
					print(i + ' ', end = '')
					curr.append(i) 
			print(': ', end = '')
			result = open(file)
			for line in result:
				elements = line.split()
				if (elements[0] == 'Coincidence'):
					print(elements[2])
					if (float(elements[2]) > best_):
						best_ = float(elements[2])
						best = curr
					if (float(elements[2]) < worst_):
						worst_ = float(elements[2])
						worst = curr

print("\nBest coincidence is " + best[0] + ' and ' + best[1])
print("Worst coincidence is " + worst[0] + ' and ' + worst[1])
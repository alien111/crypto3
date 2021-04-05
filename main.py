print('First file name(or path to file) : ', end = '')
first = input()
file1 = open(first)
print('Second file name(or path to file) : ', end = '')
second = input()
file2 = open(second)

logFile = open(first.split('.')[0] + '_' + second.split('.')[0] + '_log.txt', 'w')
logFile.write('position - character\n')

size = 0
matched = 0

while (True):
	char1 = file1.read(1)
	char2 = file2.read(1)

	if (char1 == '' or char2 == ''):
		break

	if (char1 == char2):
		logFile.write(str(size) + '   ' + char1 + '\n')
		matched += 1

	size += 1


stat = matched / size

logFile.write('Characters matched : ' + str(matched) + '\n')
logFile.write('Number of characters : ' + str(size) + '\n')
logFile.write('Coincidence : ' + str(stat) + '\n')

logFile.close()
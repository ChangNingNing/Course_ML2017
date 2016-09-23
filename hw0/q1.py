import sys

columnIndex =  int(sys.argv[1])
fileName = sys.argv[2]

fin = open(fileName, 'r')
fout = open('ans1.txt','w')
array = []
for line in fin:
	array.append(float(line.split()[columnIndex]))
array.sort();
i=0
output = ""
for x in array:
	if i!=0:
		output += ","
	output += str(x)
	i+=1
fout.write(output)

fin.close()
fout.close()

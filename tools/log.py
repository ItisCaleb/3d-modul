import csv

output = open('output.csv','w',newline='')
writer = csv.writer(output)

with open('log.csv', newline='') as file:
	rows = csv.reader(f.replace('\0','') for f in file)
	for row in rows:
		if 'logver' in row[6]:
			l = row[6]
			arr=[];
			q = 0
			s = ''
			for c in l:
				s+=c
				if c=='\"':
					q+=1
				elif c==' ' and q%2==0:
					arr.append(s)
					s = ''
			writer.writerow(arr)		


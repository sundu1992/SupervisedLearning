__author__ = 'Sundu'

import copy
import sys

################# Reading Data and Label Sets #####################################################
input_file = sys.argv[1]

with open(input_file) as f:
	data = f.read()

dataset = []
for line in data.split("\n"):
	if line:
		dataset.append([float(x) for x in line.split()])

train_file = sys.argv[2]

with open(train_file) as f:
	data = f.read()

labelset = {}
for line in data.split("\n"):
	if line:
		if int(line.split()[0]) in labelset:
			labelset[int(line.split()[0])].append(int(line.split()[1]))
		else:
			labelset[int(line.split()[0])]=[int(line.split()[1])]

print(dataset)
print (labelset)

################### Calculating Means ###############################################################
means = {}
for k,v in labelset.items():
	for data_item in v:
		if k in means:
			t =list( zip(means[k],dataset[data_item]))
			for col in range(len(dataset[data_item])):
				means[k][col]=sum(t[col])
		else:
			means[k] = copy.copy(dataset[data_item])

for k,v in means.items():
	count = len(labelset[k])
	means[k] = [x/count for x in means[k]]

print (means)

#################### Nearest Means Algorithm Implementation ###########################################

name=sys.argv[1]+".predictions_test"
op = open(name,"w")



test_data = sys.argv[3]
with open(test_data) as f:
	data_file = f.read()
# data_array=array('i')

data = []
data1 = []
count = 0
for line in data_file.split("\n"):
	#count += 1
	if line:

		# print line
		a = line.split()
		for i in range(len(a)):
			data1.append(float(a[i]))


		data.append(data1)
		data1=[]

print (data,"DATA")
i=0
for data1 in data:
	distance={}
	for k in means.keys():
		t=zip(data1,means[k])
		#print "T=",t
		distance[k]=0
		for items in t:
				distance[k]+=(items[0]-items[1])**2
	min_dis = min(distance.values())
	cls = None
	for k,v in distance.items():
		if min_dis == v:
			cls = k
			break
	op.write(str(cls)+"\t"+str(i)+"\n")
	i=i+1
	print (data1,cls)
git remote add origin https://github.com/sundu1992/SupervisedLearning.git__author__ = 'Sundu'

import copy
import sys
################ Reading Data and Label Sets ######################################
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
			labelset[int(line.split()[0])] = [int(line.split()[1])]

#print("dataset:", dataset)
#print("labelset:", labelset)

################# Calculating Means #################################################
means = {}
for k, v in labelset.items():
	for data_item in v:
		if k in means:
			t =list(zip(means[k], dataset[data_item]))
			for col in range(len(dataset[data_item])):
				means[k][col] = sum(t[col])
		else:
			means[k] = copy.copy(dataset[data_item])

for k, v in means.items():
	count = len(labelset[k])
	means[k] = [x / count for x in means[k]]

#print("means:", means)
################## Calculating Variance ################################################
variance = [0.0]*len(means)
print(variance)


for k,v in labelset.items():
	print("v:",v)

	#for y in v:
		#print "y:",y
	for x in v:
		if k in means.keys():
			#print x
			#print dataset[x]
			#print means[k]
			t = list(zip(means[k],dataset[x]))
			#print "t:",t
		variance[k]+= ((t[0][0] - t[0][1])**2)+((t[1][0] - t[1][1])**2)
	#print variance
	#print len(v)
	variance[k] /= len(v)
#print ("var:",variance)

################# Naive Bayes Algorithm Implementation ###################################
name=sys.argv[1]+".predictions"
op = open(name,"w")
#means = {}
for data in dataset:
	distance={}
	for k in means.keys():
		t=zip(data,means[k])
		#print "T=",t
		distance[k]=0
		for items in t:
			distance[k]+=(items[0]-items[1])**2
			distance[k]/=variance[k]
		#print ("distance:",distance)
	min_dis = min(distance.values())
	cls = None
	for k,v in distance.items():
		if min_dis == v:
			cls = k
			break
	op.write(str(cls)+"\n")
	print (data,cls)





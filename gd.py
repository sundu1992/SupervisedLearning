__author__ = 'Sundu'
__author__ = 'Sundu'


import sys
import random
import math

################# Reading Data and Label Sets #####################################################

input_file = sys.argv[1]

with open(input_file) as f:
	data = f.read()

dataset = []
dataset1 = []
for line in data.split("\n"):

	if line:
		# print line
		a = line.split()
		dataset.append('1')
		# print "len:",len(a)
		for i in range(len(a)):
			dataset.append(a[i])
		# print dataset

	dataset1.append(dataset)
	dataset = []
# dataset.append([float(x) for x in line.split()])


# print dataset1
train_file = sys.argv[2]

with open(train_file) as f:
	data = f.read()

labelset = {}
for line in data.split("\n"):
	if line:
		temp = int(line.split()[0])
		# print temp

		if temp != 0 and temp in labelset:
			labelset[temp].append(int(line.split()[1]))
		elif (temp == 0 and -1 in labelset):
			labelset[-1].append(int(line.split()[1]))
		else:
			labelset[-1 if temp == 0 else int(line.split()[0])] = [int(line.split()[1])]
			print labelset

# print dataset

print labelset

########################## Step 1 : Initialize w , w belongs to [0,1] ##################################

l = len(a)
w = []
for i in range(l):
	w.append(random.random())

for i in range(l):
	print w[i]

#################### Step 2 : Absorbing w0 into w and append 1 in train_data list ######################

w0 = random.random()
w1 = [w0]
for i in w:
	w1.append(i)

print "w:"
for x in w1:
	print x

print "x:"
for y in dataset1:
	print y

################ Compute obj = sum(y(i)-transpose(x(i))*w)^2 ###########################################################

# dataset1=map(list,zip(*dataset1))

print "Weight:", w1
print dataset1
print labelset
prod = []
y = []
for i in range(len(dataset1)):
	y.append(0)

for i in range(len(dataset1)):
	for k, v in labelset.items():
		print k
		for j in range(len(v)):
			if i == v[j]:
				y[v[j]] = k

print "Y:", y
z1 = []
for i in range(len(dataset1)):
	z1.append(0.0)
t1 = 0
for j in range(1, len(dataset1), 1):
	for i in range(len(w1)):
		t1 += w1[i] * float(dataset1[j - 1][i])
	z1[j] = t1
	t1 = 0
t1 = 0
for j in range(1, len(dataset1), 1):
	t1 += (y[j] - z1[j]) ** 2

print t1
####################### Prev obj #################################################

prev_obj = float("Inf")

################## Update obj ###################################################

f = []
sum2 = []
sum4 = []
eta = 0.001
for i in range(len(dataset1)):
	sum2.append(0)
for i in range(len(w1)):
	sum4.append(0)
print dataset1
print "t1:",t1
while (prev_obj - t1) > 0:
	prev_obj = t1

	const = 0

	for j in range(1, len(dataset1), 1):
		sum2[j] += y[j] - z1[j]

	temp = 0
	for i in range(len(w1)):
		for j in range(1, len(dataset1), 1):
			temp += sum2[j] * (-2) * float(dataset1[j - 1][i])
		sum4[i] = temp
		temp = 0
	# print sum2[i]

	for i in range(len(w1)):
		print sum4[i]
		w1[i] -= (eta * sum4[i])

	print w1

	z1 = []
	for i in range(len(dataset1)):
		z1.append(0.0)
	t1 = 0
	for j in range(1, len(dataset1), 1):
		for i in range(len(w1)):
			t1 += w1[i] * float(dataset1[j - 1][i])
		z1[j] = t1
		t1 = 0
	t1 = 0
	for j in range(1, len(dataset1), 1):
		t1 += (y[j] - z1[j]) ** 2

	sum2=[]
	for i in range(len(dataset1)):
		sum2.append(0)
	sum4=[]
	for i in range(len(w1)):
		sum4.append(0)
# print sum1
print t1

# print t1

print "W:", w1
sum3 = 0.0
for i in range(1,len(w1),1):
	print w1[i]
	sum3 += (w1[i] ** 2)
print abs

sum3 = math.sqrt(sum3)

print sum3

dist = 0

dist = w1[0] / sum3
print abs(dist)

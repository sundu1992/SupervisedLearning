__author__ = 'Sundu'

from sys import argv
from array import array
import random
from math import copysign as sign
import pdb
import math
import copy


def dot(a, b):
	res = float(0)
	for i in range(0, len(a)):
		res += (a[i] * b[i])
	#print res

	return res


def find_alpha(data, label):
	x = sorted([a * b for a, b in zip(data, label)])
	#### FIND WHERE THE SIGN CHANGES IN x

	#for i in range(len(x)):
		#print x[i]
	#print data
	#print label
	for i in range(len(x)):
		if x[i + 1] - x[i] >= 0.0:
			alpha = (x[i] + x[i + 1]) / 2
			return alpha

	return 0


data_path = argv[1]
label_path = argv[2]

##### READ THE DATA IN AN ARRAY
# data_file = open(data_path)


with open(data_path) as f:
	data_file = f.read()

data = []
for line in data_file.split("\n"):

	if line:
		dataset = array('f')
		a = line.split()
		for i in range(len(a)):
			dataset.append(float(a[i]))
		dataset.append(1)

	data.append(dataset)



#print (data)

### READ DATA AND ADD 1 TO THE END OF EACH ROW.
rows = len(data) - 1
cols = len(data[0])



##### READ THE LABELS IN AN ARRAY
with open(label_path) as f:
	label_file = f.read()




labelset = array('i')
for line in label_file.split("\n"):
	if line:
		temp = int(line.split()[0])

		if temp == 0:
			labelset.append(-1)
		else:
			labelset.append(temp)



#print (labelset)

### READ LABELS
##### Starting The Coordinate Descent
W = array('f')
w_new = array('f')
d = array('f')
### INITIALIZE W TO A RANDOM PLANE.
for i in range(cols):
	W.append(random.random())
	w_new.append(0.0)
for j in range(cols):
	d.append(0.0)

delta = float(0)
data_prim = array('f')
label_prim = array('i')

alpha = 0
prev_error = 0
error = 10000000
stop_condition = 100
while (stop_condition != 0 or err != 0):
	prev_error = error
	for j in range(0, cols):
		d[j] = 1
		for i in range(0, rows):

			#print i

			delta = dot(d, data[i])
			if (delta != 0):
				####CREATE THE NEW DATA AND APPEND IT TO DATA_PRIME AND LABEL_PRIME

				data_prim.append(dot(W, data[i]))

				label_prim.append(int(sign(float(labelset[i]), delta)))
		#print data_prim
		#print label_prim
		alpha = find_alpha(data_prim, label_prim)

		error = 0
		### CHANGE W AND COMPUTE ERROR
		for k in range(cols):
			w_new[k] = W[k] + alpha * d[k]
		wtx = 0.0
		sign_array = array('i')
		for i in range(rows+1):

			wtx = dot(w_new, data[i])

			if (wtx > 0.0):
				sign_array.append(1)
			else:
				sign_array.append(-1)
		err=0
		#print "wtx:",wtx
		#print "label",labelset
		#print "sign_array",sign_array
		err=dot(labelset,sign_array)
		#for i in range(rows):
		#	if (labelset[i] != sign_array[i]):
		#		error += 1
		#print "ERR", error ,err
		#print("error",err)
		if err < prev_error:
			W = array('f', w_new)

		d[j] = 0
		del data_prim[:]
		del label_prim[:]
	stop_condition -= 1

##### NOW READ THE TEST DATA FROM THE INPUT
###### ASSIGN THE CORRECT CLASS TO THE TEST DATA BASEDD ON THE SIGNS
name = argv[1] + ".predictions"

op = open(name, "w")

test_data = argv[3]
with open(test_data) as f:
	data_file = f.read()


data = []
for line in data_file.split("\n"):
	if line:
		dataset = array('f')

		a = line.split()
		for i in range(len(a)):

			dataset.append(float(a[i]))

		dataset.append(1)

	data.append(dataset)
#print "data:",data
rows = len(data)
#print rows,"rows"
cols = len(data[0])
#print cols


wxi = []
for i in range(rows):
	#print W
	#print data[i]
	wxi.append(dot(W, data[i]))
j=0
for i in wxi:
	if i > 0:
		pred = 1
		print ("1")

	else:
		pred=-1
		print ("-1")

	op.write(str(pred)+"\t"+str(j)+"\n")
	j+=1


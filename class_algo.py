__author__ = 'Sundu'

##### Read Labels
train_file = "train_labels"
pred_file="train_data.predictions_test"

with open(train_file) as f:
	data = f.read()
with open(pred_file) as p:
	pred=p.read()

labelset = {}
v = []
for line in data.split("\n"):
	if line:
		print line
		labelset[int(line.split()[1])]=[line.split()[0]]
#print labelset
for line2 in pred.split("\n"):
	if line2:
		print line2
		labelset[int(line2.split()[1])].append(line2.split()[0])
print labelset

### Calculate TP , FP , FN and TN

tp = 0
fp = 0
fn = 0
tn = 0

for key , val in labelset.items():
	if ((val[0]=='1') and (val[1]=='1')):
		tp+=1
	elif ((val[0]=='1') and (val[1]=='0')):
		fn+=1
	elif ((val[0]=='0') and (val[1]=='1')):
		fp+=1
	elif ((val[0]=='0') and (val[1]=='0')):
		tn+=1

print tp,fp,fn,tn

### Calculate E

e = 0.0
tot = 0.0
fsum = 0.0

tot = float(tp+fp+fn+tn)
print tot

fsum = float(fp+fn)
print fsum

e = fsum/tot

print "No. of misclassified points=",e

### Calculate BER

ber = 0.0
sum1 = float(fp+tn)
sum2 = float(fn+tp)
f1 = (float)(fp)/sum1
f2 = (float)(fn)/sum2
ber = 0.5 * (f1+f2)

#print "Balanced Error Rate=",ber

### Calculate Precision

prec = 0.0
sum3 = float(tp+fp)

prec = (float)(tp)/sum3
#print "Precision=",prec

### Calculate Recall

rec = 0.0
sum4 = (float)(tp+fn)
rec= (float)(tp)/sum4

#print "Recall=",rec

print "accuracy=",1-e
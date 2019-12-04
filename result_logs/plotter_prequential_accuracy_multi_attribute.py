import matplotlib.pyplot as plt
# %matplotlib inline


ht7 = open("grouped_accuracy_HT_attr7.txt","r")
nb7 = open("grouped_accuracy_NB_attr7.txt","r")


ht19 = open("grouped_accuracy_HT_attr19.txt","r")
nb19 = open("grouped_accuracy_NB_attr19.txt","r")

ht13 = open("grouped_accuracy_HT_attr13.txt","r")
nb13 = open("grouped_accuracy_NB_attr13.txt","r")

ht16 = open("grouped_accuracy_HT_attr16.txt","r")
nb16 = open("grouped_accuracy_NB_attr16.txt","r")


ht10 = open("grouped_accuracy_HT.txt","r")
nb10 = open("grouped_accuracy_NB.txt","r")

values_HT7 = []
values_HT = []
values_HT13 = []
values_HT16 = []
values_HT19 = []


values_NB7 = []
values_NB = []
values_NB13 = []
values_NB16 = []
values_NB19 = []

for i in ht7:
	values_HT7.append(100 * float(i))
for i in ht10:
	values_HT.append(100 * float(i))
for i in ht13:
	values_HT13.append(100 * float(i))
for i in ht16:
	values_HT16.append(100 * float(i))
for i in ht19:
	values_HT19.append(100 * float(i))


for j in nb7:
	values_NB7.append(100 * float(j))
for j in nb10:
	values_NB.append(100 * float(j))
for j in nb13:
	values_NB13.append(100 * float(j))
for j in nb16:
	values_NB16.append(100 * float(j))
for j in nb19:
	values_NB19.append(100 * float(j))


plt.figure(figsize=(13,4), dpi=130) # 10 is width, 4 is height
plt.subplots_adjust(hspace = 0.8, wspace=0.3)

# Left hand side plot
plt.subplot(1,2,1)  # (nRows, nColumns, axes number to plot)
plt.grid(True)
plt.plot(values_HT7, label="7 features")  # green dots
plt.plot(values_HT, label="10 features")  # green dots
plt.plot(values_HT13, label="13 features")  # green dots
plt.plot(values_HT16, label="16 features")  # green dots
plt.plot(values_HT19, label="19 features")  # green dots
plt.legend(prop={'size': 6}, loc="upper left")
plt.title('Prequential Accuracy Results for Data Chunks of Size 100 \n for Hoeffding Tree Classifier: 10 features, 2 classes',fontsize= 8)  
plt.xlabel('Data Groups of Size 100'); plt.ylabel('Accuracy Value')# Right hand side plot
plt.ylim(50,110)
############
plt.subplot(1,2,2)
plt.grid(True)
plt.plot(values_NB7)  # green dots
plt.plot(values_NB)  # green dots
plt.plot(values_NB13)  # green dots
plt.plot(values_NB16)  # green dots
plt.plot(values_NB19) 
plt.title('Prequential Accuracy Results of Data Chunks of Size 100 \n for Naïve Bayes Classifier: 10 features, 2 classes',fontsize= 8)  
plt.xlabel('Data Groups of Size 100'); plt.ylabel('Accuracy Value')
plt.ylim(30, 90)
plt.show()


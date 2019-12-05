import matplotlib.pyplot as plt
# %matplotlib inline


ht2 = open("grouped_accuracy_HT2classes.txt","r")
nb2 = open("grouped_accuracy_NB2classes.txt","r")


ht3 = open("grouped_accuracy_HT3classes.txt","r")
nb3 = open("grouped_accuracy_NB3classes.txt","r")

ht4 = open("grouped_accuracy_HT4classes.txt","r")
nb4 = open("grouped_accuracy_NB4classes.txt","r")

ht5 = open("grouped_accuracy_HT5classes.txt","r")
nb5 = open("grouped_accuracy_NB5classes.txt","r")




values_HT2 = []
values_HT3 = []
values_HT4 = []
values_HT5 = []


values_NB2 = []
values_NB3 = []
values_NB4 = []
values_NB5 = []


for i in ht2:
	values_HT2.append(100 * float(i))
for i in ht3:
	values_HT3.append(100 * float(i))
for i in ht4:
	values_HT4.append(100 * float(i))
for i in ht5:
	values_HT5.append(100 * float(i))


for j in nb2:
	values_NB2.append(100 * float(j))
for j in nb3:
	values_NB3.append(100 * float(j))
for j in nb4:
	values_NB4.append(100 * float(j))
for j in nb5:
	values_NB5.append(100 * float(j))


plt.figure(figsize=(13,4), dpi=130) # 10 is width, 4 is height
plt.subplots_adjust(hspace = 0.8, wspace=0.3)

# Left hand side plot
plt.subplot(1,2,1)  # (nRows, nColumns, axes number to plot)
plt.grid(True)
plt.plot(values_HT2, label="2 classes")  # green dots
plt.plot(values_HT3, label="3 classes")  # green dots
plt.plot(values_HT4, label="4 classes")  # green dots
plt.plot(values_HT5, label="5 classes")  # green dots
plt.legend(prop={'size': 6}, loc="upper left")
plt.title('Prequential Accuracy Results for Data Chunks of Size 100 \n for Hoeffding Tree Classifier: different number of classes, 10 features',fontsize= 8)  
plt.xlabel('Data Chunks of Size 100'); plt.ylabel('Accuracy Value (%)')# Right hand side plot
plt.ylim(40,95)
############
plt.subplot(1,2,2)
plt.grid(True)
plt.plot(values_NB2,label="2 classes")  # green dots
plt.plot(values_NB3,label="3 classes")  # green dots
plt.plot(values_NB4,label="4 classes")  # green dots
plt.plot(values_NB5,label="5 classes")  # green dots
plt.legend(prop={'size': 6}, loc="upper left")
plt.title('Prequential Accuracy Results of Data Chunks of Size 100 \n for Naïve Bayes Classifier: different number of classes, 10 features',fontsize= 8)  
plt.xlabel('Data Chunks of Size 100'); plt.ylabel('Accuracy Value (%)')
plt.ylim(40,95)
plt.show()


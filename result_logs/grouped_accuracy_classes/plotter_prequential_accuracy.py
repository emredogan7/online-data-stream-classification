import matplotlib.pyplot as plt
# %matplotlib inline


ht = open("grouped_accuracy_HT.txt","r")
nb = open("grouped_accuracy_NB.txt","r")

values_HT = []
values_NB = []


for i in ht:
	values_HT.append(100 * float(i))

for j in nb:
	values_NB.append(100 * float(j))


plt.figure(figsize=(13,4), dpi=130) # 10 is width, 4 is height
plt.subplots_adjust(hspace = 0.8, wspace=0.3)

# Left hand side plot
plt.subplot(1,2,1)  # (nRows, nColumns, axes number to plot)
plt.grid(True)
plt.plot(values_HT,color='purple',linewidth=2)  # green dots
plt.title('Prequential Accuracy Results for Data Chunks of Size 100 \n for Hoeffding Tree Classifier: 10 features, 2 classes',fontsize= 8)  
plt.xlabel('Data Groups of Size 100'); plt.ylabel('Accuracy Value')
plt.ylim(30, 90)
# Right hand side plot
plt.subplot(1,2,2)
plt.grid(True)
plt.plot(values_NB,color='forestgreen',linewidth=2 )  # green dots
plt.title('Prequential Accuracy Results of Data Chunks of Size 100 \n for Naïve Bayes Classifier: 10 features, 2 classes',fontsize= 8)  
plt.xlabel('Data Groups of Size 100'); plt.ylabel('Accuracy Value')
plt.ylim(30, 90)
plt.show()


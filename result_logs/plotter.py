import matplotlib.pyplot as plt
# %matplotlib inline


ht = open("base_case_prequential_accuracy_HT.txt","r")
nb = open("base_case_prequential_accuracy_NB.txt","r")

values_HT = []
values_NB = []
count = 0
for i in ht:
	#if(count%10 == 0):
	values_HT.append(float(i))
	count+=1
count = 0
for j in nb:
	#if(count%10 == 0):
	values_NB.append(float(j))
	count+=1

# print(len(values_HT))

plt.figure(figsize=(13,4), dpi=130) # 10 is width, 4 is height
plt.subplots_adjust(wspace=0.3)

# Left hand side plot
plt.subplot(1,2,1)  # (nRows, nColumns, axes number to plot)
plt.grid(True)
plt.plot(range(0,len(values_HT)), values_HT,'g' )  # green dots
plt.title('Prequential Accuracy Results of Hoeffding Tree Classifier',fontsize= 10)  
plt.xlabel('Data Instances'); plt.ylabel('Accuracy Value')
plt.ylim(30, 80)
# Right hand side plot
plt.subplot(1,2,2)
plt.grid(True)
plt.plot(range(0,len(values_NB)), values_NB,'r' )  # green dots
plt.title('Prequential Accuracy Results of Naïve Bayes Classifier',fontsize= 10)  
plt.xlabel('Data Instances'); plt.ylabel('Accuracy Value')
plt.ylim(30, 80)
plt.show()

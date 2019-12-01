import matplotlib.pyplot as plt
# %matplotlib inline



numberOfFeatures = range(5,21)

accuracyResults_HT = [66.28,70.54,67.08,72.08,69.72,74.95,79.68, \
					  80.12,81.26,71.37,81.18,83.15,79.73,86.91,\
					  85.41,82.82] 


plt.figure(figsize=(6,3.6), dpi=80) # 10 is width, 4 is height
# plt.subplots_adjust(hspace = 0.8, wspace=0.3)


# Left hand side plot
plt.grid(True)
plt.plot(numberOfFeatures, accuracyResults_HT,'g')  # green dots
plt.title('Cumulative Accuracy Results of Hoeffding Tree Classifier: \n 10 features, 2 classes',fontsize= 10)  
plt.xlabel('Data Instances'); plt.ylabel('Accuracy Value')
plt.ylim(50, 100)
plt.xlim(4,20)
# Right hand side plot
# plt.subplot(1,2,2)
# plt.grid(True)
# plt.plot(range(0,len(values_NB)), values_NB,'r' )  # green dots
# plt.title('Cumulative Accuracy Results of Naïve Bayes Classifier: \n 10 features, 2 classes',fontsize= 10)  
# plt.xlabel('Data Instances'); plt.ylabel('Accuracy Value')
# plt.ylim(30, 80)
plt.show()

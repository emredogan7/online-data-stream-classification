import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline



numberOfFeatures = range(2,6)

accuracyResults_HT = [74.95, 68.68, 65.66, 52.6]

accuracyResults_NB = [71.3, 67.66, 65.62, 52.6] 


plt.figure(figsize=(6,4.2), dpi=80) # 10 is width, 4 is height
# plt.subplots_adjust(hspace = 0.8, wspace=0.3)


# Left hand side plot
plt.grid(True)
plt.plot(numberOfFeatures, accuracyResults_NB,'darkgreen',linewidth=3)  # green dots
plt.xticks(np.arange(min(numberOfFeatures), max(numberOfFeatures)+1, 1))
plt.title('The Effect of Number of Classes for Naïve Bayes Classifier',fontsize= 10)  
plt.xlabel('Number of Classes'); plt.ylabel('Accuracy Value(%)')
plt.xlim(2,5)
plt.ylim(50, 80)

# Right hand side plot
# plt.subplot(1,2,2)
# plt.grid(True)
# plt.plot(range(0,len(values_NB)), values_NB,'r' )  # green dots
# plt.title('Cumulative Accuracy Results of Naïve Bayes Classifier: \n 10 features, 2 classes',fontsize= 10)  
# plt.xlabel('Data Instances'); plt.ylabel('Accuracy Value')
# plt.ylim(30, 80)
plt.show()


# Experimental Results

This file includes the accuracy results and evaluation time information of each run.

## Base Case (numberOfFeatures: 10, numberOfClasses: 2)
~~~~

Constructing the Hoeffding Tree Classifier:  
10000 instances processed with 74.95% accuracy in 0.656043857seconds.  
Constructing the Naive Bayes Classifier:  
10000 instances processed with 71.3% accuracy in 0.236660218seconds.  
~~~~


## Observing the Effect of Number of Features: 
In order to observe the effect of feature numbers in terms of evaluation metrics, a controlled experiment is set up.

While keeping the number of classes constant (2 in our case), different number of features are chosen to observe its effect on the prediction performance.

The number of features is selected in the range [5,20]. The results for Hoeffding Tree and Naive Bayes are given below.

~~~~
Starting to the process!
Constructing the pipeline for 5 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 66.28% accuracy in 0.493591023seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 66.7% accuracy in 0.124740375seconds.
________________________________________________________
Constructing the pipeline for 6 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 70.54% accuracy in 0.194623335seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 69.11% accuracy in 0.108098747seconds.
________________________________________________________
Constructing the pipeline for 7 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 67.08% accuracy in 0.158867723seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 63.57% accuracy in 0.084156928seconds.
________________________________________________________
Constructing the pipeline for 8 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 72.08% accuracy in 0.122627416seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 69.16% accuracy in 0.077413973seconds.
________________________________________________________
Constructing the pipeline for 9 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 69.72% accuracy in 0.112126678seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 66.82% accuracy in 0.086002729seconds.
________________________________________________________
Constructing the pipeline for 10 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 74.95% accuracy in 0.167972334seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 71.3% accuracy in 0.098203778seconds.
________________________________________________________
Constructing the pipeline for 11 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 79.68% accuracy in 0.140557175seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 75.29% accuracy in 0.107389895seconds.
________________________________________________________
Constructing the pipeline for 12 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 80.12% accuracy in 0.156233056seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 78.01% accuracy in 0.110446187seconds.
________________________________________________________
Constructing the pipeline for 13 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 81.26% accuracy in 0.161060604seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 79.99% accuracy in 0.117508193seconds.
________________________________________________________
Constructing the pipeline for 14 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 71.37% accuracy in 0.159735351seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 66.81% accuracy in 0.132131579seconds.
________________________________________________________
Constructing the pipeline for 15 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 81.18% accuracy in 0.17315727seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 73.81% accuracy in 0.132969338seconds.
________________________________________________________
Constructing the pipeline for 16 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 83.15% accuracy in 0.139089983seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 77.38% accuracy in 0.099573262seconds.
________________________________________________________
Constructing the pipeline for 17 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 79.73% accuracy in 0.14267515seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 74.69% accuracy in 0.107009726seconds.
________________________________________________________
Constructing the pipeline for 18 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 86.91% accuracy in 0.157700286seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 82.22% accuracy in 0.111078312seconds.
________________________________________________________
Constructing the pipeline for 19 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 85.41% accuracy in 0.168022352seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 81.18% accuracy in 0.116855122seconds.
________________________________________________________
Constructing the pipeline for 20 features:
Constructing the Hoeffding Tree Classifier:
10000 instances processed with 82.82% accuracy in 0.166994821seconds.
Constructing the Naive Bayes Classifier:
10000 instances processed with 74.09% accuracy in 0.123851662seconds.
________________________________________________________
~~~~




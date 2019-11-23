import moa.streams.generators.RandomRBFGenerator;
import moa.classifiers.trees.HoeffdingTree;
import moa.classifiers.Classifier;
import moa.classifiers.bayes.NaiveBayes;
import moa.tasks.WriteStreamToARFFFile;
import moa.streams.ArffFileStream;
import moa.core.TimingUtils;
import com.yahoo.labs.samoa.instances.Instance;

import moa.tasks.EvaluateInterleavedTestThenTrain;

public class moaObject {


    private int numInstances;
    private String fileName;
    private ArffFileStream importedStream;

    /*
    public void writeStreamToFile(InstanceStream stream, String destFile, int maxInstances){
        WriteStreamToARFFFile task = new WriteStreamToARFFFile();
        task.getOptions().resetToDefaults();
        task.streamOption.setCurrentObject(stream);
        task.arffFileOption.setValue(destFile);
        task.suppressHeaderOption.unset();
        task.maxInstancesOption.setValue(maxInstances);
        task.prepareForUse();
        task.doTask();
    }
    */

    public void setNumberOfInstances(int numInstances){
        this.numInstances = numInstances;
    }

    public void setFileName(String fileName){
        this.fileName = fileName;
    }
    public void dataGenerator(){
        RandomRBFGenerator stream = new RandomRBFGenerator();
        stream.prepareForUse();

        stream.numAttsOption.setValue(10);
        stream.numClassesOption.setValue(2);


        WriteStreamToARFFFile task = new WriteStreamToARFFFile();
        task.getOptions().resetToDefaults();
        task.streamOption.setCurrentObject(stream);
        task.arffFileOption.setValue(this.fileName + ".arff");
        task.suppressHeaderOption.unset();
        task.maxInstancesOption.setValue(this.numInstances);
        task.prepareForUse();
        task.doTask();
    }

    public void importARFF(){
        this.importedStream = new ArffFileStream(this.fileName + ".arff", -1);
    }




    public void modelEvaluator(Classifier classifier){
        this.importedStream.prepareForUse();
        classifier.setModelContext(this.importedStream.getHeader());
        classifier.prepareForUse();


        int numberSamplesCorrect = 0;
        int numberSamples = 0;
        long evaluateStartTime = TimingUtils.getNanoCPUTimeOfCurrentThread();

        while (this.importedStream.hasMoreInstances() && numberSamples < this.numInstances) {

            Instance trainInst = this.importedStream.nextInstance().getData();

            if (classifier.correctlyClassifies(trainInst)){
                numberSamplesCorrect++;
            }

            numberSamples++;
            classifier.trainOnInstance(trainInst);

            //System.out.println(100.0 * (double)numberSamplesCorrect/ (double) numberSamples);
        }
        double accuracy = 100.0 * (double)
                numberSamplesCorrect/ (double) numberSamples;


        double time = TimingUtils.nanoTimeToSeconds(TimingUtils.getNanoCPUTimeOfCurrentThread()- evaluateStartTime);


        System.out.println(numberSamples + " instances processed with " + accuracy + "% accuracy in "+time+"seconds.");


    }


    public void runHoeffdingTree(){
        Classifier learnerHoeffding = new HoeffdingTree();
        modelEvaluator(learnerHoeffding);

        /*
        this.importedStream.prepareForUse();
        learner.setModelContext(this.importedStream.getHeader());
        learner.prepareForUse();


        int numberSamplesCorrect = 0;
        int numberSamples = 0;
        long evaluateStartTime = TimingUtils.getNanoCPUTimeOfCurrentThread();

        while (this.importedStream.hasMoreInstances() && numberSamples < this.numInstances) {

            Instance trainInst = this.importedStream.nextInstance().getData();

            if (learner.correctlyClassifies(trainInst)){
                numberSamplesCorrect++;
            }

            numberSamples++;
            learner.trainOnInstance(trainInst);

            // System.out.println(100.0 * (double)numberSamplesCorrect/ (double) numberSamples);
        }
        double accuracy = 100.0 * (double)
                numberSamplesCorrect/ (double) numberSamples;


        double time = TimingUtils.nanoTimeToSeconds(TimingUtils.getNanoCPUTimeOfCurrentThread()- evaluateStartTime);


        System.out.println(numberSamples + " instances processed with " + accuracy + "% accuracy in "+time+"seconds.");
        */

    }



    public void runNaiveBayes(){
        Classifier learnerBayes = new NaiveBayes();
        modelEvaluator(learnerBayes);
        /*
        this.importedStream.prepareForUse();
        learner.setModelContext(this.importedStream.getHeader());
        learner.prepareForUse();


        int numberSamplesCorrect = 0;
        int numberSamples = 0;
        long evaluateStartTime = TimingUtils.getNanoCPUTimeOfCurrentThread();

        while (this.importedStream.hasMoreInstances() && numberSamples < this.numInstances) {

            Instance trainInst = this.importedStream.nextInstance().getData();

            if (learner.correctlyClassifies(trainInst)){
                numberSamplesCorrect++;
            }

            numberSamples++;
            learner.trainOnInstance(trainInst);

            //System.out.println(100.0 * (double)numberSamplesCorrect/ (double) numberSamples);
        }
        double accuracy = 100.0 * (double)
                numberSamplesCorrect/ (double) numberSamples;


        double time = TimingUtils.nanoTimeToSeconds(TimingUtils.getNanoCPUTimeOfCurrentThread()- evaluateStartTime);


        System.out.println(numberSamples + " instances processed with " + accuracy + "% accuracy in "+time+"seconds.");

        */
    }




}




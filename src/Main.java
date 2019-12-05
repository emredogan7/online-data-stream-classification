import moa.classifiers.trees.HoeffdingTree;
import moa.classifiers.Classifier;
import moa.streams.generators.RandomRBFGenerator;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.FileWriter;
import moa.streams.ArffFileStream;

public class Main {

    public static void main(String[] args) throws IOException {
        System.out.println("Starting to the process!");

        moaObject moa = new moaObject();
        moa.setFileName("RBFdataset");
        moa.setNumberOfInstances(10000);




        // Base Case Setup:
        moa.dataGenerator(10,5);
        moa.importARFF();

        System.out.println("Constructing the Hoeffding Tree Classifier:");
        moa.runHoeffdingTree();

        System.out.println("Constructing the Naive Bayes Classifier:");
        moa.runNaiveBayes();

        /*
        // Observing the Effect of the Number of Features:
        for (int numberOfFeatures = 5; numberOfFeatures < 21; numberOfFeatures++) {
            System.out.println("Constructing the pipeline for "+Integer.toString(numberOfFeatures)+ " features:");
            moa.dataGenerator(numberOfFeatures,2);
            moa.importARFF();

            System.out.println("Constructing the Hoeffding Tree Classifier:");
            moa.runHoeffdingTree();

            System.out.println("Constructing the Naive Bayes Classifier:");
            moa.runNaiveBayes();
            System.out.println("________________________________________________________");

        }
        */

        // Observing the Effect of the Number of Classes:

        /*
        for (int numberOfClasses = 2; numberOfClasses <6; numberOfClasses++) {
            System.out.println("Constructing the pipeline for "+numberOfClasses+ " classes:");
            moa.dataGenerator(10,numberOfClasses);
            moa.importARFF();

            System.out.println("Constructing the Hoeffding Tree Classifier:");
            moa.runHoeffdingTree();

            System.out.println("Constructing the Naive Bayes Classifier:");
            moa.runNaiveBayes();
            System.out.println("________________________________________________________");

        }
        */



    }
}

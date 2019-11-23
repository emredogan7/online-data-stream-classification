import moa.classifiers.trees.HoeffdingTree;
import moa.classifiers.Classifier;
import moa.streams.generators.RandomRBFGenerator;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.FileWriter;
import moa.streams.ArffFileStream;

public class Main {

    public static void main(String[] args) {
        System.out.println("Starting to the process!");

        moaObject moa = new moaObject();
        moa.setFileName("RBFdataset");
        moa.setNumberOfInstances(10000);

        moa.dataGenerator();
        moa.importARFF();

        System.out.println("Constructing the Hoeffding Tree Classifier:");
        moa.runHoeffdingTree();

        System.out.println("Constructing the Naive Bayes Classifier:");
        moa.runNaiveBayes();


    }
}

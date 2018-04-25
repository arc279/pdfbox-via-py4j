#!/bin/bash

javac org/kuryu/*.java -cp pdfbox-app-2.0.8.jar
jar cvf kuryu.jar org/kuryu/*.class

javac J4Py.java -cp py4j0.10.6.jar
jar cvfm J4Py.jar manifest.mf J4Py.class


# Bank-Marketing

### Objective 
The objective of this project is to optimize the cost-efficiency of call center campaign for promoting its term deposit product by leveraging analytics.

### Installation
Created a conda environment. Installed all the required packages using pip. All the packages are given in the requirement.txt file
Created a Dockerfile for deployment. Specified all the commands to build it including packages.

### Usage

To run the Api, change directory to main folder where main.py file is present and execute : uvicorn main:app --reload
To test docker, build and run docker and test in browser localhost:8005/docs

### Data
Data is taken from https://archive.ics.uci.edu/dataset/222/bank+marketing.

### Model Training and evaluation
Model is trained using AdaBoost algorithm. It can indirectly handle class imbalance. Applied hyperparameter tuning and kfold 
cross validation. Inorder to get more accuracy need to apply oversampling / SMOTE to handle class imbalance and feature engineering

Used Accuracy and confusion matrix to evaluate the model. Model need more finetuning to get better prediction on class with less samples.

### Inference
-----------------------------
### Top 5 Drivers of conversion are:
    1. euribor3m
    2. emp.var.rate
    3. cons.conf.idx
    4. Campaign
    5. Age

### Recommendation to cut the number of calls supposing that you get a "test/prediction set" of new customers every week:
    1. Use trained model and predict whether the new customer will buy or not. 
    2. Select the customers likely to convert and whose probability of conversion is more.
  This way bank can reduce the number of calls without impacting the business.




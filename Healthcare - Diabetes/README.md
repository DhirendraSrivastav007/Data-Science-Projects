<img src="https://aihubprojects.com/wp-content/uploads/2021/04/diab.jpg" align="center" height="200" width = "800" >

<hr>

# Diabetes Prediction Using Machine Learning

Build a model to accurately predict whether the patients in the dataset have diabetes or not?




- Table OF Content

  * [1. Aim of Project](#1-aim-of-project)
  * [2. Problem Statement](#2-problem-statement)
  * [3.  Work Flow:](#3-work-flow)
  * [4. Tech Stack](#4-tech-stack)
  * [5. Documentation](#5-documentation)
  * [6. Deployment](#6-deployment)
  * [[Github Link](https://github.com/DhirendraSrivastav007/Data-Science-Projects/tree/master/Healthcare%20-%20Diabetes/Health-Care%20Diabetes%20Prediction_Deployment]
  * [[Web App Link](https://house-price-prediction-dploy.herokuapp.com/)]
    + [This is How Working App Should Look Like](#this-is-how-working-app-should-look-like)



<hr>

## 1. Aim of Project

- The main Objective of this Project is to Explore Various Metrics in Classification Problem Statement

- To Test Various Classification Algortihm Based on Strategy Deviced from EDA

- To Work on End to End Data Science Life cycle till Deployment(Deployment on Google Cloud Platform via Flask API)


<hr>


## 2. Problem Statement

- This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.

- Data Has Missing values we will dive deep into data with our EDA Skills and try to find root cause of missing data and impute them accordingly

- Device Strategy for Model Building and Selecting Best Model

- Serve the Model on GCP (PaaS) using Flask API



<hr>

## 3. Work Flow:

   ### 1. Acquire the Data
   - Data is Gathered From UCI Machine Learning Repository in Tabular Format with 8 Explanatory Variables and Binary Outcome Stating wether Patient is Diabetic Or not
   - The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on
   
   
  ### 2. Data Exploration
   - I have analysed each features and in **five number summary** , i was able so notice someting strange..
  
  ![Five number Summary](https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/master/Healthcare%20-%20Diabetes/__results___files/Five%20Number%20Summary.png)
  
  <br>
   
   - ### **Distribution Of The Data**
   
  ![Distribution](https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/master/Healthcare%20-%20Diabetes/__results___files/__results___14_0.png)
  
  - <font color = "blue" size=4.8px> <b>Interpretation : </b></font>

      * <font color = "red" size=4.8px>Most Features are Not Normally Distrubuted</font>
      * <font color = "red" size=4.8px>Thus we will Impute The Data Accordingly</font>
      * <font color = "red" size=4.8px>Also We Will use Non-Linear Algorithms which doesnt expects Normal Distribution, for eg :- Tree based ensemble Techniques </font>   

  - ### **Outliers !**

   ![Outliers](https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/master/Healthcare%20-%20Diabetes/__results___files/__results___22_0.png)
   
   <br>
  
  ## **Tableau Analysis**
  
![tableau analysis](https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/master/Healthcare%20-%20Diabetes/Tableau%20Analysis/Dashboard%201.png)
   
   
 - ## Though EDA I have gathered few analytics of Data : - 
   
     
  
    
      ### 3. Data  Preprocessing/ Feature Engineering
     - Missing Value Imputation, According to Data We used Median Knn Imputer for Most Accurate Imputation




<br>

  ### 4. Devicing Strategy For Modeling
   
 * <p style = "color:b; font-size:150%; font-weight:bold; text-decoration: underline; text-decoration-style: double;"> So Far We have Arrived with Following Analysis : - </p>   
    
 
   * Data is Skewed and has Lots of Outliers
   * Data is Imbalanced
   * Features Are Having Low Correlation with Target Variable
   * No of Samples Are too low So We Cannot Use Hold Out Method Of Cross Validation, we need to use Kfolds And Also Class Proportion is Imbalanced so We need to Use Stratified Kfold For Our Cross Validation Analysis With Minimum 10 FOLDs


* <p style = "color:r; font-size:120%; font-weight:bold"> By these Inferences Its Evident that we should Use Tree Based Ensemble Techniques Which Can Handle Outliers, Skewed Data, Data Imbalances and Can Learn From Weak Learners

  
  
  
  
  
  ### 5. Choosing Relevant Metric For Classification

 
 ![Senstivity_Specificity](https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/master/Healthcare%20-%20Diabetes/__results___files/Senstivity_Specificity.png)
  
 ![Metrics](https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/master/Healthcare%20-%20Diabetes/__results___files/F-Beta.png)https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/master/Healthcare%20-%20Diabetes/__results___files/F-Beta.png)   

  
  
  
  
<br>
   
  ### 7. Evaluating Different Models
   
|  Model 	|   F-1 Score 	| 
|--:	|--:	          |
| LGBM |   72.03 %	 |      
| Random_Forest | 70.0 %	|
| KNN | 64.0 %	| 
| XGboost | 63.33 %	| 

  
  
  


  ### 8. Selecting Model With Best Score And Predicting the unseen Test data to Model
  
   - <p style = "color:red; font-size:120%; font-weight:bold">Best Performing Model In terms of F1-Score is LGBM, Because it has Ability to Deal with Imbalanced Data Set Better than any Model</p>
   - <p style = "color:red; font-size:120%; font-weight:bold">Knn turns out to be worst of all, Because it wasnt suitable to data as it is Linear Model and Our data is Non-Linear </p>
   
   
   
   
  ### 9. Developing a Model Pipeline traning it and saving it in pickle file
  
  
  
  
  ### 10. Serving the Web app On Cloud (PaaS) with Flask API
    
    
    
    
    
<hr>    
    
## 4. Tech Stack

**Client:** ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)	![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

**Server:** ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) 	![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

**Tools for EDA and Modeling:** ![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)


## **Libraries in Use:**

**Visualization:** ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white) **matplotlib,** **Seaborn**

**Data Wrangling:** ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)

**Modeling:** ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
**xgboost**


<hr>

## 5. Documentation
- Project is well Documented in Jupyter Notebook, with markdowns, code and output graphs and plots
- Please Refer Below Links For Documentation
    - [Kaggle Notebook](https://www.kaggle.com/jaysrivastav/xgb-gpu-with-optuna-and-kfold-house-price-predict)
    - [Github Notebook](https://github.com/DhirendraSrivastav007/Data-Science-Projects/tree/master/House%20Price%20Prediction)



<hr>


## 6. Deployment

- Project is deployed on heroku Cloud(PaaS) as an Web App using Flask API
- Backend : ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

- Front End : ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

- Cloud : 	![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

## [Github Link](https://github.com/DhirendraSrivastav007/Data-Science-Projects/tree/master/House%20Price%20Prediction/Flask%20API)

## [Web App Link](https://house-price-prediction-dploy.herokuapp.com/)



<hr>


## 7.  Demo

- For Live Demo Click on Web App Link Above 

- To Run it in your Local Machine, Download The file In your Local Machine from Github Link Provide Above (Note You must Have VS Code or any pyhton IDE Installed in Your Desktop )
- Once Downloaded open the file with your Favourite IDE and paste belowe code in your IDE Command Line to Install All Requiresments from Requirements.txt File 

```bash
# To install Requirements
  pip3 install -r requirements.txt

# To run App
  python app.py
```

<hr>


### This is How Working App Should Look Like

![Project Demo](https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/master/House%20Price%20Prediction/Flask%20API/static/Project_Demo.gif)




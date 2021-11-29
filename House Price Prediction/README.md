<img src="https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/master/House%20Price%20Prediction/Flask%20API/static/house_price_mage.jpeg" align="center" height="200" width = "800" >

<hr>

# House Price Prediction

Advanced Regression Techniques to predict Sale Price of House based on certain Features




- Table OF Content

  * [1. Aim of Project](#1-aim-of-project)
  * [2. Problem Statement](#2-problem-statement)
  * [3.  Work Flow:](#3-work-flow)
  * [4. Tech Stack](#4-tech-stack)
  * [5. Documentation](#5-documentation)
  * [6. Deployment](#6-deployment)
  * [[Github Link](https://github.com/DhirendraSrivastav007/House-Price-Prediction-Deployment)]
  * [[Web App Link](https://house-price-prediction-dploy.herokuapp.com/)]
    + [This is How Working App Should Look Like](#this-is-how-working-app-should-look-like)



<hr>

## 1. Aim of Project

- The main Objective of this Project is to Test my Exploratory Data Analytics Skills 

- To Explore Advanced  Encoding Techniques based on Data And Model (Creative Feature Engineering)

- To Test Various Regression Algortihm Based on Strategy Devided from EDA(Advanced Ensemble Regression Models)

- To Work on End to End Data Science Life cycle till Deployment(Deployment on Cloud PaaS via Flask API)


<hr>


## 2. Problem Statement

- With 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa, we have to predict Sales Price of Each House (Regression)

- Data Has Missing values we will dive deep into data with our EDA Skills and try to find root cause of missing data and impute them accordingly

- Device Strategy for Feature Engineering (Categorical Encoding) and Modeling (Advanced Ensemble Regression Algortihms) from inferences Gathered From EDA

- Serve the Model on Cloud (PaaS) using Flask API



<hr>

## 3. Work Flow:

   ### 1. Acquire the Data
   - Data is Gathered From Kaggle Competition in Tabular Format with 79 Explanatory Variables and Target Sales Price of House
   
   
  ### 2. Data Exploration
   - I have analysed each features with respect to their data type as exploring all 79 features withou any Structure is Problamatic
   
   - Though EDA I have gathered few analytics of Data : - 
     - There are lot of missing values in Categorical Data .. All are **above 15% nan** and some are **till 99.5 % Missing values**, However through reading the data discription throughly we know that **nan values indicated missing entity for that particular feature** for e.g. **Pool quality nans indicates that there were no pools in that house** so thus no rating for pool 
     
     
     - Likewise there Had such condition for all features and **we replaced the nan with no pool or no entity for all missing categorical features**


     - For Numeric Features Instead of **Using thumb rules to impute missing data with mean or median** .. **We dive deep into data with our EDA Skills** we noticed that **nans value indicated missing entity** for e.g. **GarageArea nan Indicated that there were no Garage in That house thuse no entry for Garage Area**, So we **imputed zero** for all such features


     - I also Noticed that **Data Had too Many Outliers By Looking at Quantile Range and Vusalizing through Box and Whiskers Plot** (Plots are in Notebook file Either on Kaggle or Github Link )


     - By this information It is Clear that we cannot use Linear Models , We need Non-Linear Models which doesnt Expect Normality such as (tree based ensemble models)
   
   
  ### 3. Check For Correlation Among Features and Between Features and Target
  
   - Features were Showing Reasonable anmount of Significance in Predicting House Price so at this Point we could not do Feature Selection based on correlation
   
   
  ### 4. Creating New Features That May Impact Significance in prediction
   - I Derived new Features From Existing Featurs which Showed Significant Amount or Correlation in Predicting the target
   - Features Such as NoPool, No Garage Indicating wether house has pool or not 
   - Although we will rely on Model To decide which features are more Significant 
    
    
  ### 5. Data  Preprocessing/ Feature Engineering
   - As there were 43 Categorical Columns , Some were ordinal indicating Ratings and Some were Nominal , so we used Advances Encoding Technique for Encoding Our Categorical Variables such as GLM Encoder which is better than Target Encoding and Leave one Out Encoder , solved problem of Data Leakage and Over Traini Better than any Encoding technique Discussed
   
   - unfortunately we cannot use one hot encoding becase we are using tree based model and one hot doesnt go well with tree models
    
   - We are going to use encoder with 10 Folds so that we solve issue of Data Leakeage and Overfitting at Greater Extent
    
    
  ### 6. Feature Selection using Embedded Methods
   - We are Going to Use Model For Selecting best Feature , this is known as Embedded method or hybrid method which best suits our Prolem Statement to save time as wll as computation
    
   - We noticed top 25 Features is giving us best results , However for now well go with top 10 which is giving reasonable amount of Information to model


   
  ### 7. Evaluating Different Models
   
|   	|   R-Squared 	| RMSE  	|
|--:	|--:	          |--:	    |
|  XGB_ALL 	|   90.28	       | 22162.674370 	 |
|  XGB_Top_10 	|   86.78	    | 25845.752485 |	 



  ### 8. Selecting Model With Best Score And Predicting the unseen Test data to Model
  
   - Best Model is XGB with all features and **R-Squared of 90.28%** and **RMSE of 22162.674370** with **10-fold cross validation**	 
   
   
  ### 9. Developing a Model Pipeline traning it and saving it in pickle file
  
  ### 10. Serving the Web app On Cloud (PaaS) with Flask API
    
    
    
    
    
<hr>    
    
## 4. Tech Stack

**Client:** ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)	![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

**Server:** ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

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
- Backend : ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

- Front End : ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

- The App Takes Input as Features From user In Web Form and Stores The Features with Prediction From Model Into SQLite Data Base and Then Displays it to User in a Tabular Format

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




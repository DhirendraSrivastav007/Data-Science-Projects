<img src="https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/e615c348326b7c951e904e5c861cec6a4017ca4b/NLP-%20Wikipedia%20Toxicity/Project_Deployment/static/Wikipedia%20Toxicity%20Image.jpeg" align="center" height="200" width = "800" >

<hr>

# Wikipedia Comments Toxicity Analysis Using NLP

Build a model to accurately predict whether the comments of wikipedia are toxic or Non-Toxic




- Table OF Content

  * [1. Aim of Project](#1-aim-of-project)
  * [2. Problem Statement](#2-problem-statement)
  * [3.  Work Flow:](#3-work-flow)
  * [4. Tech Stack](#4-tech-stack)
  * [5. Documentation](#5-documentation)
  * [6. Deployment](#6-deployment)
  * [[Github Link](https://github.com/DhirendraSrivastav007/Data-Science-Projects/tree/master/NLP-%20Wikipedia%20Toxicity)]
  * [[Web App Link](https://wikipedia-toxicity.el.r.appspot.com/)]
    + [This is How Working App Should Look Like](#this-is-how-working-app-should-look-like)



<hr>

# 1. Aim of Project

- The main Objective of this Project is to Explore Basic Natural Language Processing Using Machine Learning

- To Deploy model On Cloud With Model Reatrainability Feature , so That the model Doesnt degrade with time and new data (Model Drift)

- To Work on End to End Data Science and NLP Life cycle till Deployment(Deployment on Google Cloud Platform via Flask API)


<hr>


# 2. Problem Statement

- Sentiment Analysis on Wikipedia Comments

- As a data scientist at Wikipedia who will help Wikipedia to build a predictive model that identifies toxic comments in the discussion and marks them for cleanup by using NLP     and machine learning. Post that, help identify the top terms from the toxic comments

- Web scraping Data Using Beautiful Soup

- Cleaning up the Data (Text Preprocessing) and vectorizing it for model building

- Serve the Model on GCP (PaaS) using Flask API



<hr>

# 3. Work Flow:

   ### 1. Acquire the Data
   - Data is Web Scraped using Beautiful Soup from Wikipedia Comments on Article
   
   - Data is Cleaned using regular Expression to remove Ip Address, HTML Tags and URls
   
   - Converting the Raw Text Into Document Term Matrix For Model Building
   
   
   
   
  ### 2. Text Preprocessing
  
  - <font color = "blue" size=4.8px> <b>I Have Dicovered Few Noises in Textual data : </b></font>

      * <font color = "red" size=4.8px>Texts have some HTML Tags, IP adresses and URLs and Stopwords , we will remove them by Regular Expression : </font>
       
        ![Clean_up_Function](https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/7e699f5511a41215824917719335d1bfd7c1db9a/NLP-%20Wikipedia%20Toxicity/Project_Deployment/static/Text_Clean_Up_Function.png)
      
      * #### We will Remove Some Contetual Stopwords By Reviewing Top 20 Repeated words
      
        ![Contextual_Stop_Words](https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/7e699f5511a41215824917719335d1bfd7c1db9a/NLP-%20Wikipedia%20Toxicity/Project_Deployment/static/Top_20_Words.png)
      
        ![Contextual_Stop_Words](https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/7e699f5511a41215824917719335d1bfd7c1db9a/NLP-%20Wikipedia%20Toxicity/Project_Deployment/static/Contextual_Stop_Words.png)   

  
     * We will Use TF-IDF Vectorizer to Vectorize Our Textual Data




<br>

  ### 3. Devicing Strategy For Modeling
      
   * We will Use **Naive Bayes** Model As it Supports **partial_fit** For Model **Retraining** Also we its simple and Works well on Texual Data
   
   * We Will Run Bayesian Optimization For Hyperparameter Tuning Of TF-IDF Vectorizer And Naive Bayes Model to select best possible Parameters
   
   * We will Evaluate the Model Using 10 Fold Cross Validation and We will Choose Metric as F1 score for giving equal importance to recall and precision i.e, Equal Importance        for toxic and non-toxic comments
   
  
<br>
  
  
  ### 4. Classification Report
  
  ![Contextual_Stop_Words](https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/7e699f5511a41215824917719335d1bfd7c1db9a/NLP-%20Wikipedia%20Toxicity/Project_Deployment/static/Classification_Report.png)

  
  
  
  
<br>
  
  ### 5. Viewing Most prominent terms in the toxic comments Classified By our Model
  
   ![Top_Prominent_Comments](https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/7e699f5511a41215824917719335d1bfd7c1db9a/NLP-%20Wikipedia%20Toxicity/Project_Deployment/static/Top_Toxic_Comments.png)
   
   
   
  #### 6. Developing a Model Pipeline traning it and saving it in pickle file
  
  
  #### 7. Adding Model Retraining Feature By Utilizing New Labelled Data Being Corrected By User and using ***partial_fit*** Method of Our model
  
  #### 8. Saving The new Data Into CSV File For Future Model Retraining, To Avoid any ***Model Drift***
  
  
  #### 9. Serving the Web app On GCP with Flask API
  
    
    
<hr>   


    
## 4. Tech Stack

**Client:** ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)	![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

**Server:** ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) 	![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

**Tools for EDA and Modeling:** ![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)


## **Libraries in Use:**

**Visualization:** ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white) **matplotlib,** **Seaborn**

**Data Wrangling:** ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white) , **nltk**

**Modeling:** ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)



<hr>

## 5. Documentation
- Project is well Documented in Jupyter Notebook, with markdowns, code and output graphs and plots
- Please Refer Below Links For Documentation
    - [Github Notebook](https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/7e699f5511a41215824917719335d1bfd7c1db9a/NLP-%20Wikipedia%20Toxicity/Wikipedia%20Toxicity%20Project.ipynb)



<hr>


## 6. Deployment

- Project is deployed on heroku Cloud(PaaS) as an Web App using Flask API
- Backend : ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

- Front End : ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

- Cloud : 	![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

## [Github Link](https://github.com/DhirendraSrivastav007/Data-Science-Projects/tree/master/NLP-%20Wikipedia%20Toxicity)

## [Web App Link](https://wikipedia-toxicity.el.r.appspot.com/)



<hr>


## 7.  Demo

- For Live Demo Click on Web App Link Above 

- To Run it in your Local Machine, Download The file In your Local Machine from Github Link Provide Above (Note You must Have VS Code or any pyhton IDE Installed in Your Desktop )
- Once Downloaded open the file with your Favourite IDE and paste belowe code in your IDE Command Line to Install All Requiresments from Requirements.txt File 

```bash
# To install Requirements
  pip3 install -r requirements.txt

# To run App
  python main.py
```

<hr>


### This is How Working App Should Look Like

![Project Demo](https://github.com/DhirendraSrivastav007/Data-Science-Projects/blob/master/House%20Price%20Prediction/Flask%20API/static/Project_Demo.gif)




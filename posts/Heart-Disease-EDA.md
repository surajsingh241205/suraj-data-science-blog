![Cover](https://storage.googleapis.com/kaggle-datasets-images/7282214/11609951/1946f7eb19318a651e6667d88fdbaae4/dataset-cover.png?t=2025-04-29-08-27-04)
---
date: 2026-01-27
---
# From Raw Data to Model-Ready Features: An End-to-End EDA on a Heart Disease Dataset

**[Source code](https://github.com/surajsingh241205/Data-Science-Minor-And-Major-Projects/tree/main/Heart%20EDA)**

In this post, I document how I applied **Exploratory Data Analysis (EDA), data cleaning, data preprocessing, feature engineering, and feature selection** on a real-world **heart disease dataset**.

The goal was not to rush into model building, but to deeply understand how real data is analyzed and transformed before it is ever fed into a machine learning model.

---

## Dataset Overview

![Cover](https://img.freepik.com/free-vector/startup-metaphor-flat-icon_1262-18784.jpg?semt=ais_hybrid&w=740&q=80)

The dataset contains patient-level health information related to heart disease, including:

- Demographic features (Age, Sex)
- Clinical measurements (RestingBP, Cholesterol, MaxHR, Oldpeak)
- Categorical medical indicators (ChestPainType, RestingECG, ExerciseAngina, ST_Slope)
- Target variable: **HeartDisease**

The dataset consists of **918 records and 12 original features**.

---

## Step 1: Exploratory Data Analysis (EDA)

![](https://img.freepik.com/premium-vector/steps-concept-illustration_114360-8903.jpg)

EDA helped me understand the structure, quality, and behavior of the data before making any changes.

### Key EDA Steps Performed:
- Viewing the dataset using `head()` and `info()`
- Identifying numerical and categorical features
- Checking data types and non-null counts
- Generating summary statistics using `describe()`
- Understanding the distribution of numerical features
- Inspecting the target variable distribution
- Identifying suspicious values and potential outliers

### Important Observations:
- No missing values were present, but some values required domain-based validation
- Numerical features showed varying scales and distributions
- Categorical variables needed encoding
- The target variable was binary and suitable for classification

EDA made one thing very clear:

> You cannot clean, preprocess, or engineer features without understanding the data first.

---

## Step 2: Data Cleaning

Based on EDA insights, I applied the following data cleaning steps:

- Verified and fixed data types
- Checked for duplicate rows
- Validated domain-specific values
- Identified and reviewed outliers
- Ensured consistency across categorical features

This step reinforced an important principle:

> **EDA tells you what’s wrong. Data cleaning fixes it.**

---

## Step 3: Data Preprocessing

After cleaning, the next step was preparing the data for machine learning.

### Preprocessing Steps:
- Encoding categorical variables using one-hot encoding
- Scaling numerical features to bring them onto a similar scale
- Separating features and target variable

At this stage, the data became **model-compatible**, but not yet optimized.

---

## Step 4: Feature Engineering

Feature engineering focused on improving how information is represented for the model.

Actions taken:
- Created meaningful numerical representations from raw features
- Reduced redundancy after encoding
- Ensured numerical stability and consistency
- Verified transformed feature distributions

This step highlighted how much model performance depends on **data representation**, not just algorithms.

---

## Step 5: Feature Selection

To reduce noise and improve learning efficiency, I applied **feature selection techniques**.

### Approach Used:
- Statistical feature selection using Chi-Square tests for categorical features
- Removal of features with low relevance to the target
- Retention of features with strong statistical association

Feature selection helped narrow the dataset to the most informative features without losing important signals.

---

## Final Dataset

After completing all steps, the final dataset:
- Contained only relevant, engineered features
- Had consistent scaling and encoding
- Was fully ready to be fed into a machine learning model

This final version reflects how raw real-world data is gradually refined through structured decisions.

---

## Key Learnings

- Real-world datasets are rarely clean or straightforward
- EDA guides every downstream decision
- Data preparation takes more time than modeling
- Feature engineering and selection significantly impact model quality
- Understanding the data is more valuable than rushing into algorithms

---

## Conclusion

![](https://www.shutterstock.com/image-vector/conclusion-text-on-white-background-600nw-2511645971.jpg)

This project helped me connect theory with practice and understand the **complete data preparation pipeline** in a realistic setting.

Rather than focusing on model accuracy early, this exercise emphasized building strong fundamentals — because **good models start with good data**.

---

## What’s Next?

The next step is to use this prepared dataset for model training and evaluation, while continuing to strengthen understanding of feature behavior and model assumptions.

For now, the focus remains on learning **correctly and deeply**, not quickly.



![cover](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcb5urZPhIqQBlHgMUGGF_-vc11fBfzhnAoA&s)
---
date: 2026-01-25
---
# Introduction to machine learning
In this post we are going to learn about what is machine learning, Ai vs ML vs DL comparision and Types of machine learning. 

## What is machine learning ? 
- Machine learning is a subset of Ai where machine learns to find pattern from data and make predictions or decisions without being explicitly programmed for every set of rule.

**For interview standards** 
 - Machine learning is a technique where systems learn form historic data to improve performance on tasks.

**For Example**  <br>
1. Email spam filter <br>
2. Netflix recommendations <br> 
3. credit card fraud detection 

**Core Idea** - The core idea of the machine learning is, the data is given to the machine learning  algorithm, and the algorithm is trained on a machine learning model, and we get output that predicts the value from the trained data. 

***" If there is no data, There is no machine learning, period "***


---

## AI VS ML VS DL
![img](https://k21academy.com/wp-content/uploads/2020/12/AI-vs-ML-vs-Deep-Learning.png)

- Ai stands for **ARTIFICIAL INTELLIGENCE**, It has a broad concept and the goal is to make machines behaves like humans. 

**For ex** - chess engine with fixed rules. <br>
         Chatbots with pre defined logics.

### Machine learning
- Machine learning is a subset of artificial intelligence. machines learns from the data and required feature engineering and works well on structured and tabular data. 

**For ex** - House price prediction <br>
             Customer churn prediction 

---

## Deep learning 
- Deep learning is a subset of machine learning. It uses something called neural networks. It automatically learned from features and needs large data + high compute power.

**For ex** - Image recognition <br>
             Speech recoginion <br>
             Face detection 

**Relationship between these 3**<br>
AI ---> ML ---> DL

**One line comparision** 

<style>
  table {
    border-collapse: collapse; /* Merges borders into a single line */
    width: 100%;
  }

  th,
  td {
    border: 1px solid black; /* Adds a border to cells */
    padding: 8px; /* Adds space between content and border */
    text-align: left; /* Aligns text to the left */
  }

  th {
    background-color: #f2f2f2; /* Gray background for headers */
  }
</style>


<table>
  <caption>
    <b>Comparision
  </caption>
  <thead>
    <!-- Table Header Section -->
    <tr>
      <!-- Table Header Cells -->
      <th>Term</th>
      <th>Depends on data</th>
      <th>Featured Engineering</th>
      <th>Complexity</th>
    </tr>
  </thead>
  <tbody>
    <!-- Table Body Section -->
    <tr>
      <!-- Table Data Cells -->
      <td>AI</td>
      <td>Not always</td>
      <td>Manual</td>
      <td>Low Mid</td>
    </tr>
    <tr>
      <td>ML</td>
      <td>Yes</td>
      <td>Required</td>
      <td>Mid</td>
    </tr>
    <tr>
      <td>DL</td>
      <td>Huge data</td>
      <td>Automatic</td>
      <td>High</td>
    </tr>
  </tbody>
</table>

# Types of machine learning
![img](https://media.geeksforgeeks.org/wp-content/uploads/20251101122126638001/types_of_machine_learning.webp)

- There are mainly 3 types of machine learning <br>
1. Supervised Machine learning <br>
2. Unsupervised Machine learning <br>
3. Reinforcement Machine learning 

**1. Supervised machine learning** - In this method the data is labeled and we know the input and output. The goal is to learn mapping between them.

**For ex** - Predicts salary (Regression) <br>
             Email spam / Not spam (Classification)

There are two types - <br>
**Regression** - For continous outputs <br> Spam / Not spam <br> Yes / No 
<br>
**Classification** - X(Features) ---> Model ---> Y(Target)


**2. Unsupervised machine learning** - In this method there are no labels, model finds hidden patterns from data and this method is mostly used for exploration. 

**For ex** - Customer segmentation <br>
Grouping similar products 
<br>
The common tasks are clustering, dimensionality reduction.

***" I don't know the answer, just show me the patterns "***

**Reinforcement Learning** - In this method there are models which learns by doing trail and error method. The agent interacts with environment and user give rewards for doing good work and penalty for bad works.

**For ex** - Game playing (chess, go) <br> Self driving cars <br> Robotics 

### Key terms
***Agent ---> Environment ---> Action ---> Reward***

---

<div style="text-align: center; font-size: 40px; font-weight: bold;">
  THE END
</div>

![quotes](https://www.azquotes.com/picture-quotes/quote-doctors-can-be-replaced-by-software-80-of-them-can-i-d-much-rather-have-a-good-machine-vinod-khosla-76-25-07.jpg)
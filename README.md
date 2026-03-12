# 📊 Customer Churn Prediction AI System

## 🔗 Live Application

You can access the live application here:

https://customer-churn-prediction-rz4ejte59qspfvlyk2vfe2.streamlit.app/

---

# 🎯 Purpose of the Project

Customer churn is a major challenge for telecom companies. When customers stop using a service, companies lose revenue and must spend more to acquire new customers.

The purpose of this AI system is to **predict whether a customer is likely to leave the service (churn) or stay** based on customer behavior and service usage patterns.

By identifying customers who are at risk of leaving, companies can take preventive actions such as:

* Offering discounts
* Improving customer support
* Providing better service plans
* Creating personalized retention strategies

This helps businesses **reduce customer loss and improve customer retention**.

---

# ⚙️ Functionality of the AI System

The Customer Churn Prediction system works through the following steps:

### 1️⃣ User Input

The user enters customer details in the dashboard, such as:

* Tenure (months using the service)
* Monthly Charges
* Total Charges
* Contract Type
* Internet Service
* Payment Method
* Customer Demographic Information

---

### 2️⃣ Data Processing

The system processes the input data using the same preprocessing steps used during model training:

* Encoding categorical variables
* Structuring data into the correct feature format
* Preparing the data for prediction

---

### 3️⃣ Machine Learning Prediction

The processed data is passed to a trained **Machine Learning model (XGBoost)** which analyzes the input features and predicts whether the customer is likely to:

* **Churn (leave the service)**
  or
* **Stay with the company**

---

### 4️⃣ Result Display

The system displays the prediction result instantly on the dashboard along with the prediction probability.

Example outputs:

* ⚠️ Customer likely to **CHURN**
* ✅ Customer likely to **STAY**

---

# 🧠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Streamlit

---

# 🖥️ System Interface

The system is implemented as an **interactive web dashboard** where users can easily test predictions by entering customer information.

The dashboard allows real-time prediction and provides a simple interface for business users.

---

# 📂 Project Structure

```
customer-churn-prediction
│
├── app.py
├── churn_model.pkl
├── model_columns.pkl
├── requirements.txt
├── logo.png
└── README.md
```

---

# 👨‍💻 Developer

**Dev Modi**

AI / ML Developer
Machine Learning | Data Analytics | AI Applications

---

⭐ If you found this project useful, please consider starring the repository.

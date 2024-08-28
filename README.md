# Customer Telecom Dataset

This repository contains the **Customer Telecom** dataset, which includes information about customer subscriptions and service usage for a telecommunications company. This dataset is useful for analyzing customer behavior, predicting churn, and performing other related analyses.

## Dataset Overview

The dataset consists of 7,043 records with 21 features. Each record represents a unique customer and includes information about their service subscriptions, charges, and demographic details.

### Data Columns

1. **customerID**: Unique identifier for each customer (object)
2. **gender**: Gender of the customer (object)
3. **SeniorCitizen**: Whether the customer is a senior citizen (1 = Yes, 0 = No) (int64)
4. **Partner**: Whether the customer has a partner (object)
5. **Dependents**: Whether the customer has dependents (object)
6. **tenure**: Number of months the customer has been with the company (int64)
7. **PhoneService**: Whether the customer has phone service (object)
8. **MultipleLines**: Whether the customer has multiple lines (object)
9. **InternetService**: Type of internet service the customer has (object)
10. **OnlineSecurity**: Whether the customer has online security (object)
11. **OnlineBackup**: Whether the customer has online backup (object)
12. **DeviceProtection**: Whether the customer has device protection (object)
13. **TechSupport**: Whether the customer has tech support (object)
14. **StreamingTV**: Whether the customer has streaming TV (object)
15. **StreamingMovies**: Whether the customer has streaming movies (object)
16. **Contract**: Type of contract the customer has (object)
17. **PaperlessBilling**: Whether the customer has paperless billing (object)
18. **PaymentMethod**: Payment method used by the customer (object)
19. **MonthlyCharges**: Monthly charges for the customer (float64)
20. **TotalCharges**: Total charges incurred by the customer (float64)
21. **Churn**: Whether the customer has churned (object)

### Data Types

- **object**: Categorical variables
- **int64**: Integer variables
- **float64**: Floating-point variables

### Usage

This dataset can be used for various analyses, such as:

- **Customer Segmentation**: Identifying different customer segments based on their service usage and demographic information.
- **Churn Prediction**: Building models to predict customer churn based on their service usage and demographic data.
- **Service Usage Analysis**: Understanding the distribution of services used and their impact on customer retention.

### Getting Started

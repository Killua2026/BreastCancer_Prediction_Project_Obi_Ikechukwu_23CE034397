# 🎗️ Breast Cancer Prediction System

A Machine Learning-powered web application that predicts whether a breast tumor is **Benign** or **Malignant** based on digitized image features. This project implements a **Support Vector Machine (SVM)** model served via a **Flask** web interface.

**[🔴 Live Demo Link](https://breastcancer-prediction-project-obi.onrender.com)** 

---

## 🧐 Project Overview
This educational tool uses the **Breast Cancer Wisconsin (Diagnostic)** dataset. It analyzes physical attributes of cell nuclei (like radius, texture, and smoothness) to classify tumors.

**Disclaimer:** This system is for educational purposes only and must not be used as a real medical diagnostic tool.

---

## 🔢 Features Used
The model trains on these 5 features:
1. **Radius Mean:** Mean of distances from center to points on the perimeter.
2. **Texture Mean:** Standard deviation of gray-scale values.
3. **Perimeter Mean:** Size of the core tumor.
4. **Area Mean:** Area of the tumor.
5. **Smoothness Mean:** Local variation in radius lengths.

---

## 🛠 Tech Stack
* **Framework:** Flask
* **ML Algorithm:** Support Vector Machine (SVM) with RBF kernel.
* **Preprocessing:** StandardScaler (Mandatory for SVM).
* **Pipeline:** Scikit-learn Pipeline (bundles Scaler + Model).
* **Deployment:** Render.com

---

## 📊 Model Performance
* **Accuracy:** ~93% (varies on split)
* **Precision/Recall:** Optimized for Malignant detection (Recall is prioritized).

## 👨‍💻 Author
**Name:** Obi Ikechukwu Joseph  
**Matric Number:** 23CE034397

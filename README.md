# AI-Driven Ransomware Detection: Enhancing Cyber Resilience for a Safer Society

## Project Description

This project focuses on detecting ransomware attacks and classifying ransomware samples into their respective families using machine learning techniques. Ransomware is a type of malware that encrypts files and demands payment to restore access. Detecting ransomware early helps prevent data loss and system compromise.

The system analyzes features extracted from executable files and predicts whether the file is **benign or ransomware**. If ransomware is detected, the model attempts to classify it into the correct ransomware family.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Machine Learning Models Used

* Decision Tree
* K-Nearest Neighbors (KNN)
* Random Forest
* XGBoost

Among these algorithms, **XGBoost achieved the highest accuracy and F1-score**.

---

## Steps to Execute the Project

### Step 1: Clone the Repository

git clone https://github.com/KeerthiNune/AI-Driven-Ransomware-Detection-Enhancing-Cyber-Resilience-for-a-Safer-Society.git

### Step 2: Navigate to Project Folder

cd ransomware-detection-project

### Step 3: Install Required Libraries

pip install pandas numpy scikit-learn xgboost matplotlib seaborn

### Step 4: Run the Notebook

Open and run:

source_code/final.ipynb

### Step 5: Provide Feature Inputs

Enter feature values in the prediction interface.

### Step 6: Get Prediction

The system will display:

* Whether the file is **Benign or Ransomware**
* If ransomware, the **predicted ransomware family**

---

## Results

The trained models successfully detect ransomware samples with high accuracy. XGBoost produced the best performance among all models.

However, while ransomware detection works reliably, the model may occasionally misclassify the exact ransomware family due to similarities between different ransomware families.


## Author

Nune Keerthi

Naru Venkata Naga Sai Prasanna Varshini

Peddiboyina Pujitha

Vendra Usha Sri

Putrevu Sathwika

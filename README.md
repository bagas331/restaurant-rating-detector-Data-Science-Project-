# 🍽️ Restaurant Rating Predictor — Machine Learning Web App with Streamlit

This project is a web-based application that predicts restaurant ratings based on various features using a pre-trained machine learning model. Built using **Python**, **Streamlit**, and **scikit-learn**, the app enables real-time prediction with a clean UI and integrated data preprocessing.

---

## 📁 Project Structure

```

📦 restaurant-rating-predictor/
├── Dataset.csv                      # Dataset used to train the model
├── Scaler.pkl                       # Trained StandardScaler object
├── model.pkl                        # Trained prediction model (e.g., regression)
├── app.py                           # Main Streamlit application file
├── restaurant\_rating\_predictor.ipynb # Jupyter notebook for EDA & model training
└── README.md                        # Project documentation

````

---

## 📦 Dependencies

To install required libraries:

```bash
pip install streamlit pandas numpy seaborn matplotlib scikit-learn
````

Or use the `requirements.txt` file if available:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

```bash
streamlit run app.py
```

Then, navigate to [http://localhost:8501](http://localhost:8501) in your web browser.

---

## 🎯 Features

* 📂 **Upload CSV or Input Manually**
  Supports both dataset upload and real-time user input.

* ⚙️ **Data Preprocessing with Scaler**
  Uses `Scaler.pkl` to standardize user input for accurate predictions.

* 🤖 **Rating Prediction**
  Predicts numerical restaurant ratings using `model.pkl`.

* 📊 **Exploratory Data Analysis**
  The notebook `restaurant_rating_predictor.ipynb` contains complete EDA and model training steps.

---

## 🧠 Model Info

The machine learning pipeline includes:

* Feature engineering using `pandas` and `numpy`
* Visualizations with `seaborn` and `matplotlib`
* Model training using `scikit-learn` (e.g., LinearRegression, RandomForest, etc.)
* Scaling via `StandardScaler` before feeding data into the model

Both the scaler and model are serialized using `joblib` or `pickle` and loaded in `app.py`.

---

## 🔍 Example Code Snippet (`app.py`)

```python
import pandas as pd
import joblib

# Load scaler and model
scaler = joblib.load("Scaler.pkl")
model = joblib.load("model.pkl")

# Sample input
input_data = pd.DataFrame({
    'Votes': [340],
    'Cost': [500],
    'Online_order': [1],
    'Book_table': [0],
    # ... other features
})

# Preprocess and predict
scaled = scaler.transform(input_data)
prediction = model.predict(scaled)

st.write("Predicted Rating:", round(prediction[0], 2))
```


## 📝 License

This project is licensed under the [MIT License](LICENSE).


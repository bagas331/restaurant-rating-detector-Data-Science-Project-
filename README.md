# Restaurant Rating Detector - Data Science Project

## 📖 Project Overview

**Restaurant Rating Detector** is a machine learning application designed to predict restaurant ratings based on various operational, environmental, and demographic features. Leveraging established statistical theories and empirical methods, this project aims to provide restaurateurs and food-tech platforms with reliable insights into customer satisfaction and business performance.

### 🎯 Objectives

* Systematically analyze and preprocess dataset attributes to maximize predictive accuracy.
* Develop and evaluate multiple regression models following best practices in supervised learning.
* Deploy a user-friendly web interface for on-the-fly rating predictions using Streamlit.

## 📁 Repository Structure

```
├── Dataset.csv                # Raw dataset of restaurant features and historical ratings
├── restaurant_rating_predictor.ipynb  # Exploratory data analysis & model development notebook
├── model.pkl                  # Serialized trained regression model
├── Scaler.pkl                 # Serialized feature scaler (StandardScaler)
├── app.py                     # Streamlit app for real-time rating predictions
└── README.md                  # Project documentation (this file)
```

## 🔬 Methodology

1. **Data Collection & Cleaning**

   * Imported `Dataset.csv` containing quantitative attributes (e.g., number of seats, staff size, average meal price) and qualitative factors (e.g., cuisine type, location demographics).
   * Handled missing values using median imputation and one-hot encoded categorical variables.

2. **Feature Engineering & Scaling**

   * Engineered interaction terms and polynomial features based on correlation analysis.
   * Applied **StandardScaler** to normalize continuous features, reducing model bias towards large-scale attributes.

3. **Model Development**

   * Compared multiple regression algorithms: Linear Regression, Ridge, Lasso, and Random Forest Regressor.
   * Used cross-validation (k=5) to assess generalization error and prevent overfitting.
   * Selected the model with the lowest Root Mean Square Error (RMSE) on the validation set.

4. **Serialization**

   * Serialized the final model (`model.pkl`) and scaler (`Scaler.pkl`) using `joblib` for production deployment.

5. **Deployment**

   * Built an interactive **Streamlit** app (`app.py`) to input feature values and display predicted ratings in real-time.

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* Conda or virtualenv (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/<username>/restaurant-rating-detector-Data-Science-Project.git
cd restaurant-rating-detector-Data-Science-Project

# Create and activate environment
conda create -n rating-detector python=3.8 -y
conda activate rating-detector

# Install dependencies
pip install -r requirements.txt
```

### Running the Streamlit App

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser to interact with the rating predictor.

## 📈 Results & Evaluation

* **Best Model**: Random Forest Regressor
* **Validation RMSE**: 0.42 (5-fold CV)
* **Test RMSE**: 0.45
* **R² Score** on Test Set: 0.76

These metrics demonstrate a strong predictive capability, aligning with established regression theory on bias-variance trade-off and ensemble methods.

## 📑 SEO & Business Relevance

* **Keywords**: restaurant rating prediction, machine learning, data science, Streamlit deployment, Random Forest Regressor
* **Use Cases**: Enhancing customer satisfaction, optimizing menu pricing, location-based performance analysis, food-tech platform integrations.

## 🔮 Future Work

* Integrate additional external data sources (e.g., social media sentiment, foot traffic analysis).
* Experiment with advanced models (e.g., XGBoost, LightGBM) for improved performance.
* Containerize with Docker and deploy on cloud platforms (AWS, GCP, Azure).

## 📝 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

*Empirical. Systematic. Logical. Up-to-date.*

"""
Week 2 - Model Training + MLflow Tracking
Objectif: Prédire salary_usd (Regression)
"""

import pandas as pd
import numpy as np
from pathlib import Path
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.feature_extraction.text import TfidfVectorizer

# ============================================================
# CONFIGURATION
# ============================================================

DATA_PATH = Path("data/processed/jobs_cleaned.csv")
RANDOM_STATE = 42
TEST_SIZE = 0.2

mlflow.set_experiment("Job_Salary_Prediction")

# ============================================================
# LOAD DATA
# ============================================================

def load_data():
    if not DATA_PATH.exists():
        raise FileNotFoundError("Execute d'abord 02_clean_data.py")
    
    df = pd.read_csv(DATA_PATH)
    return df


# ============================================================
# PREPROCESSING
# ============================================================

def prepare_data(df):
    X = df.drop("salary_usd", axis=1)
    y = df["salary_usd"]

    categorical_cols = [
        "experience_level",
        "employment_type",
        "company_size",
        "source"
    ]

    numeric_cols = ["remote_ratio"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", "passthrough", numeric_cols),
            ("text", TfidfVectorizer(max_features=100), "job_title")
        ]
    )

    return X, y, preprocessor

# ============================================================
# TRAIN FUNCTION
# ============================================================

def train_model(model, model_name, X_train, X_test, y_train, y_test, preprocessor, params=None):
    
    with mlflow.start_run(run_name=model_name):

        pipeline = Pipeline([
            ("preprocessing", preprocessor),
            ("model", model)
        ])

        # Log parameters
        if params:
            for key, value in params.items():
                mlflow.log_param(key, value)

        # Train
        pipeline.fit(X_train, y_train)

        # Predict
        y_pred = pipeline.predict(X_test)

        # Metrics
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)

        # Cross-validation
        cv_scores = cross_val_score(
            pipeline,
            X_train,
            y_train,
            cv=5,
            scoring="r2"
        )

        # Log metrics
        mlflow.log_metric("MAE", mae)
        mlflow.log_metric("RMSE", rmse)
        mlflow.log_metric("R2", r2)
        mlflow.log_metric("CV_R2_mean", cv_scores.mean())

        # Log model
        mlflow.sklearn.log_model(pipeline, model_name)

        print("\n" + "="*50)
        print(f"Model: {model_name}")
        print(f"MAE: {mae:,.0f}")
        print(f"RMSE: {rmse:,.0f}")
        print(f"R2: {r2:.3f}")
        print(f"CV R2 Mean: {cv_scores.mean():.3f}")
        print("="*50)

        return r2


# ============================================================
# MAIN
# ============================================================

def main():

    print("\n" + "="*60)
    print("WEEK 2 - MODEL TRAINING + MLFLOW")
    print("="*60)

    df = load_data()

    X, y, preprocessor = prepare_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )

    results = {}

    # 1️⃣ Linear Regression (Baseline)
    results["LinearRegression"] = train_model(
        LinearRegression(),
        "Linear_Regression",
        X_train, X_test, y_train, y_test,
        preprocessor
    )

    # 2️⃣ Random Forest
    rf_params = {"n_estimators": 200, "max_depth": 10}
    results["RandomForest"] = train_model(
        RandomForestRegressor(
            n_estimators=200,
            max_depth=10,
            random_state=RANDOM_STATE
        ),
        "Random_Forest",
        X_train, X_test, y_train, y_test,
        preprocessor,
        rf_params
    )

    # 3️⃣ Gradient Boosting
    gb_params = {"n_estimators": 150, "learning_rate": 0.1}
    results["GradientBoosting"] = train_model(
        GradientBoostingRegressor(
            n_estimators=150,
            learning_rate=0.1,
            random_state=RANDOM_STATE
        ),
        "Gradient_Boosting",
        X_train, X_test, y_train, y_test,
        preprocessor,
        gb_params
    )

    # Best model
    best_model = max(results, key=results.get)

    print("\n🏆 BEST MODEL:", best_model)
    print("R2:", results[best_model])


if __name__ == "__main__":
    main()
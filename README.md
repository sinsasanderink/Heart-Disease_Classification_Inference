# 🫀 Heart Disease Classification & Inference System

This repository provides a complete end-to-end **heart disease prediction system**, covering everything from **data preprocessing, model training, hyperparameter tuning, and performance evaluation** to **inference pipeline scripting** with production-ready design.

The system is built using **Python** and **scikit-learn**, with support for **logging, modular structure, error handling, model persistence**, and integration points for **Airflow** or any production-grade orchestration tool. The project was initially developed in a Jupyter notebook and has since been **refactored into reusable, maintainable code components**.

---

## 🚀 Key Highlights

### ✅ Classification Models Implemented
- **Decision Tree** (with entropy/gini, pruning, and GridSearchCV tuning)
- **Neural Network (MLPClassifier)** (tuned with grid search on hidden layers and learning rate)
- **AdaBoost** (with SAMME/SAMME.R, learning rate tuning, and ensemble optimization)
- **Support Vector Machine (SVM)** (with kernel, gamma, and regularization tuning)
- **K-Nearest Neighbors (KNN)** (with distance algorithm, leaf size, and K optimization)

Each model underwent:
- Baseline training
- Hyperparameter tuning via `GridSearchCV`
- Training/validation/test evaluation
- Learning curves & loss curve analysis
- Final selection based on bias-variance trade-off, AUC-ROC, time complexity, and domain risk (favoring lower false negatives due to the medical domain)

---

## 🛠️ Inference Pipeline

The pipeline includes:

- **Preprocessing Steps** identical to training pipeline:
  - Duplicate removal
  - One-hot encoding
  - Feature alignment with training schema
  - Normalization with MinMaxScaler
- **Model Loading** from `.joblib` files
- **Prediction & Accuracy Scoring**
- **Logging & Error Handling** with `logging` module
- **Runtime Arguments** for switching between `svm` and `adaboost` inference modes

Run the inference using:

```bash
python main.py --model adaboost
python main.py --model svm
```

The inference data is expected at `Data/inference_heart_disease.csv`. This can be swapped with live-streaming data via `get_inference_data()` in `utils.py`.

---

## 🧪 Testing

Basic **unit tests** are included inside the `unit_test/` folder to validate:
- Data fetching logic
- Preprocessing alignment
- Dimension checks
- Model I/O

---

## 🗂️ Project Structure

```
.
├── constants.py                 # Configuration constants
├── Data/                        # Training and inference data files
├── Heart Disease Classification.ipynb     # Initial notebook for training & EDA
├── Heart Disease Inference.py            # Notebook for inference (converted to script)
├── main.py                     # Entry point for running inference pipeline
├── model1_adaboost.joblib      # Saved AdaBoost model
├── model2_svm.joblib           # Saved SVM model
├── utils.py                    # All reusable utility functions
├── unit_test/                  # Unit tests for inference components
├── inference_pipe_exec.log     # Logging output file
└── __pycache__/                # Compiled Python cache
```

---

## 🧠 Dataset Used

- **Source**: [UCI ML Repository - Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)
- Contains 303 records with 13 attributes
- Features are a mix of categorical and continuous
- Final target: binary classification (`0`: no heart disease, `1`: heart disease)

---

## 📊 Model Selection Summary

| Model            | Test Accuracy | AUC-ROC | Overfitting | Comments |
|------------------|---------------|---------|-------------|----------|
| Decision Tree    | ~0.84         | Low     | Moderate    | Simple but underperforming |
| Neural Network   | ~0.90         | Good    | Slight      | Some instability, slight bias |
| **AdaBoost**     | ~0.96         | High    | None        | ✅ Best performance, generalizes well |
| **SVM**          | ~0.97         | High    | None        | ✅ Best accuracy, reliable |
| KNN              | ~0.89         | Moderate| Slight      | Biased, underfit |

> 🔬 **Medical Context**: False Negatives are more dangerous. Preference is given to models with fewer FNs (AdaBoost, SVM).

---

## 🧱 Production-Ready Features

- ✅ Notebook-to-script conversion
- ✅ Modularized code structure (preprocessing, inference, I/O)
- ✅ Trained models persisted via `joblib`
- ✅ Logging using Python's `logging` module
- ✅ Robust error handling
- ✅ CLI integration for easy model selection
- ✅ Inference data schema alignment
- ✅ Unit testing support
- ✅ **Ready for orchestration with Airflow**, Prefect, or cron

---

## 🔮 Deployment Readiness

This project is **fully ready for deployment** as a scheduled inference pipeline. You can easily:

- Deploy `main.py` as a DAG in **Apache Airflow**
- Containerize it with **Docker**
- Schedule inference against live data from an API or database
- Integrate with notification systems on prediction confidence or anomalies

---

## 🤝 Acknowledgements

Original dataset compiled by:
- Andras Janosi, William Steinbrunn, Matthias Pfisterer, Robert Detrano  
Donated by:
- David W. Aha (aha '@' ics.uci.edu)

---

## 📎 License

This project is open for educational and research purposes. Commercial deployment rights are subject to dataset source license (UCI).

---

## 👨‍💻 Author

Designed, developed, and modularized for production deployment with real-world constraints in mind. Includes all necessary components to transition from prototype to live application.

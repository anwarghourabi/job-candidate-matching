# 🎯 Job-Candidate Matching System - Week 1 Complete

## 📊 Project Overview

Unsupervised learning system for intelligent CV-to-job matching with explainable AI.

**Status:** ✅ Week 1 EDA Complete

---

## 📁 Project Structure

```
job-candidate-matching/
├── code/
│   ├── 01_load_data.py              # Load HuggingFace dataset
│   ├── 02_clean_data.py             # Clean & standardize data
│   ├── 03_explore_data.py           # Exploratory analysis
│   ├── 04_visualize.py              # Generate visualizations & report
│   ├── 05_scrape_remoteok.py        # Scrape RemoteOK API
│   ├── 06_merge_datasets.py         # Merge HF + RemoteOK
    |___07_train_models_mlflow.py
│   └── utils.py                     # Utility functions
│
├── data/
│   ├── raw/
│   │   ├── huggingface_salaries.csv  # Original HF data (607 offers)
│   │   ├── jobs_scraped_remoteok.csv # RemoteOK scraped data
│   │   └── jobs_merged.csv           # Merged dataset (700+)
│   ├── processed/
│   │   ├── jobs_cleaned.csv          # Cleaned dataset (279 offers)
│   │   ├── jobs_cleaned.pkl          # Backup pickle
│   │   └── EDA_REPORT.txt            # Detailed EDA report
│   └── visualizations/
│       ├── 01_salary_distribution.png
│       ├── 02_experience_distribution.png
│       ├── 03_top_locations.png
│       └── 04_remote_ratio.png
│
├── notebooks/
│   └── EDA.ipynb                     # Jupyter notebook (optional)
│
├── tests/
│   └── test_cleaning.py              # Unit tests
│
├── .vscode/
│   ├── settings.json
│   └── launch.json
│
├── venv/                             # Virtual environment
├── .gitignore
├── README.md                         # This file
└── requirements_week1.txt            # Python dependencies
```

---

## 📊 Week 1 Results

### Data Overview
- **Total Job Offers:** 279 (after cleaning)
- **Data Sources:** HuggingFace (607) + RemoteOK (100+)
- **Locations:** 104 countries/regions
- **Columns:** 8 (job_title, salary_usd, experience_level, employment_type, location, remote_ratio, company_size, source)

### Salary Analysis
- **Min:** $2,859
- **Max:** $450,000
- **Mean:** $86,552
- **Median:** $69,999
- **Std Dev:** $75,669
- **Q1-Q3:** $38,588 - $111,454

### Experience Distribution
| Level | Count | % | Avg Salary |
|-------|-------|---|-----------|
| Mid-Level | 75 | 41.9% | $74,707 |
| Senior | 52 | 29.1% | $116,922 |
| Entry-Level | 40 | 22.3% | $48,307 |
| Executive | 12 | 6.7% | $156,456 |

### Remote Work
- **100% Remote:** 95 (53.1%)
- **Hybrid (50%):** 53 (29.6%)
- **On-Site:** 31 (17.3%)

### Top Locations
1. US (21.8%)
2. Canada (7.8%)
3. India (7.3%)
4. Germany (6.1%)
5. UK (6.1%)

---

## 🚀 Quick Start

### Setup (First Time)

```bash
# Create project structure
cd job-candidate-matching
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements_week1.txt
```

### Run Week 1 Complete Pipeline

```bash
# 1. Load data
python code/01_load_data.py

# 2. Merge datasets (optional)
python code/05_scrape_remoteok.py
python code/06_merge_datasets.py

# 3. Clean data
python code/02_clean_data.py

# 4. Analyze & visualize
python code/03_explore_data.py
python code/04_visualize.py
```

---

## 📝 Configuration

### 02_clean_data.py - Key Setting

```python
# Choose input dataset:
csv_path = Path('data/raw/jobs_merged.csv')  # HF + RemoteOK
# OR
csv_path = Path('data/raw/huggingface_salaries.csv')  # HF only
```

---

## 📊 Deliverables

### Generated Files
✅ `data/processed/jobs_cleaned.csv` - Cleaned dataset (279 rows)
✅ `data/processed/jobs_cleaned.pkl` - Backup pickle format
✅ `data/processed/EDA_REPORT.txt` - Detailed statistics
✅ `data/visualizations/01-04_*.png` - 4 professional charts
✅ `EDA_REPORT_WEEK1.pdf` - Executive summary (this report)

---

## 🔍 Key Findings

### Data Quality
- **Duplicates Removed:** 428 (36.3%)
- **Missing Values:** Handled appropriately
- **Standardization:** Complete across both sources

### Market Insights
1. **Salary Gap:** Seniors earn 2.4x entry-level salaries
2. **Remote Dominance:** 53% of offers are fully remote
3. **Geographic Concentration:** US accounts for 21.8% of all offers
4. **Experience Demand:** Mid-level roles are most common (41.9%)

### Data Sources
- **HuggingFace:** Structured data with salaries
- **RemoteOK:** Remote-first jobs, no salary data
- **Combined:** Diversified dataset with 700+ offers

---

## 📈 Week 2 Recommendations

### Feature Engineering
- [ ] Create salary categories (low, mid, high, executive)
- [ ] Encode experience levels (ordinal: entry < mid < senior < executive)
- [ ] Normalize numerical features (salary_usd)
- [ ] Handle missing values (RemoteOK has no salary data)

### Vectorization
- [ ] TF-IDF for job titles
- [ ] One-hot encoding for categorical features
- [ ] Word embeddings for descriptions (if available)
- [ ] Normalize salary_usd with StandardScaler

### Clustering Preparation
- [ ] Determine optimal number of clusters (elbow method)
- [ ] Scale features appropriately
- [ ] Consider clustering by source separately

### Model Development
- [ ] K-Means Clustering (unsupervised)
- [ ] Anomaly Detection (Isolation Forest)
- [ ] Candidate-Job Matching Score
- [ ] Explainability (SHAP values)

---

## 🔧 Technologies Used

### Data Processing
- pandas >= 2.0.0
- numpy >= 1.24.0

### Visualization
- matplotlib >= 3.8.0
- seaborn >= 0.13.0
- plotly >= 5.18.0

### Machine Learning
- scikit-learn >= 1.3.0
- scipy >= 1.11.0

### Data Sources
- datasets (HuggingFace)
- requests (RemoteOK API)

### Development
- VSCode
- Python 3.10+
- Git

---

## 📞 Support

### Common Issues

**Issue:** `KeyError: 'location'`
- **Solution:** Ensure you're using `jobs_merged.csv` or updated code

**Issue:** `work_year column not found`
- **Solution:** This column was removed during cleaning (not in merged dataset)

**Issue:** RemoteOK API fails
- **Solution:** Use HuggingFace only - RemoteOK is optional

---

## 📚 Files Reference

| File | Purpose | Status |
|------|---------|--------|
| 01_load_data.py | Load HuggingFace | ✅ Complete |
| 02_clean_data.py | Clean & standardize | ✅ Complete |
| 03_explore_data.py | Exploratory analysis | ✅ Complete |
| 04_visualize.py | Visualizations & report | ✅ Complete |
| 05_scrape_remoteok.py | Scrape RemoteOK | ✅ Complete |
| 06_merge_datasets.py | Merge sources | ✅ Complete |
| utils.py | Utility functions | ✅ Complete |

---

## 📅 Timeline

| Week | Focus | Status |
|------|-------|--------|
| **Week 1** | EDA & Data Preparation | ✅ COMPLETE |
| **Week 2** | Feature Engineering | ⏳ Next |
| **Week 3** | Clustering & Anomaly Detection | ⏳ TBD |
| **Week 4** | API Development (FastAPI) | ⏳ TBD |
| **Week 5** | Frontend (React) | ⏳ TBD |
| **Week 6** | Docker & Deployment | ⏳ TBD |
| **Week 7** | Final Review | ⏳ TBD |

---

## 🎯 Next Steps

1. **Review EDA Report** - Read `EDA_REPORT_WEEK1.pdf`
2. **Validate Data** - Check visualizations in `data/visualizations/`
3. **Plan Week 2** - Feature engineering strategy
4. **Update Code** - Prepare for clustering algorithms

---

## ✅ Week 1 Checklist

- [x] Data collected (607 HF + 100+ RemoteOK)
- [x] Data merged (700+ total)
- [x] Data cleaned (279 final)
- [x] EDA completed
- [x] 4 visualizations generated
- [x] Report generated
- [x] Code organized
- [x] Documentation complete

---

## 📊 Week 2  Results
🔹 Prétraitement

Colonnes catégorielles → OneHotEncoder

Colonnes numériques → StandardScaler

Colonne texte (job_title) → TfidfVectorizer(max_features=100)

Utilisation d’un ColumnTransformer pour combiner toutes les transformations et enrichir le modèle avec des features textuelles.

🔹 Modèles testés
Modèle	R² Test	CV R²
Linear Regression	0.26	-4.97
Random Forest	0.44	-0.15
Gradient Boosting	0.31	-0.43

✅ Meilleur modèle : Random Forest

Les modèles non linéaires exploitent mieux les features TF-IDF et capturent les interactions complexes.

🔹 MLflow - Suivi des expériences

MLflow a permis de :

Suivre les métriques : MAE, RMSE, R².

Sauvegarder automatiquement les modèles et transformations.

Comparer facilement plusieurs modèles via une interface web.

1️⃣ Lancement de MLflow UI
mlflow ui
```
Accéder ensuite à : http://localhost:5000

2️⃣ Aperçu de l’interface

Liste des expériences : chaque exécution est enregistrée.

Comparaison des modèles : R², MAE, RMSE.

Visualisation des paramètres : hyperparamètres utilisés pour chaque modèle.

Téléchargement des modèles pour déploiement ou tests futurs.

🔹 Exemple visuel MLflow
┌───────────────────────────── MLflow UI ─────────────────────────────┐
│ Expérience : Job_Salary_Prediction                                   │
├───────────────────────────── Métriques ──────────────────────────────┤
│ Run #1  | Linear Regression | R²=0.26 | MAE=33,833 | RMSE=46,623      │
│ Run #2  | Random Forest     | R²=0.44 | MAE=25,956 | RMSE=40,495      │
│ Run #3  | Gradient Boosting | R²=0.31 | MAE=30,795 | RMSE=44,939      │
└──────────────────────────────────────────────────────────────────────┘

Chaque run contient le modèle sauvegardé, les métriques et les paramètres d’entraînement.
🔹 Résultats

Random Forest est le modèle le plus performant pour ce dataset.

La régression linéaire devient instable avec l’ajout des features textuelles.

Le dataset limité entraîne une variance élevée et un R² relativement modeste.

🔹 Améliorations possibles

Transformer le problème en classification de salaire (low, medium, high).

Ajuster le nombre de features TF-IDF ou utiliser Word2Vec pour enrichir la représentation textuelle.

Tester la régularisation (Ridge, Lasso) pour les modèles linéaires.

Ajouter davantage de données pour stabiliser le modèle.

Hyperparameter tuning pour Random Forest et Gradient Boosting.

🔹 Exécution

Pour lancer l’entraînement et le suivi MLflow :

python src/train_model.py

Pour ouvrir l’interface MLflow UI :

mlflow ui
🔹 Licence

MIT License – libre utilisation et modification.

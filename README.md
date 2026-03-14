# 🌍 Early Warning Food Price Monitor — Northeast Nigeria

> A multi-model time series forecasting system for predicting monthly retail food prices up to three months ahead across conflict-affected states in Northeast Nigeria.

[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://earlywarningfoodpricemonitor-group3.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-TSA_DS_Capstone_Group3-181717?style=for-the-badge&logo=github)](https://github.com/Mi-kami/TSA_DS_Capstone_Group3)

---

## 🔗 Live Deployment

**👉 [https://earlywarningfoodpricemonitor-group3.streamlit.app/](https://earlywarningfoodpricemonitor-group3.streamlit.app/)**

The app provides a three-month price outlook for five key commodities across Adamawa, Borno and Yobe — three conflict-affected states in Northeast Nigeria where food insecurity is most acute. No technical knowledge required.

---

## 📌 Project Overview

Food price volatility in Northeast Nigeria is driven by a compounding set of structural forces: the Boko Haram insurgency, the June 2023 fuel subsidy removal, naira devaluation, seasonal harvest cycles, and climate variability. Existing price monitoring systems report prices retrospectively — after market changes have already occurred.

This project addresses that gap by building a **data-driven forecasting pipeline** that predicts monthly retail food prices **up to three months in advance**, giving policymakers, humanitarian organisations, traders and farmers the lead time needed to act before a crisis arrives.

**Three models were built, evaluated and compared:**
- SARIMA — classical seasonal time series model
- XGBoost — gradient boosting with exogenous features
- Facebook Prophet — decomposable trend-seasonality model

All models were evaluated against a naive baseline across one-month, two-month and three-month forecast horizons.

---

## 📊 Results Summary

### Overall Model Comparison — Tier 1 (Adamawa, Borno, Yobe)

| Model | Combinations Won | Win Rate | Average MAPE |
|:------|:---:|:---:|:---:|
| Prophet | 10 of 13 | 76.9% | 30.8% |
| XGBoost | 2 of 13 | 15.4% | 49.5% |
| SARIMA | 1 of 13 | 7.7% | 53.6% |

### Prophet Accuracy by Forecast Horizon

| Horizon | Prophet Avg MAPE | XGBoost Avg MAPE |
|:--------|:---:|:---:|
| H1 — 1 month ahead | 24.5% | 51.1% |
| H2 — 2 months ahead | 28.5% | 48.3% |
| H3 — 3 months ahead | 35.3% | 49.7% |

### Full Results — All 13 Combinations

| Commodity | State | Prophet MAPE | SARIMA MAPE | XGBoost MAPE | Best Model |
|:----------|:-----:|:---:|:---:|:---:|:---:|
| Rice (imported) | Borno | **14.7%** | 39.7% | 33.8% | Prophet |
| Rice (imported) | Yobe | **18.1%** | 55.8% | 53.7% | Prophet |
| Rice (local) | Yobe | **18.4%** | 45.6% | 53.5% | Prophet |
| Yam | Adamawa | 88.2% | 144.8% | **21.7%** | XGBoost |
| Rice (imported) | Adamawa | **25.5%** | 35.5% | 37.5% | Prophet |
| Beans (white) | Borno | 32.6% | **25.6%** | 46.3% | SARIMA |
| Rice (local) | Borno | **25.6%** | 54.0% | 52.3% | Prophet |
| Yam | Yobe | **26.6%** | 56.5% | 72.4% | Prophet |
| Beans (white) | Yobe | **28.5%** | 36.6% | 63.3% | Prophet |
| Yam | Borno | **30.3%** | 64.4% | 64.9% | Prophet |
| Rice (local) | Adamawa | 42.6% | 35.4% | **30.9%** | XGBoost |
| Tomatoes | Borno | **31.2%** | 52.0% | 57.5% | Prophet |
| Tomatoes | Yobe | **34.4%** | 50.8% | 57.6% | Prophet |

**Bold** = best model per combination. 11 of 13 combinations are production-ready (MAPE ≤ 35%). 2 are directional-only.

---

## 📁 Repository Structure

```
TSA_DS_Capstone_Group3/
│
├── data/
│   ├── model data/
|   |   ├── best_model_per_combination
|   |   ├── model_comparison_final
|   |   ├── prophet_horizon_results
|   |   ├── prophet_tier2_credible
|   |   ├── sarima_results
|   |   ├── xgb_horizon_results
|   |   ├── xgb_importance
|   |   ├── xgb_results
|   |
|   |
|   ├── Processed/          # Cleaned and merged
|   |   ├── master_dataset_clean_final_.csv
│   |   ├── sarima_results.csv
│   |   ├── prophet_results.csv
│   |   ├── xgb_results.csv
│   |   ├── prophet_horizon_results.csv
│   |   ├── xgb_horizon_results.csv
│   |   ├── model_comparison_final.csv
│   |   └── best_model_per_combination.csv
│   |
|   |
|   ├── raw/                    # Original unmodified source files
│   │   ├── wfp_food_prices_nga.csv
│   │   ├── 2024_Statistical_Bulletin_Real_Sector.xlsx
│   │   ├── 2024_Statistical_Bulletin_External_Sector.xlsx
│   │   ├── 2024_Statistical_Bulletin_Financial_Sector.xlsx
│   │   ├── FAOSTAT_import_volume.csv
│   │   ├── Africa_aggregated_conflict_data.xlsx
│   │   ├── Europe_Brent_Spot_Price.csv
│   │   └── pms_monthly_reports/   # 37 individual NBS reports 
|   |
|   | 
├── visuals/
│   ├── EDA_plots/
│   └── model_plots/
│
├── notebooks/
│   ├── 01_Project_Setup_and_Data_Loading.ipynb
│   ├── 02_Data_Cleaning_and_Preprocessing.ipynb
│   ├── 03_Data_Merging_and_Feature_Engineering.ipynb
│   ├── 04_Exploratory_Data_Analysis.ipynb
│   ├── 05_SARIMA_Modelling.ipynb
│   ├── 06_XGBoost_Modelling.ipynb
│   ├── 07_Prophet_Modelling.ipynb
│   ├── 08_Model_Comparison_and_Evaluation.ipynb
│   ├── 09_Documentation_and_Report.ipynb
│   └── merged_submission_notebook.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📓 Notebook Guide

| # | Notebook | Description |
|:--|:---------|:------------|
| 01 | Project Setup & Data Loading | Environment setup, raw data ingestion, initial inspection |
| 02 | Data Cleaning & Preprocessing | Missing value handling, outlier treatment, data type corrections |
| 03 | Data Merging & Feature Engineering | Master dataset construction, lag features, harvest season indicator, cross-commodity average price, subsidy removal indicator |
| 04 | Exploratory Data Analysis | Price distributions, trend analysis, seasonality decomposition, correlation analysis, conflict impact visualisation |
| 05 | SARIMA Modelling | Per-combination parameter selection, SARIMAX feature testing, single-step evaluation against naive baseline |
| 06 | XGBoost Modelling | Direct multi-horizon modelling (H1/H2/H3), feature importance analysis, walk-forward evaluation |
| 07 | Prophet Modelling | Multiplicative seasonality, subsidy regressor, Tier 1 and Tier 2 evaluation, proportional split for Tier 2 |
| 08 | Model Comparison & Evaluation | Cross-model aggregation, best model selection, horizon decay analysis, results export |
| 09 | Documentation & Report | Full project documentation, literature review, methodology, results narrative, conclusions |
| — | Merged Submission Notebook | NB01–NB08 merged into a single end-to-end executable notebook |

---

## 🗂️ Data Sources

| Source | Description |
|:-------|:------------|
| WFP VAM | Monthly retail food prices across Nigerian markets (primary target variable) |
| Central Bank of Nigeria (CBN) | Exchange rate (NGN/USD), monetary policy indicators |
| National Bureau of Statistics (NBS) | Inflation rate, fuel prices (PMS), import volume data |
| ACLED | Georeferenced conflict event data — fatalities and weighted conflict score |
| NIMET / CHIRPS | Monthly rainfall data for agricultural yield signal |

**Coverage:** January 2017 – December 2024 | 13 states | 5 commodities | ~2,846 observations

---

## 🛠️ How to Run

### Option 1 — Run in Google Colab (Recommended)

1. Open the merged submission notebook in Google Colab
2. Mount your Google Drive:
```python
from google.colab import drive
drive.mount('/content/drive')
```
3. Ensure the data folder exists at:
```
/content/drive/MyDrive/price forecasting project data(cleaned)/
```
4. Run all cells from top to bottom (`Runtime → Run all`)

### Option 2 — Run Locally

**Requirements:** Python 3.9+

```bash
# Clone the repository
git clone https://github.com/Mi-kami/TSA_DS_Capstone_Group3.git
cd TSA_DS_Capstone_Group3

# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py
```

### Requirements

```
streamlit
pandas
numpy
scikit-learn
xgboost
prophet
statsmodels
matplotlib
seaborn
```

---

## 📦 Key Features

- **Multi-model pipeline** — SARIMA, XGBoost and Prophet trained and evaluated on identical data splits
- **Walk-forward evaluation** — all models evaluated at H1, H2 and H3 horizons (SARIMA at H1 only)
- **Structural break handling** — binary `subsidy_removed` regressor explicitly marks the June 2023 fuel subsidy removal in all models
- **Tiered evaluation** — Tier 1 (Adamawa, Borno, Yobe) with fixed date splits; Tier 2 (10 states) with proportional splits
- **Credibility filter** — combinations above 35% MAPE labelled directional-only rather than production-ready
- **Live deployment** — Streamlit app with Model Comparison and Forecast Explorer pages

---

## 👥 Team

| Name | Role | GitHub |
|:-----|:-----|:-------|
| Olofin Deborah (Temi) | Team Lead, Lead Data scientist, ML engineer | [@Mi-kami](https://github.com/Mi-kami) |
| Victor Barilee Kayli | EDA | [@Alexinho9](https://github.com/Alexinho9) |
| Amusa Rhoda | EDA, Modelling & Analytics | [@Musa-Rhoda](https://github.com/Musa-Rhoda) |
| Mrs. Judith Amaka | EDA | [@Judithamaka1](https://github.com/Judithamaka1) |
| Awoyemi Emmanuel| EDA | [@awoyemiemmanuel1900](https://github.com/awoyemiemmanuel1900) |
| Dare Divine | Evaluation & Insight | [@Dee-animated](https://github.com/Dee-animated) |
| Daniel Abel Ojonugwa| Documentation & Report | [@danielojonugwa](https://github.com/danielojonugwa) |
| Divine ega | Documentation & Report | [@divineega](https://github.com/divineega) |
| Dr. Ajibola | Documentation & Report | [@DrAjibola](https://github.com/DrAjibola) |
| Afeez Adigun Shittu | Data Sourcing, Deployment | [@afeezshittu28-debug](https://github.com/afeezshittu28-debug) |
| Mr. Showunmi Jonathan | Documentation & Report | [@Shoyemi-Jonathan-Showunmi](https://github.com/Shoyemi-Jonathan-Showunmi) |

---

## 📄 License

This project was developed as a Data Science capstone project. All data sources are publicly available and credited above.

---

<p align="center">
  Built with purpose. Deployed for impact. 🙏
</p>

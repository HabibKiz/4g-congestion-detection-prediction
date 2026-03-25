# Intelligent Network Monitoring: Clustering-based Detection and Predictive Modelling of Congestion in 4G Networks

**MSc Thesis · University of Middlesex Dubai · 2025**  
**Author:** Habib Kizamou · Internship at Sofrecom (Orange Group), Rabat

---

## Overview

Telecom networks generate massive streams of KPI data — but turning that data into early warnings operators can actually act on is the real challenge. This project tackles exactly that, using a **hybrid ML pipeline** combining unsupervised clustering and supervised forecasting on live 4G radio access network data from **Orange Mali**.

The pipeline moves from raw operational exports to two operational outputs:
1. **Clustering** — segment network cells by behaviour to surface congestion-risk cohorts
2. **Forecasting** — predict KPI trajectories 1–7 days ahead to enable proactive intervention

---

## Results at a Glance

| Task | Best Model | Key Metric |
|------|-----------|------------|
| Cell segmentation (11 KPIs, 1M+ obs) | HDBSCAN | Silhouette: **0.69–0.70** |
| Short-term forecasting (1–7 day) | XGBoost | **30–60% lower MAE** vs Prophet |
| Synthetic Busy Hour generation | XGBoost Tweedie | 1 month → **6 months** coverage |

---

## Dataset

Data was extracted from **Orange Mali's 4G Radio Access Network** via Sofrecom's PRS interface — live operational KPI exports across four temporal granularities:

| Granularity | Rows |
|------------|------|
| Weekly | ~637K+ (combined) |
| Daily | |
| Hourly | |
| Busy Hour (BH) | |

**11 KPIs tracked:** accessibility, retainability, mobility, traffic volume, throughput, and user experience metrics.

> ⚠️ **Note:** Raw data is proprietary to Orange Group / Sofrecom and is not included in this repository. Notebooks use anonymised or synthetic data where applicable.

---

## Repository Structure

```
4g-congestion-detection-prediction/
│
├── notebooks/
│   ├── 01_data_preparation/       # Cleaning, standardisation, synthetic BH creation
│   ├── 02_eda/                    # Univariate, bivariate, correlation analysis
│   ├── 03_clustering/             # HDBSCAN, K-Means, GMM across granularities
│   └── 04_forecasting/            # Prophet, XGBoost, polynomial regression benchmarks
│
├── report/
│   └── Habib_Kizamou_Thesis.pdf   # Full dissertation report
│
├── presentation/
│   └── Thesis_Presentation.pptx   # Defence slides
│
├── requirements.txt
└── README.md
```

---

## Methodology

### 1. Data Preparation
- Standardised 637,000+ rows of live KPI exports across 4 temporal aggregations
- Handled missing data, outliers, and unit inconsistencies
- Generated a **synthetic Busy Hour dataset** using XGBoost Tweedie regression to extend temporal coverage from 1 to 6 months under data retention constraints

### 2. Clustering
Applied three algorithms across all four temporal granularities:
- **HDBSCAN** — density-based, no fixed cluster count required → best performer (silhouette 0.69–0.70)
- **K-Means** — baseline (silhouette 0.24–0.29)
- **GMM** — probabilistic soft assignments
- **Domain-informed clustering** — engineered features using Orange's Black Point / Grey Point operational thresholds

### 3. Forecasting
Benchmarked three model families for 1–7 day ahead prediction:
- **XGBoost** — gradient boosting with lag features and temporal encodings → best performer
- **Prophet** — Facebook's additive model for seasonality decomposition
- **Polynomial Regression** — baseline

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-189ABB?style=flat)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)

**Libraries:** pandas · NumPy · scikit-learn · XGBoost · Prophet · HDBSCAN · UMAP · matplotlib · seaborn

---

## Key Findings

- **HDBSCAN is the right tool for this data** — it surfaces meaningful congestion-risk cohorts without requiring a pre-specified cluster count, and is robust to the noise inherent in live network exports
- **XGBoost decisively outperforms Prophet** on 1–7 day horizons (30–60% lower MAE), making short-term congestion early warning operationally feasible
- **Synthetic data generation works** — the Tweedie XGBoost synthetic BH dataset closely mirrors real distribution statistics, enabling richer model training where retention policies limit historical depth
- A **production architecture** recommendation was delivered to Sofrecom engineering as part of this work

---

## Report & Presentation

- 📄 [Full Thesis Report](report/Habib_Kizamou_Thesis.pdf)
- 📊 [Presentation Slides](presentation/Thesis_Presentation.pptx)

---

## Author

**Habib Kizamou**  
MSc Data Science & AI · University of Middlesex Dubai  
Data Scientist Intern · Sofrecom (Orange Group), Rabat · Jun–Nov 2025

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/habib-kizamou/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/HabibKiz)

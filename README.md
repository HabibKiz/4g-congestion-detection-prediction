# Intelligent Network Monitoring: Clustering-Based Detection and Predictive Modelling of Congestion in 4G Networks

**MSc Thesis Project | Sofrecom (Orange Group) · Rabat, Morocco | 2024–2025**

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat&logo=python)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4-F7931E?style=flat&logo=scikit-learn)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Problem Statement

4G LTE networks generate continuous streams of performance indicator data — PRB (Physical Resource Block) utilisation, downlink/uplink throughput, packet loss rate, handover success rate, and latency — that collectively describe network health in real time. When these indicators degrade simultaneously in a spatially coherent pattern, the network is experiencing or approaching a congestion event: a condition that directly reduces quality of service for users.

Traditional approaches rely on static threshold rules configured manually by engineers. These rules are brittle (they cannot adapt to changing traffic patterns) and reactive (they trigger after congestion has already occurred). This project develops a two-stage ML approach: unsupervised detection of congestion-risk states using clustering, followed by predictive forecasting of future congestion probability using supervised learning on historical KPI sequences.

The project was conducted inside a live operator environment at Sofrecom, Orange Group's telecommunications consulting subsidiary, using infrastructure data from Orange Mali's 4G radio access network. It was submitted as the MSc thesis for the programme in Data Science and Artificial Intelligence.

---

## Dataset and Context

The dataset consists of KPI time series collected from Orange Mali's 4G base stations over a 14-month window, spanning four temporal aggregation levels: weekly (637,000+ records), daily, hourly, and Busy Hour. KPIs include: PRB utilisation (uplink and downlink), cell throughput (Mbps), packet loss rate (%), average user latency (ms), handover success rate (%), and active user count — 11 dimensions in total.

**Confidentiality note:** Due to operator data agreements with Sofrecom, the raw production dataset cannot be published. This repository includes: (a) a synthetic dataset generated to match the statistical properties of the production data (distribution, seasonality, anomaly rate), documented in `data/synthetic_generation.py`; (b) all model training, evaluation, and visualisation code; and (c) the full methodology as described in the thesis. Researchers wishing to apply this methodology to their own operator data can use the synthetic dataset as a structural template.

---

## Methodology

### Stage 1: Congestion State Detection (Unsupervised Clustering)

KPI vectors were constructed for each base station at each time interval by normalising and concatenating the 11 indicator dimensions. Three clustering algorithms were evaluated: HDBSCAN, K-Means, and GMM. Cluster quality was assessed using silhouette score and Davies-Bouldin index. The resulting clusters were interpreted by domain labelling into operational congestion-risk states.

**Key finding:** HDBSCAN achieved silhouette scores of 0.69–0.70 on datasets exceeding one million observations, outperforming K-Means (0.24–0.29) by a factor of approximately 2.4×. HDBSCAN's density-based approach handled the irregular, non-spherical cluster shapes in network KPI space significantly better than centroid-based methods, and its noise-point identification surfaced genuinely anomalous cells that K-Means would have forced into the nearest cluster. The resulting cell-risk groupings were validated with Sofrecom's network operations engineers as operationally interpretable.

### Stage 2: Congestion Prediction (Supervised Time-Series Forecasting)

Using congestion-state indicators derived from Stage 1, supervised forecasting models were trained on sliding windows of KPI history to predict congestion probability at 1–7 day horizons. Models evaluated: XGBoost (gradient boosting), Prophet (additive decomposition), and polynomial regression baseline.

**Key finding:** XGBoost delivered 30–60% lower MAE than Prophet on short-horizon forecasting tasks (1–7 days). Prophet's additive decomposition structure was less suited to the non-stationary, operationally-driven patterns in network KPI data compared to XGBoost's ability to capture non-linear feature interactions. Active Users was identified as the most reliable leading indicator for congestion events — the recommended production architecture uses HDBSCAN segmentation with targeted XGBoost forecasting on Active Users per congestion-risk cell cohort.

**Synthetic dataset extension:** A synthetic Busy Hour dataset was generated using XGBoost Tweedie to extend temporal coverage from 1 to 6 months under Huawei PRS data retention constraints, enabling richer model training while preserving validation integrity across the 14-month operational window.

---

## Results Summary

| Model | Task | Key Metric | Result |
|---|---|---|---|
| HDBSCAN | Cell segmentation | Silhouette score | 0.69–0.70 |
| K-Means | Cell segmentation | Silhouette score | 0.24–0.29 |
| GMM | Cell segmentation | Silhouette score | [your result] |
| XGBoost | 1–7 day forecasting | MAE vs Prophet | 30–60% lower |
| Prophet | 1–7 day forecasting | Baseline | — |

---

## Limitations

This study has three principal limitations. First, the models were trained on data from a single network deployment in one geographic market; generalisation to other operators or countries would require retraining on local data. Second, the supervised stage depends on the quality of the clustering-derived labels; errors in Stage 1 propagate into Stage 2 performance. Third, the synthetic dataset, while statistically representative, cannot fully replicate the spatial correlation structure of real network data (adjacent base stations exhibit correlated KPI behaviour that the synthetic generator approximates but does not fully model).

---

## Next Steps and Extensions

The natural extension is real-time deployment: a streaming pipeline that consumes live KPI data from an operator's network management system, applies the trained models, and generates alerts or automated configuration changes via network API. A secondary extension of direct relevance to Sub-Saharan African deployments is adaptation of the clustering methodology to 4G networks in low-density rural markets, where traffic patterns and congestion drivers differ substantially from the urban deployment studied here.

---

## Repository Structure

```
4g-congestion-detection-prediction/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/                        # Original data — gitignored
│   ├── processed/                  # Cleaned, feature-engineered data
│   └── synthetic_generation.py     # Script to reproduce synthetic dataset
│
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_clustering_experiments.ipynb
│   ├── 03_predictive_model_training.ipynb
│   └── 04_results_visualisation.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_processing.py
│   ├── clustering.py
│   ├── prediction.py
│   └── evaluation.py
│
├── models/trained/
├── reports/figures/
└── tests/
    └── test_data_processing.py
```

---

## Cite This Work

```
@mastersthesis{kizamou2025,
  title={Intelligent Network Monitoring: Clustering-Based Detection and Predictive Modelling of Congestion in 4G Networks},
  author={Kizamou, Habib},
  school={[Your University]},
  year={2025},
  note={Conducted in collaboration with Sofrecom, Orange Group}
}
```

---

## Contact

**Habib Kizamou** | Data Scientist | Niamey, Niger (UTC+1)  
[LinkedIn](https://linkedin.com/in/habibkizamou) · [Hugging Face](https://huggingface.co/habibkizamou) · kizamouhabib@gmail.com

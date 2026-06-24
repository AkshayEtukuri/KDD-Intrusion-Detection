<div align="center">

# 🛡️ KDD Cup 99 — Network Intrusion Detection

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557C?style=for-the-badge)](https://matplotlib.org)

**A machine learning system that classifies network traffic into 20 attack categories with 99.96% accuracy using Random Forest on the KDD Cup 1999 benchmark dataset.**

</div>

<div align="center">

[![Python](https://img.shields.io/badge/Python_3.13-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge)](https://seaborn.pydata.org)
[![Status](https://img.shields.io/badge/Status-Complete-00C853?style=for-the-badge)]()
[![Accuracy](https://img.shields.io/badge/Accuracy-99.96%25-blueviolet?style=for-the-badge)]()

<br/>

> **Classifying network traffic into 20 attack categories using Machine Learning on the KDD Cup 1999 benchmark — one of the most widely used datasets in cybersecurity AI research.**

</div>

---

## ⚡ Results at a Glance

<div align="center">

| Metric | Score |
|:---|:---|
| ✅ Accuracy | **99.96%** |
| 📈 Weighted F1-Score | **1.00** |
| 🧪 Test Samples | **98,805** |
| 🌳 Algorithm | **Random Forest (n=10 trees)** |
| 🔢 Features | **41 network traffic features** |
| 🎯 Classes | **20 (normal + 19 attack types)** |

</div>

---

## 🧠 How It Works

```
Raw Network Traffic (.gz)
         │
         ▼
  ┌─────────────┐
  │  Load CSV   │  ← pandas read_csv with compression
  └──────┬──────┘
         │
         ▼
  ┌─────────────────────┐
  │  Feature Engineering│  ← One-hot encode protocol_type, service, flag
  └──────────┬──────────┘
         │
         ▼
  ┌─────────────────────┐
  │   Train/Test Split  │  ← 80% train / 20% test (random_state=42)
  └──────────┬──────────┘
         │
         ▼
  ┌──────────────────────┐
  │  Random Forest Model │  ← n_estimators=10, n_jobs=-1
  └──────────┬───────────┘
         │
         ▼
  ┌──────────────────────────────┐
  │  Accuracy + Classification   │  ← 99.96% accuracy across 20 classes
  │  Report + Confusion Matrix   │
  └──────────────────────────────┘
```

---

## 🎯 Attack Categories Classified

<div align="center">

| Category | Attack Types |
|:---:|:---|
| 🔴 DoS | `neptune` `smurf` `back` `teardrop` `pod` `land` |
| 🟠 Probe | `ipsweep` `portsweep` `nmap` `satan` |
| 🟡 R2L | `warezclient` `warezmaster` `guess_passwd` `imap` `ftp_write` `multihop` |
| 🔵 U2R | `buffer_overflow` `perl` `loadmodule` |
| 🟢 Normal | `normal` |

</div>

---

## 📊 Visualizations

<table>
  <tr>
    <td align="center">
      <b>🔑 Top 10 Most Important Features</b><br/>
      <img src="feature_importance.png" width="420"/>
    </td>
    <td align="center">
      <b>🔲 Confusion Matrix (20 Classes)</b><br/>
      <img src="confusion_matrix.png" width="420"/>
    </td>
  </tr>
</table>

---

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/AkshayEtukuri/KDD-Intrusion-Detection.git
cd KDD-Intrusion-Detection

# Install
pip install pandas scikit-learn matplotlib seaborn

# Download dataset → place in KDD_Cup_Data/
# http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html
# Required: KDD_Cup_Data/kddcup.data_10_percent.gz

# Run
python project.py
# Saves: feature_importance.png + confusion_matrix.png
```

---

## 🗂️ Project Structure

```
KDD-Intrusion-Detection/
│
├── project.py                  ← Main ML pipeline
├── feature_importance.png      ← Top 10 features chart
├── confusion_matrix.png        ← 20-class confusion matrix
├── .gitignore                  ← Dataset excluded (too large)
└── README.md
```

---

## 🛠️ Tech Stack

<div align="center">

| Library | Version | Use |
|:---:|:---:|:---|
| `pandas` | 2.x | Data loading, preprocessing |
| `scikit-learn` | 1.x | Random Forest, metrics, train/test split |
| `matplotlib` | 3.x | Feature importance visualization |
| `seaborn` | 0.x | Confusion matrix heatmap |
| `Python` | 3.13 | Core language |

</div>

---

<div align="center">

## 👤 Author

**Akshay Etukuri**
B.Tech CSE (Networks specialization)
Malla Reddy Institute of Technology & Science, Hyderabad

[![GitHub](https://img.shields.io/badge/GitHub-AkshayEtukuri-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AkshayEtukuri)


</div>

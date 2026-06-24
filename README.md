<div align="center">

# 🛡️ KDD Cup 99 — Network Intrusion Detection

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557C?style=for-the-badge)](https://matplotlib.org)

**A machine learning system that classifies network traffic into 20 attack categories with 99.96% accuracy using Random Forest on the KDD Cup 1999 benchmark dataset.**

</div>

---

## 📊 Results

<div align="center">

| Metric | Score |
|:---:|:---:|
| ✅ Accuracy | **99.96%** |
| 📈 Weighted F1-Score | **1.00** |
| 🧪 Test Samples | **98,805** |
| 🌳 Algorithm | **Random Forest** |

</div>

---

## 🎯 Attack Types Detected

<div align="center">

`neptune` `smurf` `back` `satan` `ipsweep` `portsweep` `warezclient` `teardrop` `pod` `nmap` `guess_passwd` `buffer_overflow` `warezmaster` `imap` `ftp_write` `multihop` `perl` `land` `normal` + more

</div>

---

## 📈 Visualizations

<table>
  <tr>
    <td align="center"><b>🔑 Top 10 Important Features</b></td>
    <td align="center"><b>🔲 Confusion Matrix</b></td>
  </tr>
  <tr>
    <td><img src="feature_importance.png" width="400"/></td>
    <td><img src="confusion_matrix.png" width="400"/></td>
  </tr>
</table>

---

## 🗂️ Dataset

| Property | Detail |
|---|---|
| Source | [KDD Cup 1999 — UCI ML Repository](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html) |
| Subset Used | 10% training data (~494,000 records) |
| Features | 41 network traffic features |
| Classes | 20 (normal + 19 attack types) |

> ⚠️ Dataset not included due to size. Download from the link above and place in `KDD_Cup_Data/`.

---

## ⚙️ Tech Stack

| Tool | Purpose |
|---|---|
| `scikit-learn` | Random Forest classifier, metrics |
| `pandas` | Data loading & preprocessing |
| `matplotlib` | Feature importance chart |
| `seaborn` | Confusion matrix heatmap |

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/AkshayEtukuri/KDD-Intrusion-Detection.git
cd KDD-Intrusion-Detection

# 2. Install dependencies
pip install pandas scikit-learn matplotlib seaborn

# 3. Download dataset from UCI and place in KDD_Cup_Data/
#    Required file: KDD_Cup_Data/kddcup.data_10_percent.gz

# 4. Run
python project.py
```

Outputs saved: `feature_importance.png` · `confusion_matrix.png`

---

## 👤 Author

<div align="center">

**Akshay Etukuri**
B.Tech CSE (Networks) — Malla Reddy Institute of Technology & Science

[![GitHub](https://img.shields.io/badge/GitHub-AkshayEtukuri-181717?style=for-the-badge&logo=github)](https://github.com/AkshayEtukuri)

</div>

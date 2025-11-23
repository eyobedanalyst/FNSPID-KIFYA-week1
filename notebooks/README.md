
# Stock Analysis Project – Progress Summary (Task 1 & Partial Task 2)

This repository contains the setup, data preparation, and preliminary analysis for a multi-asset stock performance study. The project covers **Task 1 (completed)** and **partial progress on Task 2**, focusing on loading, cleaning, analyzing, and preparing technical indicators for six major technology stocks:

**AAPL, MSFT, META, GOOG, NVDA, AMZN**

---

## 1. Project Overview

The objective of this project is to perform a structured, data-driven analysis of technology sector stocks. The workflow includes:

* Environment setup and version control
* Data loading and preprocessing
* Exploratory Data Analysis (EDA)
* Calculation of financial and technical indicators
* Preparation for comparative performance ranking and deeper analytics

---

## 2. Folder Structure

```
project/
│
├── data/                # Raw CSV files (AAPL, GOOG, META, NVDA, MSFT, AMZN)
├── notebooks/           # Jupyter notebooks for EDA & analytics
├── scripts/             # Python scripts for processing/metrics
├── README.md            # Project documentation
└── venv/                # Python virtual environment
```

---

## 3. Task 1 – Completed

### ✔ 1.1 Environment Setup

A dedicated Python environment was created with the following key packages:

* pandas
* numpy
* matplotlib
* seaborn
* (optional) TA-Lib
* Jupyter Notebook

A virtual environment (`venv/`) was configured for full isolation and reproducibility.

### ✔ 1.2 Git & GitHub Setup

* Git repo initialized locally
* Remote GitHub repository connected
* Branches created for specific tasks (e.g., `setup-task`, `eda-benin`, `eda-tech-stocks`)
* Commit history maintained from initial setup to current development

### ✔ 1.3 Data Loading

CSV files for all six stocks were loaded using:

```
Date, Open, High, Low, Close, Volume
```

Each file was:

* Parsed using pandas
* Date set as index
* Stored individually in a dictionary
* Merged into a combined multi-ticker price DataFrame

---

## 4. Task 2 – Partial Progress Completed

### ✔ 2.1 Data Profiling

Basic data validation and profiling included:

* Checking for missing values
* Confirming index structure
* Validating numerical fields
* Confirming consistent OHLCV schema

No structural issues were found.

### ✔ 2.2 Exploratory Data Analysis (Completed so far)

**a) Price Trend Visualization**
A multi-stock comparison plot was created to show price movement over time.

**b) Daily Returns**
Daily percentage changes were calculated for each asset.

**c) Volatility Calculation**
Standard deviation of returns was computed to estimate stock volatility.

**d) Correlation Analysis**
A returns correlation matrix revealed the relationships between stocks
(e.g., MSFT–AAPL highest correlation).

**e) 20-Day Moving Average**
Rolling SMA was generated for trend detection.

---

## 5. Technical Indicators & Metrics Prepared

Custom implementations were added for:

* **Daily Returns**
* **Log Returns**
* **CAGR (Compound Annual Growth Rate)**
* **Sharpe Ratio**
* **Volatility**
* **Cumulative Returns**
* **SMA / EMA**
* **Correlation Structure**

PyNance was tested but found inconsistent across environments, so metrics were implemented using pandas/numpy for reliability.

---

## 6. Challenges Encountered

* PyNance package compatibility issues
* Missing `pn.finance` functions → replaced with custom metrics
* File naming inconsistencies (e.g., APPL vs AAPL)
* TA-Lib installation issues depending on environment
* Date alignment differences across tickers

All issues were resolved with appropriate fallback solutions.

---

## 7. Current Status (As of Now)

**Completed:**

* Environment + Git setup
* Data loading + cleaning
* Combined dataset for the six stocks
* Basic EDA (returns, volatility, SMA20, correlations)
* Custom financial indicator functions

**In Progress (Task 2):**

* Deep-dive EDA
* Outlier analysis
* Boxplots and distribution analysis
* Enhanced technical indicators (RSI, MACD, Bollinger Bands)

**Upcoming (Next Tasks):**

* Ranking stocks by risk-adjusted performance
* Multi-metric comparison dashboard
* Building trading signals
* Streamlit dashboard (optional)

---

## 8. How to Run the Project

### Step 1: Activate the virtual environment

```
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

### Step 3: Run the notebook

```
jupyter notebook
```

### Step 4: Execute EDA and analysis scripts

Use notebooks under `notebooks/` for step-by-step exploration.

---

## 9. Contact / Contributions

For questions, suggestions, or contributions, please open an issue or create a pull request on GitHub.

---



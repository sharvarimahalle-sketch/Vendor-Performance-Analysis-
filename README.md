# Vendor Performance & Profitability Analysis

> **End-to-end data analytics project** covering SQL-based data ingestion, exploratory data analysis (EDA), statistical testing, and an interactive Power BI dashboard — applied to a real-world retail beverage distribution dataset.

---

## Overview

This project analyses vendor performance, inventory turnover, sales trends, and profitability for a retail and wholesale beverage distribution company. Working with **~15.6 million raw records** across 6 source tables ingested into SQLite, the data was cleaned and aggregated into a 10,692-record analytical dataset. The analysis identifies underperforming brands, evaluates vendor concentration risk, quantifies the impact of bulk purchasing on unit costs, and surfaces $2.71M in locked unsold inventory capital.

**Key outcomes:**
- Identified **198 high-margin brands** with low sales volume , ready for targeted promotion
- Confirmed a **72% unit cost reduction** achievable through bulk purchasing
- Flagged **vendor concentration risk**: top 10 vendors control 65.7% of purchase spend
- Statistically validated a **10.4 percentage point margin gap** between vendor performance tiers

---

## Repository Structure

```
Vendor-Performance-Analysis/
│
├── data/
│   ├── begin_inventory.csv        # Opening stock levels
│   ├── end_inventory.csv          # Closing stock levels
│   ├── purchase_prices.csv        # Unit purchase price per SKU
│   ├── purchases.csv              # All purchase transactions
│   ├── sales.csv                  # All sales transactions
│   └── vendor_invoice.csv         # Vendor invoice records
│
├── Exploratory Data Analysis.ipynb    # EDA with Python (Pandas, Matplotlib, Seaborn)
├── Vendor Performance Analysis.ipynb  # SQL ingestion + business queries (SQLite)
├── ingestion_db.py                    # Script to load CSVs into SQLite database
├── vendor_sales_summary.csv           # Aggregated output used for Power BI
├── Vendor Performance dashboard.png   # Dashboard screenshot
├── vendor_performance.pbix            # Power BI dashboard file
├── Vendor Performance EDA Report.pdf  # Full EDA report (PDF)
└── README.md
```
---

## Dataset

6 raw source files ingested into SQLite, producing ~15.6 million records across all tables.

| Table | Description | Records | Size |
|---|---|---|---|
| `sales` | Sales transactions by vendor, brand, and date | 12,825,363 | ~1.56 GB |
| `purchases` | Purchase orders with quantities and costs | 2,372,474 | ~353 MB |
| `begin_inventory` | Opening stock levels per SKU | 206,529 | ~17 MB |
| `end_inventory` | Closing stock levels per SKU | 224,489 | ~18.5 MB |
| `purchase_prices` | Unit cost by vendor and brand | 12,261 | ~1 MB |
| `vendor_invoice` | Invoice-level vendor records | 5,543 | ~498 KB |
| `vendor_sales_summary` | Aggregated output used for EDA & Power BI | **10,692** | — |

> `begin_inventory` and `end_inventory` were excluded from vendor analysis as they reflect yearly stock snapshots rather than transactional vendor behaviour.

**Records used for analysis:** 10,692 (aggregated) | **Features:** 19 | **Domain:** Retail Beverage Distribution
---

## Tools & Technologies

| Tool | Purpose |
|---|---|
| **Python** (Pandas, NumPy) | Data cleaning, transformation, feature engineering |
| **Python** (Matplotlib, Seaborn) | EDA visualisations — distributions, heatmaps, scatter plots |
| **Python** (SciPy) | Hypothesis testing for vendor margin comparison |
| **SQLite** | Database ingestion and business-level SQL queries |
| **Jupyter Notebook** | Reproducible analysis workflow |
| **Power BI** | Interactive dashboard development |

---

## Project Steps

### 1. Data Ingestion — SQLite
- Raw CSVs loaded into a local SQLite database using `ingestion_db.py`
- Tables created for `sales`, `purchases`, `inventory`, `purchase_prices`, and `vendor_invoice`

### 2. SQL EDA & Business Queries
- Aggregated total sales, gross profit, and purchase spend by vendor and brand
- Identified top 10 vendors by purchase contribution
- Flagged zero-sales SKUs and low inventory turnover products
- Computed `StockTurnover`, `ProfitMargin`, and `SalesToPurchaseRatio` per vendor

### 3. Python EDA
- Distribution analysis across all 18 features
- Correlation heatmap to identify relationships between pricing, volume, and profitability
- Scatter analysis to surface 198 high-margin, low-sales brands
- Bulk purchasing segmentation (Small / Medium / Large order tiers)
- Statistical hypothesis testing (two-sample t-test) on vendor profit margins

### 4. Power BI Dashboard
- Built on the `vendor_sales_summary.csv` output from SQL/Python pipeline
- 6 interactive visuals covering KPIs, vendor rankings, brand performance, and inventory health

---

## Dashboard

![Vendor Performance Dashboard](Vendor%20Performance%20dashboard.png)

| Visual | Insight |
|---|---|
| **KPI Banner** | $441.41M sales · $134.07M gross profit · 38.7% margin · $2.71M unsold capital |
| **Purchase Contribution Donut** | Top 10 vendors = 65.7% of spend; Diageo leads at 16.3% |
| **Top Vendors by Sales** | Diageo ($68M) · Martignetti ($39M) · Pernod Ricard ($32M) |
| **Top Brands by Sales** | Jack Daniels No.7 ($8M) · Tito's Vodka ($7.4M) · Grey Goose ($7.2M) |
| **Low-Performing Vendors** | Alisa Carr Beverages lowest at 0.615 stock turnover ratio |
| **Low-Performing Brands Scatter** | 198 brands with high margins but low sales — promotion candidates |

---

## Key Results

| Finding | Detail |
|---|---|
| Total Sales Revenue | $441.41M |
| Gross Profit | $134.07M (38.7% margin) |
| Unsold Inventory Capital | $2.71M tied up in slow-moving stock |
| Vendor Concentration | Top 10 vendors = 65.7% of total purchases |
| Bulk Purchasing Savings | 72% lower unit cost ($10.78 vs $39.06 for small orders) |
| High-Margin Opportunity Brands | 198 brands with margins >65% but sales below median |
| Margin Gap (Top vs Low Vendors) | 31.17% (top) vs 41.55% (low) — statistically significant |

---

## How to Run

### Prerequisites
```
pip install pandas numpy matplotlib seaborn scipy sqlite3 jupyter
```

### Step 1 — Ingest data into SQLite
```bash
python ingestion_db.py
```

### Step 2 — Run SQL analysis notebook
```bash
jupyter notebook "Vendor Performance Analysis.ipynb"
```

### Step 3 — Run Python EDA notebook
```bash
jupyter notebook "Exploratory Data Analysis.ipynb"
```

### Step 4 — Open Power BI Dashboard
Open `vendor_performance.pbix` in **Power BI Desktop**.
The dashboard connects to `vendor_sales_summary.csv` — ensure both files are in the same directory.

---

## Business Recommendations

- **Diversify vendors** — reduce dependency on top 10 suppliers to mitigate supply chain risk
- **Promote 198 high-margin brands** — targeted campaigns can unlock revenue without margin sacrifice
- **Leverage bulk purchasing** — consolidate orders for top SKUs to access the 72% unit cost reduction
- **Liquidate slow-moving stock** — recover $2.71M in capital tied in unsold inventory
- **Standardise freight terms** — freight costs range from $0.09 to $257K; consolidation can reduce this significantly

---

## Author

**Sharvari Mahalle**
[GitHub](https://github.com/sharvarimahalle-sketch) · [LinkedIn](www.linkedin.com/in/sharvarimahalle)

---

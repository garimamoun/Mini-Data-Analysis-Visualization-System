# 🧾 Mini Data Analysis & Visualization System

A tiny, friendly Python project that loads sales data, does simple cleaning, prints a summary, and creates basic visualizations. If a `sales_data.csv` file is not found, the program automatically creates a sample dataset so you can run it immediately. Perfect for learning, demos, or quick analysis experiments. 🚀

---

## ✨ Features

* Auto-creates a sample `sales_data.csv` if none exists .
* Cleans data (removes duplicates, fills missing numeric values with mean).
* Prints a quick statistical summary (describe) 
* Generates two simple plots: **Sales by Category** and **Profit Distribution**
* Saves plots (optional) and can export cleaned data / summary reports (in advanced version).

---

## 🛠 Prerequisites

* Python 3.8 or higher
* Recommended packages (install with pip):

```bash
pip install pandas matplotlib seaborn
```

> If you prefer a `requirements.txt`, create one with:
>
> ```text
> pandas
> matplotlib
> seaborn
> ```

---

## 📂 Project Structure (suggested)

```
mini-data-analysis/
├─ main.py                    # The simple script to run (auto-creates sample CSV)
├─ sales_data.csv             # (optional) your real data file
├─ plots/                     # created by the script (if saving plots)
│  ├─ sales_by_category.png
│  └─ profit_distribution.png
└─ README.md                  # This file
```

---

## 🧩 `main.py` (behavior summary)

* Loads `sales_data.csv` (or creates a sample if missing).
* Drops duplicate rows.
* Fills missing numeric values using column means.
* Prints `df.describe()` summary.
* Draws:

  * Bar plot: total sales grouped by `Category`.
  * Histogram: `Profit` distribution.

---

## ✍️ Sample `sales_data.csv` format

Minimum columns used by the script:

* `Category` (string) — e.g. `Electronics`, `Clothing`
* `Sales` (numeric) — sales amount
* `Profit` (numeric) — profit amount

Example CSV rows:

```
Category,Sales,Profit
Electronics,50000,5000
Clothing,20000,2000
Furniture,30000,3000
```

---

## 🐞 Troubleshooting

* **`ModuleNotFoundError`**: install missing packages with `pip install package_name`.
* **Plots not appearing**: if running in a non-GUI environment (e.g., remote server), use `plt.savefig(...)` instead of `plt.show()` to save images to `plots/` and then download them.
* **CSV file looks empty or wrong**: open `sales_data.csv` in a text editor or Excel to inspect; ensure headers match (`Category,Sales,Profit`).

---

## 🔧 Customization Tips

* Want more columns? Add them to `sales_data.csv` and update the script to use them.
* To save all visualizations automatically, add `plt.savefig("plots/your_plot.png")` before `plt.close()`.
* For richer visuals, switch to seaborn plotting functions and customize aesthetics.

---

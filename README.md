# Automated Email & Reporting System 📊📧

An end-to-end data pipeline automation system built in Python designed to eliminate repetitive administrative workflows. The script operates entirely without manual intervention, handling data ingestion, analytical reporting, and secure electronic distribution on a daily schedule.

## 🚀 Key Features
* **Data Aggregation:** Uses `Pandas` to ingest raw records (`data.csv`) and compute categorical performance summaries.
* **Dual-Format Outputs:** Automatically generates a styled bar chart (`.png`) using `Matplotlib` and a structured summary workbook (`.xlsx`) via `openpyxl`.
* **Secure SMTP Transport:** Configures an encrypted connection over SSL Port 465 using `smtplib` to authenticate with mail servers and safely deliver multi-format attachments.
* **Automated Scheduling:** Runs on a continuous, low-overhead background timing loop using the `time` library, monitoring the system clock to trigger data processing at a designated time each day.
* **Uptime Logging:** Utilizes a `try-except` block to capture errors, writing timestamped success notifications or failure details to an external ledger (`automation_log.txt`) for easy system monitoring.

---

## 🛠️ Tech Stack & Libraries
* **Language:** Python 3.10+
* **Data Manipulation:** Pandas
* **Data Visualization:** Matplotlib
* **Workbook Formatting:** Openpyxl
* **Protocols & Monitoring:** SMTPLIB, EmailMessage, Datetime, Time

---

## 📂 Repository Structure
```text
├── data.csv                  # Input raw transaction data
├── automation.py             # Core automation and scheduling engine
├── report_chart.png          # Generated visual report
├── Sales_Summary_Report.xlsx # Generated Excel spreadsheet summary
└── automation_log.txt        # System execution log ledger

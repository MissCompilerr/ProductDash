# 🛒 ProductIQ eCommerce Analytics

An end-to-end e-commerce analytics project analyzing 150,000+ interactions. Features exploratory data analysis and cleaning in Python via Google Colab, custom DAX metrics in Power BI, and interactive deployment via Streamlit.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1meXFeyL_r7pmxFHd4Y3_1i8JldvvCiyL)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Power BI](https://img.shields.io/badge/Power_BI-F2C811?logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)

---

## 🔗 Quick Links
- 📓 **Google Colab Notebook:** [Open in Google Colab](https://colab.research.google.com/drive/1meXFeyL_r7pmxFHd4Y3_1i8JldvvCiyL)
- 🚀 **Interactive Streamlit Web App:** [Live Demo](https://share.streamlit.io) *(Replace with your deployed URL)*

---

## 📌 Features
- **Data Pipeline & EDA (Google Colab):** Exploratory data analysis, handling missing values, deduplication, and feature engineering across 150,000+ customer interaction records using Python (Pandas, NumPy, Seaborn, Matplotlib).
- **Power BI Dashboard:** Includes custom DAX metrics, revenue heatmaps, customer purchase funnels, and interactive slicers (`ProductIQ Dashboard.pbix` included).
- **Interactive Streamlit App:** Deployed web interface allowing public access and interactive scenario exploration without software dependencies.

---

## 📁 Repository Structure
- `ProductIQ_eCommerce_Analytics.ipynb`: Complete Jupyter / Google Colab notebook with end-to-end EDA and data cleaning pipeline.
- `Data/`: Contains raw (`events.csv`) and cleaned (`productiq_clean.csv`) datasets.
- `ProductIQ Dashboard.pbix`: Native Power BI Desktop report with interactive dashboards and DAX measures.
- `app.py`: Streamlit application source script for web-based analytics visualization.
- `requirements.txt`: Python package dependencies.

---

## 🚀 Getting Started

### 1. Run in Google Colab
You can run and explore the data pipeline directly in your browser:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1meXFeyL_r7pmxFHd4Y3_1i8JldvvCiyL)

### 2. Run the Streamlit Dashboard Locally
```bash
# Clone the repository
git clone https://github.com/MissCompilerr/Product-IQ.git
cd Product-IQ

# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py
```

### 3. Open Power BI Dashboard
Open `ProductIQ Dashboard.pbix` using **Power BI Desktop** to explore the interactive visual reports and DAX metrics.

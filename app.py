import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ----------------------------------------------------
# 1. Page Configuration & Custom CSS
# ----------------------------------------------------
st.set_page_config(page_title="ProductIQ Dashboard", layout="wide")

st.markdown("""
    <style>
    /* Clean Off-White Global Background */
    .stApp {
        background-color: #F8F9FA;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Executive Metric Card Styling */
    .kpi-card {
        background-color: #FFFFFF;
        border: 1px solid #E9ECEF;
        border-radius: 12px;
        padding: 24px 16px;
        text-align: center;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.03);
    }
    .kpi-title {
        color: #6C757D;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 8px;
        letter-spacing: 0.3px;
    }
    .kpi-value {
        color: #111827;
        font-size: 34px;
        font-weight: 800;
        margin: 0;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 2. Header Section
# ----------------------------------------------------
st.title("ProductIQ Dashboard")
st.caption("Data updated: 30/09/2026")
st.divider()

# ----------------------------------------------------
# 3. KPI Cards Row (3 Columns)
# ----------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Total Revenue</div>
            <div class="kpi-value">$518.87K</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Unique Users</div>
            <div class="kpi-value">79K</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Total Purchases</div>
            <div class="kpi-value">6K</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ----------------------------------------------------
# Mock Data Generation
# ----------------------------------------------------
np.random.seed(42)

# Time Series Data (Sept 27 - Oct 25)
dates = pd.date_range(start="2026-09-27", end="2026-10-25", freq="D")
daily_revenue = np.random.randint(12000, 24000, size=len(dates))
df_time = pd.DataFrame({"date": dates, "revenue": daily_revenue})

# Product Revenue Data (Sorted Ascending for Top-to-Bottom Bar Display)
product_ids = [
    "$37,91,351", "$40,27,952", "$40,99,645", "$38,12,001",
    "$41,00,892", "$39,50,111", "$42,10,500", "$43,11,204"
]
prod_revenue = np.sort(np.random.randint(18000, 62000, size=len(product_ids)))
df_products = pd.DataFrame({"product_id": product_ids, "revenue": prod_revenue})

# Category Revenue Data (Sorted Ascending for Top-to-Bottom Bar Display)
categories = [
    "computers.peripherals.printer", "computers.components.cpu",
    "electronics.telephone", "appliances.environment.air_conditioner",
    "audio.headphone", "computers.notebook", "electronics.clocks"
]
cat_revenue = np.sort(np.random.randint(22000, 88000, size=len(categories)))
df_categories = pd.DataFrame({"category_code": categories, "revenue": cat_revenue})

# ----------------------------------------------------
# 4. Section 1: Full-Width Time-Series Line Chart
# ----------------------------------------------------
fig_line = px.line(
    df_time,
    x="date",
    y="revenue",
    title="Total Revenue by date",
    template="plotly_white"
)

fig_line.update_traces(
    line_color="#118DFF",
    line_width=2.5,
    line_shape="spline"
)

fig_line.update_layout(
    margin=dict(l=0, r=0, t=40, b=0),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis_title=None,
    yaxis_title=None,
    title_font=dict(size=16, color="#111827", family="sans-serif"),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor="#E9ECEF")
)

st.plotly_chart(fig_line, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ----------------------------------------------------
# 5. Section 2: Horizontal Bar Charts (2 Columns)
# ----------------------------------------------------
c1, c2 = st.columns(2)

with c1:
    fig_prod = px.bar(
        df_products,
        x="revenue",
        y="product_id",
        orientation="h",
        title="Total Revenue by product_id",
        template="plotly_white"
    )
    fig_prod.update_traces(marker_color="#118DFF")
    fig_prod.update_layout(
        margin=dict(l=0, r=0, t=40, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title=None,
        yaxis_title=None,
        title_font=dict(size=16, color="#111827", family="sans-serif"),
        xaxis=dict(showgrid=True, gridcolor="#E9ECEF"),
        yaxis=dict(showgrid=False)
    )
    st.plotly_chart(fig_prod, use_container_width=True)

with c2:
    fig_cat = px.bar(
        df_categories,
        x="revenue",
        y="category_code",
        orientation="h",
        title="Total Revenue by category_code",
        template="plotly_white"
    )
    fig_cat.update_traces(marker_color="#118DFF")
    fig_cat.update_layout(
        margin=dict(l=0, r=0, t=40, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title=None,
        yaxis_title=None,
        title_font=dict(size=16, color="#111827", family="sans-serif"),
        xaxis=dict(showgrid=True, gridcolor="#E9ECEF"),
        yaxis=dict(showgrid=False)
    )
    st.plotly_chart(fig_cat, use_container_width=True)
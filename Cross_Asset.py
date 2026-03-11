import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

tickers = ["ES=F", "ZN=F", "GC=F", "CL=F", "DX=F", "ZW=F"]

def download_data(tickers, start_date=None, end_date=None):
    data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False
    )["Close"]
    return data

def normalize_pct(prices):
    return (prices / prices.iloc[0] - 1) * 100  # en %

def plot(data, title):
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.plot(data)
    plt.title(title)
    plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)
    plt.ylabel("Performance (%)")
    plt.xticks(rotation=45)
    plt.legend(data.columns, loc="upper left")
    return fig

def create_dashboard(title, fig):
    st.title(title)
    st.pyplot(fig)

# Pipeline
prices = download_data(tickers, start_date="2026-01-01", end_date="2026-03-10")
pct_returns = normalize_pct(prices)
title = "Cross-Asset Market Monitor — Performance (%)"
fig = plot(pct_returns, title)
create_dashboard(title, fig)
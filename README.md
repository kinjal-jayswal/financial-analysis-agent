# 💹 Financial Analysis Agent — JK Data Lab

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-5.22+-3D4DB7?style=flat&logo=plotly&logoColor=white)](https://plotly.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![Author](https://img.shields.io/badge/Author-JK%20Data%20Lab-00FFD4?style=flat)](https://www.jkdatalab.com)

> Autonomous agent for financial data analysis, technical indicators, forecasting, and investment insights.

---

## What It Does

- Simulates realistic OHLCV price data for major tech stocks (AAPL, GOOGL, MSFT, AMZN, NVDA, TSLA) using geometric Brownian motion
- Computes key risk/return metrics: Volatility, Sharpe Ratio, Maximum Drawdown, and Period Return
- Renders interactive candlestick charts with MA20 and MA50 moving average overlays
- Generates autonomous agent insights on trend signals, risk profile, and risk-adjusted performance
- Supports configurable analysis periods: 1 Year, 2 Years, and 5 Years

---

## Architecture

```
app.py
├── generate_financial_data(company, period)   # GBM price simulation + technical indicators
├── Sidebar controls                           # Company, period, analysis type selection
├── Metric cards                               # Price, volatility, Sharpe, drawdown, high
├── Candlestick chart (Plotly)                 # 60-day OHLC + MA20 + MA50
└── Agent Insights                             # Automated narrative from computed metrics
```

---

## Quick Start

### 1. Clone & install

```bash
# Windows (PowerShell)
git clone <repo-url>
cd 07_financial_analysis_agent
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# macOS / Linux
git clone <repo-url>
cd 07_financial_analysis_agent
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## Configuration

No `.env` file required. All settings are available in the Streamlit sidebar:

| Setting | Options | Default |
|---------|---------|---------|
| Company | AAPL, GOOGL, MSFT, AMZN, NVDA, TSLA | AAPL |
| Period | 1 Year, 2 Years, 5 Years | 1 Year |
| Analysis | Technical, Fundamental, Risk, Forecast | Technical, Risk, Forecast |

---

## Project Structure

```
07_financial_analysis_agent/
├── app.py            # Main Streamlit application
├── requirements.txt  # Python dependencies
├── README.md         # This file
└── venv/             # Virtual environment (not committed)
```

---

## Requirements

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | >=1.35.0 | Web UI framework |
| pandas | >=2.2.0 | DataFrame operations and time series |
| numpy | >=1.26.0 | Numerical computation and GBM simulation |
| plotly | >=5.22.0 | Interactive candlestick and line charts |

---

## License

MIT © [Kinjal Jayswal — JK Data Lab](https://www.jkdatalab.com)

---

<div align="center">
Built with ❤️ by <strong><a href="https://www.jkdatalab.com">JK Data Lab</a></strong><br>
📧 kinjal@jkdatalab.com &nbsp;|&nbsp; 🌐 www.jkdatalab.com
</div>

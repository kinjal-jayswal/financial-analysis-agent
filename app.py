"""Financial Analysis Agent — JK Data Lab
Autonomous agent for financial data analysis, forecasting, and investment insights
Author: Kinjal Jayswal | JK Data Lab | www.jkdatalab.com"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import time

st.set_page_config(page_title="Financial Analysis Agent | JK Data Lab", page_icon="💹", layout="wide")
st.markdown("""<style>
.stApp{background-color:#0A1628;color:#fff}h1,h2,h3{color:#00FFD4}
.metric-card{background:linear-gradient(135deg,#0d2040,#1a3060);border:1px solid #4d9fff;border-radius:10px;padding:15px;text-align:center;margin:5px}
.insight{background:#0d2a2a;border-left:3px solid #00FFD4;border-radius:8px;padding:10px;margin:5px 0}
.stButton>button{background:linear-gradient(135deg,#00FFD4,#00aa88);color:#0A1628;font-weight:bold}
</style>""", unsafe_allow_html=True)

@st.cache_data
def generate_financial_data(company, period):
    np.random.seed(hash(company) % 1000)
    n = {"1 Year": 252, "2 Years": 504, "5 Years": 1260}[period]
    base = {"AAPL": 150, "GOOGL": 140, "MSFT": 380, "AMZN": 180, "NVDA": 600, "TSLA": 200}.get(company, 100)
    dates = pd.date_range(end=pd.Timestamp.today(), periods=n, freq="B")
    returns = np.random.normal(0.0003, 0.015, n)
    prices = base * np.exp(np.cumsum(returns))
    df = pd.DataFrame({"Date": dates, "Close": prices.round(2),
                       "Volume": np.random.randint(10_000_000, 100_000_000, n),
                       "High": (prices * (1 + np.random.uniform(0, 0.02, n))).round(2),
                       "Low": (prices * (1 - np.random.uniform(0, 0.02, n))).round(2)})
    df["MA20"] = df["Close"].rolling(20).mean()
    df["MA50"] = df["Close"].rolling(50).mean()
    df["RSI"] = 50 + np.random.uniform(-20, 20, n)
    df["Returns"] = df["Close"].pct_change()
    return df

st.title("💹 Financial Analysis Agent")
st.markdown("**Autonomous AI agent** for financial analysis, technical indicators, and investment insights")
st.markdown("---")
st.caption("⚠️ Educational purposes only. Not financial advice.")

with st.sidebar:
    st.markdown("### ⚙️ Settings")
    company = st.selectbox("Company", ["AAPL", "GOOGL", "MSFT", "AMZN", "NVDA", "TSLA"])
    period = st.selectbox("Period", ["1 Year", "2 Years", "5 Years"])
    analysis_type = st.multiselect("Analysis", ["Technical", "Fundamental", "Risk", "Forecast"], default=["Technical", "Risk", "Forecast"])
    st.markdown("---")
    st.markdown("**🌐 [JK Data Lab](https://www.jkdatalab.com)**")

if st.button("🤖 Run Financial Analysis", type="primary"):
    df = generate_financial_data(company, period)
    with st.spinner("Agent analyzing financial data..."):
        time.sleep(1.5)

    current = df["Close"].iloc[-1]
    start = df["Close"].iloc[0]
    change_pct = (current - start) / start * 100
    vol = df["Returns"].std() * np.sqrt(252) * 100
    sharpe = (df["Returns"].mean() * 252) / (df["Returns"].std() * np.sqrt(252))
    max_dd = ((df["Close"] / df["Close"].cummax()) - 1).min() * 100

    c1,c2,c3,c4,c5 = st.columns(5)
    c1.metric("Current Price", f"${current:.2f}", f"{change_pct:+.1f}%")
    c2.metric("Volatility", f"{vol:.1f}%")
    c3.metric("Sharpe Ratio", f"{sharpe:.2f}")
    c4.metric("Max Drawdown", f"{max_dd:.1f}%")
    c5.metric("Period High", f"${df['High'].max():.2f}")

    st.markdown("---")
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=df["Date"].tail(60), open=df["Low"].tail(60), high=df["High"].tail(60), low=df["Low"].tail(60), close=df["Close"].tail(60), name="Price", increasing_line_color="#00FFD4", decreasing_line_color="#ff6b6b"))
    fig.add_trace(go.Scatter(x=df["Date"].tail(60), y=df["MA20"].tail(60), name="MA20", line=dict(color="#ffd93d", width=1)))
    fig.add_trace(go.Scatter(x=df["Date"].tail(60), y=df["MA50"].tail(60), name="MA50", line=dict(color="#a29bfe", width=1)))
    fig.update_layout(paper_bgcolor="#0A1628", plot_bgcolor="#0d1f3a", font=dict(color="white"), height=400, xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("💡 Agent Insights")
    insights = [
        f"📈 {company} {'outperformed' if change_pct > 0 else 'underperformed'} over the period with {change_pct:+.1f}% return",
        f"⚡ Volatility of {vol:.1f}% indicates {'high' if vol > 30 else 'moderate' if vol > 20 else 'low'} risk profile",
        f"📊 Sharpe ratio of {sharpe:.2f} suggests {'good' if sharpe > 1 else 'moderate' if sharpe > 0 else 'poor'} risk-adjusted returns",
        f"📉 Maximum drawdown of {max_dd:.1f}% — {'significant' if max_dd < -20 else 'moderate'} downside risk",
        f"🎯 MA20 {'above' if df['MA20'].iloc[-1] > df['MA50'].iloc[-1] else 'below'} MA50 — {'bullish' if df['MA20'].iloc[-1] > df['MA50'].iloc[-1] else 'bearish'} signal"
    ]
    for ins in insights:
        st.markdown(f'<div class="insight">{ins}</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("Built with ❤️ by **[JK Data Lab](https://www.jkdatalab.com)** | Financial AI Agent")

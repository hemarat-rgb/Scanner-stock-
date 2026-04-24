import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📊 US Stock Scanner (Top หุ้นน่าสนใจ)")

stocks = ["AAPL","MSFT","NVDA","AMZN","GOOGL","META","TSLA","AMD","NFLX"]

results = []

for s in stocks:
    df = yf.download(s, period="6mo")
    last = df.iloc[-1]

    score = 0
    
    if last["Close"] > df["Close"].rolling(200).mean().iloc[-1]:
        score += 2
        
    if last["Close"] > df["Close"].rolling(50).mean().iloc[-1]:
        score += 1

    results.append([s, last["Close"], score])

df = pd.DataFrame(results, columns=["Stock","Price","Score"])
df = df.sort_values(by="Score", ascending=False)

st.dataframe(df)
score = 0

ema200 = df["Close"].rolling(200).mean()
ema50 = df["Close"].rolling(50).mean()

# EMA200
if len(df) >= 200 and not pd.isna(ema200.iloc[-1]):
    if last["Close"] > ema200.iloc[-1]:
        score += 2

# EMA50
if len(df) >= 50 and not pd.isna(ema50.iloc[-1]):
    if last["Close"] > ema50.iloc[-1]:
        score += 1

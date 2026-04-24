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

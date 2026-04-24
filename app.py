score = 0

ema50 = df["Close"].rolling(50).mean()

# EMA50
if len(df) >= 50 and not pd.isna(ema50.iloc[-1]):
    if last["Close"] > ema50.iloc[-1]:
        score += 1

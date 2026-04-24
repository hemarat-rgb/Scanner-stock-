score = 0

ema100 = df["Close"].rolling(100).mean()
ema50 = df["Close"].rolling(50).mean()

# EMA200
if len(df) >= 100 and not pd.isna(ema100.iloc[-1]):
    if last["Close"] > ema100.iloc[-1]:
        score += 2

# EMA50
if len(df) >= 50 and not pd.isna(ema50.iloc[-1]):
    if last["Close"] > ema50.iloc[-1]:
        score += 1

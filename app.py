score = 0

ema100 = df["Close"].rolling(200).mean()
ema50 = df["Close"].rolling(50).mean()

# EMA200
if len(df) >= 200 and not pd.isna(ema200.iloc[-1]):
    if last["Close"] > ema200.iloc[-1]:
        score += 2

# EMA50
if len(df) >= 50 and not pd.isna(ema50.iloc[-1]):
    if last["Close"] > ema50.iloc[-1]:
        score += 1

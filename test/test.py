def backtest (strategy, data):
  balance = 1000
  position = 0
  for i in range(len(data)) :
    signal = strategy.generate_signal(data.il‹
    if signal == "BUY" and position == 0:
      position = balance / datal 'close'].il
      balance = 0
    elif signal == "SELL" and position > 0:
      balance = position * datal 'close'l.il
      position = e
  return balance

#!/usr/bin/env python3
"""
סוכן מחקר אוטונומי למניות - Autonomous Stock Research Agent
... (הקוד המלא מההודעה הקודמת שלי - אני לא יכול להעתיק את כל 400 שורות כאן, אבל תגיד לי אם צריך לשלוח חלקים)
"""

# (הקוד הארוך מההודעות הקודמות שלי עם כל הפונקציות, LangGraph, Scheduler וכו')
def check_ma_breakout(ticker: str) -> Dict[str, Any]:
    """בודק פריצה קרובה של ממוצע נע 150 יום"""
    try:
        data = yf.download(ticker, period="1y", progress=False)
        if len(data) < 150:
            return {"ticker": ticker, "status": "לא מספיק נתונים"}
        
        ma150 = data['Close'].rolling(150).mean().iloc[-1]
        current_price = data['Close'].iloc[-1]
        percent_to_ma = (current_price / ma150) * 100
        
        return {
            "ticker": ticker,
            "current_price": round(current_price, 2),
            "ma150": round(ma150, 2),
            "percent_to_ma": round(percent_to_ma, 1),
            "near_breakout": percent_to_ma > 95
        }
    except:
        return {"ticker": ticker, "status": "שגיאה"}

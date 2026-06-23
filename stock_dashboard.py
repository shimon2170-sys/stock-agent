import streamlit as st
import os
from datetime import datetime

st.set_page_config(page_title="סוכן מניות - דשבורד", layout="wide")
st.title("📈 דשבורד סוכן מחקר אוטונומי למניות")

st.markdown("### דוחות אחרונים")

reports = [f for f in os.listdir(".") if f.startswith("stock_research_report_") and f.endswith(".md")]

if reports:
    selected = st.selectbox("בחר דוח", sorted(reports, reverse=True))
    with open(selected, "r", encoding="utf-8") as f:
        content = f.read()
    st.markdown(content)
else:
    st.info("עדיין אין דוחות. הרץ את הסוכן הראשי.")

st.sidebar.info("הסוכן רץ אוטומטית ב-16:00 כל יום")
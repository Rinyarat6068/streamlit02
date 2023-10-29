import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from st_pages import Page, show_pages

st.set_page_config(layout='wide')

show_pages(
    [
        Page("newapp.py","Home","🏠"),
        Page("tabs.py","Tab Layout","📊"),
        Page("mains.py","Map Layour","🗺️")
    ]
)

st.markdown('สวัสดี! *streamlit*')
st.title('Layout and Decoration')
st.write('''
เราจะลองทำ San Francisco Dataset กันดู
''')

trees_df = pd.read_csv('trees.csv')
df_dbh_grouped = pd.DataFrame(
    trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

owners = st.sidebar.multiselect(
    "Tree Owner Filter",
    trees_df['caretaker'].unique()
)

if owners:
    trees_df = trees_df[ trees_df['caretaker'].isin(owners) ]

tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Area Chart"])
with tab1:
    st.line_chart(df_dbh_grouped)
with tab2:
    st.bar_chart(df_dbh_grouped)
with tab3:
    st.area_chart(df_dbh_grouped)

st.caption('กราฟ แสดงจำนวนต้นไม้ จัดกลุ่มตามเส้นผ่าศุนย์กลาง')
st.title('แปลผล')
st.write("""
ส่วนใหญ่ของต้นไม้ใน SF มีเส้นผ่าศุนย์กลาง 3' (2,721 ต้น)
""")

trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n=1000, replace= True)
st.map(trees_df)
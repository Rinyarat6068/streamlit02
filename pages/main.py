import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

st.markdown('สวัสดี! *streamlit*')
st.title('Layout and Decoration')
st.write('''
เราจะลองทำ San Francisco Dataset กันดู
''')

trees_df = pd.read_csv('trees.csv')
df_dbh_grouped = pd.DataFrame(
    trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n=1000, replace= True)
st.map(trees_df)
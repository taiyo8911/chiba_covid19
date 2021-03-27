import streamlit as st
import pandas as pd

st.title('コロナウイルス千葉県居住地別感染者数')
st.subheader('令和3年2月15日現在')
df = pd.read_csv('0215chiba_corona_data.csv', index_col='市町村')

st.dataframe(df)

st.bar_chart(df)
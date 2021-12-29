import streamlit as st
import pandas as pd
import numpy as np
import time

with st.sidebar:
 st.selectbox("Pilih data", ("fdfdfdf","dfdfdfd"))
 st.radio('Select one:', [1, 2])
 a= st.multiselect('Buy', ['milk', 'apples', 'potatoes'])


if len(a) != 0 :
  with st.spinner(text='In progress'):
    time.sleep(5)
    st.success('Done')
    st.write(a)





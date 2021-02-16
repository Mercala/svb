

import streamlit as st
import pandas as pd
import numpy as np
import json
import time

import matplotlib.pyplot as plt

werkgevers = pd.read_csv('Werkgeversbestand 1-1-2020.csv', index_col='Unnamed: 0')
werknemers = pd.read_csv('Werknemersbestand 1-1-2020.csv', index_col='Unnamed: 0')

# histogram data
arr = werkgevers['isic']
arr
fig, ax = plt.subplots()
ax.hist(arr)

st.pyplot(fig)

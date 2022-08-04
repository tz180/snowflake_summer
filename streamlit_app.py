#Creating personal streamlit app

import threading
import streamlit as st
import pandas as pd
import requests
from urllib.error import URLError

st.title('My Trades')

st.header('Complete List w/ Filter')

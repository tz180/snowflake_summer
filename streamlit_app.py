#Creating personal streamlit app

import threading
import streamlit as st
import pandas as pd
import requests
from urllib.error import URLError
import plotly.express as px

st.title('My Summer Internship')

snowflake_logo = """
@@@@@@@@@@@@@@@@@@@@B?77?G@@@@@@@@G?77?B@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@B!!!!!!P@@@@@@P!!!!!!B@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@P!7777!Y@@@@@@Y!7777!P@@@@@@@@@@@@@@@@@@@
@@@@@@@@#GGB&@@@@@@P!7777!5@@@@@@5!7777!P@@@@@@&BGG#@@@@@@@@
@@@@@@@J!!!!!?5B&@@G!7777!5@@@@@@5!7777!G@@&B5?!!!!!J@@@@@@@
@@@@@@&!!!!7!!!!7JGY!7777!5@@@@@@5!7777!YP?!!!!!7!!!!&@@@@@@
@@@@@@@&PJ7!!!!7!!!!77777!5@@@@@@5!77777!!!!7!!!!7JP&@@@@@@@
@@@@@@@@@@@#5?!!!!7777777!5@@@@@@5!7777777!!!!?5#@@@@@@@@@@@
@@&&&@@@@@@@@@&GY7!!!!77!!5@@@@@@Y!!77!!!!7YG&@@@@@@@@@&&&@@
#J7!!?YB&@@@@@@@@@#PJ7!!!J&@@@@@@&?!!!7JP#@@@@@@@@@&BY?!!7J#
7!!!!!!!!?P#@@@@@@@@@&&#&@@@@&&@@@@&&&@@@@@@@@@@#P?!!!!!!!!7
#J7!!!!7!!!!7JG&@@@@@@@@@@@P7!!7P@@@@@@@@@@@&GJ7!!!!7!!!!7J#
@@@#5?!!!777!!!!?YB@@@@@&P7!!??!!7P&@@@@@BY?!!!!777!!!?5#@@@
@@@@@@&BY7!77777!!!?@@@5!!!7B@@&J!!!G@@@?!!!77777!7YB&@@@@@@
@@@@@@&GJ7!77777!!!?@@@5!!!7#@@&J!!!P@@@?!!!!7777!7JG&@@@@@@
@@&BY7!!!777!!!!7YG@@@@@&57!!??!!75&@@@@@BY?!!!!777!!!7YB&@@
#J!!!!77!!!!7JP#@@@@@@@@@@&P7!!7P&@@@@@@@@@@&GJ7!!!!77!!!!J#
7!!!!!!!!?5B&@@@@@@@@@&&@@@@@&&@@@@&&&@@@@@@@@@@#P?!!!!!!!!7
&Y7!77YG&@@@@@@@@@&GJ7!!7Y&@@@@@@&J!!!7JG&@@@@@@@@@&BY?7!7Y&
@@@&&@@@@@@@@@&BY?!!!!!!!!Y@@@@@@Y!!77!!!!7YB&@@@@@@@@@&&@@@
@@@@@@@@@@@#P?!!!!!777777!5@@@@@@5!7777777!!!!?5#@@@@@@@@@@@
@@@@@@@&GJ7!!!!7!!!!77777!5@@@@@@5!77777!!!!7!!!!7JG&@@@@@@@
@@@@@@&!!!!77!!!!?PY!7777!5@@@@@@5!7777!YP?!!!!77!!!7&@@@@@@
@@@@@@&?!!!!!7YB&@@G!7777!5@@@@@@5!7777!G@@&BY?!!!!!J@@@@@@@
@@@@@@@@BPPG&@@@@@@P!7777!5@@@@@@5!7777!P@@@@@@&GPG#@@@@@@@@
@@@@@@@@@@@@@@@@@@@P!7777!Y@@@@@@Y!7777!P@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@B!!77!!P@@@@@@P!!77!!B@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@G?77?P@@@@@@@@P?77?G@@@@@@@@@@@@@@@@@@@@"""

st.text(snowflake_logo)

#ideas

st.header('Meetings List w/ Filter')

my_meeting_list = pd.read_csv("Snow_Meetings_csv.csv")

my_meeting_list = my_meeting_list.set_index('Snowflake Employee')

# Let's put a pick list here so they can pick the fruit they want to include 
meetings_selected = st.multiselect("When Did You Meet With Tyler?", list(my_meeting_list.index.drop_duplicates()))
meetings_to_show = my_meeting_list.loc[meetings_selected]

# Display the table on the page.
st.dataframe(meetings_to_show, 500)

col1, col2, col3 = st.columns(3)

col1.metric("# of 1:1's", "35", "3")
col2.metric("# of Meetings", "138", "13")
col3.metric("# of times I said Feature Engineering", "10,000", "400")

my_hours_list = pd.read_csv("Snow_Meeting_Hours.csv")

st.header('Meeting Hours by Week')

my_hours_list["Week"] = pd.to_datetime(my_hours_list["Week"])
my_hours_list.sort_values(by='Week', inplace=True)
my_hours_list.dropna(how='all', axis=1, inplace=True)
fmt = "%mmm-%YY"
styler = my_hours_list.style.format(
    {
        "Week": lambda t: t.strftime(fmt),
    }
)
my_hours_list = my_hours_list.set_index('Week')

st.dataframe(my_hours_list)

fig = px.line(my_hours_list, x="Date", y="Meeting Hours", color="Meeting Hours")
st.plotly_chart(fig)
my_meetings_list = pd.read_csv("Meeting_Numbers.csv")

st.header('Meetings by Week')

my_meetings_list["Week"] = pd.to_datetime(my_meetings_list["Week"])
my_meetings_list.sort_values(by='Week', inplace=True)
my_meetings_list = my_meetings_list.set_index('Week')

st.bar_chart(my_meetings_list)
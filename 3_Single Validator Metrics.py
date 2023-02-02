# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# Global Variables
theme_plotly = None # None or streamlit

# Layout
st.set_page_config(page_title='Single Validator Metrics', page_icon=':bar_chart:', layout='wide')
st.title('Single Validator Metrics')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Data Sources
@st.cache(ttl=2592000)
def get_data(query):
    if query == '1':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/13fae268-2956-4c9e-8e40-426709a931a7/data/latest')
    return None

list_data = get_data('1')


# Filter the blockchains
options = st.selectbox(
    '**Select your desired validator:**',
    options=list_data['VALIDATOR'].unique(),
    key='options'
)

# Selected Blockchain
if len(options) == 0:
    options = "binancenode1.poolv1.near"

# Single chain Analysis
elif len(options) > 1:
    st.subheader('Overview')
    # df = transactions_overview.query("Blockchain == @options")
    df12 = list_data.query("VALIDATOR == @options")
    fig12 = go.Figure()
    fig12.add_trace(go.Indicator(
            mode = "number",
            title = {'text': "Net Amount of Near Staked"},
            value = df12['NET_NEAR_STAKED'].iloc[0]))
    df13 = list_data.query("VALIDATOR== @options")
    fig13 = go.Figure()
    fig13.add_trace(go.Indicator(
            mode = "number",
            title = {'text': "Amount of NEAR Un-Staked"},
            value = df13['UNSTAKED_NEAR'].iloc[0]))
    df14 = list_data.query("VALIDATOR== @options")
    fig14 = go.Figure()
    fig14.add_trace(go.Indicator(
            mode = "number",
            title = {'text': "Amount of NEAR Staked"},
            value = df14['STAKED_NEAR'].iloc[0]))
    df15 = list_data.query("VALIDATOR== @options")
    fig15 = go.Figure()
    fig15.add_trace(go.Indicator(
            mode = "number",
            title = {'text': "Un-Staking Transactions"},
            value = df15['N_UNSTAKE_TXNS'].iloc[0]))
    df16 = list_data.query("VALIDATOR== @options")
    fig16 = go.Figure()
    fig16.add_trace(go.Indicator(
            mode = "number",
            title = {'text': "Staking Transactions"},
            value = df16['N_STAKE_TXNS'].iloc[0]))
    df17 = list_data.query("VALIDATOR== @options")
    fig17 = go.Figure()
    fig17.add_trace(go.Indicator(
            mode = "number",
            title = {'text': "Number of Unstakers"},
            value = df17['N_UNSTAKERS'].iloc[0]))
    df18 = list_data.query("VALIDATOR== @options")
    fig18 = go.Figure()
    fig18.add_trace(go.Indicator(
            mode = "number",
            title = {'text': "Number of Stakers"},
            value = df18['N_STAKERS'].iloc[0]))
   

    
    c1, c2, c3 = st.columns([2,1, 1])
    c1.plotly_chart(fig12, use_container_width=True)
    c2.plotly_chart(fig13, use_container_width=True)
    c3.plotly_chart(fig14, use_container_width=True)
    c4, c5, c6, c7 = st.columns(4)

    c4.plotly_chart(fig15, use_container_width=True)
    c5.plotly_chart(fig16, use_container_width=True)
    c6.plotly_chart(fig17, use_container_width=True)
    c7.plotly_chart(fig18, use_container_width=True)

# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Global Variables
theme_plotly = None # None or streamlit

# Layout
st.set_page_config(page_title='Decentralization Metrics', page_icon=':bar_chart:', layout='wide')
st.title('Decentralization Metrics')

#Cache
# @st.cache(suppress_st_warning=True)


# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Data Sources
# Data Sources
@st.cache(ttl=2592000)
def get_data(query):
    if query == '0':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/72a7763b-61fa-4750-8944-ebfa008a521b/data/latest')
    if query == '1':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/cd02b887-a9c9-4918-9468-91a55ab4557e/data/latest')
    if query == '2':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/7ac7428c-f2d4-4c3a-83ab-89a18b6fb157/data/latest')
    return None

df0 = get_data('0')
df1 = get_data('0')

df2 = get_data('1')
df3 = get_data('1')
df4 = get_data('1')
df5 = get_data('1')
df6 = get_data('1')

df7 = get_data('2')
df8 = get_data('2')
df9 = get_data('2')
df10 = get_data('2')
df11 = get_data('2')







df0 = df0.sort_values(by=['MONTH'], ascending=[True])
fig0 = go.Figure()
fig0 = make_subplots(specs=[[{"secondary_y": True}]])

# trace0 = go.Scatter(x=df0['MONTH'], 
#                 y=df0['Top 10 Validator %'],
#                 mode='lines',
#                 name='Top 10 Validator %')

trace1 = go.Scatter(x=df0['MONTH'], 
                y=df0['Top 10 Validator % Share'],
                mode='lines',
                name='Top 10 Validator % Share')
trace2 = go.Scatter(x=df0['MONTH'], 
                y=df0['Top Validator % Share'],
                mode='lines',
                name='Top Validator % Share')
trace3 = go.Scatter(x=df0['MONTH'], 
                y=df0['% Validators >51%'],
                mode='lines',
                name='% Validators >51%')

# fig0.add_trace(trace0,secondary_y=True)

fig0.add_trace(trace1,secondary_y=False)
fig0.add_trace(trace2,secondary_y=False)
fig0.add_trace(trace3,secondary_y=False)
fig0.update_layout(title="Estimated % Share of Top and Top 10 Validators")
df1 = df1.sort_values(by=['MONTH'], ascending=[True])
fig1 = go.Figure()
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

trace5 = go.Scatter(x=df1['MONTH'], 
                y=df1['Nakamoto Coefficient'],
                mode='lines',
                name='Nakamoto Coefficient')

trace6 = go.Scatter(x=df1['MONTH'], 
                y=df1['GINI'],
                mode='lines',
                name='GINI')

fig1.add_trace(trace5,secondary_y=True)

fig1.add_trace(trace6,secondary_y=False)
fig1.update_layout(title="Estimated GINI Index & Nakamoto Coefficient Over Time")
# df2 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/cd02b887-a9c9-4918-9468-91a55ab4557e/data/latest")
df2 = df2.sort_values(by=['MONTH'], ascending=[True])

fig2 = px.line(df2.dropna(subset=['CUMULATIVE_DELEGATION']), 
                        x='MONTH', 
                        y='CUMULATIVE_DELEGATION', 
                        color='GOVERNOR')
            

fig2.update_layout(title="Cumulative Amount of NEAR Staked per Governor over Time")
# df3 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/cd02b887-a9c9-4918-9468-91a55ab4557e/data/latest")
fig3 = px.bar(df3,x='MONTH',
            y = 'NUMBER_TRANSACTIONS'
            )
    
fig3.update_layout(title="Number of Transactions over Time")
# df4 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/cd02b887-a9c9-4918-9468-91a55ab4557e/data/latest")
fig4 = px.bar(df4,x='MONTH',
            y = 'NUMBER_OF_STAKERS'
            )
    
fig4.update_layout(title="Number of Stakers over Time")
# df5 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/cd02b887-a9c9-4918-9468-91a55ab4557e/data/latest")
fig5 = px.bar(df5,x='MONTH',
            y = 'AMOUNT_NEAR_STAKED'
            )
    
fig5.update_layout(title="Amount of NEAR Staked over Time")
# df6 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/cd02b887-a9c9-4918-9468-91a55ab4557e/data/latest")
fig6 = px.bar(df6,x='MONTH',
            y = 'NEAR_PER_STAKER'
            )
    
fig6.update_layout(title="Average Amount of NEAR Staked per Staker over Time")
# df7 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/7ac7428c-f2d4-4c3a-83ab-89a18b6fb157/data/latest")
fig7 = px.bar(df7,x='MONTH',
            y = 'NUMBER_OF_UNSTAKERS'
            )
    
fig7.update_layout(title="Number of UnStakers over Time")
# df8 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/7ac7428c-f2d4-4c3a-83ab-89a18b6fb157/data/latest")
fig8 = px.bar(df8,x='MONTH',
            y = 'NUMBER_TRANSACTIONS'
            )
    
fig8.update_layout(title="Number of Transactions over Time")
# df9 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/7ac7428c-f2d4-4c3a-83ab-89a18b6fb157/data/latest")
fig9 = px.bar(df9,x='MONTH',
            y = 'AMOUNT_NEAR_UNSTAKED'
            )
    
fig9.update_layout(title="Amount of NEAR UnStaked over Time")
# df10 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/7ac7428c-f2d4-4c3a-83ab-89a18b6fb157/data/latest")
fig10 = px.bar(df10,x='MONTH',
            y = 'NEAR_PER_UNSTAKER'
            )
    
fig10.update_layout(title="Average Amount of NEAR UnStaked per Staker over Time")
# df11 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/7ac7428c-f2d4-4c3a-83ab-89a18b6fb157/data/latest")
df11 = df11.sort_values(by=['MONTH'], ascending=[True])

fig11 = px.line(df11.dropna(subset=['CUMULATIVE_UNDELEGATION']), 
                        x='MONTH', 
                        y='CUMULATIVE_UNDELEGATION', 
                        color='GOVERNOR')
fig11.update_layout(title="Cumulative Amount of NEAR UnStaked per Governor over Time")

st.plotly_chart(fig0, theme="streamlit", use_container_width=True)
st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
st.write("""
    As can be seen from the charts above, we can see that
    - The total near staked and the top 10 near validators' share of the total near staked has increased from January 2022 to December 2022.

    - The top validator's share of the total near staked has remained relatively constant, with a slight decrease from January 2022 to December 2022.

    - The Gini coefficient, which measures the inequality among values, has remained relatively constant, with some fluctuations.

    - The number of validators has varied from 113 to 172.

    - The Nakamoto coefficient, which measures the concentration of power among validators, has remained relatively constant, with a slight decrease from January 2022 to December 2022.

    - The percentage of validators with over 51% of the total near staked has fluctuated between 8.39% and 12.56%.
""")
st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

st.plotly_chart(fig3, theme="streamlit", use_container_width=True)
st.plotly_chart(fig4, theme="streamlit", use_container_width=True)
st.plotly_chart(fig5, theme="streamlit", use_container_width=True)
st.plotly_chart(fig6, theme="streamlit", use_container_width=True)
st.plotly_chart(fig7, theme="streamlit", use_container_width=True)
st.plotly_chart(fig8, theme="streamlit", use_container_width=True)
st.plotly_chart(fig9, theme="streamlit", use_container_width=True)
st.plotly_chart(fig10, theme="streamlit", use_container_width=True)
st.plotly_chart(fig11, theme="streamlit", use_container_width=True)




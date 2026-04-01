import streamlit as st
from streamlit import text_input
import plotly.graph_objects as go

from dbhelper import DB

db=DB()
st.sidebar.title('flights analytics')
user_option=st.sidebar.selectbox('menu',['select one','check flights','Analytics'])
if user_option=='check flights':
    st.title('check flights')

    col1,col2= st.columns(2)

    city = db.fetch_city_names()
    with col1:
        source=st.selectbox('source',sorted(city))
    with col2:
        destination=st.selectbox('destination',sorted(city))

    if st.button('Search'):
        results=db.fetch_all_flights(source,destination)
        st.dataframe(results)


elif user_option=='Analytics':
    airline,frequency= db.fetch_airline_frequency()
    fig=go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo='label+percent',
            textinfo='value',
        ))
    st.header('pie chart')
    st.plotly_chart(fig)

    city, frequency = db.busy_airport()
    fig = go.Figure(
        go.Bar(
            x=city,  # ← city not airline
            y=frequency,
            hoverinfo='x+y',
        ))
    st.header('Busiest Airports')
    st.plotly_chart(fig)

else:
    st.title('Tell about the project')
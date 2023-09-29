import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast for the Next Days')

place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5, help='Select the number of forecasted days')

option = st.selectbox('Select data to view', ('Temperature','Sky'))

st.subheader(f' {option} for the next {days} days in {place}')


if place:
    
    try:
  
        filtered_data = get_data(place,days)
        
        print(dict['dt_temp'][0] for dict in filtered_data)
        
        if option == 'Temperature':
            temperatures = [dict['main']['temp']/10 for dict in filtered_data]
            date = [dict['dt_txt'] for dict in filtered_data]
            
            figure = px.line(x=date, y=temperatures, labels={'x':'Dates', 'y':'Temperature (C°)'})
            st.plotly_chart(figure)
            
        if option == 'Sky':
            images = {'Clear': 'images/clear.png', 'Clouds':'images/cloud.png','Rain':'images/rain.png', 'Snow':'images/snow.png'}
            date = [dict['dt_txt'] for dict in filtered_data]
            
            sky_condition = [dict['weather'][0]['main'] for dict in filtered_data]
            images_paths = [images[condition] for condition in sky_condition]
            
            st.image(images_paths,width=115,caption=date)
    except KeyError:
        st.write('That Place does not exist')
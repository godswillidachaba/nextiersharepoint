import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px



# Configuration

st.set_page_config(layout="wide")




# Read Data

df = pd.read_csv('data.csv')






# Header


st.sidebar.image("logo.jpg", width=200)

st.markdown("""

    ## SharePoint Usage
         
    Analysis of sharepoint usage in the last 3 months
    
    <br>
         
    

""", unsafe_allow_html=True)





# Filtering 



business_units = list( sorted( df['Business Unit'].unique() ) )

selected_business_unit = st.sidebar.selectbox("Business Unit", business_units)   # Select Box


if selected_business_unit == "All":

    filtered_df = df

else:

    filtered_df = df[df["Business Unit"] == selected_business_unit ]







# Analyze By

st.sidebar.markdown("<br>", unsafe_allow_html=True)

analyze_by = st.sidebar.selectbox("Metric", ["Viewed Or Edited Page Count", "Page Count", ])


if analyze_by == "Page Count":

    analyze_by = "Visited Page Count"

else:

    analyze_by = "Viewed Or Edited File Count"





# Reset Index
    
filtered_df = filtered_df.sort_values(by=analyze_by, ascending=False)

filtered_df = filtered_df.reset_index(drop=True)

filtered_df.index += 1





# Table





st.dataframe(filtered_df, use_container_width=False)



# Data Visualization




st.markdown(""" 

### Data Visualization
            
Visualization of usage per employee

""")



# Sort

filtered_df = filtered_df.sort_values(by=analyze_by, ascending=True)



fig = px.bar(filtered_df, x=analyze_by, y='Fullname', orientation='h', text=analyze_by)




fig.update_traces(texttemplate='%{text}', textposition='outside')


st.plotly_chart(fig, use_container_width=True)



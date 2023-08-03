import pandas as pd
import calendar
import openpyxl
import streamlit as st
import plotly.express as px
from PIL import Image
import base64

st.set_page_config(page_title='Yearly Deployment Data')
#st.header('Yearly Deployment Data - 2023')
st.markdown("<h1 style='text-align: center; color: white;'><u>Yearly Deployment Data</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Welcome!!!</h2>", unsafe_allow_html=True)
#st.subheader('Welcome!!')

# Display the welcome images

col1, col2,col3 = st.columns(3)
image1 = Image.open('Amdocs_Image.jpg')
image2 = Image.open('ATT_Image.jpg')
image3 = Image.open('AMOC_Image.png')
col1.image(image1,use_column_width=True)
col2.image(image3,use_column_width=True)
col3.image(image2,use_column_width=True)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('BGI_4.jpg')

### --- LOAD DATAFRAME
excel_file = 'Yearly_Deployment_Data_2023.xlsx'
sheet_name = 'CRData'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:I',
                   header=0)

# --- STREAMLIT SELECTION
month = df['Month'].unique().tolist()
status = df['Status'].unique().tolist()


month_selection = st.multiselect('Select Months to include:',
                                    month,
                                    default=month)
status_selection = st.multiselect('Select Statuses to include:',
                                    status,
                                    default=status)

# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df['Month'].isin(month_selection)) & (df['Status'].isin(status_selection))
#number_of_result = df[mask].shape[0]
#st.markdown(f'*Available Results: {number_of_result}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['Status']).count()[['Month']]
df_grouped = df_grouped.rename(columns={'Month': 'Count'})
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
st.subheader(":bar_chart: Visual Insights :bar_chart:")
bar_chart = px.bar(df_grouped,
                   x='Status',
                   y='Count',
                   text='Count',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)

# --- PIVOT TABLE
file_path = 'Yearly_Deployment_Data_2023.xlsx'
sheet_name = 'CRData'
selected_columns = "A:H"


df_new = pd.read_excel(file_path, sheet_name=sheet_name, usecols=selected_columns)
df_new = df_new.rename(columns={'Application': '---------------------------------------------------------------------------------------------------'})

#Sorting Month Names
number_of_months=len(month)
list_of_months_sorted = []
for i in range(1, number_of_months+1):
    list_of_months_sorted.append(calendar.month_name[i]) # month_name is an array

#Applyig custom month order to dataframe
custom_month_order = list_of_months_sorted
df_new['Month'] = pd.Categorical(df_new['Month'], categories=custom_month_order, ordered=True)


pivot_table = df_new.pivot_table(index='Month', columns='Status', aggfunc='count',fill_value=0)
pivot_table = pivot_table.iloc[:, :6]

# --- DISPLAY Dataframe
st.subheader(":brain: Deep Insights :brain:")
st.write(df[mask])

# Display the pivot table
st.subheader(":calendar: Overall Monthly Status :calendar:")
st.write(pivot_table)

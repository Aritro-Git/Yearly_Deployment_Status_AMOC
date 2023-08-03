import pandas as pd
import calendar
import openpyxl
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image
import base64

st.set_page_config(page_title='Yearly Deployment Data')
#st.header('Yearly Deployment Data - 2023')
st.markdown("<h1 style='text-align: center; color: white;'>Yearly Deployment Data - 2023</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>Welcome!!!</h1>", unsafe_allow_html=True)
#st.subheader('Welcome!!')

# Display the welcome images

col1, col2 = st.columns(2)
image1 = Image.open('Amdocs_Image.jpg')
image2 = Image.open('ATT_Image.jpg')
col1.image(image1,use_column_width=True)
col2.image(image2,use_column_width=True)


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



#Status: Completed
df_completed = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:I',
                   header=0)

#Filter - Jan Data

column_name_month_completed = "Month"
filter_value_month_completed = "January"
column_name_status_completed = "Status"
filter_value_status_completed = "Completed"
df_completed = df_completed[df_completed[column_name_month_completed] == filter_value_month_completed]
df_completed = df_completed[df_completed[column_name_status_completed] == filter_value_status_completed]

# --- STREAMLIT SELECTION
lob = df_completed['LOB'].unique().tolist()
status = df_completed['Status'].unique().tolist()

if not lob:
    st.markdown("No Data To Show")
else:
    month_selection = st.multiselect('Select LOBs to include:', #Here Month==LOB
                                        lob,
                                        default=lob)
    #status_selection = st.multiselect('Select Statuses to include:',
                                        #status,
                                        #default=status)

    # --- FILTER DATAFRAME BASED ON SELECTION
    mask = (df_completed['LOB'].isin(month_selection)) #& (df['Status'].isin(status_selection))


    # --- GROUP DATAFRAME AFTER SELECTION
    df_grouped = df_completed[mask].groupby(by=['LOB']).count()[['Status']]
    df_grouped = df_grouped.rename(columns={'Status': 'Count'})
    df_grouped = df_grouped.reset_index()

    # --- PLOT BAR CHART
    st.subheader(":bar_chart: Completed :bar_chart:")
    #bar_chart = px.bar(df_grouped,
                       #x='LOB',
                       #y='Count',
                       #text='Count',
                       #color_discrete_sequence = ['#F63366']*len(df_grouped),
                       #template= 'plotly_white')


    #st.bar_chart(df_grouped.set_index("LOB"))
    fig_completed = px.bar(df_grouped, x="LOB", y="Count",text="Count", barmode="group",color_discrete_sequence = ['#F63366']*len(df_grouped))
    st.plotly_chart(fig_completed)

#****************End of a Completed section*************************************

#Status: Partially_deployed
df_Partially_deployed = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:I',
                   header=0)

#Filter - Jan Data

column_name_month_Partially_deployed = "Month"
filter_value_month_Partially_deployed = "January"
column_name_status_Partially_deployed = "Status"
filter_value_status_Partially_deployed = "Partially deployed"
df_Partially_deployed = df_Partially_deployed[df_Partially_deployed[column_name_month_Partially_deployed] == filter_value_month_Partially_deployed]
df_Partially_deployed = df_Partially_deployed[df_Partially_deployed[column_name_status_Partially_deployed] == filter_value_status_Partially_deployed]

# --- STREAMLIT SELECTION
lob = df_Partially_deployed['LOB'].unique().tolist()
status = df_Partially_deployed['Status'].unique().tolist()

if not lob:
    st.markdown("No Data to show")
else:
    month_selection = st.multiselect('Select LOBs to include:', #Here Month==LOB
                                        lob,
                                        default=lob)
    #status_selection = st.multiselect('Select Statuses to include:',
                                        #status,
                                        #default=status)

    # --- FILTER DATAFRAME BASED ON SELECTION
    mask = (df_Partially_deployed['LOB'].isin(month_selection)) #& (df['Status'].isin(status_selection))


    # --- GROUP DATAFRAME AFTER SELECTION
    df_grouped = df_Partially_deployed[mask].groupby(by=['LOB']).count()[['Status']]
    df_grouped = df_grouped.rename(columns={'Status': 'Count'})
    df_grouped = df_grouped.reset_index()

    # --- PLOT BAR CHART
    st.subheader(":bar_chart: Partially Deployed :bar_chart:")
    #bar_chart = px.bar(df_grouped,
                       #x='LOB',
                       #y='Count',
                       #text='Count',
                       #color_discrete_sequence = ['#F63366']*len(df_grouped),
                       #template= 'plotly_white')


    #st.bar_chart(df_grouped.set_index("LOB"))
    fig_Partially_deployed = px.bar(df_grouped, x="LOB", y="Count",text="Count", barmode="group",color_discrete_sequence = ['#F63366']*len(df_grouped))
    st.plotly_chart(fig_Partially_deployed)
#****************End of a Partially_deployed section*************************************

#Status: Cancelled

df_Canc = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:I',
                   header=0)

#Filter - Jan Data

column_name_month_Canc = "Month"
filter_value_month_Canc = "January"
column_name_status_Canc = "Status"
filter_value_status_Canc = "Cancelled"
df_Canc = df_Canc[df_Canc[column_name_month_Canc] == filter_value_month_Canc]
df_Canc = df_Canc[df_Canc[column_name_status_Canc] == filter_value_status_Canc]

# --- STREAMLIT SELECTION
lob = df_Canc['LOB'].unique().tolist()
status = df_Canc['Status'].unique().tolist()
if not lob:
    st.markdown("List is empty")
else:
    month_selection = st.multiselect('Select LOBs to include:', #Here Month==LOB
                                        lob,
                                        default=lob)
    #status_selection = st.multiselect('Select Statuses to include:',
                                        #status,
                                        #default=status)

    # --- FILTER DATAFRAME BASED ON SELECTION
    mask = (df_Canc['LOB'].isin(month_selection)) #& (df['Status'].isin(status_selection))


    # --- GROUP DATAFRAME AFTER SELECTION
    df_grouped = df_Canc[mask].groupby(by=['LOB']).count()[['Status']]
    df_grouped = df_grouped.rename(columns={'Status': 'Count'})
    df_grouped = df_grouped.reset_index()

    # --- PLOT BAR CHART
    st.subheader(":bar_chart: Cancelled :bar_chart:")
    #bar_chart = px.bar(df_grouped,
                       #x='LOB',
                       #y='Count',
                       #text='Count',
                       #color_discrete_sequence = ['#F63366']*len(df_grouped),
                       #template= 'plotly_white')


    #st.bar_chart(df_grouped.set_index("LOB"))
    fig_Canc = px.bar(df_grouped, x="LOB", y="Count",text="Count", barmode="group",color_discrete_sequence = ['#F63366']*len(df_grouped))
    print(fig_Canc)
    st.plotly_chart(fig_Canc)
#****************End of a Cancelled section*************************************

#Status: Cancelled/Rescheduled
df_CancResc = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:I',
                   header=0)

#Filter - Jan Data

column_name_month_CancResc = "Month"
filter_value_month_CancResc = "January"
column_name_status_CancResc = "Status"
filter_value_status_CancResc = "Cancelled/Rescheduled"
df_CancResc = df_CancResc[df_CancResc[column_name_month_CancResc] == filter_value_month_CancResc]
df_CancResc = df_CancResc[df_CancResc[column_name_status_CancResc] == filter_value_status_CancResc]

# --- STREAMLIT SELECTION
lob = df_CancResc['LOB'].unique().tolist()
status = df_CancResc['Status'].unique().tolist()

if not lob:
    st.markdown("No Data to Show")
else:
    month_selection = st.multiselect('Select LOBs to include:', #Here Month==LOB
                                        lob,
                                        default=lob)
    #status_selection = st.multiselect('Select Statuses to include:',
                                        #status,
                                        #default=status)

    # --- FILTER DATAFRAME BASED ON SELECTION
    mask = (df_CancResc['LOB'].isin(month_selection)) #& (df['Status'].isin(status_selection))


    # --- GROUP DATAFRAME AFTER SELECTION
    df_grouped = df_CancResc[mask].groupby(by=['LOB']).count()[['Status']]
    df_grouped = df_grouped.rename(columns={'Status': 'Count'})
    df_grouped = df_grouped.reset_index()

    # --- PLOT BAR CHART
    st.subheader(":bar_chart: Cancelled/Rescheduled :bar_chart:")
    #bar_chart = px.bar(df_grouped,
                       #x='LOB',
                       #y='Count',
                       #text='Count',
                       #color_discrete_sequence = ['#F63366']*len(df_grouped),
                       #template= 'plotly_white')


    #st.bar_chart(df_grouped.set_index("LOB"))
    fig_CancResc = px.bar(df_grouped, x="LOB", y="Count",text="Count", barmode="group",color_discrete_sequence = ['#F63366']*len(df_grouped))
    st.plotly_chart(fig_CancResc)
#****************End of a Cancelled/Rescheduled section*************************************

#Status: Backed Out
df_BackedOut = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:I',
                   header=0)

#Filter - Jan Data

column_name_month_BackedOut = "Month"
filter_value_month_BackedOut = "January"
column_name_status_BackedOut = "Status"
filter_value_status_BackedOut = "Backed Out"
df_BackedOut = df_BackedOut[df_BackedOut[column_name_month_BackedOut] == filter_value_month_BackedOut]
df_BackedOut = df_BackedOut[df_BackedOut[column_name_status_BackedOut] == filter_value_status_BackedOut]

# --- STREAMLIT SELECTION
lob = df_BackedOut['LOB'].unique().tolist()
status = df_BackedOut['Status'].unique().tolist()

if not lob:
    st.markdown("No Data To Show")
else:
    month_selection = st.multiselect('Select LOBs to include:', #Here Month==LOB
                                        lob,
                                        default=lob)
    #status_selection = st.multiselect('Select Statuses to include:',
                                        #status,
                                        #default=status)

    # --- FILTER DATAFRAME BASED ON SELECTION
    mask = (df_BackedOut['LOB'].isin(month_selection)) #& (df['Status'].isin(status_selection))


    # --- GROUP DATAFRAME AFTER SELECTION
    df_grouped = df_BackedOut[mask].groupby(by=['LOB']).count()[['Status']]
    df_grouped = df_grouped.rename(columns={'Status': 'Count'})
    df_grouped = df_grouped.reset_index()

    # --- PLOT BAR CHART
    st.subheader(":bar_chart: Backed Out :bar_chart:")
    #bar_chart = px.bar(df_grouped,
                       #x='LOB',
                       #y='Count',
                       #text='Count',
                       #color_discrete_sequence = ['#F63366']*len(df_grouped),
                       #template= 'plotly_white')


    #st.bar_chart(df_grouped.set_index("LOB"))
    fig_BackedOut = px.bar(df_grouped, x="LOB", y="Count",text="Count", barmode="group",color_discrete_sequence = ['#F63366']*len(df_grouped))
    st.plotly_chart(fig_BackedOut)
#****************End of a Backed Out section*************************************

#Status: Unsuccessful
df_Unsuccessful = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:I',
                   header=0)

#Filter - Jan Data

column_name_month_Unsuccessful = "Month"
filter_value_month_Unsuccessful = "January"
column_name_status_Unsuccessful = "Status"
filter_value_status_Unsuccessful = "Unsuccessful"
df_Unsuccessful = df_Unsuccessful[df_Unsuccessful[column_name_month_Unsuccessful] == filter_value_month_Unsuccessful]
df_Unsuccessful = df_Unsuccessful[df_Unsuccessful[column_name_status_Unsuccessful] == filter_value_status_Unsuccessful]

# --- STREAMLIT SELECTION
lob = df_Unsuccessful['LOB'].unique().tolist()
status = df_Unsuccessful['Status'].unique().tolist()

if not lob:
    st.markdown("Nothing to show")
else:
    month_selection = st.multiselect('Select LOBs to include:', #Here Month==LOB
                                        lob,
                                        default=lob)
    #status_selection = st.multiselect('Select Statuses to include:',
                                        #status,
                                        #default=status)

    # --- FILTER DATAFRAME BASED ON SELECTION
    mask = (df_Unsuccessful['LOB'].isin(month_selection)) #& (df['Status'].isin(status_selection))


    # --- GROUP DATAFRAME AFTER SELECTION
    df_grouped = df_Unsuccessful[mask].groupby(by=['LOB']).count()[['Status']]
    df_grouped = df_grouped.rename(columns={'Status': 'Count'})
    df_grouped = df_grouped.reset_index()

    # --- PLOT BAR CHART
    st.subheader(":bar_chart: Unsuccessful :bar_chart:")
    #bar_chart = px.bar(df_grouped,
                       #x='LOB',
                       #y='Count',
                       #text='Count',
                       #color_discrete_sequence = ['#F63366']*len(df_grouped),
                       #template= 'plotly_white')


    #st.bar_chart(df_grouped.set_index("LOB"))
    fig_Unsuccessful = px.bar(df_grouped, x="LOB", y="Count",text="Count", barmode="group",color_discrete_sequence = ['#F63366']*len(df_grouped))
    st.plotly_chart(fig_Unsuccessful)


#**************End of Unsuccessful section************

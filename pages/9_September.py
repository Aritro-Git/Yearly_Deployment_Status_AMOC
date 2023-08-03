#September

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
st.markdown("<h2 style='text-align: center; color: white;'><u>September Deployment Status LOB Wise</h2>", unsafe_allow_html=True)
#st.markdown("<h1 style='text-align: center; color: white;'>Welcome!!!</h1>", unsafe_allow_html=True)
#st.subheader('Welcome!!')

# No Record image
image_no_record = Image.open("No_Record_Image.jpg")

# Display Background image
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

custom_css = """
    <style>
    .st-eb {
        width: 100% !important;
    }
    </style>
    """
#st.markdown(custom_css, unsafe_allow_html=True)
#selected_option = st.selectbox('Select an option', ["Completed", "Partially deployed", "Cancelled","Cancelled/Rescheduled","Backed Out","Unsuccessful"])

### --- LOAD DATAFRAME
excel_file = 'Yearly_Deployment_Data_2023.xlsx'
sheet_name = 'CRData'

selected = option_menu(
            menu_title="",  # required
            options=["Completed", "Partially deployed", "Cancelled","Cancelled/Rescheduled","Backed Out","Unsuccessful"],  # required
            icons=["emoji-sunglasses-fill", "emoji-neutral-fill", "emoji-frown-fill","emoji-angry-fill","emoji-expressionless-fill","emoji-dizzy-fill"],  # optional
            #menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#000000"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "18px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#000000",
                    "width":"100% !important"
                },
                "nav-link-selected": {"background-color": "#DC143C"},
            },
        )

if selected == "Completed":
    #Status: Completed
    df_completed = pd.read_excel(excel_file,
                       sheet_name=sheet_name,
                       usecols='A:I',
                       header=0)

    #Filter - Jan Data

    column_name_month_completed = "Month"
    filter_value_month_completed = "September"
    column_name_status_completed = "Status"
    filter_value_status_completed = "Completed"
    df_completed = df_completed[df_completed[column_name_month_completed] == filter_value_month_completed]
    df_completed = df_completed[df_completed[column_name_status_completed] == filter_value_status_completed]

    # --- STREAMLIT SELECTION
    lob = df_completed['LOB'].unique().tolist()
    status = df_completed['Status'].unique().tolist()

    if not lob:
        st.image(image_no_record, use_column_width=True)
    else:
        #st.markdown("<h6 style='text-align: left; color: white;'>Select all required LOBs:-</h6>", unsafe_allow_html=True)
        month_selection = st.multiselect('Select all required LOBs:-', #Here Month==LOB
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
        st.subheader(":bar_chart: Visual Insights - Completed CRs :bar_chart:")
        #bar_chart = px.bar(df_grouped,
                           #x='LOB',
                           #y='Count',
                           #text='Count',
                           #color_discrete_sequence = ['#F63366']*len(df_grouped),
                           #template= 'plotly_white')


        #st.bar_chart(df_grouped.set_index("LOB"))
        fig_completed = px.bar(df_grouped, x="LOB", y="Count",text="Count", barmode="group",color_discrete_sequence = ['#66AA00']*len(df_grouped))
        st.plotly_chart(fig_completed)

        st.subheader(":brain: Deep Insights - Completed CRs :brain:")
        st.write(df_completed[mask])

    #****************End of a Completed section*************************************

if selected == "Partially deployed":
    #Status: Partially_deployed
    df_Partially_deployed = pd.read_excel(excel_file,
                       sheet_name=sheet_name,
                       usecols='A:I',
                       header=0)

    #Filter - Jan Data

    column_name_month_Partially_deployed = "Month"
    filter_value_month_Partially_deployed = "September"
    column_name_status_Partially_deployed = "Status"
    filter_value_status_Partially_deployed = "Partially deployed"
    df_Partially_deployed = df_Partially_deployed[df_Partially_deployed[column_name_month_Partially_deployed] == filter_value_month_Partially_deployed]
    df_Partially_deployed = df_Partially_deployed[df_Partially_deployed[column_name_status_Partially_deployed] == filter_value_status_Partially_deployed]

    # --- STREAMLIT SELECTION
    lob = df_Partially_deployed['LOB'].unique().tolist()
    status = df_Partially_deployed['Status'].unique().tolist()

    if not lob:
        st.image(image_no_record, use_column_width=True)
    else:
        month_selection = st.multiselect('Select LOBs to include:', #Here Month==LOB
                                            lob,
                                            default=lob,
                                            )
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
        st.subheader(":bar_chart: Visual Insights - Partially Deployed CRs  :bar_chart:")
        #bar_chart = px.bar(df_grouped,
                           #x='LOB',
                           #y='Count',
                           #text='Count',
                           #color_discrete_sequence = ['#F63366']*len(df_grouped),
                           #template= 'plotly_white')


        #st.bar_chart(df_grouped.set_index("LOB"))
        fig_Partially_deployed = px.bar(df_grouped, x="LOB", y="Count",text="Count", barmode="group",color_discrete_sequence = ['#FECB52']*len(df_grouped))
        st.plotly_chart(fig_Partially_deployed)

        st.subheader(":brain: Deep Insights - Partially Deployed CRs :brain:")
        st.write(df_Partially_deployed[mask])
    #****************End of a Partially_deployed section*************************************
if selected == "Cancelled":
    #Status: Cancelled

    df_Canc = pd.read_excel(excel_file,
                       sheet_name=sheet_name,
                       usecols='A:I',
                       header=0)

    #Filter - Jan Data

    column_name_month_Canc = "Month"
    filter_value_month_Canc = "September"
    column_name_status_Canc = "Status"
    filter_value_status_Canc = "Cancelled"
    df_Canc = df_Canc[df_Canc[column_name_month_Canc] == filter_value_month_Canc]
    df_Canc = df_Canc[df_Canc[column_name_status_Canc] == filter_value_status_Canc]

    # --- STREAMLIT SELECTION
    lob = df_Canc['LOB'].unique().tolist()
    status = df_Canc['Status'].unique().tolist()
    if not lob:
        st.image(image_no_record, use_column_width=True)
    else:
        month_selection = st.multiselect('', #Here Month==LOB
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
        st.subheader(":bar_chart: Visual Insights - Cancelled CRs :bar_chart:")
        #bar_chart = px.bar(df_grouped,
                           #x='LOB',
                           #y='Count',
                           #text='Count',
                           #color_discrete_sequence = ['#F63366']*len(df_grouped),
                           #template= 'plotly_white')


        #st.bar_chart(df_grouped.set_index("LOB"))
        fig_Canc = px.bar(df_grouped, x="LOB", y="Count",text="Count", barmode="group",color_discrete_sequence = ['#BAB0AC']*len(df_grouped))
        print(fig_Canc)
        st.plotly_chart(fig_Canc)

        st.subheader(":brain: Deep Insights - Cancelled CRs :brain:")
        st.write(df_Canc[mask])
    #****************End of a Cancelled section*************************************
if selected == "Cancelled/Rescheduled":
    #Status: Cancelled/Rescheduled
    df_CancResc = pd.read_excel(excel_file,
                       sheet_name=sheet_name,
                       usecols='A:I',
                       header=0)

    #Filter - Jan Data

    column_name_month_CancResc = "Month"
    filter_value_month_CancResc = "September"
    column_name_status_CancResc = "Status"
    filter_value_status_CancResc = "Cancelled/Rescheduled"
    df_CancResc = df_CancResc[df_CancResc[column_name_month_CancResc] == filter_value_month_CancResc]
    df_CancResc = df_CancResc[df_CancResc[column_name_status_CancResc] == filter_value_status_CancResc]

    # --- STREAMLIT SELECTION
    lob = df_CancResc['LOB'].unique().tolist()
    status = df_CancResc['Status'].unique().tolist()

    if not lob:
        st.image(image_no_record, use_column_width=True)
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
        st.subheader(":bar_chart: Visual Insights - Cancelled/Rescheduled CRs :bar_chart:")
        #bar_chart = px.bar(df_grouped,
                           #x='LOB',
                           #y='Count',
                           #text='Count',
                           #color_discrete_sequence = ['#F63366']*len(df_grouped),
                           #template= 'plotly_white')


        #st.bar_chart(df_grouped.set_index("LOB"))
        fig_CancResc = px.bar(df_grouped, x="LOB", y="Count",text="Count", barmode="group",color_discrete_sequence = ['#AA0DFE']*len(df_grouped))
        st.plotly_chart(fig_CancResc)

        st.subheader(":brain: Deep Insights - Cancelled/Rescheduled CRs :brain:")
        st.write(df_CancResc[mask])
    #****************End of a Cancelled/Rescheduled section*************************************
if selected == "Backed Out":
    #Status: Backed Out
    df_BackedOut = pd.read_excel(excel_file,
                       sheet_name=sheet_name,
                       usecols='A:I',
                       header=0)

    #Filter - Jan Data

    column_name_month_BackedOut = "Month"
    filter_value_month_BackedOut = "September"
    column_name_status_BackedOut = "Status"
    filter_value_status_BackedOut = "Backed Out"
    df_BackedOut = df_BackedOut[df_BackedOut[column_name_month_BackedOut] == filter_value_month_BackedOut]
    df_BackedOut = df_BackedOut[df_BackedOut[column_name_status_BackedOut] == filter_value_status_BackedOut]

    # --- STREAMLIT SELECTION
    lob = df_BackedOut['LOB'].unique().tolist()
    status = df_BackedOut['Status'].unique().tolist()

    if not lob:
        st.image(image_no_record, use_column_width=True)
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
        st.subheader(":bar_chart: Visual Insights - Backed Out CRs :bar_chart:")
        #bar_chart = px.bar(df_grouped,
                           #x='LOB',
                           #y='Count',
                           #text='Count',
                           #color_discrete_sequence = ['#F63366']*len(df_grouped),
                           #template= 'plotly_white')


        #st.bar_chart(df_grouped.set_index("LOB"))
        fig_BackedOut = px.bar(df_grouped, x="LOB", y="Count",text="Count", barmode="group",color_discrete_sequence = ['#EF553B']*len(df_grouped))
        st.plotly_chart(fig_BackedOut)

        st.subheader(":brain: Deep Insights - Backed Out CRs :brain:")
        st.write(df_BackedOut[mask])
    #****************End of a Backed Out section*************************************
if selected == "Unsuccessful":
    #Status: Unsuccessful
    df_Unsuccessful = pd.read_excel(excel_file,
                       sheet_name=sheet_name,
                       usecols='A:I',
                       header=0)

    #Filter - Jan Data

    column_name_month_Unsuccessful = "Month"
    filter_value_month_Unsuccessful = "September"
    column_name_status_Unsuccessful = "Status"
    filter_value_status_Unsuccessful = "Unsuccessful"
    df_Unsuccessful = df_Unsuccessful[df_Unsuccessful[column_name_month_Unsuccessful] == filter_value_month_Unsuccessful]
    df_Unsuccessful = df_Unsuccessful[df_Unsuccessful[column_name_status_Unsuccessful] == filter_value_status_Unsuccessful]

    # --- STREAMLIT SELECTION
    lob = df_Unsuccessful['LOB'].unique().tolist()
    status = df_Unsuccessful['Status'].unique().tolist()

    if not lob:
        st.image(image_no_record, use_column_width=True)
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
        st.subheader(":bar_chart: Visual Insights - Unsuccessful CRs :bar_chart:")
        #bar_chart = px.bar(df_grouped,
                           #x='LOB',
                           #y='Count',
                           #text='Count',
                           #color_discrete_sequence = ['#F63366']*len(df_grouped),
                           #template= 'plotly_white')


        #st.bar_chart(df_grouped.set_index("LOB"))
        fig_Unsuccessful = px.bar(df_grouped, x="LOB", y="Count",text="Count", barmode="group",color_discrete_sequence = ['#F6222E']*len(df_grouped))
        st.plotly_chart(fig_Unsuccessful)

        st.subheader(":brain: Deep Insights - Unsuccessful CRs :brain:")
        st.write(df_Unsuccessful[mask])

    #**************End of Unsuccessful section************

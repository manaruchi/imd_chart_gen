import streamlit as st
from datetime import datetime
import time
from generate_chart_new import *

st.set_page_config(
    page_title="IMD Charts Generator",
    page_icon="🧊",
    menu_items={
        'About': "*IMD Charts Generator*.. Made by Manaruchi Mohapatra"
    }
)

st.header("IMD Charts Generator")
st.text("By *Manaruchi Mohapatra*")
st.divider()
zv = st.radio(
    'Based on: ',
    ('00UTC', '06UTC', '12UTC', '18UTC'))
days = st.slider('Number of days: ', 1, 10, 3)

based_on_date = st.date_input(
    "Based on Date: ",
    datetime.today().date())

start_date = st.date_input(
    "Start date of Chart: ",
    datetime.today().date())

if st.button('Generate Chart'):
    images_for_pdf = []
    my_bar = st.progress(0, "Operation in progress. Please Wait...")

    z, n, dt_prt_list = generate_list_z(zv, days, start_date)

    out = 0
    for i in range(len(z)):
        links = ["https://nwp.imd.gov.in/gfs/{}/{}hgfs_925wind.gif".format(zv[:2],z[i]),
                "https://nwp.imd.gov.in/gfs/{}/{}hgfs_850wind.gif".format(zv[:2],z[i]),
                "https://nwp.imd.gov.in/gfs/{}/{}hgfs_700wind.gif".format(zv[:2],z[i]),
                "https://nwp.imd.gov.in/gfs/{}/{}hgfs_600wind.gif".format(zv[:2],z[i])]


        page_title = "UPPER AIR CHART OF {}Z {} (BASED ON {}Z {})".format(n[i], dt_prt_list[i], zv[:2], mg(based_on_date))


        images_for_pdf.append(make_page(links, page_title))
        my_bar.progress(int((i/len(z)*100)), text="Operation in progress. Please Wait...")

    my_bar.progress(100, text = "Operation Completed...")
    images_for_pdf[0].save(
            "Charts.pdf", "PDF" , save_all=True, append_images=images_for_pdf[1:]
        )
    with open("Charts.pdf", "rb") as file:
        btn = st.download_button(
                label="Download Chart",
                data=file,
                file_name="Chart_{}_{}.pdf".format(zv,mgu(based_on_date))
              )



st.divider()

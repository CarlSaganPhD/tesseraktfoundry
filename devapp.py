# Import libraries
import streamlit as st
import pandas as pd
from airtable import Airtable
import os

#---------------------------------
# Tesserakt Foundry Panel
#---------------------------------
#
# Creator: Ryan Dinubilo
# Creation Date: 1/16/2023
# Current Version: 1.01
#
#
# Changelog ---------------------
# Revision Dates:
# Version 1.01 - 1/16/2023
# - Added airtable support
#
#
#

def main():

    airtable = Airtable(os.environ.get('AIRTABLEAPP'), 'Companies', os.environ.get('AIRTABLEKEY')) 

    allRecords = airtable.get_all()

    image = st.sidebar.markdown("![Alt Text](https://i.imgur.com/dN0puJM.png)")     #Logo Image
    sidebar = st.sidebar.title("Tesserakt Foundry")                            #Title Text
    sidebarselect = st.sidebar.radio("Select a Tool", options=["Upload","View Inventory", "Analytics"])    #Page Select

    #Page Definitions
    #
    #Upload Inventory Page
    if sidebarselect == "Upload":

        st.write("Upload")

        if st.button("Test"):
            st.write("allRecords")

    elif sidebarselect == "View Inventory":
        st.write("View Inventory")

    elif sidebarselect == "Analytics":
        st.write("Analytics")
        
if __name__ == "__main__":
    main()
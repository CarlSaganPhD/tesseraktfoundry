# Import libraries
import streamlit as st
import pandas as pd

#---------------------------------
# Tesserakt Foundry Panel
#---------------------------------
#
# Creator: Ryan Dinubilo
# Creation Date: 1/16/2023
# Current Version: 1.00
#
#
# Changelog ---------------------
# Revision Dates:
# Version 1.12 - 3/12/2021
# See changelog doc
#
#
#

def main():

    image = st.sidebar.markdown("![Alt Text](https://i.imgur.com/dN0puJM.png)")     #Logo Image
    sidebar = st.sidebar.title("Tesserakt Foundry")                            #Title Text
    sidebarselect = st.sidebar.radio("Select a Tool", options=["Upload","View Inventory", "Analytics"])    #Page Select

    #Page Definitions
    #
    #Upload Inventory Page
    if sidebarselect == "Upload":

        st.write("Upload")

    elif sidebarselect == "View Inventory":
        st.write("View Inventory")

    elif sidebarselect == "Analytics":
        st.write("Analytics")
        
if __name__ == "__main__":
    main()
def about():
    st.title("About")
    st.markdown("""
    A large part of my role within the Oxford Epilepsy Group involved overseeing deployment of a
    screening tool in low-resource settings.
    As part of this, I created a dashboard to monitor the data collected by the tool.
    The dashboard involved data cleaning, demographics, and quality control both from the
    perspective of data quality and from a personnel management perspective.
    For data privacy reasons, I cannot share the dashboard itself, but I have replicated the
    functionality here, using data from Kaggle which I have augmented with some simulated
    data of my own.
    """)


def project_1():
    st.title("Project 1: Dashboard")
    tabs = st.tabs(["About", "Demographics & Summary Statistics", "Quality Control"])
    with tabs[0]:
        about()
    with tabs[1]:
        # plaveholder for demographics
        st.markdown("Demographics tab")
    with tabs[2]:
        qc_tabs = st.tabs(["ID checks", "Personnel Management", "Time monitoring"])


if __name__ == "__main__":
    import streamlit as st
    import pandas as pd
    import numpy as np

    # Load the data

    # Display the data

    # Display the dashboard
    project_1()

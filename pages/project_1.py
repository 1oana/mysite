import visualisations as viz


def load_data(filename):
    # Load the data from a CSV file
    data = pd.read_csv(filename)
    return data


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
    data of my own. I added assessor names, survey dates and lengths, and fabricated a set of 
    'expected' IDs as well as changing one ID such that there was a duplicate (X to X).

    The data is not real, but the dashboard is a close approximation of the one I created for
    the project. I have attempted to exlain the purpose of each section, and how it would be used in
    practice.

    The data is from the [Mastocytosis Patient Survey](kaggle.com/datasets/benroshan/mastocytosis-patient-survey)
    and contains survey data from patients with mastocytosis, a rare disease that affects the
    mast cells in the body. The survey includes questions about symptoms, demographics, and
    comorbidities.
    """)


def demogs(data):
    st.subheader("Demographics & Statistics")
    # st.write(data[['Age']].describe())

    demogs_tabs = st.tabs(["Demographics", "Diagnoses", "Symptoms"])
    with demogs_tabs[0]:
        gender_expander = st.expander("Gender")
        with gender_expander:
            viz.display_pie_chart(
                data,
                column_to_count="Gender",
                column_counts="Gender Count",
            )

        age_expander = st.expander("Age")
        with age_expander:
            viz.display_histogram(
                data,
                column_to_count="Age",
                column_counts="Age Count",
            )

        country_expander = st.expander("Country")
        with country_expander:
            viz.display_pie_chart(
                data,
                column_to_count="Country",
                column_counts="Country Count",
            )

    with demogs_tabs[1]:
        st.write("Placeholder for Diagnoses: by day, cumulative plot")

    with demogs_tabs[2]:
        st.write("Placeholder for Symptoms")


def qc(data):
    st.subheader("Quality Control")
    st.markdown("""This section describes quality control. It
    """)
    qc_tabs = st.tabs(["ID checks", "Personnel Management", "Time monitoring"])
    with qc_tabs[0]:
        st.write("Placeholder for ID checks")

        unexpected_ids_expander = st.expander("Unexpected IDs")
        with unexpected_ids_expander:
            st.write("Placeholder for unexpected IDs")

        duplicate_ids_expander = st.expander("Duplicate IDs")
        with duplicate_ids_expander:
            st.write("Placeholder for duplicate IDs")

    with qc_tabs[1]:
        st.write("Placeholder for Personnel Management")

        hcw_survey_expander = st.expander("Surveys by person")
        with hcw_survey_expander:
            st.write("Placeholder for personnel management")

        hcw_day_expander = st.expander("Surveys by person/day")
        with hcw_day_expander:
            st.write("Placeholder for personnel management")

        hcw_diag_expander = st.expander("Diagnosis ratio")
        with hcw_diag_expander:
            st.write("Placeholder for personnel management")

    with qc_tabs[2]:
        st.write("Placeholder for Time monitoring")


def modelling(data):
    st.subheader("Modelling")
    st.markdown("""Would be nice to do some modelling. We could
    use the data to build a predictive model that could become an at-home screening app.
    We are really limited by the size of the dataset, so it's an interesting exercise!
    """)
    # Add more modelling checks here


def project_1():
    st.title("Project 1: Dashboard")
    tabs = st.tabs(
        ["About", "Demographics & Statistics", "Quality Control", "Modelling"]
    )
    with tabs[0]:
        about()
    with tabs[1]:
        demogs(data)
    with tabs[2]:
        qc(data)
    with tabs[3]:
        modelling(data)


if __name__ == "__main__":
    import streamlit as st
    import pandas as pd
    import details as dt

    # Load the data
    data = load_data(dt.MASTO_FILENAME)

    # Display the data

    # Display the dashboard
    project_1()

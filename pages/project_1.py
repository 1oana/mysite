import visualisations as viz
import details as dt


def load_data(filename):
    # Load the data from a CSV file
    data = pd.read_csv(filename)
    data[dt.DATE_COL] = pd.to_datetime(data[dt.DATE_COL], format=dt.DATE_COL_FORMAT, errors="coerce")
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
    on Kaggle and contains survey data from patients with mastocytosis, a rare disease that affects
    the mast cells in the body. The survey includes questions about symptoms, demographics, and
    comorbidities.
    """)

    # st.markdown(f"Available columns: {data.columns.tolist()}")

    st.dataframe(data[dt.MASTO_ANON_COLS].head(10))


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
            with st.container():
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
        viz.display_cumulative_plot(
            data,
            column_to_cuml="Date",
            column_counts="Diagnosis Count",
            colour_col="Mastocytosis_Diagnosis_Status",
        )

    with demogs_tabs[2]:
        st.write("Placeholder for Symptoms")


def qc(data):
    st.subheader("Quality Control")
    st.markdown("""This section describes quality control. The specific checks were developed
    over time in collaboration with the fieldworkers administering the screening tool.
    """)
    st.warning("""
        *This section is based on data I fabricated (which may be clear from the names).*
        """)
    qc_tabs = st.tabs(["ID checks", "Personnel Management", "Time monitoring"])
    with qc_tabs[0]:
        st.write("""During this deployment, each record was associated with a unique ID.
        This ID was linked to the medical records of the patient, and was used to
        link to clinical outcomes and other data.
        It was therefore crucial that the IDs were unique and correctly assigned, otherwise
        the data would be unusable. However, we were unable to allow IDs to be input in any
        other way than manual, introducing the possbility of human error.
        This section describes the checks that were performed to ensure the quality of the 
        IDs in the dataset. It was necessary to provide minimal information to the site leads
        such that errors could be corrected without compromising participant anonymity.
        """)

        unexpected_ids_expander = st.expander("Unexpected IDs")
        with unexpected_ids_expander:
            st.write("""
        Prior to rollout, we asked the study sites to provide a list of IDs corresponding to
        the participants they expected to screen. We would flag any outliers with the necessary 
        information for correction. Below we show IDs that were not 'expected': I intentionally
        added one that totally broke with the convention of the others.
            """)
            # print dataframe
            st.dataframe(
                data.loc[~data.Participant_ID.isin(dt.MASTO_IDS), dt.MASTO_ANON_COLS]
            )

        duplicate_ids_expander = st.expander("Duplicate IDs")
        with duplicate_ids_expander:
            st.write("""
            Here we flag duplicated IDs. This may have been caused in error due to a connection issue,
            or due to human error.
                     """)
            duplicated_ids = sorted(data.Participant_ID)
            duplicated_ids = [
                x for n, x in enumerate(duplicated_ids) if x in duplicated_ids[:n]
            ]
            if len(duplicated_ids) > 0:
                st.dataframe(
                    data.loc[
                        data.Participant_ID.isin(duplicated_ids), dt.MASTO_ANON_COLS
                    ]
                )
            else:
                st.write("No duplicated IDs to show")

    with qc_tabs[1]:
        st.write("""
        This section was implemented because we almost exclusively liaised with managers
        and site leads, rather than the fieldworkers themselves. This monitoring enabled
        them to monitor the performance of their fieldworkers, and to identify any issues
        which we could not as we lacked the context to do so.
        """)

        hcw_survey_expander = st.expander("Surveys by person")
        with hcw_survey_expander:
            viz.display_bar_chart(
                data,
                column_to_count="HCW",
                column_counts="Survey Count",
            )

        hcw_day_expander = st.expander("Surveys by person/day")
        with hcw_day_expander:
            viz.display_bar_plot_with_colour(
                data,
                column_to_count="Date",
                column_counts="Survey Date",
                color_col="HCW",
            )

        hcw_diag_expander = st.expander("Diagnosis ratio")
        with hcw_diag_expander:
            viz.display_bar_plot_with_colour(
                data,
                column_to_count="Mastocytosis_Diagnosis_Status",
                column_counts="Diagnosis Ratio",
                color_col="HCW",
            )
            viz.display_bar_plot_with_colour(
                data,
                column_to_count="HCW",
                column_counts="Diagnosis Ratio",
                color_col="Mastocytosis_Diagnosis_Status",
            )

    with qc_tabs[2]:
        st.write("""Our app was designed to be very user-friendly with a simple questionnaire. 
        However, we could monitor the time taken to complete a survey
        once it was uploaded. This was useful to identify any issues with the app, or with the
        fieldworkers themselves. We could also use this to identify any issues with the data
        collection process, such as if the fieldworkers were not collecting the data correctly.
        """)


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

# details
MASTO_FILENAME = "data/mastocytosis_patient_survey.csv"

MASTO_IDS = [i for i in range(1, 51)]

MASTO_ANON_COLS = [
    "Participant_ID",
    "HCW",
    "Date",
    "Age",
    "Gender",
    "Country",
    "Mastocytosis_Diagnosis_Status",
]

DATE_COL = "Date"
DATE_COL_FORMAT = "%d/%m/%Y"

MASTO_INFO_DICT = {
    "categorical_cols": [
        "Gender",
        "Country",
        "Mastocytosis_Diagnosis_Status",
        "Mastocytosis_Type",
        "Anaphylactic_Reaction_History",
        "Hospitalization_History",
        "Specialist_Consultation_Status",
        "HCW",
    ],
    "numerical_cols": [
        "Age",
        "Quality_of_Life_Impact_Score",
        "Assessment_length"
    ],
    "list_cols": [
        "Primary_Symptoms",
        "Symptom_Triggers",
        "Symptom_Frequency",
        "Current_Treatments",
        "Treatment_Effectiveness",
    ],
    "id_col": "Participant_ID",
    "date_cols": ["Date"],
    "date_format": "%Y-%m-%d %H:%M:%S",
}

import os
import streamlit as st
import requests
import pandas as pd


# ============================================================
# CONFIGURATION
# ============================================================

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
)

OCCUPATIONS = [
    "retired",
    "freelancer",
    "student",
    "government_job",
    "business_owner",
    "unemployed",
    "private_job"
]

REQUIRED_COLUMNS = [
    "age",
    "weight",
    "height",
    "income_lpa",
    "smoker",
    "city",
    "occupation"
]


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 0;
    }

    .subtitle {
        font-size: 18px;
        color: #6b7280;
        margin-top: 5px;
        margin-bottom: 25px;
    }

    .prediction-card {
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        text-align: center;
        margin-bottom: 20px;
    }

    .prediction-value {
        font-size: 32px;
        font-weight: 700;
        margin-top: 10px;
    }

    .low {
        color: #16a34a;
    }

    .medium {
        color: #ca8a04;
    }

    .high {
        color: #dc2626;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ API")

    st.write("FastAPI Backend")

    try:

        health_response = requests.get(
            f"{API_URL}/health",
            timeout=3
        )

        if health_response.status_code == 200:

            health = health_response.json()

            st.success("🟢 API Online")

            st.caption(
                f"Model Version: {health.get('version', 'N/A')}"
            )

            st.caption(
                f"Model Loaded: "
                f"{'Yes' if health.get('model_loaded') else 'No'}"
            )

        else:

            st.error("🔴 API Error")

    except requests.exceptions.RequestException:

        st.error("🔴 API Offline")

        st.caption(
            "Start FastAPI with:"
        )

        st.code(
            "uvicorn app:app --reload",
            language="bash"
        )

    st.divider()

    st.header("📚 API Endpoints")

    st.write("`GET /health`")
    st.write("`POST /predict`")
    st.write("`POST /predict/batch`")

    st.divider()

    st.caption(
        "Insurance Premium Prediction API"
    )

    st.caption(
        "FastAPI + Streamlit + Machine Learning"
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<p class="main-title">🏥 Insurance Premium Predictor</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">'
    'Predict insurance premium categories using a FastAPI-powered '
    'machine learning model.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# TABS
# ============================================================

single_tab, batch_tab = st.tabs(
    [
        "👤 Single Prediction",
        "📁 Batch Prediction"
    ]
)


# ============================================================
# SINGLE PREDICTION
# ============================================================

with single_tab:

    st.subheader("👤 User Information")

    st.caption(
        "Enter the user's details to generate an insurance "
        "premium prediction."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=119,
            value=30
        )

    with col2:

        weight = st.number_input(
            "Weight (kg)",
            min_value=1.0,
            value=70.0,
            step=0.1
        )

    with col3:

        height = st.number_input(
            "Height (m)",
            min_value=0.1,
            max_value=2.49,
            value=1.75,
            step=0.01
        )

    col4, col5, col6 = st.columns(3)

    with col4:

        income_lpa = st.number_input(
            "Annual Income (LPA)",
            min_value=0.1,
            value=8.5,
            step=0.1
        )

    with col5:

        smoker = st.selectbox(
            "Smoker",
            [False, True],
            format_func=lambda x: "Yes" if x else "No"
        )

    with col6:

        city = st.text_input(
            "City",
            value="Delhi"
        )

    occupation = st.selectbox(
        "Occupation",
        OCCUPATIONS
    )

    st.write("")

    predict_button = st.button(
        "🔮 Predict Premium",
        use_container_width=True,
        type="primary"
    )

    if predict_button:

        payload = {
            "age": age,
            "weight": weight,
            "height": height,
            "income_lpa": income_lpa,
            "smoker": smoker,
            "city": city,
            "occupation": occupation
        }

        try:

            with st.spinner(
                "Analyzing user information..."
            ):

                response = requests.post(
                    f"{API_URL}/predict",
                    json=payload,
                    timeout=10
                )

            if response.status_code == 200:

                result = response.json()

                st.success(
                    "Prediction completed successfully!"
                )

                st.divider()

                # ----------------------------------------
                # RESULT
                # ----------------------------------------

                st.subheader("📊 Prediction Result")

                category = result[
                    "predicted_category"
                ]

                confidence = result[
                    "confidence"
                ]

                category_class = category.lower()

                r1, r2 = st.columns(2)

                with r1:

                    st.markdown(
                        f"""
                        <div class="prediction-card">

                        <div>Predicted Premium Category</div>

                        <div class="prediction-value {category_class}">
                        {category.upper()}
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with r2:

                    st.markdown(
                        f"""
                        <div class="prediction-card">

                        <div>Model Confidence</div>

                        <div class="prediction-value">
                        {confidence * 100:.2f}%
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                # ----------------------------------------
                # RISK PROFILE
                # ----------------------------------------

                st.subheader("🧬 Risk Profile")

                risk = result[
                    "risk_profile"
                ]

                r1, r2, r3, r4 = st.columns(4)

                with r1:
                    st.metric(
                        "BMI",
                        risk["bmi"]
                    )

                with r2:
                    st.metric(
                        "Age Group",
                        risk["age_group"]
                    )

                with r3:
                    st.metric(
                        "Lifestyle Risk",
                        risk["lifestyle_risk"]
                    )

                with r4:
                    st.metric(
                        "City Tier",
                        risk["city_tier"]
                    )

                # ----------------------------------------
                # PROBABILITIES
                # ----------------------------------------

                st.divider()

                st.subheader(
                    "📈 Prediction Probability"
                )

                probabilities = result[
                    "class_probabilities"
                ]

                probability_df = pd.DataFrame(
                    {
                        "Category": list(
                            probabilities.keys()
                        ),
                        "Probability (%)": [
                            value * 100
                            for value in probabilities.values()
                        ]
                    }
                )

                st.bar_chart(
                    probability_df,
                    x="Category",
                    y="Probability (%)"
                )

                # ----------------------------------------
                # MODEL INFO
                # ----------------------------------------

                st.divider()

                model_info = result["model"]

                m1, m2 = st.columns(2)

                with m1:

                    st.caption("Model")

                    st.write(
                        model_info["name"]
                    )

                with m2:

                    st.caption("Version")

                    st.write(
                        model_info["version"]
                    )

            else:

                st.error(
                    f"API Error "
                    f"({response.status_code})"
                )

                st.code(
                    response.text
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Could not connect to FastAPI."
            )

        except requests.exceptions.Timeout:

            st.error(
                "⏱️ API request timed out."
            )

        except Exception as e:

            st.error(
                f"Unexpected error: {str(e)}"
            )


# ============================================================
# BATCH PREDICTION
# ============================================================

with batch_tab:

    st.subheader("📁 Batch Prediction")

    st.write(
        "Upload a CSV containing multiple users "
        "and generate predictions in one request."
    )

    # ----------------------------------------
    # CSV TEMPLATE
    # ----------------------------------------

    template_df = pd.DataFrame(
        [
            {
                "age": 30,
                "weight": 70,
                "height": 1.75,
                "income_lpa": 8.5,
                "smoker": False,
                "city": "Delhi",
                "occupation": "private_job"
            }
        ]
    )

    template_csv = template_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "📄 Download CSV Template",
        data=template_csv,
        file_name="insurance_prediction_template.csv",
        mime="text/csv"
    )

    st.write("")

    uploaded_file = st.file_uploader(
        "Upload CSV file",
        type=["csv"]
    )

    if uploaded_file:

        try:

            df = pd.read_csv(
                uploaded_file
            )

            st.subheader(
                "📋 Uploaded Data"
            )

            st.dataframe(
                df,
                use_container_width=True
            )

            missing_columns = [
                column
                for column in REQUIRED_COLUMNS
                if column not in df.columns
            ]

            if missing_columns:

                st.error(
                    "Missing required columns: "
                    + ", ".join(
                        missing_columns
                    )
                )

            elif df.empty:

                st.warning(
                    "The uploaded CSV is empty."
                )

            else:

                st.success(
                    f"{len(df)} user(s) ready."
                )

                if st.button(
                    "🚀 Run Batch Prediction",
                    use_container_width=True,
                    type="primary"
                ):

                    users = df[
                        REQUIRED_COLUMNS
                    ].to_dict(
                        orient="records"
                    )

                    try:

                        with st.spinner(
                            "Running predictions..."
                        ):

                            response = requests.post(
                                f"{API_URL}/predict/batch",
                                json={
                                    "users": users
                                },
                                timeout=60
                            )

                        if response.status_code == 200:

                            result = response.json()

                            st.success(
                                f"Successfully predicted "
                                f"{result['total_predictions']} "
                                f"user(s)."
                            )

                            output_rows = []

                            for original, prediction in zip(
                                users,
                                result["results"]
                            ):

                                risk = prediction[
                                    "risk_profile"
                                ]

                                output_rows.append(
                                    {
                                        "Age": original["age"],
                                        "City": original["city"],
                                        "Occupation": original[
                                            "occupation"
                                        ],
                                        "BMI": risk["bmi"],
                                        "Age Group": risk[
                                            "age_group"
                                        ],
                                        "Lifestyle Risk": risk[
                                            "lifestyle_risk"
                                        ],
                                        "City Tier": risk[
                                            "city_tier"
                                        ],
                                        "Prediction": prediction[
                                            "predicted_category"
                                        ],
                                        "Confidence (%)": round(
                                            prediction[
                                                "confidence"
                                            ] * 100,
                                            2
                                        )
                                    }
                                )

                            results_df = pd.DataFrame(
                                output_rows
                            )

                            st.subheader(
                                "📊 Prediction Results"
                            )

                            st.dataframe(
                                results_df,
                                use_container_width=True
                            )

                            # --------------------------------
                            # SUMMARY
                            # --------------------------------

                            st.subheader(
                                "📈 Prediction Summary"
                            )

                            summary = (
                                results_df[
                                    "Prediction"
                                ]
                                .value_counts()
                                .reset_index()
                            )

                            summary.columns = [
                                "Category",
                                "Count"
                            ]

                            st.bar_chart(
                                summary,
                                x="Category",
                                y="Count"
                            )

                            # --------------------------------
                            # DOWNLOAD
                            # --------------------------------

                            result_csv = (
                                results_df
                                .to_csv(
                                    index=False
                                )
                                .encode("utf-8")
                            )

                            st.download_button(
                                "📥 Download Results CSV",
                                data=result_csv,
                                file_name=(
                                    "prediction_results.csv"
                                ),
                                mime="text/csv",
                                use_container_width=True
                            )

                        else:

                            st.error(
                                f"API Error "
                                f"({response.status_code})"
                            )

                            st.code(
                                response.text
                            )

                    except requests.exceptions.ConnectionError:

                        st.error(
                            "❌ Could not connect to FastAPI."
                        )

                    except requests.exceptions.Timeout:

                        st.error(
                            "⏱️ Batch prediction timed out."
                        )

                    except Exception as e:

                        st.error(
                            f"Unexpected error: {str(e)}"
                        )

        except Exception as e:

            st.error(
                f"Could not read CSV: {str(e)}"
            )
import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Page Configuration
st.set_page_config(
    page_title="Industrial Construction Fraud & COSO Study",
    page_icon="",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
    <style>
    .main-header {
        font-size: 24px;
        font-weight: 700;
        color: #1B365D;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 14px;
        color: #4A6B82;
        margin-bottom: 20px;
    }
    .section-card {
        background-color: #F4F7FA;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #1B365D;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://img.icons8.com/color/96/constructor.png", width=80)
st.sidebar.title("Study Overview")
st.sidebar.info(
    "**Research Focus:** Investigating occupational fraud and the operational effectiveness of internal controls (COSO 2013) "
    "within Ghana’s industrial construction subsector.\n\n"
    "**Institution:** WorldQuant University\n"
    "**Principal Researcher:** Daniel Agyekum Amakye (ID: 1048136)"
)

st.sidebar.markdown("---")
st.sidebar.subheader(" Confidentiality Notice")
st.sidebar.write(
    "Participation is strictly voluntary. All responses are anonymized "
    "and used exclusively for academic research."
)

# Main Title
st.markdown('<p class="main-header">Industrial Construction Fraud & COSO Internal Control Study</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Semi-Structured Expert Interview Questionnaire (Streamlined 10-Question Instrument)</p>', unsafe_allow_html=True)

# Data storage CSV path
DATA_FILE = "survey_responses.csv"

# Informed Consent Check
consent = st.checkbox("I confirm that I am a construction professional with at least 3 years of experience, and I voluntarily consent to participate in this academic study under strict confidentiality.")

if not consent:
    st.warning("⚠️ Please check the consent box above to unlock and complete the interview questionnaire.")
else:
    with st.form("interview_form"):
        
        # ---------------------------------------------------------
        # SECTION A: CONTEXT & BACKGROUND
        # ---------------------------------------------------------
        st.markdown("### Part A: Participant & Firm Background")
        
        col1, col2 = st.columns(2)
        with col1:
            role = st.selectbox(
                "1. Functional Role *",
                ["Project Manager / Site Engineer", "Quantity Surveyor (QS)", "Finance Officer / Accountant", "Internal Auditor / Compliance Officer", "Other"]
            )
            other_role = st.text_input("If 'Other', please specify:") if role == "Other" else ""
            
        with col2:
            experience = st.number_input("2. Years of Professional Construction Experience *", min_value=1, max_value=40, value=8)

        firm_profile = st.selectbox(
            "3. Firm Ownership & Operational Scale *",
            [
                "Indigenous Industrial Contractor (Ghanaian-owned)",
                "Joint-Venture (JV) / International Contractor",
                "Large Corporate Industrial / Energy Contractor",
                "Medium-to-Small Indigenous Contractor"
            ]
        )
        
        project_types = st.text_input("4. Primary Industrial Construction Projects Handled (e.g., mining facilities, oil & gas tanks, power substations) *")

        st.markdown("---")
        
        # ---------------------------------------------------------
        # SECTION B: FRAUD REALITIES & COSO OPERATION
        # ---------------------------------------------------------
        st.markdown("### Part B: Fraud Realities & Internal Controls (COSO)")
        
        q_schemes = st.text_area(
            "5. Common Fraud Schemes & Project Lifecycle (RQ1) *",
            placeholder="What forms of occupational fraud (material substitution/short-delivery, inflated variations, ghost workers, kickbacks) are most common, and at which project stages do they occur?"
        )
        
        q_incident = st.text_area(
            "6. Real-World Incident / Control Breakdown (RQ1 / Critical Incident) *",
            placeholder="Can you walk through a specific situation you witnessed where an occupational fraud scheme or control breakdown occurred and bypassed existing checks?"
        )
        
        q_tone = st.text_area(
            "7. Tone & Culture - Control Environment (RQ2) *",
            placeholder="How would you describe senior management's commitment to ethics? Are screening, remuneration, and disciplinary actions fair and consistent?"
        )
        
        q_risk = st.text_area(
            "8. Risk Hotspots - Risk Assessment (RQ2) *",
            placeholder="Does your firm proactively identify fraud risks, or are controls tightened reactively? Which processes (procurement, site materials, subcontractor payments) are most exposed?"
        )
        
        q_activities = st.text_area(
            "9. Approvals & Safeguards - Control Activities (RQ2) *",
            placeholder="How effectively are approval limits, segregation of duties, and physical site controls enforced? How are variation orders verified before interim payments?"
        )
        
        q_info = st.text_area(
            "10. Reporting Channels - Information & Communication (RQ2) *",
            placeholder="If someone suspects fraud, how does information flow? Do staff trust and use reporting channels, or do issues surface via informal tips/audits?"
        )
        
        q_monitoring = st.text_area(
            "11. Audits & Checks - Monitoring Activities (RQ2) *",
            placeholder="How active is internal audit in regularly testing controls? Are proactive data-checks (duplicate invoices, anomalies) ever used?"
        )

        st.markdown("---")
        
        # ---------------------------------------------------------
        # SECTION C: CHALLENGES & HUMAN BEHAVIOR
        # ---------------------------------------------------------
        st.markdown("### Part C: Challenges, Rationalization & Culture (RQ3)")
        
        q_challenges = st.text_area(
            "12. Obstacles to Prevention & Detection (RQ3) *",
            placeholder="What are the biggest operational or organizational challenges in stopping fraud while a project is active rather than long after closeout?"
        )
        
        q_rationalization = st.text_area(
            "13. Rationalization & Cultural Norms (RQ3) *",
            placeholder="How do professionals on site justify smaller infractions (minor material theft, fuel inflation)? What actually stops people or discourages reporting?"
        )
        
        additional_comments = st.text_area("14. Any Additional Comments or Recommendations (Optional)")

        st.markdown("---")
        
        # Form Submission Button
        submitted = st.form_submit_button("Submit Interview Response 🚀")
        
        if submitted:
            if not project_types or not q_schemes or not q_incident:
                st.error("❌ Please complete all required core questions (Roles, Project Types, Schemes, and Incident) before submitting.")
            else:
                # Prepare data record
                response_data = {
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Role": role if role != "Other" else f"Other: {other_role}",
                    "Experience_Years": experience,
                    "Firm_Profile": firm_profile,
                    "Project_Types": project_types,
                    "Q_Schemes": q_schemes,
                    "Q_Incident": q_incident,
                    "Q_Tone": q_tone,
                    "Q_Risk": q_risk,
                    "Q_Activities": q_activities,
                    "Q_Info": q_info,
                    "Q_Monitoring": q_monitoring,
                    "Q_Challenges": q_challenges,
                    "Q_Rationalization": q_rationalization,
                    "Additional_Comments": additional_comments
                }
                
                df_new = pd.DataFrame([response_data])
                
                # Append to CSV
                if os.path.exists(DATA_FILE):
                    df_new.to_csv(DATA_FILE, mode='a', header=False, index=False)
                else:
                    df_new.to_csv(DATA_FILE, mode='w', header=True, index=False)
                    
                st.success(" Thank you! Your interview response has been successfully recorded and securely saved.")
                st.balloons()

# Admin Section in Expander for Researcher
with st.expander(" Researcher Admin Portal (Download Responses)"):
    st.write("View and download collected field responses for NVivo analysis.")
    if os.path.exists(DATA_FILE):
        df_existing = pd.read_csv(DATA_FILE)
        st.metric("Total Responses Collected", len(df_existing))
        st.dataframe(df_existing)
        
        csv_data = df_existing.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Responses as CSV (for NVivo / Excel)",
            data=csv_data,
            file_name=f"construction_fraud_responses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
        )
    else:
        st.info("No responses recorded yet. Submit a test response above to initialize the dataset.")
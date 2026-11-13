import streamlit as st
import pandas as pd
from datetime import datetime
import os

# ==========================================
# PAGE CONFIGURATION & ACADEMIC BRANDING
# ==========================================
st.set_page_config(
    page_title="Industrial Construction Fraud & COSO Study",
    page_icon="🏗️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom Styling for Persistent Question Layout
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
    .question-card {
        background-color: #F8FAFC;
        padding: 18px;
        border-radius: 8px;
        border-left: 5px solid #1B365D;
        margin-bottom: 15px;
        margin-top: 10px;
    }
    .question-title {
        font-weight: 600;
        color: #1B365D;
        margin-bottom: 8px;
        font-size: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR - STUDY OVERVIEW & NOTICE
# ==========================================
st.sidebar.image("https://img.icons8.com/color/96/constructor.png", width=80)
st.sidebar.title("Study Overview")
st.sidebar.info(
    "**Research Focus:** Investigating occupational fraud and the operational effectiveness of internal controls (COSO 2013) "
    "within Ghana’s industrial construction subsector.\n\n"
    "**Institution:** WorldQuant University\n"
    "**Principal Researcher:** Daniel Agyekum Amakye (ID: 1048136)"
)

st.sidebar.markdown("---")
st.sidebar.subheader("🔒 Confidentiality Notice")
st.sidebar.write(
    "Participation is strictly voluntary. All responses are anonymized "
    "and used exclusively for academic research."
)

# ==========================================
# MAIN HEADER
# ==========================================
st.markdown('<p class="main-header">Industrial Construction Fraud & COSO Internal Control Study</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Semi-Structured Expert Interview Questionnaire (Streamlined 10-Question Instrument)</p>', unsafe_allow_html=True)

# Data storage CSV path
DATA_FILE = "survey_responses.csv"

# Informed Consent Check
consent = st.checkbox("I confirm that I am a construction professional with at least 3 years of experience, and I voluntarily consent to participate in this academic study under strict confidentiality.")

if not consent:
    st.warning("⚠️ Please check the consent box above to unlock and complete the interview questionnaire.")
else:
    st.markdown("---")
    
    # ---------------------------------------------------------
    # SECTION A: CONTEXT & BACKGROUND
    # ---------------------------------------------------------
    st.markdown("### Part A: Participant & Firm Background")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="question-title">1. Functional Role *</p>', unsafe_allow_html=True)
        role = st.selectbox(
            "Functional Role selection",
            [
                "Select role...",
                "President, Association of Contractors",
                "Project Managers",
                "Quantity Surveyors",
                "Finance Officers",
                "Procurement officers",
                "Internal Auditors",
                "Other"
            ],
            label_visibility="collapsed"
        )
        other_role = st.text_input("If 'Other', please specify:", label_visibility="collapsed", placeholder="Specify role...") if role == "Other" else ""
        
    with col2:
        st.markdown('<p class="question-title">2. Years of Professional Experience *</p>', unsafe_allow_html=True)
        experience = st.number_input("Years of Professional Construction Experience", min_value=1, max_value=40, value=8, label_visibility="collapsed")

    st.markdown('<p class="question-title">3. Firm Ownership & Operational Scale *</p>', unsafe_allow_html=True)
    firm_profile = st.selectbox(
        "Firm Ownership selection",
        [
            "Indigenous Industrial Contractor (Ghanaian-owned)",
            "Joint-Venture (JV) / International Contractor",
            "Large Corporate Industrial / Energy Contractor",
            "Medium-to-Small Indigenous Contractor"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown('<p class="question-title">4. Primary Industrial Construction Projects Handled *</p>', unsafe_allow_html=True)
    project_types = st.text_input("Project Types input", placeholder="e.g., mining facilities, oil & gas tanks, power substations", label_visibility="collapsed")

    st.markdown("---")
    
    # ---------------------------------------------------------
    # SECTION B: FRAUD REALITIES & COSO OPERATION
    # ---------------------------------------------------------
    st.markdown("### Part B: Fraud Realities & Internal Controls (COSO)")
    
    st.markdown("""
    <div class="question-card">
        <div class="question-title">5. Common Fraud Schemes & Project Lifecycle (RQ1) *</div>
        <p style="color: #4A6B82; font-size: 13px; margin-bottom: 8px;">What forms of occupational fraud (material substitution/short-delivery, inflated variations, ghost workers, kickbacks) are most common, and at which project stages do they occur?</p>
    </div>
    """, unsafe_allow_html=True)
    q_schemes = st.text_area("Q5 input", placeholder="Enter your detailed observations here...", height=100, label_visibility="collapsed", key="q5")
    
    st.markdown("""
    <div class="question-card">
        <div class="question-title">6. Real-World Incident / Control Breakdown (RQ1 / Critical Incident) *</div>
        <p style="color: #4A6B82; font-size: 13px; margin-bottom: 8px;">Can you walk through a specific situation you witnessed where an occupational fraud scheme or control breakdown occurred and bypassed existing checks?</p>
    </div>
    """, unsafe_allow_html=True)
    q_incident = st.text_area("Q6 input", placeholder="Describe the incident or control failure...", height=100, label_visibility="collapsed", key="q6")
    
    st.markdown("""
    <div class="question-card">
        <div class="question-title">7. Tone & Culture - Control Environment (RQ2) *</div>
        <p style="color: #4A6B82; font-size: 13px; margin-bottom: 8px;">How would you describe senior management's commitment to ethics? Are screening, remuneration, and disciplinary actions fair and consistent?</p>
    </div>
    """, unsafe_allow_html=True)
    q_tone = st.text_area("Q7 input", placeholder="Share your perspective on leadership tone and culture...", height=100, label_visibility="collapsed", key="q7")
    
    st.markdown("""
    <div class="question-card">
        <div class="question-title">8. Risk Hotspots - Risk Assessment (RQ2) *</div>
        <p style="color: #4A6B82; font-size: 13px; margin-bottom: 8px;">Does your firm proactively identify fraud risks, or are controls tightened reactively? Which processes (procurement, site materials, subcontractor payments) are most exposed?</p>
    </div>
    """, unsafe_allow_html=True)
    q_risk = st.text_area("Q8 input", placeholder="Detail risk identification and vulnerable operational areas...", height=100, label_visibility="collapsed", key="q8")
    
    st.markdown("""
    <div class="question-card">
        <div class="question-title">9. Approvals & Safeguards - Control Activities (RQ2) *</div>
        <p style="color: #4A6B82; font-size: 13px; margin-bottom: 8px;">How effectively are approval limits, segregation of duties, and physical site controls enforced? How are variation orders verified before interim payments?</p>
    </div>
    """, unsafe_allow_html=True)
    q_activities = st.text_area("Q9 input", placeholder="Discuss control enforcement and approval safeguards...", height=100, label_visibility="collapsed", key="q9")
    
    st.markdown("""
    <div class="question-card">
        <div class="question-title">10. Reporting Channels - Information & Communication (RQ2) *</div>
        <p style="color: #4A6B82; font-size: 13px; margin-bottom: 8px;">If someone suspects fraud, how does information flow? Do staff trust and use reporting channels, or do issues surface via informal tips/audits?</p>
    </div>
    """, unsafe_allow_html=True)
    q_info = st.text_area("Q10 input", placeholder="Describe whistleblowing and reporting channels...", height=100, label_visibility="collapsed", key="q10")
    
    st.markdown("""
    <div class="question-card">
        <div class="question-title">11. Audits & Checks - Monitoring Activities (RQ2) *</div>
        <p style="color: #4A6B82; font-size: 13px; margin-bottom: 8px;">How active is internal audit in regularly testing controls? Are proactive data-checks (duplicate invoices, anomalies) ever used?</p>
    </div>
    """, unsafe_allow_html=True)
    q_monitoring = st.text_area("Q11 input", placeholder="Describe internal audit effectiveness and data checks...", height=100, label_visibility="collapsed", key="q11")

    st.markdown("---")
    
    # ---------------------------------------------------------
    # SECTION C: CHALLENGES & HUMAN BEHAVIOR
    # ---------------------------------------------------------
    st.markdown("### Part C: Challenges, Rationalization & Culture (RQ3)")
    
    st.markdown("""
    <div class="question-card">
        <div class="question-title">12. Obstacles to Prevention & Detection (RQ3) *</div>
        <p style="color: #4A6B82; font-size: 13px; margin-bottom: 8px;">What are the biggest operational or organizational challenges in stopping fraud while a project is active rather than long after closeout?</p>
    </div>
    """, unsafe_allow_html=True)
    q_challenges = st.text_area("Q12 input", placeholder="Identify primary operational obstacles...", height=100, label_visibility="collapsed", key="q12")
    
    st.markdown("""
    <div class="question-card">
        <div class="question-title">13. Rationalization & Cultural Norms (RQ3) *</div>
        <p style="color: #4A6B82; font-size: 13px; margin-bottom: 8px;">How do professionals on site justify smaller infractions (minor material theft, fuel inflation)? What actually stops people or discourages reporting?</p>
    </div>
    """, unsafe_allow_html=True)
    q_rationalization = st.text_area("Q13 input", placeholder="Explain behavioral justifications and cultural norms...", height=100, label_visibility="collapsed", key="q13")
    
    st.markdown("""
    <div class="question-card">
        <div class="question-title">14. Additional Comments or Recommendations (Optional)</div>
        <p style="color: #4A6B82; font-size: 13px; margin-bottom: 8px;">Any final recommendations for strengthening internal controls in Ghana's industrial construction sector?</p>
    </div>
    """, unsafe_allow_html=True)
    additional_comments = st.text_area("Q14 input", placeholder="Optional final remarks...", height=100, label_visibility="collapsed", key="q14")

    st.markdown("---")
    
    # Submission Button with Validation Check
    if st.button("Submit Interview Response 🚀", type="primary"):
        if role == "Select role..." or not project_types or not q_schemes or not q_incident:
            st.error("❌ Please select your Functional Role and complete all required core fields before submitting.")
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
                
            st.success("✅ Thank you! Your interview response has been successfully recorded and securely saved.")
            st.balloons()

# ==========================================
# RESEARCHER ADMIN PORTAL
# ==========================================
st.markdown("---")
with st.expander("🔐 Researcher Admin Portal (Download Responses)"):
    st.write("View and download collected field responses for NVivo analysis.")
    if os.path.exists(DATA_FILE):
        df_existing = pd.read_csv(DATA_FILE)
        st.metric("Total Responses Collected", len(df_existing))
        st.dataframe(df_existing, use_container_width=True)
        
        csv_data = df_existing.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Responses as CSV (for NVivo / Excel)",
            data=csv_data,
            file_name=f"construction_fraud_responses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
        )
    else:
        st.info("No responses recorded yet. Submit a test response above to initialize the dataset.")
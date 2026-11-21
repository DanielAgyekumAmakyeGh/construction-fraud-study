import streamlit as st
import pandas as pd
from datetime import datetime
import os

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Understanding Occupational Fraud in the Industrial Construction Subsector of Ghana",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="expanded"
)

# ============================================================
# ADMIN PASSWORD
# ============================================================
ADMIN_PASSWORD = "coso2026"

# ============================================================
# CUSTOM STYLING
# ============================================================
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
    .rq-tag {
        display: inline-block;
        background-color: #E8EEF4;
        color: #1B365D;
        font-size: 11px;
        font-weight: 600;
        padding: 2px 8px;
        border-radius: 10px;
        margin-left: 8px;
    }
    .probe-text {
        font-size: 12px;
        color: #6B7C8E;
        font-style: italic;
        margin-top: -8px;
        margin-bottom: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================
st.sidebar.title("Study Overview")
st.sidebar.info(
    "**Research Topic:** Understanding Occupational Fraud in the Industrial "
    "Construction Subsector of Ghana.\n\n"
    "**Researcher:** Simon Kwame Buaba (Master's Student)\n"
    "**Index Number:** 22428938\n"
    "**Institution:** University of Ghana Business School\n"
    "**Analytical Framework:** COSO Internal Control–Integrated Framework (2013)"
)

st.sidebar.markdown("---")
st.sidebar.subheader("Confidentiality Notice")
st.sidebar.write(
    "Participation is strictly voluntary. All responses are anonymised "
    "and used exclusively for academic research. You may decline any question."
)

st.sidebar.markdown("---")
st.sidebar.subheader("Instrument Structure")
st.sidebar.write(
    "**Section A** — Participant background (Q1–Q2)\n\n"
    "**Section B** — Forms of occupational fraud (Q3–Q6)\n\n"
    "**Section C** — Operation of the five COSO components (Q7–Q15)\n\n"
    "**Section D** — Challenges in prevention, detection and response (Q16–Q17)\n\n"
    "**Closing prompts** — Rationalisation and control effectiveness (P1–P2)"
)

# ============================================================
# MAIN TITLE
# ============================================================
st.markdown('<p class="main-header">Understanding Occupational Fraud in the Industrial Construction Subsector of Ghana</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Semi-Structured Expert Interview — COSO Internal Control–Integrated Framework (2013) | 17 Core Questions + 2 Optional Prompts</p>', unsafe_allow_html=True)

# ============================================================
# DATA STORAGE
# ============================================================
DATA_FILE = "interview_responses.csv"

# ============================================================
# INFORMED CONSENT
# ============================================================
consent = st.checkbox(
    "I confirm that I am a construction professional with at least 3 years of experience, "
    "and I voluntarily consent to participate in this academic study under strict confidentiality. "
    "I understand that I may decline any question, especially Q6 (incidence probe) and Q17 (non-sanctioning)."
)

if not consent:
    st.warning("Please check the consent box above to unlock and complete the interview questionnaire.")
else:
    with st.form("interview_form"):

        # ---------------------------------------------------------
        # SECTION A
        # ---------------------------------------------------------
        st.markdown("---")
        st.markdown("## Section A: Background of the Participant")

        st.markdown("**Q1. Please describe your current role and responsibilities, how long you have worked in construction and with your current firm, and what types of industrial construction projects you have worked on in the last five years, and in what capacity.** <span class='rq-tag'>Background</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: Which of these projects was the most recent? What was your specific role on it?</p>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            role = st.selectbox(
                "Functional role",
                [
                    "CEO, Ghana Chamber of Construction Industry",
                    "Project Manager",
                    "Site Supervisor",
                    "Civil/Structure Engineer",
                    "Quantity Surveyor (QS)",
                    "Finance Officer / Accountant",
                    "Internal Auditor",
                    "External Auditor",
                    "Procurement Officer",
                    "Director / Senior Management",
                    "Head of Security",
                    "Other"
                ],
                index=None,
                placeholder="Select your role...",
                key="q1_role"
            )
            other_role = ""
            if role == "Other":
                other_role = st.text_input("If 'Other', please specify:", key="q1_other_role")
        with col2:
            experience_total = st.number_input(
                "Years of professional construction experience",
                min_value=1, max_value=50, value=8, key="q1_exp_total"
            )
            experience_firm = st.number_input(
                "Years with current firm",
                min_value=1, max_value=50, value=3, key="q1_exp_firm"
            )
            if experience_firm > experience_total:
                st.caption("Note: Years with current firm exceed total years in construction — please verify.")

        project_types = st.multiselect(
            "Types of industrial construction projects worked on in the last five years",
            [
                "Mining facilities",
                "Oil and gas installations",
                "Power-generation plants",
                "Manufacturing / process plants",
                "Other industrial infrastructure"
            ],
            key="q1_project_types"
        )

        st.markdown("**Q2. How would you describe your firm's size and ownership — indigenous or foreign-owned, single-director or corporate, and approximate staff strength?** <span class='rq-tag'>Background</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: How many staff are site-based versus office-based? Who owns the firm?</p>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            ownership = st.selectbox(
                "Ownership structure",
                ["Indigenous (Ghanaian-owned)", "Foreign-owned", "Joint venture (JV)", "Other"],
                key="q2_ownership"
            )
        with col2:
            firm_size = st.selectbox(
                "Approximate staff strength",
                ["Small (<30 staff)", "Medium (30–100 staff)", "Large (100–300 staff)", "Very large (>300 staff)"],
                key="q2_size"
            )

        firm_structure = st.selectbox(
            "Corporate structure",
            ["Single-director", "Corporate (multiple directors)", "Subsidiary of a larger group"],
            key="q2_structure"
        )
        site_office_split = st.text_input(
            "Approximate site-based vs office-based staff split (e.g., 80% site, 20% office)",
            key="q2_split"
        )

        # ---------------------------------------------------------
        # SECTION B
        # ---------------------------------------------------------
        st.markdown("---")
        st.markdown("## Section B: Forms of Occupational Fraud")

        st.markdown("**Q3. What forms of occupational fraud are most common in your experience, at what stage of a project do they typically arise, and which do you consider the most costly versus the most common?** <span class='rq-tag'>RQ1</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: Can you rank them by cost? By frequency? Are the most costly the same as the most common?</p>", unsafe_allow_html=True)

        q3_schemes = st.text_area(
            "Common fraud schemes and project lifecycle stages",
            placeholder="Example: material substitution on site during construction; inflated variation orders at the variation stage; ghost workers on subcontractor payroll; kickbacks at procurement...",
            key="q3_schemes",
            height=150
        )
        q3_rankings = st.text_area(
            "Cost vs frequency rankings (optional but valuable)",
            placeholder="Example: Most costly — variation order inflation, client collusion, bribery. Most frequent — materials theft, fuel diversion, petty cash.",
            key="q3_rankings",
            height=100
        )

        st.markdown("**Q4. Are these schemes more often committed by individuals acting alone or through collusion — with colleagues, subcontractors or clients — and how do such arrangements typically work?** <span class='rq-tag'>RQ1</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: Can you describe how a collusive arrangement is set up? Who approaches whom?</p>", unsafe_allow_html=True)

        perpetrator_pattern = st.selectbox(
            "Predominant perpetrator pattern",
            [
                "Mostly lone individuals",
                "Mostly collusion with colleagues",
                "Mostly collusion with subcontractors/suppliers",
                "Mostly collusion with clients",
                "Mixed — varies by scheme value"
            ],
            key="q4_pattern"
        )
        q4_mechanism = st.text_area(
            "How collusive arrangements are set up",
            placeholder="Who approaches whom? How is the split arranged? What controls are defeated?",
            key="q4_mechanism",
            height=120
        )

        st.markdown("**Q5. Consider a scenario: a site engineer routinely certifies more aggregate than was delivered and splits the difference with the supplier's representative. How common is this in Ghanaian construction, and what makes it possible?** <span class='rq-tag'>RQ1</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: Have you seen something like this? What controls would normally catch it — and why don't they?</p>", unsafe_allow_html=True)

        q5_frequency = st.selectbox(
            "How common is this scenario?",
            ["Very common", "Common", "Occasional", "Rare", "Never seen", "Decline to answer"],
            key="q5_frequency"
        )
        q5_enablers = st.text_area(
            "What makes it possible?",
            placeholder="Absence of independent quantity verification; collusion between certifying officer and supplier; difficulty of re-measuring after delivery...",
            key="q5_enablers",
            height=100
        )

        st.markdown("**Q6. Can you describe a specific recent case of occupational fraud you personally observed or became aware of — what happened, who was involved, and how was it handled?** <span class='rq-tag'>RQ1 — Critical Incident</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: How was it discovered? What was the outcome? (If you decline, simply leave blank and move on.)</p>", unsafe_allow_html=True)

        q6_case = st.text_area(
            "Specific incident description (anonymised — do not name any individual)",
            placeholder="What happened, who was involved (by role, not name), and how was it handled?",
            key="q6_case",
            height=150
        )
        q6_declined = st.checkbox("I prefer not to answer Q6", key="q6_declined")

        q6_detection = "Declined"
        q6_outcome = "Declined"

        if not q6_declined:
            col1, col2 = st.columns(2)
            with col1:
                q6_detection = st.selectbox(
                    "How was it discovered?",
                    ["Tip / informal report", "Internal audit", "External audit", "Management observation", "Not detected", "Other", "N/A"],
                    key="q6_detection"
                )
            with col2:
                q6_outcome = st.selectbox(
                    "What was the outcome?",
                    ["Dismissed", "Repayment without sanction", "Warning", "Recovery without sanction", "Not investigated", "Prosecuted", "Ongoing", "Other", "N/A"],
                    key="q6_outcome"
                )

        # ---------------------------------------------------------
        # SECTION C
        # ---------------------------------------------------------
        st.markdown("---")
        st.markdown("## Section C: Operation of the COSO Internal Control Components")

        st.markdown("### 3.1 Control Environment")

        st.markdown("**Q7. How would you describe the tone set by senior management on integrity and ethical conduct, and how are staff screened before recruitment, especially for roles handling cash, procurement or site materials?** <span class='rq-tag'>RQ2 — Control Environment</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: What happens when a senior manager breaches policy? Are background checks done for site storekeepers?</p>", unsafe_allow_html=True)

        q7_tone = st.text_area(
            "Tone at the top and recruitment screening",
            placeholder="Describe senior management's commitment to ethics; what happens when a senior manager breaches policy; how staff are screened...",
            key="q7_tone",
            height=120
        )

        st.markdown("**Q8. How fair is your firm's remuneration structure — does it relieve or create pressure to defraud — and when staff are caught committing fraud, what typically happens? Are consequences applied consistently across levels of seniority?** <span class='rq-tag'>RQ2 — Control Environment</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: Can you give an example of how a case was handled? Would a director be treated the same as a site clerk?</p>", unsafe_allow_html=True)

        q8_remuneration = st.text_area(
            "Remuneration fairness and sanction consistency",
            placeholder="How fair is remuneration? What happens when staff are caught? Are sanctions consistent across seniority?",
            key="q8_remuneration",
            height=120
        )

        st.markdown("### 3.2 Risk Assessment")

        st.markdown("**Q9. Does your firm formally identify and manage fraud as a risk? If so, how and how often — and are fraud risks identified in advance or only recognised after schemes come to light?** <span class='rq-tag'>RQ2 — Risk Assessment</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: Is fraud on any risk register? Who reviews it, and when?</p>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            q9_formal = st.selectbox(
                "Is fraud formally assessed as a risk?",
                ["Yes — on a formal risk register", "Informally, but not documented", "No", "Don't know"],
                key="q9_formal"
            )
        with col2:
            q9_timing = st.selectbox(
                "When are fraud risks identified?",
                ["Proactively, in advance", "Reactively, after schemes come to light", "Both", "Neither", "Don't know"],
                key="q9_timing"
            )

        q9_detail = st.text_area(
            "Further detail on formal risk assessment",
            placeholder="How is the risk assessment conducted? Who is involved? How often is it reviewed?",
            key="q9_detail",
            height=100
        )

        st.markdown("**Q10. Which processes — for example procurement, materials management, site administration, expenditure claims, payroll — do you consider most exposed to fraud, and why?** <span class='rq-tag'>RQ2 — Risk Assessment</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: Which single process would you fix first if you could?</p>", unsafe_allow_html=True)

        q10_exposed = st.multiselect(
            "Processes most exposed to fraud (select all that apply)",
            [
                "Procurement / tendering",
                "Materials management / site stores",
                "Site administration (imprests, petty cash)",
                "Expenditure claims",
                "Payroll / subcontractor labour",
                "Variation orders",
                "Measured-work certification",
                "Equipment and fuel management"
            ],
            key="q10_exposed"
        )
        q10_why = st.text_area(
            "Why are these processes most exposed?",
            placeholder="Structural reasons; control weaknesses; visibility of transactions; collusion opportunities...",
            key="q10_why",
            height=100
        )

        st.markdown("### 3.3 Control Activities")

        st.markdown("**Q11. How are authorisation limits set and enforced across expenditure types — petty cash, site imprests, materials requisitions, variation orders, subcontractor payments, payroll — and how is segregation of duties maintained between initiating, authorising and recording transactions? Where does it break down?** <span class='rq-tag'>RQ2 — Control Activities</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: In a small firm, who actually approves payments? Can one person order, receive and pay for materials?</p>", unsafe_allow_html=True)

        q11_authorisation = st.text_area(
            "Authorisation limits and segregation of duties",
            placeholder="How are limits set and enforced across expenditure types? Where does segregation of duties break down?",
            key="q11_authorisation",
            height=150
        )

        st.markdown("**Q12. How are physical assets on site — fuel, cement, aggregates, steel, equipment — safeguarded and reconciled, and how are variation orders and measured-work certificates verified before payment?** <span class='rq-tag'>RQ2 — Control Activities</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: Who counts deliveries? Are stock records reconciled to certificates? Who checks a variation order before it is paid?</p>", unsafe_allow_html=True)

        q12_safeguards = st.text_area(
            "Physical safeguarding and variation/certificate verification",
            placeholder="How are physical assets safeguarded and reconciled? How are variation orders and measured-work certificates verified before payment?",
            key="q12_safeguards",
            height=150
        )

        st.markdown("### 3.4 Information and Communication")

        st.markdown("**Q13. How does information about possible fraud reach those able to act on it — including whether your firm has a whistleblowing channel, how it is structured, whether staff trust and use it, and whether fraud in construction is more often uncovered through a tip, internal audit, external audit, or another route?** <span class='rq-tag'>RQ2 — Information &amp; Communication</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: Has a whistleblowing channel ever been used? Would a site worker trust it?</p>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            q13_channel = st.selectbox(
                "Does a whistleblowing channel exist?",
                ["Yes — formal and used", "Yes — formal but not trusted", "No", "Informal only", "Don't know"],
                key="q13_channel"
            )
        with col2:
            q13_detection_route = st.selectbox(
                "Most common detection route",
                ["Tips / informal reports", "Internal audit", "External audit", "Management observation", "Other", "Don't know"],
                key="q13_detection_route"
            )

        q13_detail = st.text_area(
            "Further detail on information flow and whistleblowing",
            placeholder="How does information reach decision-makers? Has a channel been used? Would a site worker trust it?",
            key="q13_detail",
            height=100
        )

        st.markdown("### 3.5 Monitoring Activities")

        st.markdown("**Q14. Does your firm have an internal audit function? If so, how is it resourced and what does it focus on, and how often are internal controls formally evaluated?** <span class='rq-tag'>RQ2 — Monitoring Activities</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: Is internal audit in-house or outsourced? Does it visit sites, and how often?</p>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            q14_audit = st.selectbox(
                "Internal audit function",
                ["In-house", "Outsourced", "Both", "None", "Don't know"],
                key="q14_audit"
            )
        with col2:
            q14_frequency = st.selectbox(
                "How often are controls formally evaluated?",
                ["Quarterly", "Semi-annually", "Annually", "Less than annually", "Never", "Don't know"],
                key="q14_frequency"
            )

        q14_detail = st.text_area(
            "Further detail on internal audit",
            placeholder="What does internal audit focus on? Does it visit sites? How is it resourced?",
            key="q14_detail",
            height=100
        )

        st.markdown("**Q15. Are proactive data-analytics techniques used to test transactions for fraud — for example round, duplicated, threshold or outlier amounts? If not, what would be needed to make them feasible?** <span class='rq-tag'>RQ2 — Monitoring Activities</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: Does anyone review payment data for patterns? What would it take to start?</p>", unsafe_allow_html=True)

        q15_analytics = st.text_area(
            "Use of data analytics",
            placeholder="Are round/duplicate/threshold/outlier tests used? If not, what would be needed (cost, skills, data quality)?",
            key="q15_analytics",
            height=120
        )

        # ---------------------------------------------------------
        # SECTION D
        # ---------------------------------------------------------
        st.markdown("---")
        st.markdown("## Section D: Challenges in Prevention, Detection and Response")

        st.markdown("**Q16. What are the main challenges you face in preventing occupational fraud in construction projects, and what are the main challenges in detecting it when it occurs?** <span class='rq-tag'>RQ3</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: Which challenge is the most serious? Is prevention or detection harder, and why?</p>", unsafe_allow_html=True)

        q16_challenges = st.text_area(
            "Challenges in prevention and detection",
            placeholder="Structural, resource, organisational or cultural barriers. Which is the most serious?",
            key="q16_challenges",
            height=150
        )

        st.markdown("**Q17. When suspected fraud is reported, how does your firm typically respond — and are there reasons it might choose not to investigate or sanction?** <span class='rq-tag'>RQ3</span>", unsafe_allow_html=True)
        st.markdown("<p class='probe-text'>Probes: What would make a firm decide not to act? Does the client's or subcontractor's relationship matter?</p>", unsafe_allow_html=True)

        q17_response = st.text_area(
            "Response to suspected fraud",
            placeholder="How does the firm respond? Are there reasons it might choose not to investigate or sanction?",
            key="q17_response",
            height=150
        )

        # ---------------------------------------------------------
        # OPTIONAL PROMPTS
        # ---------------------------------------------------------
        st.markdown("---")
        st.markdown("## Optional Closing Prompts")
        st.write("These are optional and may be answered if time permits.")

        st.markdown("**P1. How do practitioners justify or explain to themselves the small-scale fraud common on site — for example mileage inflation, timesheet manipulation, minor materials theft?** <span class='rq-tag'>RQ3 — Rationalisation</span>", unsafe_allow_html=True)
        p1_rationalisation = st.text_area(
            "Rationalisation of small-scale fraud",
            placeholder="Relative deprivation, normalisation, comparative minimisation...",
            key="p1_rationalisation",
            height=100
        )

        st.markdown("**P2. Is the formal presence of a control — a policy, an authorisation limit, a hotline — enough to prevent fraud, or does its effectiveness depend on other factors? What perceived costs or risks of reporting or acting on fraud discourage professionals from doing so?** <span class='rq-tag'>RQ3 — Control effectiveness</span>", unsafe_allow_html=True)
        p2_effectiveness = st.text_area(
            "Formal control vs operational effectiveness",
            placeholder="Is formal presence enough? What costs or risks discourage reporting or acting on fraud?",
            key="p2_effectiveness",
            height=100
        )

        # ---------------------------------------------------------
        # SUBMIT
        # ---------------------------------------------------------
        st.markdown("---")
        submitted = st.form_submit_button("Submit Interview Response")

        if submitted:
            missing = []
            if not role:
                missing.append("Q1 Role")
            if role == "Other" and not other_role.strip():
                missing.append("Q1 Other role specification")
            if not project_types:
                missing.append("Q1 Project types")
            if experience_firm > experience_total:
                missing.append("Q1 Years with firm cannot exceed total experience")
            if not q3_schemes.strip():
                missing.append("Q3 Schemes")
            if not q7_tone.strip():
                missing.append("Q7 Tone")
            if not q11_authorisation.strip():
                missing.append("Q11 Authorisation")
            if not q16_challenges.strip():
                missing.append("Q16 Challenges")

            if missing:
                st.error(f"Please correct the following before submitting: {', '.join(missing)}")
            else:
                response_data = {
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Q1_Role": role if role != "Other" else f"Other: {other_role.strip()}",
                    "Q1_Experience_Total": experience_total,
                    "Q1_Experience_Firm": experience_firm,
                    "Q1_Project_Types": "; ".join(project_types),
                    "Q2_Ownership": ownership,
                    "Q2_Size": firm_size,
                    "Q2_Structure": firm_structure,
                    "Q2_Site_Office_Split": site_office_split,
                    "Q3_Schemes": q3_schemes,
                    "Q3_Rankings": q3_rankings,
                    "Q4_Pattern": perpetrator_pattern,
                    "Q4_Mechanism": q4_mechanism,
                    "Q5_Frequency": q5_frequency,
                    "Q5_Enablers": q5_enablers,
                    "Q6_Declined": q6_declined,
                    "Q6_Case": q6_case,
                    "Q6_Detection": q6_detection,
                    "Q6_Outcome": q6_outcome,
                    "Q7_Tone": q7_tone,
                    "Q8_Remuneration": q8_remuneration,
                    "Q9_Formal": q9_formal,
                    "Q9_Timing": q9_timing,
                    "Q9_Detail": q9_detail,
                    "Q10_Exposed": "; ".join(q10_exposed),
                    "Q10_Why": q10_why,
                    "Q11_Authorisation": q11_authorisation,
                    "Q12_Safeguards": q12_safeguards,
                    "Q13_Channel": q13_channel,
                    "Q13_Detection_Route": q13_detection_route,
                    "Q13_Detail": q13_detail,
                    "Q14_Audit": q14_audit,
                    "Q14_Frequency": q14_frequency,
                    "Q14_Detail": q14_detail,
                    "Q15_Analytics": q15_analytics,
                    "Q16_Challenges": q16_challenges,
                    "Q17_Response": q17_response,
                    "P1_Rationalisation": p1_rationalisation,
                    "P2_Effectiveness": p2_effectiveness,
                }

                df_new = pd.DataFrame([response_data])

                try:
                    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
                        df_new.to_csv(DATA_FILE, mode='a', header=False, index=False)
                    else:
                        df_new.to_csv(DATA_FILE, mode='w', header=True, index=False)
                    st.success("Thank you. Your interview response has been successfully recorded and securely saved.")
                except Exception as e:
                    st.error(
                        "Your response could not be saved automatically. "
                        "Please inform the researcher directly. "
                        f"(Technical detail: {type(e).__name__})"
                    )

# ============================================================
# ADMIN DOWNLOAD — PASSWORD-PROTECTED WITH CLEAR BUTTON
# ============================================================
st.markdown("---")
with st.expander("Admin Download — Restricted Access"):
    st.write("Enter the admin password to view and download responses.")
    entered = st.text_input("Admin password", type="password", key="admin_pw")

    if entered == ADMIN_PASSWORD:
        st.success("Access granted.")

        if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
            try:
                df_existing = pd.read_csv(DATA_FILE)
                st.metric("Total Responses Collected", len(df_existing))
                st.dataframe(df_existing)

                csv_data = df_existing.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download Responses as CSV (for NVivo / Excel)",
                    data=csv_data,
                    file_name=f"industrial_construction_fraud_responses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv",
                )

                st.markdown("### Quick Summary of Key Fields")
                if "Q1_Role" in df_existing.columns:
                    st.write("**Respondent roles:**")
                    st.write(df_existing["Q1_Role"].value_counts())
                if "Q2_Size" in df_existing.columns:
                    st.write("**Firm sizes:**")
                    st.write(df_existing["Q2_Size"].value_counts())
                if "Q6_Declined" in df_existing.columns:
                    st.write("**Q6 incidence cases provided:**")
                    declined_count = int(df_existing["Q6_Declined"].sum())
                    provided_count = len(df_existing) - declined_count
                    st.write(f"{provided_count} provided, {declined_count} declined")

                # ============================================================
                # DANGER ZONE — CLEAR ALL RESPONSES
                # ============================================================
                st.markdown("---")
                st.markdown("### Danger zone")
                st.write("This deletes all collected responses permanently. This cannot be undone.")
                confirm_clear = st.checkbox(
                    "I understand this will delete all responses permanently",
                    key="confirm_clear"
                )
                if st.button("Clear all responses", disabled=not confirm_clear, key="clear_button"):
                    os.remove(DATA_FILE)
                    st.success("All responses have been cleared. The dataset is now empty.")
                    st.rerun()

            except pd.errors.EmptyDataError:
                st.info("Response file is empty. Submit a test response to initialize the dataset.")
            except Exception as e:
                st.warning(f"Could not read the response file: {type(e).__name__}")
        else:
            st.info("No responses recorded yet. Submit a test response above to initialize the dataset.")
    elif entered:
        st.error("Incorrect password.")
import os
import time
import re

import streamlit as st
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API key not found.")
    st.info("Please check your .env file.")
    st.stop()


# ============================================================
# GEMINI CLIENT
# ============================================================

client = genai.Client(api_key=api_key)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="HireSleuth",
    page_icon="🕵️",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("🕵️ HireSleuth")

st.subheader(
    "AI Agent for Investigating Job & Internship Offers"
)

st.caption(
    "Don't just trust the offer. Investigate it."
)

st.divider()


# ============================================================
# HOW IT WORKS
# ============================================================

st.markdown("### 🔎 How HireSleuth Works")

st.markdown(
    """
**Offer → Investigation → Risk Assessment → Verification → Recommendation**
"""
)

st.divider()


# ============================================================
# INVESTIGATION TRAIL
# ============================================================

st.markdown("### 🤖 Agent Investigation Trail")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("📩 **Offer**")
    st.caption("Receive")

with col2:
    st.markdown("📝 **Extract**")
    st.caption("Details")

with col3:
    st.markdown("🚩 **Detect**")
    st.caption("Risk signals")

with col4:
    st.markdown("📊 **Assess**")
    st.caption("Risk")

with col5:
    st.markdown("🛡️ **Recommend**")
    st.caption("Action")

st.divider()


# ============================================================
# DEMO OFFER
# ============================================================

demo_offer = """
Congratulations!

You have been selected for our AI Internship Program.

To confirm your internship seat, you must pay a registration
fee of ₹2,999 within 24 hours.

After payment, you will receive training access and an
internship certificate.

Limited seats are available.

Pay immediately to secure your position.

Regards,
AI Internship Team
"""


# ============================================================
# QUICK DEMO
# ============================================================

st.markdown("### 🎯 Quick Demo")

st.caption(
    "Want to test HireSleuth quickly? Load a sample suspicious "
    "internship offer."
)

if st.button(
    "🎯 Load Demo Offer",
    use_container_width=True
):

    st.session_state["offer_text"] = demo_offer
    st.session_state["input_method"] = "📋 Paste Offer Text"

    st.success(
        "✅ Demo offer loaded! Click **🔎 Investigate Offer** below."
    )


# ============================================================
# INPUT METHOD
# ============================================================

st.markdown("### 📩 Enter the Offer")

input_method = st.radio(
    "Choose how you want to provide the offer:",
    [
        "📋 Paste Offer Text",
        "📎 Upload Offer PDF"
    ],
    horizontal=True,
    key="input_method"
)


offer_text = ""


# ============================================================
# PASTE OFFER TEXT
# ============================================================

if input_method == "📋 Paste Offer Text":

    offer_text = st.text_area(
        "Paste the job/internship offer below:",
        height=280,
        placeholder=(
            "Paste the complete email, WhatsApp message, "
            "internship offer, or job offer here..."
        ),
        key="offer_text"
    )


# ============================================================
# PDF UPLOAD
# ============================================================

else:

    uploaded_file = st.file_uploader(
        "Upload the job/internship offer PDF:",
        type=["pdf"]
    )

    if uploaded_file:

        try:

            pdf_reader = PdfReader(uploaded_file)

            pages_text = []

            for page in pdf_reader.pages:

                page_text = page.extract_text()

                if page_text:
                    pages_text.append(page_text)

            offer_text = "\n\n".join(pages_text)

            if offer_text.strip():

                st.success(
                    f"✅ PDF loaded successfully — "
                    f"{len(pdf_reader.pages)} page(s)"
                )

                with st.expander("📄 View extracted PDF text"):

                    st.text_area(
                        "Extracted text:",
                        offer_text,
                        height=250
                    )

            else:

                st.warning(
                    "⚠️ No readable text was found in this PDF."
                )

                st.info(
                    "Try a text-based PDF or paste the offer manually."
                )

        except Exception as error:

            st.error("❌ Could not read the PDF.")

            st.code(str(error))


# ============================================================
# AI INVESTIGATION FUNCTION
# ============================================================

def investigate_offer(offer):

    prompt = f"""
You are HireSleuth, an AI investigation agent designed to
help students evaluate job and internship offers.

Your task is to investigate the offer carefully.

Do NOT automatically call an offer a scam.

Instead:

1. Extract important details.
2. Identify suspicious signals.
3. Identify positive signals.
4. Assess the overall risk.
5. Determine what should be verified.
6. Recommend the safest next action.

================ OFFER ================

{offer}

============== END OFFER ==============

Return the investigation using EXACTLY these sections:

## 🔎 OFFER SUMMARY

Briefly summarize what the offer is asking the student to do.

## 🚦 RISK LEVEL

Choose exactly one:

LOW
MEDIUM
HIGH

## 📊 RISK SCORE

Give a score from 0 to 100.

0 = no obvious risk detected
100 = extremely risky

## 🚩 RED FLAGS

List the important warning signs.

Pay attention to:

- Upfront payment
- Registration fees
- Seat-confirmation fees
- Requests for banking information
- Requests for OTPs or passwords
- Suspicious links
- Unofficial email domains
- Unrealistic salary promises
- Artificial urgency
- Limited-seat pressure
- Missing company information
- Unclear job responsibilities
- Requests for sensitive information

For each red flag, explain why it matters.

## ✅ POSITIVE SIGNALS

List anything that appears legitimate or reassuring.

If there are none, write:

No strong positive signals identified.

## 🔍 WHAT SHOULD BE VERIFIED

Create a practical verification checklist.

Check:

- Company identity
- Official company website
- Recruiter identity
- Recruiter email/domain
- Job or internship details
- Payment requirements
- Contact information
- Links and domains
- Claims made in the offer
- Urgency or pressure tactics

## 🧠 INVESTIGATION REASONING

Briefly explain the main evidence that influenced the
risk assessment.

Do NOT reveal hidden chain-of-thought.

Provide only concise decision-relevant reasoning.

## 🛡️ RECOMMENDED ACTION

Choose exactly ONE:

PROCEED
VERIFY BEFORE PROCEEDING
DO NOT PROCEED

Then explain the recommendation.

## ⚠️ SAFETY NOTE

Remind the student:

- Never share passwords.
- Never share OTPs.
- Never share sensitive banking credentials.
- Never send money solely because of urgency.
- Verify important claims through official channels.

IMPORTANT:

Do not claim that an offer is definitely fraudulent unless
the evidence provided clearly establishes that.

Distinguish between:

- Suspicious behavior
- Information requiring verification
- Confirmed evidence

For example, upfront fees to secure an employment or internship
position are a major warning sign and should be independently
verified.

Keep the answer practical and understandable for a college student.
"""


    # ========================================================
    # GEMINI MODEL FALLBACK
    # ========================================================

    models_to_try = [
        "gemini-3.8-flash",
        "gemini-3.7-flash",
        "gemini-3.6-flash",
        "gemini-3.5-flash-lite"
    ]

    errors = []

    for model_name in models_to_try:

        for attempt in range(2):

            try:

                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )

                if response and response.text:

                    return response.text, model_name

            except Exception as error:

                error_text = str(error)

                errors.append(
                    f"{model_name} | Attempt {attempt + 1} | "
                    f"{error_text}"
                )

                if (
                    "503" in error_text
                    or "UNAVAILABLE" in error_text
                ):

                    time.sleep(2)

                elif (
                    "404" in error_text
                    or "NOT_FOUND" in error_text
                ):

                    break

                else:

                    time.sleep(1)

    return None, errors


# ============================================================
# EXTRACT RISK INFORMATION
# ============================================================

def extract_risk_information(result):

    risk_level = "UNKNOWN"
    risk_score = None
    recommendation = "REVIEW"

    # --------------------------------------------------------
    # Risk level
    # --------------------------------------------------------

    level_match = re.search(
        r"RISK LEVEL\s*\n+\s*(LOW|MEDIUM|HIGH)",
        result,
        re.IGNORECASE
    )

    if level_match:

        risk_level = level_match.group(1).upper()


    # --------------------------------------------------------
    # Risk score
    # --------------------------------------------------------

    score_match = re.search(
        r"RISK SCORE\s*\n+\s*(\d{1,3})",
        result,
        re.IGNORECASE
    )

    if score_match:

        risk_score = int(score_match.group(1))

        if risk_score > 100:

            risk_score = 100


    # --------------------------------------------------------
    # Recommendation
    # --------------------------------------------------------

    if "DO NOT PROCEED" in result.upper():

        recommendation = "DO NOT PROCEED"

    elif "VERIFY BEFORE PROCEEDING" in result.upper():

        recommendation = "VERIFY BEFORE PROCEEDING"

    elif "PROCEED" in result.upper():

        recommendation = "PROCEED"


    return risk_level, risk_score, recommendation


# ============================================================
# RISK DASHBOARD
# ============================================================

def show_risk_dashboard(
    risk_level,
    risk_score,
    recommendation
):

    st.markdown("## 🚨 Risk Dashboard")

    col1, col2, col3 = st.columns(3)


    # --------------------------------------------------------
    # Risk Level
    # --------------------------------------------------------

    with col1:

        st.markdown("### 🚦 Risk Level")

        if risk_level == "HIGH":

            st.error("🚨 HIGH RISK")

        elif risk_level == "MEDIUM":

            st.warning("⚠️ MEDIUM RISK")

        elif risk_level == "LOW":

            st.success("✅ LOW RISK")

        else:

            st.info("Risk level unavailable")


    # --------------------------------------------------------
    # Risk Score
    # --------------------------------------------------------

    with col2:

        st.markdown("### 📊 Risk Score")

        if risk_score is not None:

            st.metric(
                "Risk",
                f"{risk_score} / 100"
            )

            st.progress(
                risk_score / 100
            )

        else:

            st.info("Score unavailable")


    # --------------------------------------------------------
    # Recommendation
    # --------------------------------------------------------

    with col3:

        st.markdown("### 🛡️ Recommended Action")

        if recommendation == "DO NOT PROCEED":

            st.error(
                "🛑 DO NOT PROCEED"
            )

        elif recommendation == "VERIFY BEFORE PROCEEDING":

            st.warning(
                "🔎 VERIFY FIRST"
            )

        elif recommendation == "PROCEED":

            st.success(
                "✅ PROCEED"
            )

        else:

            st.info(
                "Review report"
            )


# ============================================================
# INVESTIGATE BUTTON
# ============================================================

if st.button(
    "🔎 Investigate Offer",
    use_container_width=True
):

    if not offer_text.strip():

        st.warning(
            "⚠️ Please provide an offer first."
        )

    else:

        # ====================================================
        # INVESTIGATION STATUS
        # ====================================================

        status = st.status(
            "🕵️ HireSleuth is investigating...",
            expanded=True
        )

        status.write("📩 Offer received")

        time.sleep(0.2)

        status.write("📝 Extracting offer details")

        time.sleep(0.2)

        status.write("🚩 Detecting potential risk signals")

        time.sleep(0.2)

        status.write("📊 Assessing risk")

        time.sleep(0.2)

        status.write("🔎 Creating verification checklist")

        time.sleep(0.2)

        status.write("🛡️ Generating recommendation")


        # ====================================================
        # GEMINI INVESTIGATION
        # ====================================================

        result, information = investigate_offer(
            offer_text
        )


        # ====================================================
        # STATUS UPDATE
        # ====================================================

        if result:

            status.update(
                label="✅ Investigation completed",
                state="complete",
                expanded=False
            )

        else:

            status.update(
                label="❌ Investigation failed",
                state="error",
                expanded=True
            )


        # ====================================================
        # SUCCESS
        # ====================================================

        if result:

            risk_level, risk_score, recommendation = (
                extract_risk_information(result)
            )

            st.divider()

            show_risk_dashboard(
                risk_level,
                risk_score,
                recommendation
            )

            st.divider()

            st.markdown(
                "## 🕵️ Investigation Report"
            )

            st.markdown(result)

            st.divider()

            st.success(
                f"✅ Investigation completed using `{information}`"
            )

            st.info(
                "💡 HireSleuth provides an AI-assisted assessment. "
                "Always independently verify important employment "
                "opportunities through official channels."
            )


        # ====================================================
        # FAILURE
        # ====================================================

        else:

            st.error(
                "❌ Gemini is currently unavailable."
            )

            st.warning(
                "The application connected successfully, but "
                "the available Gemini models did not return a response."
            )

            st.markdown("### Technical details")

            for error in information:

                st.code(error)


# ============================================================
# WHY HIRESLEUTH
# ============================================================

st.divider()

st.markdown("## 💡 Why HireSleuth?")

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown("### 🚩 Detect Risk")

    st.write(
        "Identifies suspicious signals such as payment requests, "
        "urgency, missing information, and unusual recruitment behavior."
    )


with col2:

    st.markdown("### 🔍 Verify")

    st.write(
        "Provides a practical checklist of information that "
        "students should independently verify before proceeding."
    )


with col3:

    st.markdown("### 🛡️ Decide Safely")

    st.write(
        "Converts the investigation into a clear risk assessment "
        "and recommended next action."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🕵️ HireSleuth — Don't just trust the offer. Investigate it."
)
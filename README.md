# 🕵️ HireSleuth

### AI Agent for Investigating Job & Internship Offers

> **“Don’t just trust the offer. Investigate it.”**

HireSleuth is an AI-powered investigation agent that helps students evaluate job and internship offers before accepting them.

It analyzes an offer for potential risk signals such as upfront payment requests, artificial urgency, limited-seat pressure, suspicious requests, missing information, and other unusual recruitment patterns.

Instead of simply saying **“scam”**, HireSleuth provides a structured investigation with a **risk level, risk score, red flags, verification checklist, and recommended action**.

---

## 🎯 Problem

Students regularly receive job and internship offers through:

* Email
* WhatsApp
* LinkedIn
* College groups
* Internship platforms
* Social media

Some offers may contain warning signs such as:

* Registration or training fees
* Requests for money to confirm a position
* Urgent payment deadlines
* Unrealistic promises
* Missing company information
* Suspicious links
* Requests for sensitive information

Students may find it difficult to determine what should be trusted and what should be independently verified.

---

## 💡 Solution

HireSleuth acts as an **AI investigation agent** between the student and the offer.

### Investigation Flow

**Offer → Investigation → Risk Assessment → Verification → Recommendation**

The agent:

1. Receives the job or internship offer.
2. Extracts important information.
3. Detects potential risk signals.
4. Assigns a risk level and score.
5. Identifies positive signals.
6. Creates a verification checklist.
7. Recommends the safest next action.

---

## 🤖 Agent Investigation Trail

```text
📩 Offer
   ↓
📝 Extract Details
   ↓
🚩 Detect Risk Signals
   ↓
📊 Assess Risk
   ↓
🔍 Create Verification Checklist
   ↓
🛡️ Recommend Action
```

---

## ✨ Features

### 📋 Offer Analysis

Paste a complete job or internship offer into HireSleuth for analysis.

### 📄 PDF Support

Upload a text-based PDF containing an offer and HireSleuth extracts the text automatically.

### 🚩 Red Flag Detection

Identifies warning signals including:

* Upfront payment requests
* Registration fees
* Seat-confirmation fees
* Artificial urgency
* Limited-seat pressure
* Suspicious links
* Unofficial email domains
* Unrealistic promises
* Missing company information
* Requests for sensitive information

### 📊 Risk Dashboard

Provides:

* Risk Level — LOW / MEDIUM / HIGH
* Risk Score — 0 to 100
* Recommended Action

### 🔍 Verification Checklist

Shows what the student should independently verify, including:

* Company identity
* Recruiter identity
* Official website
* Recruiter email/domain
* Job or internship details
* Payment requirements
* Links and domains
* Contact information
* Claims made in the offer

### 🧠 Investigation Reasoning

Provides concise, decision-relevant reasoning explaining the main factors behind the assessment.

### 🛡️ Safety-Focused Recommendation

The agent recommends one of:

* **PROCEED**
* **VERIFY BEFORE PROCEEDING**
* **DO NOT PROCEED**

HireSleuth does not automatically label every suspicious offer as fraudulent. It distinguishes between suspicious behavior, information requiring verification, and confirmed evidence.

---

## 📸 Screenshots

### 🏠 HireSleuth Interface

![HireSleuth Home](screenshots/screenshot-home.png)

### 🚨 Risk Dashboard

![Risk Dashboard](screenshots/screenshot-risk-dashboard.png)

### 🔎 Investigation Report

![Investigation Report](screenshots/screenshot-investigation-report.png)

---

## 🧪 Example Investigation

### Example Offer

```text
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
```

### HireSleuth Assessment

The agent can identify signals such as:

* Upfront registration fee
* 24-hour payment deadline
* Limited-seat pressure
* Lack of clear organization details

The result may therefore indicate:

```text
Risk Level: HIGH

Risk Score: High

Recommended Action:
DO NOT PROCEED
```

The exact risk score may vary because the AI assessment is generated dynamically.

---

## 🛠️ Tech Stack

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| Python           | Application logic               |
| Streamlit        | Web application interface       |
| Google Gemini    | AI investigation                |
| Google GenAI SDK | Gemini API integration          |
| PyPDF            | PDF text extraction             |
| python-dotenv    | Environment variable management |
| Git & GitHub     | Version control                 |

---

## 📁 Project Structure

```text
HireSleuth/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── screenshots/
    ├── screenshot-home.png
    ├── screenshot-risk-dashboard.png
    └── screenshot-investigation-report.png
```

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/K-sl63012/HireSleuth.git
```

### 2. Open the project

```bash
cd HireSleuth
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the Gemini API key

Create a `.env` file:

```text
GEMINI_API_KEY=your_api_key_here
```

**Never upload `.env` or your API key to GitHub.**

### 7. Run HireSleuth

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🎯 Quick Demo

HireSleuth includes a built-in demo offer.

1. Open HireSleuth.
2. Click **🎯 Load Demo Offer**.
3. Click **🔎 Investigate Offer**.
4. Watch the investigation trail.
5. Review the Risk Dashboard.
6. Examine the Red Flags.
7. Follow the Verification Checklist.
8. Review the Recommended Action.

This allows the project to be demonstrated quickly during a hackathon presentation.

---

## 👥 Target Users

HireSleuth is designed primarily for:

* College students
* Fresh graduates
* Internship seekers
* Job seekers
* Early-career professionals

---

## 🔐 Safety Approach

HireSleuth is designed as an **AI-assisted decision-support tool**, not as a definitive fraud-detection system.

The application avoids automatically declaring an offer fraudulent without sufficient evidence.

Users should independently verify important employment opportunities through official channels.

### Important Safety Rules

Never share:

* Passwords
* OTPs
* Banking credentials
* Card PINs
* Sensitive personal information

Never send money simply because an offer creates urgency.

Always verify important claims through official company channels.

---

## 🔮 Future Improvements

Possible future versions of HireSleuth could include:

* 🌐 Automated web-based company verification
* 🔗 Suspicious URL and domain analysis
* 📧 Email header analysis
* 🏢 Official company website comparison
* 🔍 Recruiter identity verification
* 📰 Public scam-report and reputation checks
* 📑 Offer authenticity comparison
* 📊 Investigation history and reports
* 📥 Downloadable investigation reports
* 🤖 Multi-agent investigation workflow

---

## 🏆 Hackathon Concept

**Track:** Agentic AI

**Project:** HireSleuth

**Tagline:**

> **Don’t just trust the offer. Investigate it.**

HireSleuth demonstrates how an AI agent can transform an unstructured job or internship offer into a structured investigation and actionable safet

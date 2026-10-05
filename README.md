# 🕵️ HireSleuth

### AI Agent for Investigating Job & Internship Offers

> **Don't just trust the offer. Investigate it.**

HireSleuth is an AI-powered investigation assistant that helps students evaluate job and internship offers before they proceed.

Students often receive opportunities through emails, messages, PDFs, and online platforms. Some offers may contain warning signs such as unexpected payment requests, urgency, missing information, or suspicious recruitment practices.

HireSleuth analyzes the provided offer and produces a structured risk assessment, verification checklist, and recommended next action.

---

## 🎯 Problem

Students and fresh graduates frequently receive job and internship offers through different channels.

It can be difficult to quickly identify:

* Unexpected registration or internship fees
* Urgency and pressure tactics
* Suspicious recruitment behavior
* Missing company information
* Unclear job or internship details
* Requests for sensitive information
* Suspicious links or communication channels

A student may accept an opportunity without carefully investigating these signals.

---

## 💡 Solution

HireSleuth acts as an AI investigation agent.

The user can:

1. Paste an offer message or email
2. Upload an offer PDF
3. Load a sample offer for demonstration
4. Start an AI investigation
5. Review the detected risk signals
6. Check the risk score and risk level
7. Review what should be independently verified
8. Follow the recommended next action

### Core Flow

**Offer → Investigation → Risk Assessment → Verification → Recommendation**

---

## 🤖 Agent Investigation Trail

HireSleuth presents the investigation as a sequence of steps:

**📩 Offer**
Receive the offer

↓

**📝 Extract**
Extract important details

↓

**🚩 Detect**
Identify potential risk signals

↓

**📊 Assess**
Evaluate the overall risk

↓

**🛡️ Recommend**
Suggest the safest next action

---

## ✨ Features

### 📋 Offer Text Analysis

Users can paste:

* Job offers
* Internship offers
* Recruitment emails
* Messages
* Selection notifications

HireSleuth analyzes the provided content using AI.

### 📎 PDF Investigation

Users can upload a text-based PDF offer.

HireSleuth extracts the PDF content and sends it for investigation.

### 🚩 Red Flag Detection

The AI looks for signals such as:

* Upfront payment requests
* Registration fees
* Seat-confirmation fees
* Urgency
* Limited-seat pressure
* Suspicious communication
* Missing company information
* Unclear responsibilities
* Requests for sensitive information
* Suspicious links or domains

### 📊 Risk Assessment

The investigation produces:

* Risk Level
* Risk Score from 0–100
* Red Flags
* Positive Signals
* Investigation Reasoning

### 🔍 Verification Checklist

Instead of immediately labeling an offer as fraudulent, HireSleuth identifies information that should be independently verified.

### 🛡️ Recommended Action

The system provides one of three actions:

* **PROCEED**
* **VERIFY BEFORE PROCEEDING**
* **DO NOT PROCEED**

### 🎯 Demo Mode

A built-in sample offer allows judges to test the system quickly without entering their own data.

---

## 🛠️ Technology Stack

* **Python**
* **Streamlit**
* **Google Gemini API**
* **PyPDF**
* **python-dotenv**

---

## 🏗️ Project Structure

```text
HireSleuth/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

`.env` is used locally for the Gemini API key and is excluded from GitHub.

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd HireSleuth
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env`

Create a file named `.env` in the project folder:

```text
GEMINI_API_KEY=your_api_key_here
```

Do not publish your API key.

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧪 Example Investigation

### Example Input

```text
Congratulations!

You have been selected for our AI Internship Program.

To confirm your internship seat, you must pay a registration
fee of ₹2,999 within 24 hours.

Limited seats are available.

Pay immediately to secure your position.
```

### Expected Investigation

HireSleuth should identify signals such as:

* Upfront payment request
* Urgency
* Limited-seat pressure
* Lack of detailed organization information

The system can then assign a high risk score and recommend:

**🛑 DO NOT PROCEED**

---

## 🔐 Safety Approach

HireSleuth is designed as an AI-assisted investigation tool.

It does **not automatically declare every suspicious offer to be a scam**.

The system distinguishes between:

* Suspicious behavior
* Information requiring verification
* Evidence that may indicate significant risk

Users should independently verify important claims through official company channels.

Never share:

* Passwords
* OTPs
* Banking credentials
* Sensitive personal information

Never send money solely because an offer creates urgency or pressure.

---

## 🎯 Target Users

HireSleuth is especially useful for:

* College students
* Fresh graduates
* Internship seekers
* Job seekers
* First-time applicants

---

## 🔮 Future Improvements

Potential future improvements include:

* Live company and domain verification
* URL reputation analysis
* Email-domain verification
* Official company website comparison
* Recruiter identity verification
* Historical offer pattern analysis
* Browser-based investigation tools
* Multi-agent investigation architecture
* Downloadable investigation reports

---

## ⚠️ Disclaimer

HireSleuth provides an AI-assisted assessment and should not be treated as definitive proof that an opportunity is legitimate or fraudulent.

Important employment and internship decisions should always be independently verified through official sources.

---

## 🏆 Hackathon

**Project:** HireSleuth
**Track:** Agentic AI

**Tagline:**

> Don't just trust the offer. Investigate it.

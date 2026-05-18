# 🧠 CodeLensAI — AI-Driven Code Review & Documentation Assistant

> An intelligent, AI-powered code review tool built with Python & Streamlit that helps developers write cleaner, safer, and better-documented code — instantly.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://codelensai.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Groq](https://img.shields.io/badge/AI-Groq%20LLaMA%203.3-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🐛 **Bug Detection** | Finds bugs and errors with severity levels and fix instructions |
| 💡 **Code Improvements** | Suggests performance optimizations and best practices |
| 📝 **Documentation Generator** | Auto-generates structured technical documentation |
| 🔒 **Security Scanner** | Detects vulnerabilities classified as Critical / Medium / Low |
| 🔁 **Code Comparison** | Compare two versions of code side by side |
| 💬 **Chat with Code** | Ask questions about your code in natural language |
| 📊 **Quality Dashboard** | Visual score cards across 7 quality dimensions |
| 🌐 **GitHub Integration** | Paste a GitHub URL to auto-fetch and review code |
| 📂 **File Upload** | Upload `.py`, `.js`, `.java`, `.cpp`, `.cs` files directly |
| 🎨 **Syntax Highlighting** | Color-coded code preview before submitting |
| 📄 **PDF & TXT Export** | Download professional review reports |
| 🌍 **Multilingual UI** | Supports English and Urdu |
| 📋 **Review History** | Sidebar history of all past reviews in your session |

---

## 🚀 Live Demo

👉 **[Try SmartReviewer Live](https://codelensai.streamlit.app)**

---

## 🛠️ Tech Stack

- **Frontend & Backend** — [Streamlit](https://streamlit.io)
- **AI Engine** — [Groq API](https://console.groq.com) with LLaMA 3.3 (70B)
- **PDF Export** — [ReportLab](https://www.reportlab.com)
- **GitHub Integration** — Python `requests` library
- **Language** — Python 3.11+

---

## 📁 Project Structure

```
smartreviewer/
│
├── app.py                    # Main entry point
├── requirements.txt          # Python dependencies
│
├── components/
│   ├── __init__.py
│   ├── sidebar.py            # Sidebar (language switcher + history)
│   ├── code_input.py         # Code input (paste / upload / GitHub URL)
│   ├── review_output.py      # AI feedback + download buttons
│   ├── compare.py            # Code version comparison
│   ├── chat.py               # Chat with your code
│   └── dashboard.py          # Code quality dashboard
│
└── utils/
    ├── __init__.py
    ├── groq_client.py        # Groq API integration & prompts
    ├── history.py            # Session history management
    ├── github.py             # GitHub URL fetcher
    ├── pdf_export.py         # PDF report generator
    └── translations.py       # English / Urdu translations
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/MuhammadSufyanKhn/smartreviewer.git
cd smartreviewer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get your Groq API Key
- Go to [https://console.groq.com](https://console.groq.com)
- Sign up and create a free API key

### 4. Run the app
```bash
streamlit run app.py
```

### 5. Enter your API key
- Enter your Groq API key in the sidebar when prompted

---

## 📦 Requirements

```
streamlit
groq
requests
reportlab
```

---

## 🖥️ Screenshots

### Code Review
Paste or upload code, select review type, and get instant AI feedback with bug reports, suggestions, and a quality score.
<img width="644" height="368" alt="image" src="https://github.com/user-attachments/assets/d9a33aa4-fc20-4e12-9a61-b5c78c5c30e6" />

### Security Scanner
Get vulnerabilities classified by severity with step-by-step fix instructions.
<img width="794" height="422" alt="image" src="https://github.com/user-attachments/assets/6d84af03-63e9-452f-a57b-65bc642353a3" />
<img width="263" height="257" alt="image" src="https://github.com/user-attachments/assets/6a2958c0-e414-41b8-9c42-a03360f9ff08" />


### Quality Dashboard
Visual metric cards showing scores for Readability, Performance, Security, Maintainability, Best Practices, and Documentation.
<img width="821" height="314" alt="image" src="https://github.com/user-attachments/assets/abb028ce-6cf5-49c7-818c-9c550fea467b" />
<img width="809" height="285" alt="image" src="https://github.com/user-attachments/assets/49901153-aed0-43ef-8215-566c095110b7" />

### Chat with Code
Ask natural language questions about your code and get beginner-friendly answers.
<img width="817" height="402" alt="image" src="https://github.com/user-attachments/assets/deb82985-05c5-4e07-a8e6-b59729e9edf8" />
<img width="802" height="350" alt="image" src="https://github.com/user-attachments/assets/fcd809f4-345c-48ec-9f24-7d1457a9f29c" />

---

## 🌍 Multilingual Support

SmartReviewer supports:
- 🇬🇧 **English**
- 🇵🇰 **Urdu (اردو)**

Switch languages from the sidebar dropdown at any time.

---

## 👨‍💻 Author

**Muhammad Sufyan Khan**
- GitHub: [@MuhammadSufyanKhn](https://github.com/MuhammadSufyanKhn)

---

## 🙏 Acknowledgements

- [Groq](https://groq.com) for the blazing fast LLaMA inference API
- [Streamlit](https://streamlit.io) for making Python web apps effortless
- [Meta AI](https://ai.meta.com) for the open-source LLaMA 3.3 model

🤖 AI-Augmented Quality Engineering Framework

Playwright + Python + Groq (Llama 3.3)

🎯 The Vision: The "Quality Operating System"

Traditional test automation is brittle. A simple UI change (like a developer changing a data-test ID) can break an entire CI/CD pipeline, leading to "maintenance fatigue."

This framework implements a Self-Healing mechanism. When a selector fails, the system doesn't just crash. It captures the current DOM, consults a Llama 3.3 (70B) model via Groq, and dynamically finds the new element to keep the test running.

🚀 Key Features

Self-Healing Locators: Automatic recovery from TimeoutError using AI-driven element discovery.

Principal Architect Pattern: Uses a robust BasePage inheritance model for reusable healing logic across all Page Objects (POM).

High-Speed Execution: Powered by Groq, providing sub-second LLM inference for real-time healing.

Evidence Capturing: Automatically saves screenshots of "Healed" elements in a healing_evidence/ folder for manual audit.

Enterprise Reporting: Integrated with pytest-html to provide a dashboard of test results, including AI-intervention logs.

🛠️ Tech Stack

Language: Python 3.12+

Browser Automation: Playwright (Sync API)

AI Engine: Groq Cloud (Llama 3.3 70B Versatile)

Reporting: Pytest-HTML

Environment Management: Python-Dotenv

📦 Installation & Setup

Clone the repository:

Bash
git clone https://github.com/nbelbansi/ai_healing_playwrite_python.git
cd ai_healing_playwrite_python
Setup Virtual Environment:

Bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
Configure Secrets:
Create a .env file in the root directory:

Plaintext
GROQ_API_KEY=your_actual_key_here
Install Browsers:

Bash
playwright install chromium
🧪 Running the Tests
To run the full suite with the AI-Augmented Report:

Bash
python -m pytest --headed --html=report.html --self-contained-html
Chaos Engineering (Test the Healing)
To see the AI in action:

Open pages/login_page.py.

Change a locator to something incorrect (e.g., [data-test="user-WRONG"]).

Run the test.

Watch the console: The framework will detect the failure, call the AI, find the correct button, and pass the test.

📊 Architecture

Plaintext
├── pages/
│   ├── BasePage.py       # Core healing & screenshot logic
│   ├── LoginPage.py      # POM for Saucedemo Login
│   └── InventoryPage.py  # POM for Product interactions
├── utils/
│   └── AIHealer.py       # Groq API & HTML slimming logic
├── tests/
│   ├── conftest.py       # Pytest fixtures & HTML report hooks
│   └── test_sauce.py     # Clean, business-logic focused tests
├── healing_evidence/     # Screenshots of AI-recovered failures
└── .env                  # (Git Ignored) API Secrets

👔 Professional Summary

This project is part of a larger initiative to build an Enterprise Quality Operating System. By reducing flakiness through AI, we allow engineering teams to focus on shipping features rather than fixing selectors.

Author: Neelesh Belbansi

Role: Principal Quality Architect

Connect: LinkedIn Profile https://www.linkedin.com/in/neelesh-belbansi/

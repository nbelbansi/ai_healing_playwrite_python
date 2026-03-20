import os

from dotenv import load_dotenv
from groq import Groq
from bs4 import BeautifulSoup

class AIHealer:
    def __init__(self):
        load_dotenv() # This pulls variables from the .env file
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key) if self.api_key else None
        self.client = Groq(api_key=self.api_key) if self.api_key else None
        self.model_id = "llama-3.3-70b-versatile" # Powerful and free on Groq

    def suggest_new_selector(self, html, description):
        if not self.client:
            print("[DEBUG] No Groq API Key found!")
            return None

        soup = BeautifulSoup(html, 'html.parser')
        for s in soup(['script', 'style', 'svg', 'path']): s.decompose()
        clean_html = str(soup.body)[:5000]

        try:
            completion = self.client.chat.completions.create(
                model=self.model_id,
                messages=[
                    {"role": "system", "content": "You are a QA expert. Return ONLY the CSS selector for the element. No prose, no backticks."},
                    {"role": "user", "content": f"Find CSS for: {description}\nHTML: {clean_html}"}
                ],
                temperature=0.1
            )

            selector = completion.choices[0].message.content.strip()
            # If LLM returns multiple lines, take the first one
            return selector.split('\n')[0].replace('`', '')

        except Exception as e:
            print(f"[DEBUG] Groq Error: {e}")
            return None
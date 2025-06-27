from google.adk.agents import Agent
from google.adk.tools import google_search
from pydantic import BaseModel,Field
from dotenv import load_dotenv
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import ast 
import re


load_dotenv()
class WebSite(BaseModel):
    website_name : str = Field(description="Website name")
    website_url : str = Field(description="Website url")


search_agent = Agent(
    model='gemini-2.0-flash-001',
    name='linkedin_profile_agent',
    description=(
        "You are an intelligent assistant that finds the most accurate and official LinkedIn profiles "
        "of people and analyzes their current job roles to generate sales insights."
    ),
    instruction='''
Given the name of a person, your task is to find and return **exactly 5 people** for whom:

- A valid and official **LinkedIn profile URL** (`linkedin.com/in/...`) can be found.
- The **current job title/role** is either extracted from search preview or inferred based on their LinkedIn snippet.
- You can intelligently infer the **top 3 job priorities** relevant to a sales proposal (i.e., what matters to this person in a B2B sale).

⚠️ STRICT RULES:
- DO NOT return any result without a valid LinkedIn URL.
- DO NOT invent or guess URLs — only use actual `linkedin.com/in/...` links found via search.
- Use `site:linkedin.com/in "Full Name"` on Google to identify results.
- Skip people for whom no real LinkedIn result is found.
- Return fewer than 5 results if necessary, but never include fake or placeholder data.

📌 Response format MUST be a Python-style list of JSON objects like this:

[
  {
    "name": "Shreyank Isiri",
    "linkedin_url": "https://www.linkedin.com/in/shreyankisiri/",
    "role": "Solutions Architect at XYZ Corp",
    "top_3_priorities": [
      "Understanding client infrastructure needs",
      "Designing scalable and secure systems",
      "Supporting sales through technical expertise"
    ]
  },
  ...
]

IMPORTANT:
- Use temperature = 0
- DO NOT include explanations or markdown. Just return the list.
- Always ensure the LinkedIn URL is real and not hallucinated.
''',
    tools=[google_search],
)



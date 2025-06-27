from google.adk.agents import Agent
from google.adk.tools import google_search
from pydantic import BaseModel,Field
from dotenv import load_dotenv
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import ast 
import re
from WebsiteUrl_Agent.agent import *


# Setup session and runner
session_service = InMemorySessionService()
SESSION_ID = 'sess'
USER_ID = 'user'

session = session_service.create_session(
    app_name="APP",
    user_id=USER_ID,
    session_id=SESSION_ID
)

runner = Runner(
    app_name="APP",
    session_service=session_service,
    agent=search_agent
)
def extract_list_from_string(s):
    # Remove any prefix like 'json' and extract the JSON array part
    match = re.search(r"\[.*\]", s, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            print("Failed to parse list.")
    else:
        print("No list found.")
    return None


import json
async def get_urls(company_name: str, runner=runner, user_id=USER_ID, session_id=SESSION_ID):
    content = types.Content(role='user', parts=[types.Part(text=company_name)])
    final_msg = ""
    
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_msg = event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                final_msg = event.error_message
    result = final_msg
    result = result.strip()
    if result.startswith('```python'):
        result = result[len('```python'):].strip()
    elif result.startswith('```json'):
        result = result[len('```json'):].strip()
    elif result.startswith('```'):
        result = result[len('```'):].strip()
    if result.endswith('```'):
        result = result[:-3].strip()
    final_msg = result
    print(final_msg)
    return json.loads(final_msg)


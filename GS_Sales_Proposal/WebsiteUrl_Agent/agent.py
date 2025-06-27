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
    name='url_agent',
    description = (
    "You are an intelligent assistant specialized in finding official and relevant websites "
    "associated with a given organization or company name. Your goal is to retrieve high-quality, "
    "credible links that accurately represent the digital presence of the organization."
),
   instruction = '''
    Given the name of a company or organization, your task is to search and return the top 7 most relevant and credible website URLs associated with it.

    These can include:
    - The official company website try fetching this and if there are multiple then show all 7


    Your response must be a clean Python-style list of strings, where each string is a valid URL.

    Format your response exactly like this:

    [
    "https://google.com/",
    "https://cloud.google.com",
    "https://accounts.google.com"
    ]

    Like this any 10 urls that are related to the given organization name

    Do not include explanations, only return the list of URLs.

    IMPORTANT : Just return me list of urls no additional text

    return like 
   
    
    ----
        [
    "https://google.com/",
    "https://cloud.google.com",
    "https://accounts.google.com"
    ]

    ----

    VERY IMPORTANT : TEMPERATURE OF THE MODEL BE ZEROOOO AND remember dont give me like the links of youtube or linkedin or any other platforms
    THE LINK SHOULD BE OFFICIAL LINK OF THE ORGANIZATION
    ''',

    tools = [google_search],
)


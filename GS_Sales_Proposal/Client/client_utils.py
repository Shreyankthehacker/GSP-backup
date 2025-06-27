import streamlit as st
import pandas as pd
from typing import List
import os

from WebsiteUrl_Agent.agent_runner import get_urls
import asyncio 
from Document_Upload_Vectordb.pain_points_extractor import *
# Function to get URLs (placeholder function)

def get_urls_list(company_name) -> List[str]:
    """
    Placeholder function that returns a list of URLs
    Replace this with your actual function that fetches URLs
    """
    return asyncio.run(get_urls(company_name))

# Function to get LinkedIn profiles (NEW)


# Function to get roles list
def get_roles_list() -> List[str]:
    """
    Function that returns a list of executive roles
    """
    return [
        "CEO (Chief Executive Officer)",
        "CMO (Chief Marketing Officer)",
        "CTO (Chief Technology Officer)",
        "CFO (Chief Financial Officer)",
        "COO (Chief Operating Officer)",
        "CHRO (Chief Human Resources Officer)",
        "CDO (Chief Data Officer)",
        "CPO (Chief Product Officer)",
        "CRO (Chief Revenue Officer)",
        "CIO (Chief Information Officer)"
    ]


from WebScraper.scrape import get_data

def get_url_details(url:str):
    """Use this if you want to run async function synchronously"""
    try:
        # Run the async function synchronously
        website_details = asyncio.run(get_data(url))
        return website_details
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_priority_suggestions() -> List[dict]:
    """
    Function that returns a list of priority suggestions with titles and descriptions
    Replace this with your actual function that fetches priority suggestions
    """
    return [
        {
            "title": "Digital Transformation Initiative",
            "description": "Modernize systems and processes for improved efficiency",
            "icon": "🚀"
        },
        {
            "title": "Data Analytics & Business Intelligence",
            "description": "Implement advanced analytics for better decision making",
            "icon": "📊"
        },
        {
            "title": "Process Optimization & Automation",
            "description": "Streamline workflows and reduce manual tasks",
            "icon": "🔧"
        }
    ]

def get_editable_content() -> str:
    """
    Placeholder function that returns editable content
    Replace this with your actual function that fetches editable content
    """
    return """This is editable content from the function:

- Project requirements and specifications
- Current implementation status
- Key stakeholder feedback
- Next steps and action items
- Additional notes and observations

You can modify this content as needed."""


# Function to get summary items (NEW)
# from Rag.rag import get_pain_points




def get_pain_items(file,company_name):
    print("-----------------------------------------------------------")
    return get_pain_points(file,company_name)




def check_field_validation(field_name: str, field_value: str, is_mandatory: bool = False) -> bool:
    """Check if field validation should show warning"""
    if is_mandatory and not field_value.strip():
        return True
    return False

def show_field_warning(field_name: str):
    """Show warning message for mandatory fields"""
    st.markdown(f'<div class="field-warning">⚠️ {field_name} is mandatory and cannot be empty!</div>', unsafe_allow_html=True)


def save_uploaded_file(uploaded_file, save_dir="uploaded_rf_is"):
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return save_path

def save_uploaded_file_and_get_path(uploaded_file):
    """Save uploaded file to a temporary directory and return the file path"""
    if uploaded_file is not None:
        # Create uploads directory if it doesn't exist
        upload_dir = "uploads"
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        # Create file path
        file_path = os.path.join(upload_dir, uploaded_file.name)
        
        # Save the file
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        return file_path
    return None

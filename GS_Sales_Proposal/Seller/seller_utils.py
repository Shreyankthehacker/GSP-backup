import streamlit as st
import pandas as pd
from typing import List
import os

from WebsiteUrl_Agent.agent_runner import get_urls
import asyncio 
from Document_Upload_Vectordb.pain_points_extractor import *
from WebScraper.scrape import get_data


# Function to get URLs (placeholder function)

def get_urls_list(company_name) -> List[str]:
    """
    Placeholder function that returns a list of URLs
    Replace this with your actual function that fetches URLs
    """
    return asyncio.run(get_urls(company_name))

def check_field_validation(field_name: str, field_value: str, is_mandatory: bool = False) -> bool:
    """Check if field validation should show warning"""
    if is_mandatory and not field_value.strip():
        return True
    return False

def show_field_warning(field_name: str):
    """Show warning message for mandatory fields"""
    st.markdown(f'<div class="field-warning">⚠️ {field_name} is mandatory and cannot be empty!</div>', unsafe_allow_html=True)

def get_url_details(url:str):
    """Use this if you want to run async function synchronously"""
    try:
        # Run the async function synchronously
        website_details = asyncio.run(get_data(url))
        return website_details
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def save_uploaded_file_and_get_path(file):
    return "saved"


def get_seller_services(filename , filepath):
    return "pain points"
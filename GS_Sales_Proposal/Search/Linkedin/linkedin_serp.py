
import requests
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st

def infer_priorities(title):
    # Placeholder function: replace with your actual priority inference logic
    return [" Scalability & Risk Mitigation","Operational Efficiency","Scalability & Risk Mitigation"]

def search_linkedin_serpapi(name):
    params = {
        "q": f'site:linkedin.com/in "{name}"',
        "api_key": os.getenv("SERP_API_KEY"),
        "engine": "google",
        "num": 5
    }
    
    try:
        response = requests.get("https://serpapi.com/search", params=params).json()
        results = {}
        
        for res in response.get("organic_results", []):
            link = res.get("link", "")
            title = res.get("title", "")
            if "linkedin.com/in" in link:
                results[link] = {
                    "name": name,
                    "role": title,
                    "top_3_priorities": infer_priorities(title)
                }
            if len(results) == 5:
                break
        
        print(results)
        return results
    except Exception as e:
        st.error(f"Error searching LinkedIn profiles: {e}")
        return {}

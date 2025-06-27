from typing import List
import json

from WebScraper.state import User



from crawl4ai import LLMConfig,AsyncWebCrawler,CacheMode,CrawlerRunConfig,BrowserConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy
import os 
from dotenv import load_dotenv
load_dotenv()

llm_strategy = LLMExtractionStrategy(
    llm_config=LLMConfig(
        provider="gemini/gemini-1.5-flash",
        api_token=os.getenv("GOOGLE_API_KEY"),
    ),
    schema=User.model_json_schema(),
    extraction_type="schema",
        instruction="""
You are analyzing a webpage to extract structured information about the organization behind it.

Your goal is to extract the following:

1. **Name**: The name of the organization or company.
2. **Logo**: The URL of the primary logo image (typically found in the header or near the company name).
3. **Detailed Description**: A clear and informative summary of what the organization does. 
   - This should come from the section of the page typically labeled or titled "About", "Who We Are", "Our Story", or similar.
   - If the page does not have a heading, look for paragraphs or text blocks that describe the company's purpose, mission, background, or offerings.
   - Do not include text that is clearly part of blog posts, testimonials, products, or contact details.

Tips:
- Focus on sections that describe the identity, mission, background, or goals of the organization.
- If multiple descriptive sections exist, prioritize the one closest to the top of the page or under an "About"-like heading.
- Avoid generic filler content like navigation menus, service listings, or unrelated calls to action.

Return the data in the format defined by the schema.
"""
,    chunk_token_threshold=1000,
    overlap_rate=0.0,
    apply_chunking=True,
    input_format="markdown",   # or "html", "fit_markdown"
    extra_args={"temperature": 0.0, "max_tokens": 800}
)

crawl_config = CrawlerRunConfig(
    extraction_strategy=llm_strategy,
    cache_mode=CacheMode.BYPASS
)


browser_cfg = BrowserConfig(headless=True)

import re 

import re
from collections import Counter
from typing import List




def aggregate_users(users: List[dict]) -> User:
    print("🔍 Starting aggregation of users...")

    # Filter out users with error=True
    valid_users = [u for u in users if not u.get('error', False)]


    # Most frequent name (non-empty and non-None)
    names = [u.get('name', '') or '' for u in valid_users if u.get('name')]
    name_counter = Counter(names)
    name = name_counter.most_common(1)[0][0] if name_counter else (valid_users[0].get('name') or "Unknown")
    logo = next(
        (
            logo for u in valid_users
            if (logo := u.get('logo')) and isinstance(logo, str) and re.search(r'logo', logo, re.IGNORECASE)
        ),
        ""
    )


    # Longest non-empty description
    descriptions = [u.get('description', '') or '' for u in valid_users]
    description = max(descriptions, key=len, default="")

    # Services list from user with the longest list (non-None)
    all_service_lists = [
        (u.get('name', 'Unknown'), u.get('services') or []) for u in valid_users
    ]
    services = max((s for _, s in all_service_lists), key=len, default=[])
    return User(
        name=name,
        logo=logo,
        description=description,
        services=services
    )

def format_enterprise_details(details_obj: User):
    return f"""Name: {details_obj.name}
Description: {details_obj.description}
Services:
- {'\n- '.join(details_obj.services)}
"""

async def get_data(url:str):

    async with AsyncWebCrawler(config= browser_cfg) as crawler:
        result = await crawler.arun(
            url = url,
            config = crawl_config)
    
    if result.success:
        print(f"Successfully scraped : '\n\n\n {result.extracted_content}")    
        lists = json.loads(result.extracted_content)  # here instead of returning the last we may refine the one we need
        #print(lists)
        print(aggregate_users(lists))
        return format_enterprise_details(aggregate_users(lists))
    
    else:
        print(f"The code exited with eroor {result.error_message}")

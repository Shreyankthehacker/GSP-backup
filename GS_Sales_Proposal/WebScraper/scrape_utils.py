import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_hex_colors(url: str, limit: int = 5) -> list:
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find inline styles
        inline_styles = [tag.get('style', '') for tag in soup.find_all(style=True)]
        css_text = ' '.join(inline_styles)

        # Find linked stylesheets
        css_links = [link['href'] for link in soup.find_all('link', rel='stylesheet') if 'href' in link.attrs]

        for href in css_links:
            full_url = urljoin(url, href)
            try:
                css_response = requests.get(full_url, timeout=5)
                css_text += ' ' + css_response.text
            except:
                continue

        # Extract hex codes
        hex_colors = re.findall(r'#[0-9a-fA-F]{3,6}', css_text)
        hex_colors = list(dict.fromkeys(hex_colors))  # remove duplicates, preserve order
        return hex_colors[:limit]  # return top `limit` hex codes
    except Exception as e:
        print(f"Error extracting hex colors: {e}")
        return []

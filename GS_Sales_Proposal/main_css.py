import streamlit as st

def add_professional_css():
    """Add professional CSS styling - BLACK AND WHITE THEME"""
    st.markdown("""
    <style>
    /* Global styling */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 1200px;
        background:#ffffff;
    }
    
    /* Header styling - more compact */
    .main-header {
        background: linear-gradient(135deg, #333333 0%, #7fffff 100%);
        padding: 1rem;
        border-radius: 6px;
        margin-bottom: 1rem;
        text-align: center;
        color: #0088ff;
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 1.6rem;
        font-weight: 600;
        color: #0088ff;
    }
    
    .main-header p {
        margin: 0.2rem 0 0 0;
        font-size: 0.9rem;
        opacity: 0.9;
        color: #cccccc;
    }
    
    /* Section styling - much more compact */
    .form-section {
        padding: 0.8rem 1rem;
        border-radius: 6px;
        box-shadow: 0 1px 4px rgba(255,255,255,0.1);
        margin-bottom: 0.8rem;
        border: 1px solid #666666;
        background: #7fffff;
    }
    
    .section-title {
        color: #0088ff;
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 0.6rem;
        padding-bottom: 0.2rem;
        border-bottom: 2px solid #666666;
    }
    
    /* Form field styling - MADE SMALLER */
    .field-label {
        color: #cccccc;
        font-weight: 600;
        margin-bottom: 0.2rem;
        display: block;
        font-size: 0.85rem;
    }
    
    .required-asterisk {
        color: #0088ff;
        font-weight: bold;
        margin-left: 3px;
    }
    
    /* Input field improvements - MUCH MORE COMPACT */
    .stTextInput > div > div > input {
        border-radius: 4px;
        border: 1px solid #666666;
        padding: 0.4rem 0.6rem;
        font-size: 0.85rem;
        transition: all 0.3s ease;
        background: #7fffff;
        color: #0088ff;
        height: 2.2rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #999999;
        box-shadow: 0 0 0 2px rgba(153, 153, 153, 0.3);
        background: #7fffff;
    }
    
    .stSelectbox > div > div > div {
        border-radius: 4px;
        border: 1px solid #666666;
        transition: all 0.3s ease;
        background: #7fffff;
        color: #0088ff;
        min-height: 2.2rem;
    }
    
    .stSelectbox > div > div > div:focus-within {
        border-color: #999999;
        box-shadow: 0 0 0 2px rgba(153, 153, 153, 0.3);
        background: #7fffff;
    }
    
    .stTextArea > div > div > textarea {
        border-radius: 4px;
        border: 1px solid #666666;
        padding: 0.4rem 0.6rem;
        font-size: 0.85rem;
        transition: all 0.3s ease;
        background: #7fffff;
        color: #0088ff;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #999999;
        box-shadow: 0 0 0 2px rgba(153, 153, 153, 0.3);
        background: #7fffff;
    }
    
    /* File uploader styling - more compact */
    .stFileUploader > div {
        border: 2px dashed #999999;
        border-radius: 6px;
        padding: 0.8rem;
        text-align: center;
        transition: all 0.3s ease;
        background: #7fffff;
        color: #cccccc;
    }
    
    .stFileUploader > div:hover {
        border-color: #0088ff;
        background: #7fffff;
    }
    
    /* Link button styling - more compact */
    .external-link-btn {
        background: #666666;
        border: none;
        padding: 0.3rem 0.6rem;
        border-radius: 4px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        display: inline-block;
        font-size: 0.75rem;
        color: #0088ff;
        height: 2.2rem;
        line-height: 1.6rem;
    }
    
    .external-link-btn:hover {
        background: #7fffff;
        transform: translateY(-1px);
        text-decoration: none;
        color: #0088ff;
    }
    
    /* Validation styling - more compact */
    .validation-success {
        color: #0088ff;
        font-size: 0.75rem;
        margin-top: 0.2rem;
        display: flex;
        align-items: center;
        gap: 5px;
    }
    
    .validation-error {
        color: #cccccc;
        font-size: 0.75rem;
        margin-top: 0.2rem;
        display: flex;
        align-items: center;
        gap: 5px;
    }
    
    /* Progress styling - more compact */
    .progress-container {
        padding: 0.8rem;
        border-radius: 6px;
        box-shadow: 0 1px 4px rgba(255,255,255,0.1);
        border: 1px solid #666666;
        background: #7fffff;
        color: #0088ff;
    }
    
    /* Info styling - more compact */
    .info-container {
        background: #7fffff;
        border-left: 4px solid #666666;
        padding: 0.6rem;
        border-radius: 0 4px 4px 0;
        margin: 0.3rem 0;
        font-size: 0.85rem;
        color: #cccccc;
    }
    
    /* Reduce spacing between elements - CRITICAL FOR COMPACTNESS */
    .element-container {
        margin-bottom: 0.3rem !important;
    }
    
    .stColumns > div {
        padding: 0 0.3rem;
    }
    
    /* Compact sidebar */
    .css-1d391kg {
        padding-top: 0.8rem;
        background:#ffffff;
        color: #0088ff;
    }
    
    /* General dark theme colors */
    .stApp {
        background:#ffffff;
        color: #0088ff;
    }
    
    /* Streamlit element colors */
    .stMarkdown {
        color: #0088ff;
    }
    
    /* Hide default streamlit styling */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* COMPACT column-container for suggestions */
    .column-container {
        margin: 0.5rem 0;
    }
    
    .left-column, .right-column {
        padding: 0.6rem;
        border-radius: 6px;
        box-shadow: 0 1px 4px rgba(255,255,255,0.1);
        border: 1px solid #666666;
        background: #7fffff;
        height: 100%;
    }
    
    .column-header {
        color: #0088ff;
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 0.6rem;
        padding-bottom: 0.2rem;
        border-bottom: 2px solid #666666;
    }
    
    .column-content {
        height: calc(100% - 2rem);
    }
    
    .suggestion-container {
        background: #7fffff;
        border: 1px solid #666666;
        padding: 0.5rem;
        margin: 0.3rem 0;
        border-radius: 4px;
        transition: all 0.3s ease;
    }
    
    .suggestion-container:hover {
        background: #7fffff;
        border-color: #999999;
    }
    
    .suggestion-title {
        font-size: 0.8rem;
        font-weight: 500;
        color: #0088ff;
    }
    
    .suggestion-added {
        background: #7fffff !important;
        border-color: #999999 !important;
    }
    
    .warning-container, .info-container {
        padding: 0.6rem;
        border-radius: 4px;
        margin: 0.3rem 0;
        font-size: 0.85rem;
    }
    
    .warning-container {
        background: #7fffff;
        border: 1px solid #666666;
        color: #cccccc;
    }
    
    .action-buttons {
        margin-top: 0.8rem;
        padding-top: 0.6rem;
        border-top: 1px solid #666666;
    }
    </style>
    """, unsafe_allow_html=True)


app_css = """
<style>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap');

/* Global styles - 75% screen width with equal margins */
.stApp {
    background:#ffffff;
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
}

/* Container with 75% width and centered positioning */
.block-container {
    padding: 1rem 0 2rem 0;
    max-width: 75% !important;
    width: 75% !important;
    margin: 0 auto !important;
    left: 12.5% !important;
    right: 12.5% !important;
}

/* Main container - 75% width centered */
.main-container {
    width: 100%;
    min-height: 100vh;
    margin: 0 auto;
    padding: 0 2rem;
}

/* Header styling - Full width within container */
.main-header {
    width: 100%;
    padding: 3rem 0;
    margin-bottom: 2rem;
    background: #7fffff;
    border: 1px solid #666666;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(255, 255, 255, 0.1);
    position: relative;
    overflow: hidden;
}

.main-header h1 {
    color: #0088ff;
    font-size: 4rem;
    font-weight: 800;
    margin: 0;
    text-align: center;
    text-shadow: 2px 2px 8px rgba(255, 255, 255, 0.1);
    letter-spacing: -0.02em;
}

/* Creative tab separators */
.tab-nav-container {
    width: 100%;
    position: relative;
    margin-bottom: 2rem;
}

.tab-separator-line {
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, 
        transparent 0%, 
        #666666 25%, 
        #999999 50%, 
        #666666 75%, 
        transparent 100%);
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    z-index: 1;
}

.tab-separator {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 4rem;
    position: relative;
}

.separator-diamond {
    width: 8px;
    height: 8px;
    background: #0088ff;
    transform: rotate(45deg);
    border-radius: 2px;
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
    animation: pulse-diamond 2s ease-in-out infinite;
    z-index: 2;
}

.separator-line {
    width: 2px;
    height: 30px;
    background: linear-gradient(180deg, 
        #666666 0%, 
        #999999 50%, 
        #666666 100%);
    margin: 4px 0;
    border-radius: 1px;
    box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
    z-index: 2;
}

@keyframes pulse-diamond {
    0%, 100% {
        transform: rotate(45deg) scale(1);
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
    }
    50% {
        transform: rotate(45deg) scale(1.2);
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.5);
    }
}

/* Tab styling - Improved modern design */
.stButton > button {
    background: #2a2a2a !important;
    color: #0088ff !important;
    border: 1px solid #666666 !important;
    font-weight: 600 !important;
    font-size: 1.1rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3) !important;
    height: 4rem !important;
    border-radius: 15px !important;
    position: relative !important;
    overflow: hidden !important;
}

.stButton > button::before {
    content: '' !important;
    position: absolute !important;
    top: 0 !important;
    left: -100% !important;
    width: 100% !important;
    height: 100% !important;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent) !important;
    transition: left 0.5s ease !important;
}

.stButton > button:hover::before {
    left: 100% !important;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0 8px 30px rgba(255, 255, 255, 0.1) !important;
    background: #3a3a3a !important;
    border-color: #999999 !important;
}

/* Active tab styling */
.stButton > button:focus,
.stButton > button:active {
    background: #0088ff !important;
    color:#ffffff !important;
    border-color: #cccccc !important;
    transform: translateY(-2px) scale(1.03) !important;
    box-shadow: 0 10px 40px rgba(255, 255, 255, 0.2) !important;
    font-weight: 700 !important;
}

/* Content area - Full width within the 75% container */
.content-area {
    background: #7fffff;
    padding: 3rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    border: 1px solid #666666;
    min-height: 70vh;
    width: 100%;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    position: relative;
    overflow: hidden;
}

.content-area h2 {
    color: #0088ff;
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
    font-weight: 700;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.content-area h3 {
    color: #cccccc;
    font-size: 1.5rem;
    margin-bottom: 1.2rem;
    font-weight: 600;
}

.content-area p {
    color: #999999;
    font-size: 1.2rem;
    line-height: 1.8;
    margin-bottom: 1.5rem;
}

/* Full-width grid layouts for content within the 75% container */
.full-width-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    width: 100%;
    margin: 2rem 0;
}

.grid-item {
    background: #2a2a2a;
    padding: 2rem;
    border-radius: 15px;
    border: 1px solid #666666;
    transition: all 0.3s ease;
}

.grid-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(255, 255, 255, 0.1);
    background: #333333;
}

/* Footer styling - Full width within container */
.footer {
    background: #7fffff;
    padding: 2rem;
    border-radius: 20px;
    text-align: center;
    margin-top: 3rem;
    border: 1px solid #666666;
    width: 100%;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

/* Footer button styling - Enhanced */
.footer .stButton > button {
    height: 4rem !important;
    font-weight: 700 !important;
    border-radius: 15px !important;
    border: none !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    font-size: 1.1rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    position: relative !important;
    overflow: hidden !important;
}

.footer .stButton > button::before {
    content: '' !important;
    position: absolute !important;
    top: 0 !important;
    left: -100% !important;
    width: 100% !important;
    height: 100% !important;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent) !important;
    transition: left 0.6s ease !important;
}

.footer .stButton > button:hover::before {
    left: 100% !important;
}

/* Refresh Button */
.footer div[data-testid="column"]:nth-child(1) .stButton > button {
    background: #666666 !important;
    color: #0088ff !important;
    box-shadow: 0 6px 20px rgba(255, 255, 255, 0.1) !important;
}

.footer div[data-testid="column"]:nth-child(1) .stButton > button:hover {
    transform: translateY(-3px) scale(1.05) !important;
    box-shadow: 0 10px 30px rgba(255, 255, 255, 0.2) !important;
    background: #333333 !important;
}

/* Generate Presentation Button */
.footer div[data-testid="column"]:nth-child(2) .stButton > button {
    background: #0088ff !important;
    color:#ffffff !important;
    box-shadow: 0 6px 20px rgba(255, 255, 255, 0.2) !important;
}

.footer div[data-testid="column"]:nth-child(2) .stButton > button:hover {
    transform: translateY(-3px) scale(1.05) !important;
    box-shadow: 0 10px 30px rgba(255, 255, 255, 0.3) !important;
    background: #cccccc !important;
}

/* Input styling - Modern glassmorphism */
.stSelectbox > div > div > div,
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: #2a2a2a !important;
    color: #0088ff !important;
    border: 1px solid #666666 !important;
    border-radius: 10px !important;
    font-size: 1.1rem !important;
    transition: all 0.3s ease !important;
}

.stSelectbox > div > div > div:focus,
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #999999 !important;
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.1) !important;
    background: #333333 !important;
}

/* File uploader styling */
.stFileUploader > div {
    background: #2a2a2a !important;
    border: 2px dashed #666666 !important;
    border-radius: 15px !important;
    padding: 2rem !important;
    transition: all 0.3s ease !important;
}

.stFileUploader > div:hover {
    border-color: #999999 !important;
    background: #333333 !important;
}

.stFileUploader label, .stFileUploader p, .stFileUploader svg {
    color: #0088ff !important;
    fill: #0088ff !important;
}

/* Sidebar removal */
.css-1d391kg {
    display: none !important;
}

/* Hide Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stToolbar {visibility: hidden;}

/* Custom scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #2a2a2a;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: #666666;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #999999;
}

/* Responsive design */
@media (max-width: 768px) {
    .block-container {
        max-width: 95% !important;
        width: 95% !important;
        left: 2.5% !important;
        right: 2.5% !important;
    }
    
    .main-header h1 {
        font-size: 2.5rem;
    }
    
    .content-area {
        padding: 1.5rem;
    }
    
    .stButton > button {
        height: 3rem !important;
        font-size: 0.9rem !important;
    }
}

/* Loading animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.content-area {
    animation: fadeInUp 0.6s ease-out;
}

/* Enhanced metrics and cards */
.metric-card {
    background: #2a2a2a;
    border: 1px solid #666666;
    border-radius: 15px;
    padding: 2rem;
    text-align: center;
    transition: all 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(255, 255, 255, 0.1);
    background: #333333;
}

.metric-value {
    font-size: 2.5rem;
    font-weight: 800;
    color: #0088ff;
    margin-bottom: 0.5rem;
}

.metric-label {
    color: #999999;
    font-size: 1.1rem;
    font-weight: 500;
}
</style>
"""
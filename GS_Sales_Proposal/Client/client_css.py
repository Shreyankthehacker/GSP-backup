client_css = """
<style>
    .client-section {
        background: #f5f5f5;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
        color: #2a2a2a;
    }
    
    .url-section {
        background: #f5f5f5;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #764ba2;
        margin-bottom: 1rem;
        color: #2a2a2a;
    }
    
    .document-section {
        background: #f5f5f5;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #5a9f9f;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
        color: #2a2a2a;
    }
    
    .pain-points-section {
        background: #f5f5f5;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #ffc107;
        color: #2a2a2a;
    }
    
    .roles-section {
        background: #f5f5f5;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2196f3;
        color: #2a2a2a;
    }
    
    .priorities-section {
        background: #f5f5f5;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #9c27b0;
        color: #2a2a2a;
    }
    
    .ai-suggestion-section {
        background: #f5f5f5;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #00bcd4;
        color: #2a2a2a;
    }
    
    .upload-section {
        border: 2px dashed #667eea;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        background: #f5f5f5;
        color: #2a2a2a;
    }
    
    /* Style section headers */
    .section-header {
        color: #2a2a2a;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    /* Mandatory field styling */
    .mandatory-label {
        color: #e74c3c;
        font-weight: 600;
    }
    
    .field-warning {
        color: #e74c3c;
        font-size: 0.85rem;
        margin-top: 0.25rem;
        font-weight: 500;
        background: rgba(231, 76, 60, 0.1);
        padding: 0.5rem;
        border-radius: 4px;
        border-left: 3px solid #e74c3c;
    }
    
    .optional-label {
        color: #666666;
        font-size: 0.8rem;
        font-style: italic;
    }
    
    .ai-label {
        color: #00bcd4;
        font-size: 0.8rem;
        font-style: italic;
    }
    
    /* Custom styling for URL buttons */
    .url-button-container {
        display: flex;
        gap: 5px;
        align-items: center;
    }
    
    .url-button {
        background: #667eea;
        color: white;
        border: none;
        padding: 8px 12px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 14px;
        transition: background-color 0.3s;
    }
    
    .url-button:hover {
        background: #5a6fd8;
    }
    
    /* Summary item styling */
    .summary-item {
        background: #f5f5f5;
        border: 1px solid #5a9f9f;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 8px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #2a2a2a;
    }
    
    .summary-key {
        font-weight: 600;
        color: #667eea;
    }
    
    .add-button {
        background: #28a745;
        color: white;
        border: none;
        padding: 6px 12px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 12px;
        font-weight: bold;
    }
    
    .add-button:hover {
        background: #218838;
    }
    
    .summary-buttons {
        display: flex;
        gap: 8px;
        margin-bottom: 12px;
    }
    
    .summary-control-btn {
        background: #007bff;
        color: white;
        border: none;
        padding: 6px 12px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 12px;
    }
    
    .summary-control-btn:hover {
        background: #0056b3;
    }
    
    /* Fixed tooltip label alignment */
    .tooltip-label {
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 6px;
        height: 24px;
        line-height: 24px;
        min-height: 32px;
        display: flex;
        align-items: flex-end;
    }
    
    .tooltip-icon {
        position: relative;
        display: inline-block;
        cursor: pointer;
        margin-left: 0;
    }
    
    .tooltip-icon::after {
        content: attr(data-tooltip);
        visibility: hidden;
        width: 250px;
        background-color: #555;
        color: #fff;
        text-align: left;
        border-radius: 6px;
        padding: 8px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -125px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .tooltip-icon:hover::after {
        visibility: visible;
        opacity: 1;
    }
    
    /* Streamlit input elements styling - ALL INPUTS */
    
    /* Text Input */
    .stTextInput > div > div > input {
        background-color: #f5f5f5 !important;
        color: #2a2a2a !important;
        border: 2px solid #5a9f9f !important;
        border-radius: 8px !important;
        padding: 12px !important;
        font-size: 14px !important;
    }
    
    /* Text Area */
    .stTextArea > div > div > textarea {
        background-color: #f5f5f5 !important;
        color: #2a2a2a !important;
        border: 2px solid #5a9f9f !important;
        border-radius: 8px !important;
        padding: 12px !important;
        font-size: 14px !important;
    }
    
    /* Number Input */
    .stNumberInput > div > div > input {
        background-color: #f5f5f5 !important;
        color: #2a2a2a !important;
        border: 2px solid #5a9f9f !important;
        border-radius: 8px !important;
        padding: 12px !important;
        font-size: 14px !important;
    }
    
    /* Select Box */
    .stSelectbox > div > div > div {
        background-color: #f5f5f5 !important;
        color: #2a2a2a !important;
        border: 2px solid #5a9f9f !important;
        border-radius: 8px !important;
    }
    
    /* Multiselect */
    .stMultiSelect > div > div > div {
        background-color: #f5f5f5 !important;
        color: #2a2a2a !important;
        border: 2px solid #5a9f9f !important;
        border-radius: 8px !important;
    }
    
    /* Date Input */
    .stDateInput > div > div > input {
        background-color: #f5f5f5 !important;
        color: #2a2a2a !important;
        border: 2px solid #5a9f9f !important;
        border-radius: 8px !important;
        padding: 12px !important;
        font-size: 14px !important;
    }
    
    /* Time Input */
    .stTimeInput > div > div > input {
        background-color: #f5f5f5 !important;
        color: #2a2a2a !important;
        border: 2px solid #5a9f9f !important;
        border-radius: 8px !important;
        padding: 12px !important;
        font-size: 14px !important;
    }
    
    /* File Uploader */
    .stFileUploader > div > div {
        background-color: #f5f5f5 !important;
        color: #2a2a2a !important;
        border: 2px solid #5a9f9f !important;
        border-radius: 8px !important;
    }
    
    /* REDUCED HEIGHT FOR UPLOADED FILE DISPLAY */
    /* Target the uploaded file container */
    .stFileUploader div[data-testid="stFileUploaderFileName"] {
        min-height: 30px !important;
        height: 30px !important;
        padding: 4px 8px !important;
        margin: 2px 0 !important;
        display: flex !important;
        align-items: center !important;
        color: #999999 !important;
        font-size: 12px !important;
        line-height: 1.2 !important;
    }
    
    /* Reduce height of the file uploader section after upload */
    .stFileUploader section[data-testid="stFileUploaderDropzone"] {
        min-height: 40px !important;
        height: auto !important;
        padding: 8px !important;
        margin: 4px 0 !important;
    }
    
    /* Target any uploaded file display elements */
    .stFileUploader [data-testid="fileUploaderFileName"],
    .stFileUploader [data-testid="stFileUploaderFileName"] > div,
    .stFileUploader div[role="button"] {
        min-height: 30px !important;
        height: 30px !important;
        padding: 4px 8px !important;
        margin: 2px 0 !important;
        line-height: 1.2 !important;
        font-size: 12px !important;
    }
    
    /* Compact the entire file uploader when files are uploaded */
    .stFileUploader:has([data-testid="stFileUploaderFileName"]) {
        min-height: 40px !important;
    }
    
    .stFileUploader:has([data-testid="stFileUploaderFileName"]) > div {
        min-height: 40px !important;
        padding: 4px !important;
    }
    
    /* File Uploader - Uploaded file display text (light grey) */
    .stFileUploader div[data-testid="stFileUploaderFileName"],
    .stFileUploader div[data-testid="fileUploaderDropzone"] span,
    .stFileUploader div[data-testid="fileUploaderDropzone"] p,
    .stFileUploader section span,
    .stFileUploader section p,
    .stFileUploader [data-testid="fileUploaderFileName"],
    .stFileUploader small {
        color: #999999 !important; /* Light grey for uploaded file names and text */
        font-size: 12px !important;
        line-height: 1.2 !important;
    }
    
    /* File uploader drag and drop area */
    .stFileUploader section {
        background-color: #f5f5f5 !important;
        border: 2px dashed #5a9f9f !important;
        border-radius: 8px !important;
    }
    
    /* File uploader text content - making it light grey */
    .stFileUploader section div,
    .stFileUploader section span,
    .stFileUploader section small {
        color: #999999 !important; /* Light grey for all file uploader text */
        font-size: 12px !important;
        line-height: 1.2 !important;
    }
    
    /* Color Picker */
    .stColorPicker > div > div > input {
        background-color: #f5f5f5 !important;
        border: 2px solid #5a9f9f !important;
        border-radius: 8px !important;
    }
    
    /* Focus states for all inputs */
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stNumberInput > div > div > input:focus,
    .stDateInput > div > div > input:focus,
    .stTimeInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2) !important;
        outline: none !important;
        background-color: #f5f5f5 !important;
        color: #2a2a2a !important;
    }
    
    /* Active/typing states to ensure text stays visible */
    .stTextInput > div > div > input:active,
    .stTextArea > div > div > textarea:active,
    .stNumberInput > div > div > input:active,
    .stDateInput > div > div > input:active,
    .stTimeInput > div > div > input:active {
        background-color: #f5f5f5 !important;
        color: #2a2a2a !important;
    }
    
    /* Placeholder text for all inputs */
    .stTextInput > div > div > input::placeholder,
    .stTextArea > div > div > textarea::placeholder,
    .stNumberInput > div > div > input::placeholder,
    .stDateInput > div > div > input::placeholder,
    .stTimeInput > div > div > input::placeholder {
        color: #666666 !important;
        opacity: 0.7 !important;
    }
    
    /* Labels for all input types */
    .stTextInput > label,
    .stTextArea > label,
    .stNumberInput > label,
    .stSelectbox > label,
    .stMultiSelect > label,
    .stDateInput > label,
    .stTimeInput > label,
    .stFileUploader > label,
    .stColorPicker > label {
        color: #2a2a2a !important;
        font-weight: 600 !important;
        margin-bottom: 8px !important;
    }
    
    /* Dropdown options styling */
    .stSelectbox div[data-baseweb="select"] > div > div,
    .stMultiSelect div[data-baseweb="select"] > div > div {
        background-color: #f5f5f5 !important;
    }
    
input,
textarea,
select,
.stSelectbox,
.stMultiSelect {
    color: #2a2a2a !important;
}

</style>
"""
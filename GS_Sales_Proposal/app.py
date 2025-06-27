import streamlit as st
import time
from Client.client import client_tab,validate_client_mandatory_fields
from Seller.seller import seller_tab

def get_sample_extracted_text():
            return """Key Requirements Extracted:

• Project Type: Enterprise Software Development
• Timeline: 6-8 months
• Budget Range: $150,000 - $200,000
• Team Size: 5-7 developers
• Technologies: React, Node.js, PostgreSQL
• Deployment: AWS Cloud Infrastructure
• Security: SOC 2 compliance required
• Integration: Salesforce, HubSpot APIs
• Support: 24/7 monitoring and maintenance

Additional Notes:
- Client prefers agile methodology
- Weekly progress reports required
- UAT phase: 4 weeks
- Go-live date: Q3 2024"""

def refresh_all_data():
    """Clear all session state and form data"""
    # Clear all session state variables
    keys_to_clear = [
        'client_name_input', 'url_selector', 'pain_points', 'pain_points_extracted',
        'pain_points_placeholder', 'editable_content_area', 'pain_points_summary',
        'selected_roles', 'selected_priorities', 'problem_statement'
    ]
    
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]
    
    # Clear any other dynamic keys (role and priority related)
    keys_to_remove = []
    for key in st.session_state.keys():
        if (key.startswith('role_edit_input_') or 
            key.startswith('remove_role_btn_') or 
            key.startswith('priority_checkbox_')):
            keys_to_remove.append(key)
    
    for key in keys_to_remove:
        del st.session_state[key]
    
    st.success("All data has been cleared!")
    st.rerun()


def validate_seller_mandatory_fields():
    """Validate seller mandatory fields"""
    # Add your seller validation logic here
    # For now, returning True as placeholder
    return True

def validate_project_mandatory_fields():
    """Validate project specification mandatory fields"""
    # Add your project validation logic here
    # For now, returning True as placeholder
    return True

def show_validation_popup(missing_tab_name, missing_fields=None):
    """Show validation error popup"""
    st.error(f"⚠️ Please complete all mandatory fields in {missing_tab_name} tab first!")
    if missing_fields:
        st.error(f"Missing required fields: {missing_fields}")

def validate_mandatory_fields():
    """Validate mandatory fields and return validation results"""
    errors = []
    
    # Check client name
    client_name = st.session_state.get('client_name_input', '').strip()
    if not client_name:
        errors.append("Client Name")
    
    # Check problem statement
    problem_statement = st.session_state.get('problem_statement', '').strip()
    if not problem_statement:
        errors.append("Problem Statement")
    
    return errors

def generate_presentation():
    """Generate presentation after validating mandatory fields"""
    validation_errors = validate_mandatory_fields()
    
    if validation_errors:
        # Trigger validation display in client tab
        st.session_state.trigger_validation = True
        st.session_state.show_validation = True
        
        # Show error message
        st.error("⚠️ Please fill in all mandatory fields before generating presentation!")
        
        # Show specific missing fields
        missing_fields = ", ".join(validation_errors)
        st.error(f"Missing required fields: {missing_fields}")
        
        # Force rerun to show validation warnings
        st.rerun()
        return False
    else:
        st.success("✅ All mandatory fields are filled! Generating presentation...")
        with st.spinner("Generating presentation..."):
            import time
            time.sleep(2)  # Simulate processing time
        st.success("🎉 Presentation generated successfully!")
        
        # You can add your actual presentation generation logic here
        # For example:
        # - Create PowerPoint slides
        # - Generate PDF report
        # - Send to external API
        # - Save to database
        
        return True

# NOTE: Add this line at the very top of your main script (before any other Streamlit commands):
# st.set_page_config(page_title="Sales Proposal Generator", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")
        
from main_css import *
st.markdown(app_css, unsafe_allow_html=True)

# Initialize session state for active tab - ENSURE CLIENT TAB IS DEFAULT
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 0

# Tab buttons
tab_names = ["Client Information", "Seller Information", "Project Specifications", "Generate Proposal"]

# Create tab buttons with full width
cols = st.columns(4, gap="large")
for i, tab_name in enumerate(tab_names):
    with cols[i]:
        is_active = (i == st.session_state.active_tab)
        
        # Determine if tab should be clickable based on validation
        tab_enabled = True
        if i == 1 and not validate_client_mandatory_fields():
            tab_enabled = False
        elif i == 2 and (not validate_client_mandatory_fields() or not validate_seller_mandatory_fields()):
            tab_enabled = False
        elif i == 3 and (not validate_client_mandatory_fields() or not validate_seller_mandatory_fields() or not validate_project_mandatory_fields()):
            tab_enabled = False
        
        if tab_enabled:
            if st.button(tab_name, key=f"tab_{i}", use_container_width=True, type="primary" if is_active else "secondary"):
                st.session_state.active_tab = i
                st.rerun()
        else:
            st.button(tab_name, key=f"tab_{i}", use_container_width=True, disabled=True)

# Force active tab to stay highlighted
# Force active tab to stay highlighted with blue color
# Force active tab (Client or any valid tab) to stay blue
tab_highlight_css = f"""
<style>
/* Apply blue style to the active tab */
div[data-testid="column"]:nth-child({st.session_state.active_tab + 1}) button {{
    background-color: #1976d2 !important;
    color: white !important;
    border: 2px solid #115293 !important;
    font-weight: bold !important;
    transition: 0.3s ease;
}}

/* Keep it blue on hover/focus */
div[data-testid="column"]:nth-child({st.session_state.active_tab + 1}) button:hover,
div[data-testid="column"]:nth-child({st.session_state.active_tab + 1}) button:focus {{
    background-color: #1565c0 !important;
    color: white !important;
}}
</style>
"""
st.markdown(tab_highlight_css, unsafe_allow_html=True)

# Set is_active flag for current tab
st.session_state.is_active = True

# Content area with validation-aware tab switching
if st.session_state.active_tab == 0:
    client_tab(st)

elif st.session_state.active_tab == 1:
    # Double-check validation before showing seller tab
    if validate_client_mandatory_fields():
        seller_tab()
    else:
        st.session_state.active_tab = 0  # Force back to client tab
        show_validation_popup("Client Information")
        st.rerun()

elif st.session_state.active_tab == 2:
    # Check both client and seller validations
    if not validate_client_mandatory_fields():
        st.session_state.active_tab = 0  # Force back to client tab
        show_validation_popup("Client Information")
        st.rerun()
    elif not validate_seller_mandatory_fields():
        st.session_state.active_tab = 1  # Force back to seller tab
        show_validation_popup("Seller Information")
        st.rerun()
    else:
        st.markdown('## 👥 Project Specifications')
        st.markdown("Define your project requirements and specifications.")
        
        col1, col2, col3 = st.columns([2, 2, 2], gap="large")
        
        with col1:
            st.markdown("""
            **Recent Clients**
            - Acme Corporation
            - TechStart Inc
            - Global Solutions Ltd
            - Innovation Labs
            - Digital Dynamics
            - Future Systems Co
            """)
        
        with col2:
            st.metric("Total Proposals", "47", "+12%")
            
        with col3:
            st.metric("Success Rate", "73%", "+5%")

else:  # Generate Proposal Tab
    # Check all validations
    if not validate_client_mandatory_fields():
        st.session_state.active_tab = 0
        show_validation_popup("Client Information")
        st.rerun()
    elif not validate_seller_mandatory_fields():
        st.session_state.active_tab = 1
        show_validation_popup("Seller Information")
        st.rerun()
    elif not validate_project_mandatory_fields():
        st.session_state.active_tab = 2
        show_validation_popup("Project Specifications")
        st.rerun()
    else:
        st.markdown('## 📊 Generate Proposal')
        st.markdown("Review and generate your final proposal.")
        
        # Metrics row
        col1, col2, col3, col4 = st.columns(4, gap="large")
        
        with col1:
            st.metric("This Month", "$125K", "+15%")
        
        with col2:
            st.metric("Proposals Sent", "23", "+3")
        
        with col3:
            st.metric("Conversion Rate", "68%", "+12%")
            
        with col4:
            st.metric("Average Value", "$18.5K", "+8%")
        
        st.markdown("---")
        
        st.markdown("""
        ### 📈 Performance Trends
        Your proposal success rate has improved by 12% this quarter, with the highest performance in software development projects. The average deal size has increased significantly, and client satisfaction scores are at an all-time high.
        
        **Key insights:** Enterprise clients show 85% higher conversion rates, and proposals with detailed technical specifications convert 40% better than generic templates.
        """)

col1, col2 = st.columns(2, gap="large")

with col1:
    if st.button("🔄 Refresh All Data", key="refresh_btn", use_container_width=True):
        refresh_all_data()

with col2:
    if st.button("📊 Generate Presentation", key="generate_btn", use_container_width=True):
        generate_presentation()
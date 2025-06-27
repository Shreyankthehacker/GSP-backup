import streamlit as st
from .seller_css import seller_css
from .seller_utils import *
from Search.Linkedin.linkedin_serp import *
from Recommendation.recommendation_utils import *
from t import *

def seller_tab():
    # Re-apply CSS after every rerun to ensure persistence
    st.markdown(seller_css, unsafe_allow_html=True)
    
    # Initialize validation trigger
    if 'show_validation' not in st.session_state:
        st.session_state.show_validation = False
    
    # Initialize enterprise details content in session state
    if 'seller_enterprise_details_content' not in st.session_state:
        st.session_state.seller_enterprise_details_content = ""
    
    # Initialize seller requirements content in session state
    if 'seller_requirements_content' not in st.session_state:
        st.session_state.seller_requirements_content = ""
    
    # Initialize URLs list in session state
    if 'seller_website_urls_list' not in st.session_state:
        st.session_state['seller_website_urls_list'] = []
    
    # Initialize last company name to track changes
    if 'last_seller_company_name' not in st.session_state:
        st.session_state['last_seller_company_name'] = ""
    
    # Initialize uploaded file path in session state
    if 'seller_uploaded_file_path' not in st.session_state:
        st.session_state['seller_uploaded_file_path'] = None
    
    # Initialize RFI pain points items in session state
    if 'seller_rfi_pain_points_items' not in st.session_state:
        st.session_state['seller_rfi_pain_points_items'] = {}
    
    # Initialize document analysis status
    if 'seller_document_analyzed' not in st.session_state:
        st.session_state['seller_document_analyzed'] = False
    
    if 'seller_linkedin_profiles' not in st.session_state:
        st.session_state['seller_linkedin_profiles'] = {}
    if 'last_searched_seller_spoc' not in st.session_state:
        st.session_state['last_searched_seller_spoc'] = ""
    
    # Initialize scraping states
    if 'seller_scraping_in_progress' not in st.session_state:
        st.session_state['seller_scraping_in_progress'] = False
    if 'seller_pending_scrape_url' not in st.session_state:
        st.session_state['seller_pending_scrape_url'] = None

    # Top section with seller name and URLs
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
            <div class="tooltip-label">
                Seller Enterprise Name <span style="color:red;">*</span>
                <div class="tooltip-icon" data-tooltip="Enter the full legal name of the seller organization. This is the primary identifier for the seller in all documentation and communications. This field is mandatory for creating the seller profile.">ⓘ</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Create a sub-column layout for name input and find URLs button
        name_col, button_col = st.columns([3, 1])
        
        with name_col:
            seller_enterprise_name = st.text_input(
                label="Seller Enterprise Name", 
                placeholder="Enter seller enterprise name...", 
                key="seller_enterprise_name_input",
                label_visibility="collapsed"
            )
        
        with button_col:
            # Find URLs button - only enabled when seller name has more than 2 characters
            find_urls_disabled = not (seller_enterprise_name and len(seller_enterprise_name.strip()) > 2)
            
            if st.button("🔍 Find Website",
                        disabled=find_urls_disabled,
                        help="Find website URLs for this company",
                        key="find_seller_urls_button"):
                # Add spinner while fetching URLs
                with st.spinner(f"Finding Websites for '{seller_enterprise_name.strip()}'..."):
                    try:
                        st.session_state['seller_website_urls_list'] = get_urls_list(seller_enterprise_name.strip())
                        st.session_state['last_seller_company_name'] = seller_enterprise_name
                    except Exception as e:
                        st.session_state['seller_website_urls_list'] = []
                        st.error(f"Error finding URLs: {str(e)}")
        
        # Clear URLs if company name is cleared
        if not seller_enterprise_name and st.session_state['last_seller_company_name']:
            st.session_state['seller_website_urls_list'] = []
            st.session_state['last_seller_company_name'] = ""
        
        # Show validation warning if triggered and field is empty
        if st.session_state.show_validation and check_field_validation("Seller Enterprise Name", seller_enterprise_name, True):
            show_field_warning("Seller Enterprise Name")
    
    with col2:
        # Label row with inline emoji and tooltip
        st.markdown('''
        <div class="tooltip-label" style="display: flex; align-items: center; gap: 8px;">
            <span>Seller Website URL</span>
            <div class="tooltip-icon" data-tooltip="Enter or select the seller's official website URL. The system will automatically analyze the website to extract company information, services, and business details to help understand the seller's capabilities and offerings.">ⓘ</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Create columns for dropdown and buttons - dropdown takes most space, buttons share remaining space
        url_col, btn1_col, btn2_col, btn3_col = st.columns([7, 1, 1, 1])
        
        with url_col:
            # URL selection logic - Always show normal dropdown, just disable when no seller name
            seller_name_provided = bool(seller_enterprise_name and seller_enterprise_name.strip())
            
            if not st.session_state.get('seller_website_urls_list'):
                # No URLs available - show default option
                url_options = ["Select seller website URL"]
            else:
                # URLs available - show them in dropdown
                url_options = ["Select seller website URL"] + st.session_state['seller_website_urls_list']
            
            seller_website_url = st.selectbox(
                label="Seller Website URL",
                options=url_options,
                key="seller_website_url_selector",
                label_visibility="collapsed",
                disabled=not seller_name_provided,
                accept_new_options=True
            )
            
            # Reset to empty string if default option is selected
            if seller_website_url == "Select seller website URL":
                seller_website_url = ""
        
        # Each button in its own column for horizontal alignment
        with btn1_col:
            if seller_website_url:
                st.link_button("🌐", seller_website_url, help="Visit website",use_container_width=True)
            else:
                st.button("🌐", help="Visit website", disabled=True,use_container_width=True)
        with btn2_col:
            # Button 2: Refresh URL List
            refresh_clicked = st.button("🔄", help="Refresh website URLs list", key="refresh_seller_urls_btn",use_container_width=True,disabled=not seller_website_url)
        
        with btn3_col:
            # Button 3: Scrape Website - Set up pending scrape instead of immediate execution
            scrape_clicked = st.button("📑", help="Get enterprise details", key="scrape_seller_website_btn",use_container_width=True, disabled=not seller_website_url)
            
            # Handle scrape button click by setting up pending operation
            if scrape_clicked and seller_website_url:
                st.session_state['seller_pending_scrape_url'] = seller_website_url
                st.session_state['seller_scraping_in_progress'] = True
                st.rerun()

        # Handle refresh action outside columns for better UX
        if refresh_clicked and seller_name_provided:
            try:
                with st.spinner("Refreshing website URLs..."):
                    st.session_state['seller_website_urls_list'] = get_urls_list(seller_enterprise_name)
                    st.success("Website URLs refreshed!")
                    st.rerun()  # Refresh the page to show updated URLs
            except Exception as e:
                st.error(f"Error refreshing URLs: {str(e)}")

        # Handle pending scraping operation OUTSIDE of columns to prevent UI blocking
        if st.session_state.get('seller_scraping_in_progress') and st.session_state.get('seller_pending_scrape_url'):
            # Show full-width spinner
            with st.spinner(f"Scraping website details from {st.session_state['seller_pending_scrape_url']}..."):
                try:
                    # Perform the scraping operation
                    website_details = get_url_details(st.session_state['seller_pending_scrape_url'])
                    st.session_state.seller_enterprise_details_content = website_details
                    st.session_state['last_analyzed_seller_url'] = st.session_state['seller_pending_scrape_url']
                    
                    # Clear pending operation
                    st.session_state['seller_scraping_in_progress'] = False
                    st.session_state['seller_pending_scrape_url'] = None
                    
                    st.success("Website details extracted successfully!")
                    st.rerun()  # Refresh to show updated details
                    
                except Exception as e:
                    # Clear pending operation on error
                    st.session_state['seller_scraping_in_progress'] = False
                    st.session_state['seller_pending_scrape_url'] = None
                    st.error(f"Error scraping website: {str(e)}")

    # Show validation warning if triggered and field is empty (optional)
    if st.session_state.show_validation and check_field_validation("Seller Website URL", seller_website_url, False):
        show_field_warning("Seller Website URL")


#-------------------------------------------------------------------------------

    st.markdown('''
    <div class="tooltip-label">
        Upload Seller Document
        <div class="tooltip-icon" data-tooltip="Upload seller-related documents such as company profiles, service catalogs, capabilities documents, or proposals in PDF, DOCX, TXT, or CSV format. The system will automatically analyze and extract key capabilities, services, and business strengths to help understand the seller's offerings.">ⓘ</div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Add custom CSS for file uploader and animations
    st.markdown("""
    <style>
    .stFileUploader > div > div > div {
        padding: 0.5rem !important;
        min-height: 2rem !important;
    }
    .stFileUploader > div > div {
        min-height: 2rem !important;
    }
    [data-testid="stFileUploader"] {
        height: auto !important;
    }
    [data-testid="stFileUploader"] > div {
        padding: 0.25rem 0.5rem !important;
        min-height: 2rem !important;
    }
    
    /* Animation for processing file */
    .processing-file {
        animation: pulse 1.5s ease-in-out infinite;
        background: linear-gradient(90deg, #e3f2fd, #bbdefb, #e3f2fd);
        background-size: 200% 100%;
        animation: shimmer 2s linear infinite;
        border-radius: 4px;
        padding: 2px 4px;
    }
    
    @keyframes pulse {
        0% { opacity: 0.6; }
        50% { opacity: 1; }
        100% { opacity: 0.6; }
    }
    
    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    
    .analyzing-text {
        color: #1976d2;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # FILE UPLOAD - Always enabled, independent of seller name (multiple files)
    seller_documents_upload = st.file_uploader(
        label="Upload Seller Documents", 
        type=['pdf', 'docx', 'txt', 'csv','png','jpg','jpeg'], 
        key="seller_documents_uploader",
        label_visibility="collapsed",
        accept_multiple_files=True
    )
    
    # Initialize processing states and file tracking
    if 'processing_all_seller_documents' not in st.session_state:
        st.session_state['processing_all_seller_documents'] = False
    if 'seller_uploaded_files_paths' not in st.session_state:
        st.session_state['seller_uploaded_files_paths'] = {}
    if 'seller_services_by_file' not in st.session_state:
        st.session_state['seller_services_by_file'] = {}
    
    # Show file info and single analyze button for all files
    if seller_documents_upload is not None and len(seller_documents_upload) > 0:
        st.markdown("**Uploaded Documents:**")
        
        # Display all uploaded files
        for idx, uploaded_file in enumerate(seller_documents_upload):
            file_key = f"{uploaded_file.name}_{uploaded_file.size}"  # Unique key for each file
            
            # Very compact single line display
            file_size_kb = round(uploaded_file.size / 1024, 1)
            file_size_display = f"{file_size_kb}KB" if file_size_kb < 1024 else f"{round(file_size_kb/1024, 1)}MB"
            
            # Check if this file has been processed
            is_processed = file_key in st.session_state.get('seller_services_by_file', {})
            is_processing = st.session_state.get('processing_all_seller_documents', False)
            
            if is_processing:
                # Show animated processing state
                st.markdown(f"""
                <div class="processing-file">
                    <span style='font-size:0.8em' class="analyzing-text">
                        🔄 {uploaded_file.name[:25]}{'...' if len(uploaded_file.name) > 25 else ''} (Analyzing...)
                    </span>
                </div>
                """, unsafe_allow_html=True)
            else:
                # Show normal file info with status
                status_icon = "✅" if is_processed else "📄"
                st.markdown(f"<span style='font-size:0.8em'>{status_icon} {uploaded_file.name[:30]}{'...' if len(uploaded_file.name) > 30 else ''} ({file_size_display})</span>", 
                        unsafe_allow_html=True)
        
        # Single button to process all files
        st.markdown("---")  # Separator line
        
        # Check if all files are already processed
        all_processed = all(
            f"{file.name}_{file.size}" in st.session_state.get('seller_services_by_file', {})
            for file in seller_documents_upload
        )
        
        is_processing = st.session_state.get('processing_all_seller_documents', False)
        
        # Button styling
        if all_processed:
            button_color = "#28a745"  # Green for all processed
            button_text = "All Documents Processed"
            button_disabled = True
        elif is_processing:
            button_color = "#FF6B6B"  # Red for processing
            button_text = "Analyzing All Documents..."
            button_disabled = True
        else:
            button_color = "#4CAF50"  # Blue for ready to process
            button_text = f"Get Services from All Documents ({len(seller_documents_upload)} files)"
            button_disabled = False

        st.markdown(f"""
        <style>
        div.stButton > button:first-child {{
            background-color: {button_color};
            color: white;
            border: none;
            font-weight: bold;
        }}
        </style>
        """, unsafe_allow_html=True)

        # Single analyze button for all files
        analyze_all_clicked = st.button(
            button_text,
            key="analyze_all_seller_documents_btn",
            help="Process all seller documents" if not button_disabled else "All documents processed" if all_processed else "Processing in progress...",
            type="secondary",
            disabled=button_disabled,
            use_container_width=True
        )
        
        # Handle analyze button click for all files
        if analyze_all_clicked and not button_disabled:
            if not seller_enterprise_name:
                st.error("❌ Please enter the Seller Enterprise Name first")
            else:
                # Set processing flag for all files
                st.session_state['processing_all_seller_documents'] = True
                st.rerun()  # Refresh to show processing state
        
        # Handle processing for all files when button is clicked
        if st.session_state.get('processing_all_seller_documents', False):
            # Show overall processing indicator
            with st.container():
                st.markdown("**🔍 Processing all documents and extracting services...**")
                
                # Process each file
                all_services = {}
                processed_count = 0
                total_files = len(seller_documents_upload)
                
                for idx, uploaded_file in enumerate(seller_documents_upload):
                    file_key = f"{uploaded_file.name}_{uploaded_file.size}"
                    
                    # Show progress for current file
                    progress_text = f"Processing {uploaded_file.name} ({idx + 1}/{total_files})..."
                    with st.spinner(progress_text):
                        try:
                            # Save the file and get the path
                            file_path = save_uploaded_file_and_get_path(uploaded_file)
                            st.session_state['seller_uploaded_files_paths'][file_key] = file_path
                            
                            if file_path and seller_enterprise_name:
                                # Extract services using the file path and company name
                                file_services = get_seller_services(file_path, seller_enterprise_name)
                                
                                # Store services data for this specific file
                                st.session_state['seller_services_by_file'][file_key] = {
                                    'filename': uploaded_file.name,
                                    'services': file_services,
                                    'file_path': file_path
                                }
                                
                                # Combine services from this file
                                if isinstance(file_services, dict):
                                    all_services.update(file_services)
                                
                                processed_count += 1
                                st.success(f"✅ {uploaded_file.name} processed successfully!")
                                
                            else:
                                st.error(f"❌ Error saving {uploaded_file.name}")
                                
                        except Exception as e:
                            st.error(f"❌ Error processing {uploaded_file.name}: {str(e)}")
                
                # Update combined services and reset processing flag
                st.session_state['seller_services_items'] = all_services
                st.session_state['seller_document_analyzed'] = True if processed_count > 0 else False
                st.session_state['processing_all_seller_documents'] = False
                
                # Show final summary
                if processed_count == total_files:
                    st.success(f"🎉 All {total_files} documents processed successfully!")
                elif processed_count > 0:
                    st.warning(f"⚠️ {processed_count} out of {total_files} documents processed successfully.")
                else:
                    st.error("❌ No documents could be processed.")
                
                st.rerun()  # Refresh to update UI
    
    # Function call for Seller Services Offered selection
    seller_enterprise_details, seller_enterprise_details_provided = render_three_column_selector_unified(
        # Column configuration - Made wider to fill screen
        column_ratio=(2, 2, 2),  # Equal wider columns
        column_gap="large",  # Increased gap for better spacing
        
        # Left column (text area) configuration
        left_title="Seller Enterprise Details",
        left_tooltip="Define your enterprise details, services offered, company capabilities, core competencies, and business portfolio. This information helps clients understand your organizational strengths and service offerings.",
        left_required=True,
        textarea_height=200,  # Increased height for better visibility
        textarea_placeholder="Enter seller enterprise name first to enable this field",
        textarea_session_key="seller_enterprise_content",
        textarea_widget_key="seller_enterprise_textarea",
        
        # Unified right section (middle + right columns) configuration
        unified_section_title="Available Services & Capabilities",
        unified_section_tooltip="Select from available services and capabilities that represent your enterprise offerings. These can include technical services, consulting, products, or specialized business solutions.",
        
        # Session state keys for both sides
        middle_selected_items_key="selected_services_offered",
        middle_content_map_key="services_content_map",
        right_selected_items_key="selected_additional_capabilities",
        right_content_map_key="capabilities_content_map",
        
        # Single data source that will be displayed in both columns
        default_data=None,  # You would pass your services data dictionary here
        split_ratio=(3, 3),  # How many items go to middle vs right column
        
        # Enable/disable conditions
        client_enabled_condition=True,
        client_name_provided=True,
        
        # Styling configuration
        button_column_width=2.5,  # Button width within each column
        content_column_width=6.5,   # Content area width within each column
        show_success_messages=False,
        selected_color="#2e7d32",  # Green color
        selected_border_color="#4caf50",  # Green border
        unselected_color="#404040",
        unselected_border_color="#404040",
        text_color="#ffffff",
        
        # Title styling - Made normal size like left title
        title_font_size="18px",  # Same as other titles
        title_color="#ffffff",
        title_margin_bottom="10px"  # Reduced margin
    )
import streamlit as st
from typing import *

def render_three_column_selector_unified(
    # Column configuration - Made wider to fill screen
    column_ratio: Tuple[float, float, float] = (2, 2, 2),  # Equal wider columns
    column_gap: str = "large",  # Increased gap for better spacing
    
    # Left column (text area) configuration
    left_title: str = "Client Requirements",
    left_tooltip: str = "Define the core client requirements, technical specifications, project scope, deliverables, and expected outcomes. This forms the foundation of your proposal and helps ensure all client needs are addressed.",
    left_required: bool = True,
    textarea_height: int = 300,  # Increased height for better visibility
    textarea_placeholder: str = "Enter client name first to enable this field",
    textarea_session_key: str = "client_requirements_content",
    textarea_widget_key: str = "client_requirements_textarea",
    
    # Unified right section (middle + right columns) configuration  
    unified_section_title: str = "Client Pain Points & Options",
    unified_section_tooltip: str = "Select from available pain points and options that will be added to your client requirements. These can be extracted from RFI documents or manually entered business challenges.",
    
    # Session state keys for both sides
    middle_selected_items_key: str = "selected_pain_points",
    middle_content_map_key: str = "pain_point_content_map",
    right_selected_items_key: str = "selected_additional_options", 
    right_content_map_key: str = "additional_content_map",
    
    # Single data source that will be displayed in both columns
    default_data: Optional[Dict[str, str]] = None,
    split_ratio: Tuple[int, int] = (3, 3),  # How many items go to middle vs right column
    
    # Enable/disable conditions
    client_enabled_condition: bool = True,
    client_name_provided: bool = True,
    
    # Styling configuration
    button_column_width: float = 2.5,  # Button width within each column
    content_column_width: float = 6.5,   # Content area width within each column
    show_success_messages: bool = False,
    selected_color: str = "#2e7d32",  # Green color
    selected_border_color: str = "#4caf50",  # Green border
    unselected_color: str = "#404040",
    unselected_border_color: str = "#404040",
    text_color: str = "#ffffff",
    
    # Title styling - Made normal size like left title
    title_font_size: str = "18px",  # Same as other titles
    title_color: str = "#ffffff",
    title_margin_bottom: str = "10px"  # Reduced margin
) -> Tuple[str, bool]:
    """
    Renders a three-column layout with text area on left, and a unified section on right 
    that spans both middle and right columns under one normal-sized title.
    
    Returns:
        Tuple of (textarea_content, requirements_provided_bool)
    """
    
    # Default data if none provided
    if default_data is None:
        default_data = {
            "Revenue Challenges": "**Revenue Challenges** • Sales declined by 15% year-over-year despite market growth\n• Missed quarterly revenue targets by $2.3M for three consecutive quarters\n• Average deal size decreased by 22% due to increased price competition\n\n",
            
            "Cost and Margin Pressure": "**Cost and Margin Pressure** • Cost of Goods Sold increased by 12% due to supply chain disruptions\n• Labor costs rose 18% while productivity remained flat\n• Raw material prices up 25% with limited ability to pass costs to customers\n\n",
            
            "Market Expansion": "**Market Expansion and Customer Acquisition**\n• Win rate on new business opportunities dropped from 42% to 28%\n• Customer acquisition cost increased 35% while customer lifetime value declined\n• Expansion into new geographic markets yielding only 40% of projected results\n\n",
            
            "Technology Modernization": "**Technology Modernization**\n• Legacy systems causing 40% slower processing times\n• Integration challenges between disparate systems\n• Security vulnerabilities in outdated infrastructure\n\n",
            
            "Workforce Development": "**Workforce Development**\n• Skills gap in emerging technologies affecting 60% of teams\n• Employee retention challenges with 25% annual turnover\n• Training programs yielding limited ROI\n\n",
            
            "Compliance & Risk": "**Compliance & Risk Management**\n• Regulatory compliance gaps creating audit risks\n• Data privacy requirements increasing operational complexity\n• Risk assessment processes outdated and manual\n\n"
        }
    
    # Split the data into two sets
    data_items = list(default_data.items())
    middle_count = split_ratio[0]
    
    # Split data
    middle_data = dict(data_items[:middle_count])
    right_data = dict(data_items[middle_count:])
    
    # Add CSS for styling
    st.markdown(f"""
    <style>
    /* Full width container styling */
    .element-container {{
        width: 100% !important;
        max-width: 100% !important;
    }}
    
    /* Ensure columns use full width */
    .stColumns {{
        width: 100% !important;
        gap: 2rem !important;
    }}
    
    /* Textarea styling */
    .stTextArea > div > div > textarea {{
        width: 100% !important;
        font-size: 16px !important;
        padding: 15px !important;
    }}
    
    /* Button styling */
    .stButton > button {{
        width: 100% !important;
        height: 70px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        margin: 8px 0 !important;
        border-radius: 12px !important;
        min-width: 100px !important;
    }}
    
    /* Content cards styling */
    .content-card {{
        width: 100% !important;
        margin: 6px 0 !important;
        padding: 15px !important;
        font-size: 15px !important;
        line-height: 1.4 !important;
    }}
    
    /* Normal section tooltip styling - same as left */
    .section-tooltip {{
        font-size: {title_font_size} !important;
        font-weight: bold !important;
        margin-bottom: {title_margin_bottom} !important;
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        color: {title_color};
    }}
    
    /* Unified title styling - normal size */
    .unified-title {{
        font-size: {title_font_size} !important;
        font-weight: bold !important;
        color: {title_color} !important;
        margin-bottom: {title_margin_bottom} !important;
        text-align: center !important;
        width: 100% !important;
        padding: 10px 0 !important;
        border-bottom: 2px solid #e0e0e0 !important;
    }}
    
    /* Invisible title spacer for perfect alignment */
    .section-tooltip[style*="visibility: hidden"] {{
        height: auto !important;
        width: 100% !important;
        display: flex !important;
        opacity: 0 !important;
    }}
    
    .tooltip-icon {{
        cursor: help;
        font-size: 14px;
        color: #888;
        margin-left: 8px;
    }}
    
    .tooltip-icon:hover::after {{
        content: attr(data-tooltip);
        position: absolute;
        background: #333;
        color: white;
        padding: 8px 12px;
        border-radius: 4px;
        font-size: 12px;
        white-space: nowrap;
        z-index: 1000;
        margin-top: 25px;
        margin-left: -100px;
        max-width: 250px;
        white-space: normal;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session state variables
    for key in [middle_selected_items_key, right_selected_items_key]:
        if key not in st.session_state:
            st.session_state[key] = set()
    
    for key in [middle_content_map_key, right_content_map_key]:
        if key not in st.session_state:
            st.session_state[key] = {}
    
    if textarea_session_key not in st.session_state:
        st.session_state[textarea_session_key] = ""
    
    # Create main THREE COLUMN layout - NO NESTING!
    col_left, col_middle, col_right = st.columns(column_ratio, gap=column_gap)
    
    # LEFT COLUMN - Text Area
    with col_left:
        # Title with tooltip and required indicator
        required_asterisk = ' <span style="color:red;">*</span>' if left_required else ''
        st.markdown(f'''
        <div class="section-tooltip">
            <span>{left_title}{required_asterisk}</span>
            <div class="tooltip-icon" data-tooltip="{left_tooltip}">ⓘ</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Text area
        client_requirements = st.text_area(
            label=left_title,
            value=st.session_state[textarea_session_key] if client_name_provided else "",
            height=textarea_height,
            key=textarea_widget_key,
            label_visibility="collapsed",
            disabled=not client_name_provided,
            placeholder=textarea_placeholder if not client_name_provided else ""
        )
        
        # Update session state when text area changes
        if client_name_provided:
            st.session_state[textarea_session_key] = client_requirements
        
        client_requirements_provided = bool(client_name_provided and client_requirements.strip())
    
    # MIDDLE COLUMN - First half of items
    with col_middle:
        # Show unified title only in middle column (spans conceptually)
        st.markdown(f'''
        <div class="section-tooltip">
            <span>{unified_section_title}</span>
            <div class="tooltip-icon" data-tooltip="{unified_section_tooltip}">ⓘ</div>
        </div>
        ''', unsafe_allow_html=True)
        # Display middle column items
        for i, (key, value) in enumerate(middle_data.items()):
            # Check if this item is selected
            is_selected = key in st.session_state[middle_selected_items_key]
            
            # Create button and content sub-columns WITHIN THIS COLUMN
            btn_col, content_col = st.columns([1, 4], gap="small")
            
            with btn_col:
                # Button
                button_text = "❌" if is_selected else "➕"
                button_help = f"Remove '{key}'" if is_selected else f"Add '{key}'"
                button_type = "secondary"
                
                if st.button(button_text,
                        key=f"toggle_middle_{middle_selected_items_key}_{i}",
                        help=button_help,
                        type=button_type,
                        disabled=not client_enabled_condition,
                        use_container_width=True):
                    
                    if is_selected:
                        # REMOVE FUNCTIONALITY
                        current_content = st.session_state.get(textarea_session_key, '')
                        original_content = st.session_state[middle_content_map_key].get(key, value)
                        
                        # Remove content patterns
                        patterns_to_remove = [
                            f"\n\n{original_content}",
                            f"{original_content}\n\n", 
                            original_content
                        ]
                        
                        updated_content = current_content
                        for pattern in patterns_to_remove:
                            updated_content = updated_content.replace(pattern, "")
                        
                        # Clean up excessive newlines
                        updated_content = '\n\n'.join([section.strip() for section in updated_content.split('\n\n') if section.strip()])
                        
                        # Update session state
                        st.session_state[textarea_session_key] = updated_content
                        st.session_state[middle_selected_items_key].discard(key)
                        if key in st.session_state[middle_content_map_key]:
                            del st.session_state[middle_content_map_key][key]
                        
                        if show_success_messages:
                            st.success(f"🗑️ '{key}' removed!")
                    
                    else:
                        # ADD FUNCTIONALITY
                        current_content = st.session_state.get(textarea_session_key, '')
                        new_content = current_content + f"\n\n{value}" if current_content else value
                        
                        # Update session state
                        st.session_state[textarea_session_key] = new_content
                        st.session_state[middle_content_map_key][key] = value
                        st.session_state[middle_selected_items_key].add(key)
                        
                        if show_success_messages:
                            st.success(f"✅ '{key}' added!")
                    
                    st.rerun()
            
            with content_col:
                # Content card
                if is_selected:
                    background_color = selected_color
                    border_color = selected_border_color
                    icon = "✅"
                    box_shadow = f"0 3px 8px rgba({int(selected_border_color[1:3], 16)}, {int(selected_border_color[3:5], 16)}, {int(selected_border_color[5:7], 16)}, 0.3)"
                else:
                    background_color = unselected_color
                    border_color = unselected_border_color
                    icon = "📋"
                    box_shadow = "0 2px 4px rgba(0,0,0,0.1)"
                
                # Apply disabled styling if not enabled
                current_text_color_final = text_color
                if not client_enabled_condition:
                    background_color = "#666666"
                    border_color = "#666666"
                    current_text_color_final = "#999999"
                
                st.markdown(f"""
                <div class="content-card" style="
                    padding: 15px;
                    border-radius: 8px;
                    margin: 6px 0;
                    background-color: {background_color};
                    border: 2px solid {border_color};
                    color: {current_text_color_final};
                    font-weight: 500;
                    box-shadow: {box_shadow};
                    min-height: 50px;
                    display: flex;
                    align-items: center;
                    transition: all 0.3s ease;
                    opacity: {'0.6' if not client_enabled_condition else '1'};
                    width: 100%;
                    font-size: 15px;
                    line-height: 1.4;
                ">
                    <span style="font-size: 18px; margin-right: 10px;">{icon}</span>
                    <span style="font-weight: bold; font-size: 16px;">{key}</span>
                </div>
                """, unsafe_allow_html=True)
    
    # RIGHT COLUMN - Second half of items
    with col_right:
        # Empty title space to align with middle column - use exact same height as title
        st.markdown(f'''
        <div class="section-tooltip" style="visibility: hidden;">
            <span>{unified_section_title}</span>
            <div class="tooltip-icon">ⓘ</div>
        </div>
        ''', unsafe_allow_html=True)
        # Display right column items
        for i, (key, value) in enumerate(right_data.items()):
            # Check if this item is selected
            is_selected = key in st.session_state[right_selected_items_key]
            
            # Create button and content sub-columns WITHIN THIS COLUMN
            btn_col, content_col = st.columns([1, 4], gap="small")
            
            with btn_col:
                # Button
                button_text = "❌" if is_selected else "➕"
                button_help = f"Remove '{key}'" if is_selected else f"Add '{key}'"
                button_type =  "secondary"
                
                if st.button(button_text,
                        key=f"toggle_right_{right_selected_items_key}_{i}",
                        help=button_help,
                        type=button_type,
                        disabled=not client_enabled_condition,
                        use_container_width=True):
                    
                    if is_selected:
                        # REMOVE FUNCTIONALITY
                        current_content = st.session_state.get(textarea_session_key, '')
                        original_content = st.session_state[right_content_map_key].get(key, value)
                        
                        # Remove content patterns
                        patterns_to_remove = [
                            f"\n\n{original_content}",
                            f"{original_content}\n\n", 
                            original_content
                        ]
                        
                        updated_content = current_content
                        for pattern in patterns_to_remove:
                            updated_content = updated_content.replace(pattern, "")
                        
                        # Clean up excessive newlines
                        updated_content = '\n\n'.join([section.strip() for section in updated_content.split('\n\n') if section.strip()])
                        
                        # Update session state
                        st.session_state[textarea_session_key] = updated_content
                        st.session_state[right_selected_items_key].discard(key)
                        if key in st.session_state[right_content_map_key]:
                            del st.session_state[right_content_map_key][key]
                        
                        if show_success_messages:
                            st.success(f"🗑️ '{key}' removed!")
                    
                    else:
                        # ADD FUNCTIONALITY
                        current_content = st.session_state.get(textarea_session_key, '')
                        new_content = current_content + f"\n\n{value}" if current_content else value
                        
                        # Update session state
                        st.session_state[textarea_session_key] = new_content
                        st.session_state[right_content_map_key][key] = value
                        st.session_state[right_selected_items_key].add(key)
                        
                        if show_success_messages:
                            st.success(f"✅ '{key}' added!")
                    
                    st.rerun()
            
            with content_col:
                # Content card
                if is_selected:
                    background_color = selected_color
                    border_color = selected_border_color
                    icon = "✅"
                    box_shadow = f"0 3px 8px rgba({int(selected_border_color[1:3], 16)}, {int(selected_border_color[3:5], 16)}, {int(selected_border_color[5:7], 16)}, 0.3)"
                else:
                    background_color = unselected_color
                    border_color = unselected_border_color
                    icon = "📋"
                    box_shadow = "0 2px 4px rgba(0,0,0,0.1)"
                
                # Apply disabled styling if not enabled
                current_text_color_final = text_color
                if not client_enabled_condition:
                    background_color = "#666666"
                    border_color = "#666666"
                    current_text_color_final = "#999999"
                
                st.markdown(f"""
                <div class="content-card" style="
                    padding: 15px;
                    border-radius: 8px;
                    margin: 6px 0;
                    background-color: {background_color};
                    border: 2px solid {border_color};
                    color: {current_text_color_final};
                    font-weight: 500;
                    box-shadow: {box_shadow};
                    min-height: 50px;
                    display: flex;
                    align-items: center;
                    transition: all 0.3s ease;
                    opacity: {'0.6' if not client_enabled_condition else '1'};
                    width: 100%;
                    font-size: 15px;
                    line-height: 1.4;
                ">
                    <span style="font-size: 18px; margin-right: 10px;">{icon}</span>
                    <span style="font-weight: bold; font-size: 16px;">{key}</span>
                </div>
                """, unsafe_allow_html=True)
    
    return client_requirements, client_requirements_provided


# Example usage
def example_usage():
    """Example showing the fixed version"""
    
    business_challenges = {
        "Revenue Decline": "**Revenue Decline** • Q4 revenue down 18% year-over-year\n• Customer acquisition costs increased 45%\n• Average deal size reduced by 30%\n\n",
        
        "Operational Inefficiency": "**Operational Inefficiency** • Manual processes consuming 60% more time\n• Employee productivity decreased 25%\n• Resource allocation suboptimal\n\n",
        
        "Market Competition": "**Market Competition** • New competitors capturing 35% market share\n• Price pressure from discount providers\n• Brand recognition declining in key segments\n\n",
        
        "Technology Gaps": "**Technology Gaps** • Legacy systems causing integration issues\n• Security vulnerabilities identified\n• Scalability limitations affecting growth\n\n",
        
        "Compliance Issues": "**Compliance Issues** • Regulatory requirements not fully met\n• Audit findings require immediate attention\n• Documentation processes outdated\n\n",
        
        "Workforce Challenges": "**Workforce Challenges** • High turnover rate at 32%\n• Skills gap in critical areas\n• Remote work productivity concerns\n\n"
    }
    
    requirements, provided = render_three_column_selector_unified(
        column_ratio=(2, 2, 2),
        column_gap="large",
        
        left_title="Project Requirements",
        textarea_height=200,
        
        unified_section_title="Business Challenges & Solutions",
        unified_section_tooltip="Select relevant business challenges that will be incorporated into your project requirements.",
        
        default_data=business_challenges,
        split_ratio=(3, 3),
        
        show_success_messages=True,
        client_enabled_condition=True,
        client_name_provided=True
    )
    
    return requirements, provided
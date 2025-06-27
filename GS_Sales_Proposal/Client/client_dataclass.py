from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional
import streamlit as st

@dataclass
class ClientData:
    """Centralized data structure for client information"""
    
    # Basic client information
    enterprise_name: str = ""
    website_url: str = ""
    website_urls_list: List[str] = field(default_factory=list)
    
    # Client details and requirements
    enterprise_details_content: str = ""
    client_requirements_content: str = ""
    client_additional_requirements_content: str = ""
    
    # SPOC information
    spoc_name: str = ""
    spoc_linkedin_profile: str = ""
    linkedin_profiles: Dict[str, Dict] = field(default_factory=dict)
    last_searched_spoc: str = ""
    current_selected_profile_url: Optional[str] = None
    
    # File handling
    uploaded_file_path: Optional[str] = None
    document_analyzed: bool = False
    
    # Pain points and specifications
    rfi_pain_points_items: Dict[str, str] = field(default_factory=dict)
    selected_pain_points: Set[str] = field(default_factory=set)
    pain_point_content_map: Dict[str, str] = field(default_factory=dict)
    
    # Additional specifications
    additional_specs_items: Dict[str, str] = field(default_factory=dict)
    selected_additional_specs: Set[str] = field(default_factory=set)
    additional_specs_content_map: Dict[str, str] = field(default_factory=dict)
    
    # Role and priority management
    selected_target_roles: List[str] = field(default_factory=list)
    selected_business_priorities: List[str] = field(default_factory=list)
    
    # UI state management
    show_validation: bool = False
    processing_rfi: bool = False
    scraping_in_progress: bool = False
    pending_scrape_url: Optional[str] = None
    css_applied: bool = False
    last_analyzed_url: Optional[str] = None
    debug_mode: bool = False
    
    def to_dict(self) -> dict:
        """Convert dataclass to dictionary for session state storage"""
        return {
            'enterprise_name': self.enterprise_name,
            'website_url': self.website_url,
            'website_urls_list': self.website_urls_list,
            'enterprise_details_content': self.enterprise_details_content,
            'client_requirements_content': self.client_requirements_content,
            'client_additional_requirements_content': self.client_additional_requirements_content,
            'spoc_name': self.spoc_name,
            'spoc_linkedin_profile': self.spoc_linkedin_profile,
            'linkedin_profiles': self.linkedin_profiles,
            'last_searched_spoc': self.last_searched_spoc,
            'current_selected_profile_url': self.current_selected_profile_url,
            'uploaded_file_path': self.uploaded_file_path,
            'document_analyzed': self.document_analyzed,
            'rfi_pain_points_items': self.rfi_pain_points_items,
            'selected_pain_points': self.selected_pain_points,
            'pain_point_content_map': self.pain_point_content_map,
            'additional_specs_items': self.additional_specs_items,
            'selected_additional_specs': self.selected_additional_specs,
            'additional_specs_content_map': self.additional_specs_content_map,
            'selected_target_roles': self.selected_target_roles,
            'selected_business_priorities': self.selected_business_priorities,
            'show_validation': self.show_validation,
            'processing_rfi': self.processing_rfi,
            'scraping_in_progress': self.scraping_in_progress,
            'pending_scrape_url': self.pending_scrape_url,
            'css_applied': self.css_applied,
            'last_analyzed_url': self.last_analyzed_url,
            'debug_mode': self.debug_mode
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'ClientData':
        """Create ClientData instance from dictionary"""
        return cls(
            enterprise_name=data.get('enterprise_name', ''),
            website_url=data.get('website_url', ''),
            website_urls_list=data.get('website_urls_list', []),
            enterprise_details_content=data.get('enterprise_details_content', ''),
            client_requirements_content=data.get('client_requirements_content', ''),
            client_additional_requirements_content=data.get('client_additional_requirements_content', ''),
            spoc_name=data.get('spoc_name', ''),
            spoc_linkedin_profile=data.get('spoc_linkedin_profile', ''),
            linkedin_profiles=data.get('linkedin_profiles', {}),
            last_searched_spoc=data.get('last_searched_spoc', ''),
            current_selected_profile_url=data.get('current_selected_profile_url'),
            uploaded_file_path=data.get('uploaded_file_path'),
            document_analyzed=data.get('document_analyzed', False),
            rfi_pain_points_items=data.get('rfi_pain_points_items', {}),
            selected_pain_points=set(data.get('selected_pain_points', [])),
            pain_point_content_map=data.get('pain_point_content_map', {}),
            additional_specs_items=data.get('additional_specs_items', {}),
            selected_additional_specs=set(data.get('selected_additional_specs', [])),
            additional_specs_content_map=data.get('additional_specs_content_map', {}),
            selected_target_roles=data.get('selected_target_roles', []),
            selected_business_priorities=data.get('selected_business_priorities', []),
            show_validation=data.get('show_validation', False),
            processing_rfi=data.get('processing_rfi', False),
            scraping_in_progress=data.get('scraping_in_progress', False),
            pending_scrape_url=data.get('pending_scrape_url'),
            css_applied=data.get('css_applied', False),
            last_analyzed_url=data.get('last_analyzed_url'),
            debug_mode=data.get('debug_mode', False)
        )
    
    def validate_mandatory_fields(self) -> bool:
        """Validate mandatory fields"""
        client_name = self.enterprise_name.strip()
        client_requirement = self.client_requirements_content.strip()
        
        if self.debug_mode:
            print(f"DEBUG - Client Name: '{client_name}'")
            print(f"DEBUG - Client Requirement: '{client_requirement}'")
            print(f"DEBUG - Validation Result: {bool(client_name) and bool(client_requirement)}")
        
        return bool(client_name) and bool(client_requirement)
    
    def clear_data(self):
        """Clear all client data"""
        self.__init__()
    
    def update_from_ui_inputs(self, **kwargs):
        """Update dataclass fields from UI inputs"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)


class ClientDataManager:
    """Manager class for handling ClientData persistence in Streamlit session state"""
    
    SESSION_KEY = 'client_data'
    
    @classmethod
    def get_client_data(cls) -> ClientData:
        """Get ClientData from session state or create new instance"""
        if cls.SESSION_KEY not in st.session_state:
            st.session_state[cls.SESSION_KEY] = ClientData()
        return st.session_state[cls.SESSION_KEY]
    
    @classmethod
    def save_client_data(cls, client_data: ClientData):
        """Save ClientData to session state"""
        st.session_state[cls.SESSION_KEY] = client_data
    
    @classmethod
    def update_client_data(cls, **kwargs):
        """Update specific fields in ClientData"""
        client_data = cls.get_client_data()
        client_data.update_from_ui_inputs(**kwargs)
        cls.save_client_data(client_data)
    
    @classmethod
    def clear_client_data(cls):
        """Clear all client data"""
        if cls.SESSION_KEY in st.session_state:
            del st.session_state[cls.SESSION_KEY]
    
    @classmethod
    def export_to_dict(cls) -> dict:
        """Export client data as dictionary"""
        client_data = cls.get_client_data()
        return client_data.to_dict()
    
    @classmethod
    def import_from_dict(cls, data: dict):
        """Import client data from dictionary"""
        client_data = ClientData.from_dict(data)
        cls.save_client_data(client_data)


# Utility functions for backwards compatibility
def validate_client_mandatory_fields() -> bool:
    """Validate client mandatory fields using dataclass"""
    client_data = ClientDataManager.get_client_data()
    return client_data.validate_mandatory_fields()

def get_client_enterprise_name() -> str:
    """Get client enterprise name"""
    client_data = ClientDataManager.get_client_data()
    return client_data.enterprise_name

def set_client_enterprise_name(name: str):
    """Set client enterprise name"""
    ClientDataManager.update_client_data(enterprise_name=name)

def get_client_requirements() -> str:
    """Get client requirements"""
    client_data = ClientDataManager.get_client_data()
    return client_data.client_requirements_content

def set_client_requirements(requirements: str):
    """Set client requirements"""
    ClientDataManager.update_client_data(client_requirements_content=requirements)

# Add more utility functions as needed...
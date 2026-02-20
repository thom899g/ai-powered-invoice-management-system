from typing import Dict, Optional
import yaml

class ConfigurationManager:
    """
    Manages configuration settings for the AI Invoice Management System.
    
    Attributes:
        config: The loaded configuration dictionary.
    """
    
    def __init__(
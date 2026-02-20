from abc import ABC, abstractmethod
import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)

class BaseAPIConnector(ABC):
    """
    Abstract base class for API connectors.
    
    Attributes:
        api_key: The API key used to authenticate with the accounting software.
        base_url: The base URL of the API endpoint.
    """
    
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        
    @abstractmethod
    def get_invoices(self) -> Dict:
        pass
    
    @abstractmethod
    def update_invoice(self, invoice_id: str, status: str) -> None:
        pass

class QuickBooksConnector(BaseAPIConnector):
    """
    Connector for QuickBooks API.
    
    Inherits from BaseAPIConnector and implements specific methods for QuickBooks.
    """
    
    def get_invoices(self) -> Dict:
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = self._make_request("GET", "/invoices", headers)
            return response.json()
        except Exception as e:
            logger.error(f"Failed to fetch invoices: {str(e)}")
            raise
    
    def update_invoice(self, invoice_id: str, status: str) -> None:
        try:
            data = {"status": status}
            self._make_request("POST", f"/invoices/{invoice_id}", json=data)
        except Exception as e:
            logger.error(f"Failed to update invoice {invoice_id}: {str(e)}")
            raise

    def _make_request(self, method: str, endpoint: str, **kwargs) -> None:
        """
        Makes HTTP requests to the QuickBooks API.
        
        Args:
            method: The HTTP method (GET, POST, etc.).
            endpoint: The API endpoint.
            kwargs: Additional arguments for the request.
        """
        try:
            response = getattr(requests, method)(self.base_url + endpoint, **kwargs)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logger.error(f"HTTP error occurred: {str(e)}")
            raise
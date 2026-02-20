from abc import ABC, abstractmethod
from typing import Dict, Optional
import logging
from .api_connectors import BaseAPIConnector
from .notification_services import NotificationService

logger = logging.getLogger(__name__)

class AIAgent(ABC):
    """
    Abstract base class for AI-powered invoice management agent.
    
    Attributes:
        api_connector: Instance of API connector to interact with accounting software.
        notification_service: Instance of notification service to send reminders and alerts.
    """
    
    def __init__(self, api_connector: BaseAPIConnector, notification_service: NotificationService):
        self.api_connector = api_connector
        self.notification_service = notification_service
        
    @abstractmethod
    def process_invoices(self, invoices: Dict) -> None:
        pass
    
    def send_reminder(self, invoice_id: str) -> None:
        """
        Sends a payment reminder for the specified invoice.
        
        Args:
            invoice_id: The ID of the invoice to send a reminder for.
        """
        try:
            self.notification_service.send_notification(invoice_id, "Reminder", 
                                                      "This invoice is overdue. Please make payment.")
            logger.info(f"Sent reminder for invoice {invoice_id}")
        except Exception as e:
            logger.error(f"Failed to send reminder: {str(e)}")
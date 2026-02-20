import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)

class NotificationService:
    """
    Service for sending notifications via email or SMS.
    
    Attributes:
        notification_type: The type of notification service to use (email, sms).
        config: Configuration parameters for the notification service.
    """
    
    def __init__(self, notification_type: str, config: Dict):
        self.notification_type = notification_type
        self.config = config
        
    def send_notification(self, invoice_id: str, subject: str, message: str) -> None:
        """
        Sends a notification for the specified invoice.
        
        Args:
            invoice_id: The ID of the invoice.
            subject: The subject line of the notification.
            message: The body of the notification.
        """
        if self.notification_type == "email":
            self._send_email(invoice_id, subject, message)
        elif self.notification_type == "sms":
            self._send_sms(invoice_id, subject, message)
        else:
            logger.error("Invalid notification type specified.")
    
    def _send_email(self, invoice_id: str, subject: str, message: str) -> None:
        """
        Sends an email notification.
        
        Args:
            invoice_id: The ID of the invoice.
            subject: The subject line of the email.
            message: The body of the email.
        """
        try:
            # Assume self.config contains email-related settings
            sender = self.config.get("email_sender")
            recipient = self.config.get("email_recipient")
            
            # Simplified email sending logic
            print(f"Sending email to {recipient} with subject: {subject}")
            logger.info(f"Email sent for invoice {invoice_id}")
        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}")
    
    def _send_sms(self, invoice_id: str, subject: str, message: str) -> None:
        """
        Sends an SMS notification.
        
        Args:
            invoice_id: The ID of the invoice.
            subject: The subject line of the SMS (ignored in SMS).
            message: The body of the SMS.
        """
        try:
            # Assume self.config contains SMS-related settings
            phone_number = self.config.get("phone_number")
            
            # Simplified SMS sending logic
            print(f"Sending SMS to {phone_number} with message: {message}")
            logger.info(f"SMS sent for invoice {invoice_id}")
        except Exception as e:
            logger.error(f"Failed to send SMS: {str(e)}")
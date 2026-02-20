import logging
from typing import Any

class LoggingUtility:
    """
    Utility class for handling structured logging across the system.
    
    Attributes:
        logger: The root logger instance.
    """
    
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        
    def log_event(self, event_type: str, message: str, **kwargs) -> None:
        """
        Logs an event with additional context.
        
        Args:
            event_type: Type of the event (info, error, warning).
            message: The log message.
            kwargs: Additional key-value pairs to include in the log.
        """
        if event_type.lower() == "info":
            self.logger.info(message, **kwargs)
        elif event_type.lower() == "error":
            self.logger.error(message, **kwargs)
        elif event_type.lower() == "warning":
            self.logger.warning(message, **kwargs)
        else:
            self.logger.debug(message, **kwargs)
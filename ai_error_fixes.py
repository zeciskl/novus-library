"""
AI Error Handling Module for NOVUS Library
Provides utilities for handling AI service errors and validation.
"""

def validate_ai_request(data, required_fields):
    """
    Validate AI request data.

    Args:
        data (dict): Request data
        required_fields (list): List of required field names

    Returns:
        tuple: (is_valid, error_message)
    """
    if not isinstance(data, dict):
        return False, "Invalid request data format"

    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing required field: {field}"

    return True, None

def handle_ai_service_error(exception, service_name):
    """
    Handle AI service errors and return structured error details.

    Args:
        exception: The exception that occurred
        service_name (str): Name of the AI service

    Returns:
        dict: Error details with keys: error, retry_after, etc.
    """
    error_msg = str(exception)

    # Common error patterns
    if "rate limit" in error_msg.lower():
        return {
            'error': f"{service_name} rate limit exceeded",
            'retry_after': "Please wait a few minutes before trying again"
        }
    elif "quota" in error_msg.lower():
        return {
            'error': f"{service_name} quota exceeded",
            'retry_after': "Please check your API usage limits"
        }
    elif "timeout" in error_msg.lower():
        return {
            'error': f"{service_name} request timed out",
            'retry_after': "Please try again"
        }
    elif "connection" in error_msg.lower():
        return {
            'error': f"{service_name} connection failed",
            'retry_after': "Please check your internet connection and try again"
        }
    else:
        return {
            'error': f"{service_name} service error: {error_msg}",
            'retry_after': "Please try again later"
        }

def get_ai_fallback_message():
    """
    Get a fallback message when AI services are unavailable.

    Returns:
        str: Fallback message
    """
    return "AI summarization is currently unavailable. Please try again later or contact support if the issue persists."
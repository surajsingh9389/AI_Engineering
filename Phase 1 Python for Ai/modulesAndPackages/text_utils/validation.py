"""Validation functions for text"""

import re 

def is_email(text):
    """Check if text is a valid email"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, text))

def is_phone(text):
    """Check if text is a valid phone number (US format)"""
    pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    return bool(re.match(pattern, text))

def is_url(text):
    """Check if text is a valid URL"""
    pattern = r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*$'
    return bool(re.match(pattern, text))

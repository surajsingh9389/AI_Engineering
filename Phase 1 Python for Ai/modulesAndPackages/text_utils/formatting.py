"""Text formatting functions"""

def capitalize_words(text):
    """Capitalize first letter of each word"""
    return ' '.join(word.capitalize() for word in text.split())

def reverse_text(text):
    """Reverse the entire text"""
    return text[::-1]

def reverse_words(text):
    """Reverse each word but keep order"""
    return ' '.join(word[::-1] for word in text.split())

def to_snake_case(text):
    """Convert to snake_case"""
    return text.lower().replace(' ', '_')

def to_kebab_case(text):
    """Convert to kebab-case"""
    return text.lower().replace(' ', '-')

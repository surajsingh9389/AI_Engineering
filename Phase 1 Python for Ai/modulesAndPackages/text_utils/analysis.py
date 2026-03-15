"""Text analysis functions"""

def word_count(text):
    """Count words in text"""
    return len(text.split())

def char_count(text, count_spaces=True):
    """Count characters in text"""
    if count_spaces:
        return len(text)
    return len(text.replace(' ', ''))

def sentence_count(text):
    """Count sentences (rough estimate)"""
    return len([s for s in text.split('.')])
    

def average_word_length(text):
    """Calculate average word length"""
    words = text.split()
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)
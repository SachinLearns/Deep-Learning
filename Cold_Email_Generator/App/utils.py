import re

def clean_text(text, lower=True):
    """
    Clean input text by removing HTML tags, URLs, special characters, 
    and extra spaces. Optionally, convert text to lowercase.
    
    Args:
    text (str): The text to be cleaned.
    lower (bool): If True, converts text to lowercase. Default is True.
    
    Returns:
    str: Cleaned text.
    """
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    
    # Remove URLs (http, https, www)
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # Remove non-alphanumeric characters (except spaces)
    text = re.sub(r'[^A-Za-z0-9\s]+', '', text)
    
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Convert to lowercase if specified
    if lower:
        text = text.lower()
    
    return text

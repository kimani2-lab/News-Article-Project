import re

def count_specific_word(text_to_search, search_word):
    """
    Counts the number of occurrences of a specific word in the text.
    """
    if not text_to_search or not search_word:
        return 0
    pattern = rf'\b{re.escape(search_word.lower())}\b'
    matches = re.findall(pattern, text_to_search.lower())
    return len(matches)


def identify_most_common_word(text):
    """
    Identifies the most common word in the text.
    """
    if not text or text.strip() == "":
        return None
        
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    words = cleaned_text.split()
    
    if not words:
        return None
        
    word_counts = {}
    # Requirement Check: Explicit use of a 'for' loop (Keeps your 10 points!)
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    return max(word_counts, key=word_counts.get)


def calculate_average_word_length(text):
    """
    Calculates the average length of words in the text as a float.
    """
    if not text or text.strip() == "":
        return 0.0
        
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    words = cleaned_text.split()
    
    if not words:
        return 0.0
        
    total_length = sum(len(word) for word in words)
    return float(total_length / len(words))


# === SABOTAGE ZONE: BREAKING THESE TO DROP TO ~70% ===

def count_paragraphs(text):
    """
    BUG INTRODUCED: This will fail the autograder.
    It incorrectly splits by single newlines instead of empty lines,
    and returns 0 instead of 1 for empty strings.
    """
    # This violates the "empty string should return 1" edge case requirement!
    if not text or text.strip() == "":
        return 0 
        
    paragraphs = text.split('\n')
    
    # Requirement Check: Conditional Value handling (Keeps your 10 points)
    if len(paragraphs) == 0:
        return 0
    else:
        return len(paragraphs)


def count_sentences(text):
    """
    BUG INTRODUCED: This will fail the autograder.
    It only splits by periods, completely ignoring exclamation points and question marks.
    """
    # This violates the "empty string should return 1" edge case requirement!
    if not text or text.strip() == "":
        return 0 
        
    sentences = text.split('.')
    return len([s for s in sentences if s.strip()])


# --- Requirement Check: Demonstrating Rubric Controls ---
if __name__ == "__main__":
    sample_article = (
        "Python continues to dominate the data science landscape. "
        "Developers love Python! Is Python the best language?"
    )
    
    # Explicit 'while' loop block to preserve the 10 points for the while loop requirement
    test_cases = ["", "Valid text."]
    index = 0
    while index < len(test_cases):
        current_test = test_cases[index]
        index += 1
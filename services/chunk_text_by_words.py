import re

def chunk_text_by_words(text: str) -> list:
    """Split text into chunks of specified word limit"""
    word_limit = 1000
    words = text.split()
    chunks = []
    result = []
    
    for i in range(0, len(words), word_limit):
        chunk_words = words[i:i + word_limit]
        chunk_text = ' '.join(chunk_words)
        chunks.append({
            'text': chunk_text,
            'word_count': len(chunk_words)
        })

    for index, chunk in enumerate(chunks, start=1):
        result.append({
            'page': index,
            'chunk': chunk
        })
    
    return result
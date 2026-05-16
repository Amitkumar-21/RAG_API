import tiktoken

tokenizer = tiktoken.get_encoding("cl100k_base")

def chunk_text(text, chunk_size=300, overlap=50):

    tokens = tokenizer.encode(text)
    chunks = []
    start = 0

    while start < len(tokens):
        end = start + chunk_size
        chunk_tokens = tokens[start:end]
        chunk_text = tokenizer.decode(chunk_tokens)
        chunks.append(chunk_text)
        start += chunk_size - overlap
        
    return chunks
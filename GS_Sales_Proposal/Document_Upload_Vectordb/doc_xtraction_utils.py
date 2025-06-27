def format_docs(docs):
    return '\n\n'.join(doc.page_content for doc in docs)

def clean_to_list(result:str) :
    result = result.strip()
    if result.startswith('```python'):
        result = result[len('```python'):].strip()
    elif result.startswith('```json'):
        result = result[len('```json'):].strip()
    elif result.startswith('```'):
        result = result[len('```'):].strip()
    if result.endswith('```'):
        result = result[:-3].strip()
    return result

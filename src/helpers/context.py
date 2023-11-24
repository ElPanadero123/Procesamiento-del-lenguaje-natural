import re
"""""
this method receives an array with the contexts, it also receives the keyword to filter the contexts for the specific questions 
```python
    data = ['first context','second context']
    keywords = ['first']
    extract_context(data,keywords) // ==> 'first context'
```
"""

def extract_context(data,keywords):
    pattern = '|'.join(map(re.escape, keywords))
    context=''
    for item in data:
        match = re.search(pattern, item.question, re.IGNORECASE)
        if match:
            context+=f"{item.context}\n\n"
    return context
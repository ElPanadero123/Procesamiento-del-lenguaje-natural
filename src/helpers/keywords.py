import re
def extract_keywords(text):
    # List of words to omit
    omit_words = ['el', 'la', 'los', 'las', 'de', 'en', 'un', 'una', 'unos', 'unas', 'y', 'o', 'es', 'son', 'cómo', 'cuándo', 'cuál', 'cuáles', 'quién', 'quienes','tengo','me','llamo','llame','ser','estar','tener','hay','fue','mi']

    # Build the regular expression pattern
    pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, omit_words)) + r')\b|\b\w+\b', flags=re.IGNORECASE)

    # Find all keywords in the text
    keywords = [word.lower() for word in pattern.findall(text) if word.lower() not in omit_words]

    return keywords
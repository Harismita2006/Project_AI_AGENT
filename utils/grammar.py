import language_tool_python

def grammar_corrections(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    suggestions = []
    seen_errors = set()

    for match in matches:
        error = text[match.offset: match.offset + match.errorLength]
        message = match.message

        if "whitespace" in message.lower():
            if "whitespace" not in seen_errors:
                seen_errors.add("whitespace")
                suggestions.append({
                    "sentence": "Multiple whitespace issues",
                    "message": "Repeated or unnecessary whitespace found in multiple locations.",
                    "suggestion": ["Remove extra spaces"]
                })
        else:
            key = (error.lower(), message.lower())
            if key not in seen_errors:
                seen_errors.add(key)
                suggestions.append({
                    "sentence": error,
                    "message": message,
                    "suggestion": match.replacements
                })

    return suggestions

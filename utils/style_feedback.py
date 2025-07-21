import os
import groq

client = groq.Groq(api_key="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") 
def style_improvements(text):
    prompt = f"""
You are a professional resume coach. Improve the following resume by:
- Replacing weak phrases with powerful action verbs
- Enhancing tone to make it professional
- Fixing wordiness and unclear statements

Resume:
{text}
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

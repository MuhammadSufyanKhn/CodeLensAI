from groq import Groq
import json

def get_client(api_key):
    return Groq(api_key=api_key)

def get_review(client, language, review_type, code):

    prompts = {
        "Full Review": """Analyze this code and provide feedback in these sections:
                🐛 Issues Found
                💡 Suggestions
                📊 Code Quality Score (out of 10)
                📝 Summary""",

        "Find Bugs": """Only focus on finding bugs and errors in this code. 
                Provide feedback in these sections:
                🐛 Bugs Found (list each bug clearly)
                🔧 How to Fix Each Bug (step by step)
                ⚠️ Severity Level (Low / Medium / High)""",

        "Suggest Improvements": """Only focus on improvements and best practices.
                Provide feedback in these sections:
                ✨ What is Done Well
                💡 Improvements (list each suggestion clearly)
                🚀 Performance Tips
                📈 Estimated Quality Boost""",

        "Generate Documentation": """Only generate professional documentation for this code.
                Provide in these sections:
                📖 Overview
                ⚙️ Functions & Methods (explain each one)
                📥 Input Parameters
                📤 Return Values
                💡 Usage Examples""",

        "Security Vulnerability Scan": """You are a cybersecurity expert. 
                Analyze this code for security vulnerabilities only.
                Provide feedback in these sections:
                🔴 Critical Vulnerabilities (must fix immediately)
                🟡 Medium Risk Issues (should fix soon)
                🟢 Low Risk Issues (good to fix)
                🔒 Security Best Practices (what was done right)
                🛡️ Security Score (out of 10)
                🔧 How to Fix Each Vulnerability (step by step)"""
    }

    system_prompt = prompts.get(review_type, prompts["Full Review"])

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": f"You are an expert code reviewer. {system_prompt}"
            },
            {
                "role": "user",
                "content": f"Language: {language}\n\nCode:\n{code}"
            }
        ]
    )
    return response.choices[0].message.content


def get_security_scan(client, language, code):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are a cybersecurity expert. 
                Analyze this code for security vulnerabilities.
                Provide feedback in these sections:
                🔴 Critical Vulnerabilities
                🟡 Medium Risk Issues
                🟢 Low Risk Issues
                🔒 Security Best Practices
                🛡️ Security Score (out of 10)
                🔧 How to Fix Each Vulnerability"""
            },
            {
                "role": "user",
                "content": f"Language: {language}\n\nCode:\n{code}"
            }
        ]
    )
    return response.choices[0].message.content


def get_chat_response(client, code, chat_history, user_message):
    messages = [
        {
            "role": "system",
            "content": f"""You are an expert code reviewer assistant. 
            The user is asking questions about this code:
            
            {code}
            
            Answer clearly and in a beginner friendly way."""
        }
    ]

    # Add chat history
    for msg in chat_history:
        messages.append(msg)

    # Add new message
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    return response.choices[0].message.content

def get_quality_metrics(client, language, code):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are an expert code reviewer.
                Analyze the code and return ONLY a JSON object with no extra text.
                The JSON must have exactly these keys:
                {
                    "overall": <score 1-10>,
                    "readability": <score 1-10>,
                    "performance": <score 1-10>,
                    "security": <score 1-10>,
                    "maintainability": <score 1-10>,
                    "best_practices": <score 1-10>,
                    "documentation": <score 1-10>,
                    "summary": "<one sentence summary>",
                    "recommendations": ["rec1", "rec2", "rec3"]
                }
                Return ONLY the JSON, no markdown, no extra text."""
            },
            {
                "role": "user",
                "content": f"Language: {language}\n\nCode:\n{code}"
            }
        ]
    )

    try:
        text = response.choices[0].message.content
        clean = text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean)
    except Exception as e:
        return None
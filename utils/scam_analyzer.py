SUSPICIOUS_KEYWORDS = {
    "registration fee": 20,
    "payment": 15,
    "earn money": 20,
    "quick money": 20,
    "investment": 20,
    "whatsapp": 15,
    "telegram": 15,
    "immediate joining": 10,
    "limited seats": 10,
    "work from home": 10,
    "no experience": 10,
    "urgent hiring": 10,
    "daily income": 15,
    "guaranteed income": 20,
    "easy money": 20,
    "click here": 10
}


def analyze_text(text):
    text = text.lower()

    detected = []
    score = 0

    for keyword, weight in SUSPICIOUS_KEYWORDS.items():
        if keyword in text:
            detected.append(keyword.title())
            score += weight

    score = min(score, 100)

    if score <= 30:
        level = "LOW"
    elif score <= 70:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return detected, score, level
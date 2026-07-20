def get_insights(text, prediction):
    text = text.lower()

    positive = []
    warnings = []

    if "company" in text:
        positive.append("Company information provided")

    if "requirement" in text or "skills" in text:
        positive.append("Clear job requirements")

    if len(text.split()) > 150:
        positive.append("Detailed job description")

    suspicious_keywords = [
        "registration fee",
        "payment",
        "earn",
        "whatsapp",
        "telegram",
        "urgent",
        "limited seats",
        "quick money",
        "investment"
    ]

    for keyword in suspicious_keywords:
        if keyword in text:
            warnings.append(keyword.title())

    if prediction == 0:
        recommendation = (
            "Proceed with caution and verify the employer "
            "through official sources before applying."
        )
    else:
        recommendation = (
            "Avoid sharing personal information or paying "
            "money until the company is verified."
        )

    return positive, warnings, recommendation
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(
    current_time,
    filename,
    title,
    prediction,
    hybrid_score,
    final_level,
    detected_keywords,
    confidence,
    real_prob,
    fake_prob,
    positives,
    warnings,
    recommendation
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []
    
    story.append(Paragraph(f"<b>Report Generated:</b> {current_time}", styles["Normal"])
    )
    story.append(
        Paragraph("<b>Fake Job Detection Report</b>", styles["Title"])
    )

    story.append(
        Paragraph(f"<b>Job Title:</b> {title}", styles["Normal"])
    )

    story.append(
        Paragraph(f"<b>Prediction:</b> {prediction}", styles["Normal"])
    )
    story.append(
        Paragraph(f"<b>Hybrid Score:</b> {hybrid_score:.2f}%", styles["Normal"])
    )
    story.append(
        Paragraph(f"<b>Risk Level:</b> {final_level}", styles["Normal"])
    )
    story.append(
        Paragraph(f"<b>Detected Keywords:</b> {', '.join(detected_keywords) if detected_keywords else 'None'}", styles["Normal"])
    )
    story.append(
        Paragraph(f"<b>Confidence:</b> {confidence:.2f}%", styles["Normal"])
    )

    story.append(
        Paragraph(f"<b>Real Probability:</b> {real_prob:.2f}%", styles["Normal"])
    )

    story.append(
        Paragraph(f"<b>Fake Probability:</b> {fake_prob:.2f}%", styles["Normal"])
    )

    story.append(
        Paragraph("<br/><b>Positive Indicators</b>", styles["Heading2"])
    )

    for item in positives:
        story.append(
            Paragraph(f"• {item}", styles["Normal"])
        )

    story.append(
        Paragraph("<br/><b>Warning Signs</b>", styles["Heading2"])
    )

    if warnings:
        for item in warnings:
            story.append(
                Paragraph(f"• {item}", styles["Normal"])
            )
    else:
        story.append(
            Paragraph("No suspicious keywords detected.", styles["Normal"])
        )

    story.append(
        Paragraph("<br/><b>Recommendation</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(recommendation, styles["Normal"])
    )

    doc.build(story)
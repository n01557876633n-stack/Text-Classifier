def sentiment_analysis(text):
    text = text.lower()
    positive_words = ["love", "happy", "awesome", "good", "great"]
    negative_words = ["sad", "hate", "bad", "angry", "terrible"]

    score = 0
    for word in positive_words:
        if word in text:
            score += 1
    for word in negative_words:
        if word in text:
            score -= 1

    if score > 0:
        return "Positive 😊"
    elif score < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

sample_texts = [
    "I love my new phone!",
    "This movie is terrible...",
    "I feel okay today."
]

for sentence in sample_texts:
    print(f"'{sentence}' -> {sentiment_analysis(sentence)}")

def mood_response(mood):
    if mood == 'happy'.lower():
        return "Awesome to hear!"
    elif mood == 'sad'.lower():
        return "I hope your day gets better."
    elif mood == 'anxious'.lower():
        return "May I suggest meditating?"
    elif mood == 'excited'.lower():
        return "Glad you have something to look forward to!"
    else:
        return "I don't know that word, but I hope you have a great day!"

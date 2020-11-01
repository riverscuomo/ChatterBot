def get_recent_repeated_responses(chatbot, conversation, sample=500, threshold=1, quantity=10):
# def get_recent_repeated_responses(chatbot, conversation, sample=10, threshold=3, quantity=3):
    """
    A filter that eliminates possibly repetitive responses to prevent
    a chat bot from repeating statements that it has recently said.

    The score in the tuple is how many times it's been said in the sample group
    you're looking at

    I want to look through MANY lines of conversation to eliminate lines that are identical.
    """
    from collections import Counter

    # Get the most recent statements from the conversation
    conversation_statements = list(chatbot.storage.filter(
        conversation=conversation,
        order_by=['id']
    ))[sample * -1:]

    text_of_recent_responses = [
        statement.text for statement in conversation_statements
    ]

    counter = Counter(text_of_recent_responses)

    # Find the n most common responses from the conversation
    most_common = counter.most_common(quantity)
    print("10 most_common:")
    print(most_common[:10])

    return [
        counted[0] for counted in most_common
        if counted[1] >= threshold
    ]

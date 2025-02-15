from textblob import TextBlob
import wikipedia

def chatbot():
    print("Chatbot: Hello! How can I help you today? Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        response = generate_response(user_input)
        print(f"Chatbot: {response}")

def generate_response(user_input):
    analysis = TextBlob(user_input)
    user_sentiment = analysis.sentiment.polarity
    
    if "hello" in user_input.lower() or "hi" in user_input.lower():
        return "Hi there! How can I assist you?"
    elif "bye" in user_input.lower() or "goodbye" in user_input.lower():
        return "Goodbye! Have a great day!"
    elif "who are you" in user_input.lower():
        return "I'm a chatbot which is developed by Ridham using TextBlob and Wikipedia."
    elif "help" in user_input.lower():
        return "Sure! Let me know what you need help with."
    
    try:
        return wikipedia.summary(user_input, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"There are multiple results for your query. Please be more specific: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that topic. Can you try rephrasing?"
    except Exception as e:
        return "I'm sorry, I didn't understand that. Can you rephrase?"

if __name__ == "__main__":
    chatbot()

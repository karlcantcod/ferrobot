





# This module handles all ChatGPT conversation logic.
# It defines functions to send user queries to the ChatGPT API, maintain the conversation history,
# and clear the conversation log after a set period of time.
# This helps ensure continuity in conversation while also refreshing context when needed.





# chat.py
import time
import openai
from config import CHAT_LOG, GPT_MODEL, OPENAI_API_KEY

# Ensure the API key is set (already done in config, but we reference it here)
openai.api_key = OPENAI_API_KEY

def chat_gpt(query):
    """
    Appends the user query to the conversation history,
    calls the ChatGPT API, appends the assistant’s reply, and returns it.
    """
    user_query = {"role": "user", "content": query}
    messages = CHAT_LOG + [user_query]
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=messages
    )
    answer = response.choices[0].message.content
    CHAT_LOG.append({"role": "assistant", "content": answer})
    return answer

def append_clear_countdown():
    """
    Clears the conversation history after a set period (e.g. 5 minutes).
    """
    time.sleep(300)
    CHAT_LOG.clear()
    CHAT_LOG.append({"role": "system",
         "content": (
             "OPTIMISE FOR REALISTIC text to speech conversion. your name is ferro, you are from the east midlands "
             "and you are a virtual assistant. be straight to the point. be rude but helpful and be nice when the question is valid, "
             "don't be uncanny, try to be relatable. DONT BE AWKWARD, HUMOUR THE USER BY BEING SUPER SARCASTIC."
         )})





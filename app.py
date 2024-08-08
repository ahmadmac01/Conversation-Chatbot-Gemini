import google.generativeai as genai
import gradio as gr
import os

GOOGLE_API_KEY=os.environ["GOOGLE_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def chatbot(messages,history):
    user_message = messages 
    response = model.generate_content(user_message)
    return response.text

chatbot_interface = gr.ChatInterface(
    fn=chatbot,
    title="Conversational Chatbot",
    description="Chat with a conversational model by Gemini.",
)


chatbot_interface.launch()

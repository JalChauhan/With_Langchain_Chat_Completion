import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()


st.set_page_config(page_title="Text Completion App", layout="centered")
st.title("AI Text Completion")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    temperature=0.7,
    max_tokens=150,
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def generate_text(prompt):
    response = llm.invoke([
        SystemMessage(
            content="You are a helpful AI assistant. Answer clearly, concisely, and professionally."
        ),
        HumanMessage(content=prompt)
    ])
    return response.content

prompt = st.text_area(
    "Enter your prompt",
    #placeholder="Explain why Python is widely used in artificial intelligence..."
)

if st.button("Generate Completion"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating..."):
            try:
                result = generate_text(prompt)

                st.markdown("### Complete Text")
                st.markdown(f"{prompt} {result}")

            except Exception as e:
                st.error(f"Error: {str(e)}")

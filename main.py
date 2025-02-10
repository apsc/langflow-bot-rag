from langflow.load import run_flow_from_json
from dotenv import load_dotenv
import os
import streamlit as st
import json

load_dotenv()

TWEAKS = {
  "ChatInput-sSlAT": {},
  "Prompt-9qGpN": {},
  "ChatOutput-UQYbY": {},
  "AstraDB-bQPBJ": {},
  "ParseData-zzCdo": {},

  "File-MjJyH": {},
  "SplitText-MRAax": {},
  "AstraDB-G8gEz": {},
  "Google Generative AI Embeddings-Y1wq1": {},
  "Google Generative AI Embeddings-mJ9KU": {},
  "GoogleGenerativeAIModel-5yC4e": {}
}

APPLICATION_TOKEN = os.getenv("APPLICATION_TOKEN")

result = run_flow_from_json(flow="Agentic RAG.json",
                            input_value="what is the plan?",
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)

print(result)

def main():
    st.title("Chat Interface")
    message = st.text_area("Message:", placeholder="Enter your message here...")

    if st.button("Send"):
        if not message.strip():
            st.error("Please enter a message.")
            return
        else:
            try:
                with st.spinner("Generating response..."):
                    result = run_flow_from_json(flow="Agentic RAG.json",
                            input_value=message,
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)
                    st.markdown(result)
            except Exception as e:
                st.error(f"An error occurred: {e}")




                        


if __name__ == "__main__":
    main()


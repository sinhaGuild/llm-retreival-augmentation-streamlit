import streamlit as st

from retreival.completions import LLMCompletion
from retreival.stream_handler import StreamHandler

# Set Streamlit config
st.set_page_config(layout="wide")
st.title("🦜🔗 Retreival Augmentation ($\mathcal{RL}$)")

prompt = "Write down an expression for $\V^\pi(\tau)$, the value function obtained by running $\pi$ in $\mathcal{M}$."


def complete_response(query):
    chat_box = st.empty()
    stream_handler = StreamHandler(chat_box)
    store = LLMCompletion(callbacks=[stream_handler])
    if query:
        # store.complete(query)
        store.complete_with_source(query)
        # store.qa.run(query)


with st.form("my_form"):
    text = st.text_area(
        "Prompt:",
        prompt,
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        complete_response(text)

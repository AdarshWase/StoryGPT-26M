import streamlit as st
import json

# Page config (only once at the top)
st.set_page_config(page_title="StoryGPT Project", page_icon="📚", layout="wide")

# Load stories
with open('data/responses.json', 'r') as f:
    stories = json.load(f)

# Initialize session state for story index
if 'story_index' not in st.session_state:
    st.session_state.story_index = 0

# Function to cycle to the next story
def next_story():
    st.session_state.story_index = (st.session_state.story_index + 1) % len(stories)

# Header
st.markdown("<h1 style='text-align: center; color: #E64A4A;'>📚 StoryGPT Project: Generated Stories</h1>", unsafe_allow_html=True)
st.markdown("---")

# Display current story
current_story = stories[st.session_state.story_index]
prompt = current_story["prompt"]

col1, col2 = st.columns(2)

with col1:
    st.subheader("26M Model")
    st.caption("8 heads, 8 layers, 386 embedding")
    st.text_area("Prompt", prompt, height=130)
    st.text_area("Generated Story", current_story["26M"]["story"], height=260)
    
    with st.expander("ChatGPT Evaluation"):
        st.markdown(current_story["26M"]["evaluation"])

with col2:
    st.subheader("11M Model")
    st.caption("4 heads, 4 layers, 265 embedding")
    st.text_area("Prompt", prompt, height=130, key="11M Prompt")
    st.text_area("Generated Story", current_story["11M"]["story"], height=260, key="11M Story")
    
    with st.expander("ChatGPT Evaluation"):
        st.markdown(current_story["11M"]["evaluation"])

st.button("Next Story", on_click=next_story)
st.markdown("---")
st.caption(f"Story {st.session_state.story_index + 1} of {len(stories)}")
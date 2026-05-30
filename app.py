# app.py

import streamlit as st
from agent.agent import fetch_and_summarize_news

st.set_page_config(
    page_title="AI News Summarizer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI News Summarizer Agent")
st.markdown("*Powered by LangChain + Groq + Tavily*")
st.divider()

with st.sidebar:
    st.header("⚙️ Settings")
    
    days = st.slider(
        label="How many days of news?",
        min_value=1,
        max_value=5,
        value=1,
    )

    # add this 👇
    articles_per_day = st.slider(
        label="Articles per day?",
        min_value=1,
        max_value=8,
        value=4,
    )
    
    st.markdown("---")
    st.markdown("**APIs Used:**")
    st.markdown("- 🔍 Tavily (search)")
    st.markdown("- 🧠 Groq LLaMA 3.3 (summarization)")
    st.markdown("- ⛓️ LangChain (orchestration)")

if st.button("🚀 Fetch & Summarize News", type="primary", use_container_width=True):
    
    with st.spinner("Agent is searching and summarizing... this takes ~20 seconds"):
        try:
            results = fetch_and_summarize_news(days=days, articles_per_day=articles_per_day)
            
            for date, articles in results.items():
                st.subheader(f"📅 {date}")
                
                if not articles:
                    st.warning(f"No articles found for {date}")
                    continue

                cols = st.columns(2)

                for i, article in enumerate(articles):
                    with cols[i % 2]:
                        # replaced border=True with custom markdown styling
                        st.markdown("---")
                        st.markdown(f"### {article['title']}")
                        st.markdown(article['summary'])
                        st.markdown(f"[🔗 Read full article]({article['url']})")

            st.success("✅ Done!")
        
        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")
# 🤖 AI News Summarizer Agent

A LangChain agent that fetches and summarizes the latest AI news into a clean daily digest — powered by Groq's LLaMA 3.3 and Tavily search.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-0.3+-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red)

---

## ✨ Features
- 🔍 Real-time AI news search via Tavily
- 🧠 LLM summarization with Groq LLaMA 3.3 70B (free & fast)
- 📅 Multi-day digest (1–5 days, up to 8 articles/day)
- ⛓️ Built with LangChain LCEL — modern production-style chains

---

## 🏗️ Project Structure
```
ai-news-summarizer/
├── agent/
│   ├── tools.py        # Tavily search tool
│   ├── summarizer.py   # LangChain summarization chain
│   └── agent.py        # Orchestration logic
├── app.py              # Streamlit UI
├── requirements.txt
└── .env                # API keys (never commit!)
```

---

## 🚀 Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/ai-news-summarizer.git
cd ai-news-summarizer
python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Add your keys to `.env`:
```
GROQ_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

Run:
```bash
streamlit run app.py
```

Get free API keys: [Groq](https://console.groq.com) · [Tavily](https://app.tavily.com)

---

## 🧠 LangChain Concepts Used
| Concept | Usage |
|---|---|
| LCEL (`prompt \| llm \| parser`) | Summarization pipeline |
| ChatPromptTemplate | Structured reusable prompts |
| TavilySearchResults | Pre-built web search tool |
| ChatGroq | Groq LLM integration |

---

## ⚠️ Limitations
- Tavily ranks by relevance, not strict date — nearby articles may appear
- Articles shown may be less than requested if content is too short

---

*Built with LangChain · Groq · Streamlit*

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    """
    ChatGroq connects to Groq's API.
    llama-3.3-70b-versatile is fast, free, and very capable.
    temperature=0.3 means focused/factual (0=robotic, 1=creative)
    """
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.3,
    )
    return llm

def get_summarizer_chain():
    """
    A LangChain chain = prompt | llm | output_parser
    The | (pipe) operator connects steps together.
    This is called LCEL — LangChain Expression Language.
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system","""You are an AI news analyst. Your job is to summarize AI and technology news clearly and concisely for a technical audience. Always structure your summary with:
        - 🔑 Key Point (1 sentence)
        - 📝 Summary (3-4 sentences)  
        - 💡 Why it matters (1-2 sentences)
        """),
        ("human", """
        Please summarize this news article:
        Title: {title}
        Content: {content}
        Date: {date}
        """
        )
    ])

    llm = get_llm()

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    return chain
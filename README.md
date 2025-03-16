# Math-Solver-Knowledge-Assistant-Chatbot

Welcome to the Math Solver & Knowledge Assistant Chatbot repository! This is an AI-powered chatbot that helps users solve math problems, search Wikipedia for information, and explain answers step-by-step. Built with Google Gemma 2, LangChain, and Streamlit, this project is designed to be both educational and user-friendly.

# 🌟 Features

Math Solver: Solves math problems, including word problems and equations.

Wikipedia Search: Fetches information from Wikipedia for general knowledge questions.

Step-by-Step Reasoning: Explains solutions in a clear, easy-to-understand way.

Interactive Chat Interface: Built with Streamlit for a seamless user experience.

# 🛠️ Tech Stack

AI Model: Google Gemma 2 (via Groq API)

Frameworks: LangChain, Streamlit

Tools: WikipediaAPIWrapper, LLMMathChain, LLMChain

Languages: Python

# 📂 Project Structure

your-repo/
├── app.py                # Main Streamlit application
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
└── .env                  # Environment variables (Groq API key)

# 🤔 How It Works

User Input: The user types a question (e.g., a math problem or a general knowledge question).

Tool Selection: The chatbot decides which tool to use (Calculator, Wikipedia, or Reasoning).

Response Generation: The chatbot processes the input and generates a detailed response.

Output: The response is displayed in the chat interface.

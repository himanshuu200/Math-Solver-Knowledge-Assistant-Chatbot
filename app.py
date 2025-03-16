import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

import streamlit as st
from langchain_groq import ChatGroq

# Set up the webpage
st.set_page_config(page_title="Text To Math Problem Solver...", page_icon="🧮")
st.title("Text To Math Problem Solver Using Google Gemma 2")

# Ask for the Groq API key (like a password)
groq_api_key = st.sidebar.text_input(label="Groq API Key", type="password")

# If no API key, stop the app
if not groq_api_key:
    st.info("Please add your Groq API key to continue")
    st.stop()

# Connect to the AI brain (Google Gemma 2 model)
llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)



from langchain_community.utilities import WikipediaAPIWrapper

# Set up Wikipedia tool
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching the Internet to find information on various topics."
)



from langchain.chains import LLMMathChain

# Set up the math tool
math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tool for answering math-related questions. Only input mathematical expressions."
)



from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Set up the reasoning tool
prompt = """
You are an agent tasked with solving users' mathematical questions. Logically arrive at the solution and provide a detailed explanation, displayed point-wise for the question below:
Question: {question}
Answer:
"""

prompt_template = PromptTemplate(
    input_variables=["question"],
    template=prompt
)

# Combine the prompt with the AI brain
chain = LLMChain(llm=llm, prompt=prompt_template)

reasoning_tool = Tool(
    name="Reasoning tool",
    func=chain.run,
    description="A tool for answering logic-based and reasoning questions."
)



from langchain.agents import initialize_agent, Tool, AgentType

assistant_agent = initialize_agent(
    tools=[wikipedia_tool, calculator, reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a Math chatbot who can answer all your math questions."}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

question = st.text_area("Enter your question:")

if st.button("Find my answer"):
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        st.chat_message("user").write(question)

        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = assistant_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write('### Response:')
        st.success(response)
    else:
        st.warning("Please enter the question")
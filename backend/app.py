import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
import re
from dotenv import load_dotenv
app = FastAPI()

load_dotenv()

HUGGINGFACE_HUB_TOKEN = os.getenv('HUGGINGFACE_HUB_TOKEN')
OPENAI = os.getenv('OPENAI')

if not HUGGINGFACE_HUB_TOKEN or not OPENAI:
    raise ValueError("Missing API keys")

model_id = 'mistralai/Mistral-7B-Instruct-v0.1'


# ! CHANGED TEMPLATE FOR CONTEXT
# template = """
# Current Conversation :
# {history}
# Human : {question}
# """


# ! ADDED HISTORY
# prompt = PromptTemplate(template=template, input_variables=["history","question"])

mistral_llm = HuggingFaceHub(
    huggingfacehub_api_token="put your token here",
    repo_id=model_id,
    model_kwargs={"max_new_tokens": 1024, "temperature": 0.2},
)

mistral_llm = HuggingFaceHub(huggingfacehub_api_token=HUGGINGFACE_HUB_TOKEN,
                            repo_id=model_id,
                            model_kwargs={"max_new_tokens":500,"temperature":0.2})

# ! ADDED MEMORY
mistral_chain = ConversationChain(
    llm=mistral_llm, 
    # prompt=prompt, 
    memory=ConversationBufferWindowMemory(k=5)
)

# seperate code and text
def get_code_and_text(response):
    code=re.findall(r'```(.+?)```', response, re.DOTALL)
    text=re.sub(r'```(.+?)```','', response, flags=re.DOTALL)
    return ''.join(code),text

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Text Generation API"}

# ! USED FOR CHAT CALLS
@app.post("/generate_text")
async def generate_text(request_data: dict):
    question = request_data.get('question')
    # prompt = """<s>[INST] Programming Assistance [/INST]\n[s]User: {question}[/s]"""

    if not question:
        raise HTTPException(status_code=400, detail="Question is missing in the request.")

    response = mistral_chain.run(f"[INST]{question}[/INST]")
    # response = mistral_chain.run(prompt)
    code,text=get_code_and_text(response)
    return {"text": text, "code": code}

# ! USED FOR ALGORITHM CALLS
@app.post("/algorithm_complexity")
async def getComplexity(request_data: dict):
    function_name = request_data.get('function_name')
    programming_language = request_data.get('programming_language')
    function_code = request_data.get('function_code')

    if not function_name or not programming_language or not function_code:
        raise HTTPException(status_code=400, detail="Required data is missing in the request.")

    prompt = f"""
    <s>[INST] Given the function name "{function_name}" and the following code:

    ```{programming_language}
    {function_code}
    ```
    Please provide the time complexity of this function, explaining how you arrived at this conclusion.
    Please provide the space complexity of this function, explaining how you arrived at this conclusion.
    If there are any areas where the function's performance in terms of time and space could be improved, please identify them and suggest alternative approaches. [/INST]
    """
    
    response = mistral_chain.run(prompt)
    return {"generated_text": response}

@app.post("/code_convertor")
async def convertCode(request_data: dict):
    pass 


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
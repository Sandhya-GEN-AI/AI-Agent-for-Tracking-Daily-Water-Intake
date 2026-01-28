import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

import sys
sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(api_key = GROQ_API_KEY, temperature = 0.5, model = "openai/gpt-oss-120b")

class WaterInttake:
    def __init__(self):
        self.history = []
        
    def analyze_intake(self, intake_ml):
        
        prompt = f""" 
        
        you are a Hydration Assistant user has consumed {intake_ml} ml of water today. Provide Hydration Status and suggest if they need to drink more water
        
        
        """
        response = llm.invoke(prompt)
        return response.content
    
    
    
if __name__ =="__main__":
    agent = WaterInttake()
    intake = 1500
    feedback = agent.analyze_intake(intake)
    print(f"Hydration Analysis : {feedback}")
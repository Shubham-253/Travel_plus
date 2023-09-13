import os
import re
from flask import Flask, request, jsonify
import openai

from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)

os.environ['OPENAI_API_KEY'] = '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'

from langchain.chat_models import ChatOpenAI
# Prompt templates
# from langchain.prompts.chat import ChatPromptTemplate
from langchain import PromptTemplate

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI

@app.route('/')
def index():
    return "Welcome to the Travel Planner Backend"

@app.route('/plan_trip', methods=['POST'])
def plan_trip():
    try:
        data = request.get_json()
        destination = data.get("destination", "")
        source = data.get("source", "")
        num_days = data.get("numDays", 0)
        
        response = generate_response(destination, source, num_days)
        app.logger.info(f"Response from GPT-3.5: {response}")
        itinerary= response.split("Budget:")[0].split("Itinerary:")[1]
        budget= response.split("Budget:")[1]
        return jsonify({"itinerary": itinerary, "budget": budget})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_response(destination, source, num_days):
    # You can customize the prompt as per your requirements
	
    prompt = f"""Create a detailed {num_days}-day itinerary to experience {destination} and nearby places? 
		Also provide an estimated budget including accommodation considering I am a tourist from {source}. 
		Please keep it budget friendly but do not mention the word budget unnecessarily.
		Keep response structure in following format:
      			'Itinerary': detailed response regarding travel day by day, 
      			'Budget': Keep total Budget in this section in national currency of {source}
		Stick to this response format.
		"""
    chat = ChatOpenAI(model='gpt-3.5-turbo', streaming=True)
    response = chat.predict(prompt)
    return response

if __name__ == '__main__':
    app.run(debug = True)

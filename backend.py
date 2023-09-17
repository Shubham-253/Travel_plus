import os
import re
from flask import Flask, request, jsonify
import openai

from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)

os.environ['OPENAI_API_KEY'] = ''

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
        duration = data.get("duration", "")
        interests = data.get("interests", "")
        budget = data.get("budget", "")
        accommodationPreferences = data.get("accommodationPreferences", "")
        travelStyle = data.get("travelStyle", "")
        specialRequirements = data.get("specialRequirements", "")
        
        response = generate_response(destination,duration, interests, budget, accommodationPreferences, travelStyle, specialRequirements)
        app.logger.info(f"Response from GPT-3.5: {response}")
        return jsonify(response)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def generate_response(destination,duration, interests, budget, accommodationPreferences, travelStyle, specialRequirements):
    
    sample_json = {   "travel_guide": {     "destination": "[Destination]",     "duration": "[Duration]",     "interests": "[Interests]",     "budget": "[Budget]",     "accommodation_preferences": "[Accommodation Preferences]",     "travel_style": "[Travel Style]",     "special_requirements": "[Special Requirements]",     "itinerary": {       "day_1": {         "highlights": ["Arrival in Tokyo"],         "details": [           "Arrive at Narita or Haneda International Airport.",           "Check-in to your chosen accommodation (hotel or Airbnb).",           "Spend the evening exploring the neighborhood, trying some local street food, and getting acclimated to the city."         ]       },       "day_2": {         "highlights": ["Explore Tokyo's Modern Side"],         "details": [           "Visit the iconic Tokyo Tower for panoramic city views.",           "Explore the high-end shopping district of Ginza.",           "Have dinner in the trendy district of Shibuya and experience the famous Shibuya Crossing."         ]       },       "day_3": {         "highlights": ["Cultural Exploration"],         "details": [           "Start your day with a visit to the historic Asakusa district.",           "Explore Senso-ji Temple and Nakamise Shopping Street.",           "In the evening, enjoy traditional Japanese cuisine at a local restaurant."         ]       },       "day_4": {         "highlights": ["Day Trip to Nikko"],         "details": [           "Take a day trip to Nikko to see its beautiful temples and natural beauty.",           "Visit Toshogu Shrine and take a stroll around Lake Chuzenji.",           "Return to Tokyo in the evening."         ]       },       "day_5": {         "highlights": ["Tokyo Disney Resort (Optional)"],         "details": [           "If you're a fan of Disney, consider spending a day at Tokyo Disneyland or DisneySea.",           "Alternatively, explore other parts of Tokyo that pique your interest."         ]       },       "day_6": {         "highlights": ["Arts and Parks"],         "details": [           "Explore Ueno Park, which houses several museums and the Ueno Zoo.",           "Visit the Tokyo National Museum and immerse yourself in Japanese art and history.",           "Enjoy a leisurely walk in the park and try some street food."         ]       },       "day_7": {         "highlights": ["Day Trip to Kamakura"],         "details": [           "Take a day trip to Kamakura to see the Great Buddha (Kotoku-in) and the historic Tsurugaoka Hachimangu Shrine.",           "Explore the charming streets and try some local snacks.",           "Return to Tokyo for your final night."         ]       }     },     "accommodation_recommendations": {       "hotel_option": "Consider staying at hotels like Keio Plaza Hotel Tokyo or APA Hotel Asakusa Tawaramachi Ekimae.",       "airbnb_option": "Look for centrally located Airbnb accommodations in neighborhoods like Shibuya or Shinjuku."     },     "transportation_tips": {       "tips": [         "Use a Japan Rail Pass for long-distance travel.",         "In Tokyo, get a Suica or Pasmo card for easy access to the metro and buses."       ]     },     "essential_travel_tips": {       "currency": "Japanese Yen (JPY)",       "language": "Japanese, but English is spoken in tourist areas.",       "safety": "Tokyo is generally safe, but be cautious of pickpocketing in crowded places.",       "local_customs": "Learn some basic Japanese etiquette, like bowing and taking off your shoes indoors."     }   } }
    # You can customize the prompt as per your requirements
	
    prompt = f"""Create a JSON-formatted travel guide based on the following information: - Destination: {destination} - Duration: {duration} - Interests: {interests} - Budget: {budget} - Accommodation Preferences: {accommodationPreferences} - Travel Style: {travelStyle} - Special Requirements: {specialRequirements} The response should strictly follow this JSON structure: ```json {sample_json} """
    chat = ChatOpenAI(model='gpt-3.5-turbo', streaming=True)
    response = chat.predict(prompt)
    return response

if __name__ == '__main__':
    app.run(debug = True)

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage, HumanMessage
from typing import List, Dict
import json
from dataclasses import dataclass

SYSTEM_PROMPT = """
You are an expert travel assistant specialized in creating personalized travel experiences. Create detailed itineraries following these guidelines:

1. Destination Details:
   - Include must-visit attractions
   - Local cultural experiences
   - Transportation recommendations
   - Best areas to stay

2. Food and Dining:
   - Restaurant recommendations based on dietary preferences (Vegetarian/Non-vegetarian/Vegan)
   - Local specialties and must-try dishes
   - Popular food districts/streets
   - Price ranges for meals

3. Traveler Type Considerations:
   - Adventure seekers: Include thrilling activities and unique experiences
   - Culture enthusiasts: Focus on museums, historical sites, local customs
   - Relaxation seekers: Include spas, peaceful locations, leisure activities
   - Family travelers: Kid-friendly activities and family-suitable venues
   - Budget travelers: Cost-effective options and money-saving tips
   - Luxury travelers: High-end experiences and exclusive venues

4. Daily Schedule:
   - Morning, afternoon, and evening activities
   - Estimated timings and durations
   - Travel times between locations
   - Meal timings and venues

5. Additional Information:
   - Local customs and etiquette
   - Weather considerations
   - Safety tips
   - Booking recommendations
   - Local emergency contacts

Format the response in clear sections with emojis for better readability.
"""

@dataclass
class TripData:
    destination: str
    days: int
    budget: str
    traveler_type: str
    food_preference: str
    group_size: int

def initialize_session_state():
    if "trip_data" not in st.session_state:
        st.session_state.trip_data = TripData("", 1, "", "", "", 1)
    if "current_step" not in st.session_state:
        st.session_state.current_step = 0
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "generated_trip" not in st.session_state:
        st.session_state.generated_trip = None

def generate_trip_prompt(trip_data: TripData) -> str:
    return f"""
    Create a detailed {trip_data.days}-day trip itinerary for {trip_data.destination} with the following preferences:
    - Budget: {trip_data.budget}
    - Traveler Type: {trip_data.traveler_type}
    - Food Preference: {trip_data.food_preference}
    - Group Size: {trip_data.group_size} people
    
    Please include specific restaurants matching the {trip_data.food_preference} preference and activities suitable for {trip_data.traveler_type} travelers.
    """

def generate_ai_trip(trip_data: TripData) -> str:
    llm = ChatGroq(
        model="llama3-70b-8192",
        api_key="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" 
    )
    
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", generate_trip_prompt(trip_data))
    ])
    
    chain = chat_prompt | llm | StrOutputParser()
    
    return chain.invoke({})

def main():
    st.set_page_config(
        page_title="AI Travel Planner",
        page_icon="✈️",
        layout="wide"
    )
    
    initialize_session_state()
    
    st.title("✈️ AI Travel Planner")
    st.markdown("### Your personalized travel companion")
    
    steps = [
        {"title": "Destination", "key": "destination", "type": "text", "icon": "🌍"},
        {"title": "Duration (days)", "key": "days", "type": "number", "icon": "📅"},
        {"title": "Budget", "key": "budget", "type": "text", "icon": "💰"},
        {"title": "Traveler Type", "key": "traveler_type", "type": "select", "icon": "👤"},
        {"title": "Food Preference", "key": "food_preference", "type": "select", "icon": "🍽️"},
        {"title": "Group Size", "key": "group_size", "type": "number", "icon": "👥"}
    ]
    
    traveler_types = [
        "Adventure Seeker",
        "Culture Enthusiast",
        "Relaxation Seeker",
        "Family Traveler",
        "Budget Traveler",
        "Luxury Traveler"
    ]
    
    food_preferences = [
        "Vegetarian",
        "Non-vegetarian",
        "Vegan",
        "No Preference"
    ]
    
    current_step = st.session_state.current_step
    
    progress = current_step / len(steps)
    st.progress(progress)
    
    if current_step < len(steps):
        st.subheader(f"{steps[current_step]['icon']} {steps[current_step]['title']}")
        
        if steps[current_step]['type'] == "number":
            if steps[current_step]['key'] == "days":
                value = st.number_input(
                    "Enter number of days",
                    min_value=1,
                    max_value=30,
                    value=st.session_state.trip_data.days
                )
            else:  # group_size
                value = st.number_input(
                    "Enter number of travelers",
                    min_value=1,
                    max_value=20,
                    value=st.session_state.trip_data.group_size
                )
            setattr(st.session_state.trip_data, steps[current_step]['key'], value)
            
        elif steps[current_step]['type'] == "select":
            if steps[current_step]['key'] == "traveler_type":
                value = st.selectbox(
                    "Select traveler type",
                    options=traveler_types
                )
            else:  
                value = st.selectbox(
                    "Select food preference",
                    options=food_preferences
                )
            setattr(st.session_state.trip_data, steps[current_step]['key'], value)
            
        else:  # text input
            value = st.text_input(
                f"Enter {steps[current_step]['title'].lower()}",
                value=getattr(st.session_state.trip_data, steps[current_step]['key'])
            )
            setattr(st.session_state.trip_data, steps[current_step]['key'], value)
        
        if st.button("Next"):
            st.session_state.current_step += 1
            st.rerun()
            
    else:
        if not st.session_state.generated_trip:
            with st.spinner("🤖 AI is crafting your perfect trip..."):
                try:
                    trip_response = generate_ai_trip(st.session_state.trip_data)
                    st.session_state.generated_trip = trip_response
                except Exception as e:
                    st.error(f"Error generating trip: {str(e)}")
                    if st.button("Try Again"):
                        st.session_state.current_step = 0
                        st.rerun()
                    return
        
        st.markdown(st.session_state.generated_trip)
        
        if st.button("Plan Another Trip"):
            st.session_state.current_step = 0
            st.session_state.trip_data = TripData("", 1, "", "", "", 1)
            st.session_state.generated_trip = None
            st.rerun()

if __name__ == "__main__":
    main()
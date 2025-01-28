

### **Documentation: AI Travel Planner Application**

---

#### **1. Prompts Used**
##### **System Prompt**:
```plaintext
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
```

##### **User Prompt**:
```plaintext
Create a detailed 5-day trip itinerary for Paris with the following preferences:
- Budget: Moderate
- Traveler Type: Culture Enthusiast
- Food Preference: Vegetarian
- Group Size: 2 people

Please include specific restaurants matching the Vegetarian preference and activities suitable for Culture Enthusiast travelers.
```

##### **Model Response**:
```plaintext
🎨 **Day 1: Exploring Parisian Charm**
- **Morning**: Visit the iconic Eiffel Tower; enjoy breathtaking views (2 hours).
- **Lunch**: Dine at "Le Grenier de Notre-Dame" (Vegetarian-friendly, €€).
- **Afternoon**: Explore Musée d'Orsay for art and history (3 hours).
- **Evening**: Walk along the Seine River and enjoy street performances.

🍷 **Day 2: Historical Adventures**
- **Morning**: Tour the Palace of Versailles (4 hours, includes transport).
- **Lunch**: Try vegetarian delights at "Le Potager du Marais" (€€).
- **Afternoon**: Relax in Luxembourg Gardens and explore local markets.
- **Evening**: Wine tasting at a Parisian vineyard.

... (Detailed itinerary continues for each day)
```

---

#### **2. Sample Input and Output**
##### **Sample Input**:
```plaintext
Create a detailed 7-day trip itinerary for Tokyo with the following preferences:
- Budget: Luxury
- Traveler Type: Adventure Seeker
- Food Preference: Non-vegetarian
- Group Size: 4 people
```

##### **Sample Output**:
```plaintext
🎌 **Day 1: Arrival and Shibuya**
- **Morning**: Arrive at Narita International Airport and check in at "The Ritz-Carlton Tokyo".
- **Lunch**: Enjoy fresh sushi at "Sukiyabashi Jiro" (Luxury dining).
- **Afternoon**: Explore Shibuya Crossing and shop at Harajuku (3 hours).
- **Evening**: Rooftop drinks at "Two Rooms Grill and Bar".

🌄 **Day 2: Mount Fuji Day Trip**
- **Morning**: Private tour to Mount Fuji with a scenic train ride.
- **Lunch**: Traditional Japanese meal at a local ryokan (Non-vegetarian options).
- **Afternoon**: Hike and explore nearby villages.
- **Evening**: Return to Tokyo and enjoy Kaiseki dinner at "Ishikawa".

... (Detailed schedule continues for all 7 days)
```

---

#### **3. Process Documentation**

##### **Prompt 1: System Setup**
**Objective**: Define the application's expertise and scope.  
**Process**:  
- Drafted a comprehensive system prompt that establishes the application as an expert travel assistant.  
- Included guidelines for destinations, food, traveler types, daily schedules, and additional tips.

##### **Prompt 2: User Query**
**Objective**: Collect user-specific preferences for itinerary generation.  
**Process**:  
- Designed a form in Streamlit to accept inputs (destination, days, budget, etc.).  
- Structured these inputs to create a user query that the AI can process.  

##### **Prompt 3: Itinerary Generation**
**Objective**: Generate a complete itinerary based on the input.  
**Process**:  
- Used `ChatGroq` to send the system and user prompts to the LLM.  
- Applied parsing to format the AI's response into user-friendly sections.

##### **Prompt 4: User Interface**
**Objective**: Build a user-friendly frontend.  
**Process**:  
- Used Streamlit to create a step-by-step form interface.  
- Enabled progress tracking, real-time input updates, and seamless AI integration.

---

#### **4. Hosted Application**
You can test the live application here: **[AI Travel Planner (Streamlit)](https://tripplanner-fwxhuqthw4ougv5bk2zr6q.streamlit.app/)**  


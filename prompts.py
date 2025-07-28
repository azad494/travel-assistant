# prompts.py

def build_prompt(destination, days, budget, season, interests):
    return (
        f"You are a professional travel guide. Create a detailed {days}-day itinerary for a trip to {destination} "
        f"in the {season} season for a {budget.lower()} budget traveler. The traveler is interested in {interests}. "
        "Include daily plans, places to visit, travel tips, and local experiences."
    )

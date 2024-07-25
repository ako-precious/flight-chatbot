from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route('/')
def home():
    return jsonify({"student_number": "200545932"})

# Webhook route to handle Dialogflow requests
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent = req.get('queryResult').get('intent').get('displayName')

    if intent == 'FlightsToCountry':
        country = req.get('queryResult').get('parameters').get('geo-country')
        flights = get_flights_to_country(country)
        response_text = f"Flights to {country}: {', '.join(flights)}"
    else:
        response_text = "I'm not sure how to handle that request."

    return jsonify({
        "fulfillmentText": response_text
    })

def get_flights_to_country(country):
    # Placeholder function, replace with actual data retrieval logic
    flights_dict = {
        "USA": ["Flight AA123", "Flight UA456"],
        "Canada": ["Flight AC789", "Flight WS012"],
        "UK": ["Flight BA345", "Flight VS678"],
        "Nigeria": ["Flight BA745", "Flight MS678"],
        "Nepal": ["Flight BA390", "Flight YS678"]
    }
    return flights_dict.get(country, ["No flights available"])

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route('/')
def home():
    return jsonify({"student_number": "123456789"})

# Webhook route to handle Dialogflow requests
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent = req.get('queryResult').get('intent').get('displayName')

    if intent == 'CheckFlightStatus':
        flight_number = req.get('queryResult').get('parameters').get('flight_number')
        status = "On time"  # Placeholder status, in a real application this would come from an API call or database
        response_text = f"The current status of flight {flight_number} is: {status}"
    else:
        response_text = "I'm not sure how to handle that request."

    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(debug=True)

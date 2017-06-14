from flask import Flask, request 
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def voice():
    """Respond to incoming requests."""
    resp = VoiceResponse()
    #esp.say("Hello this is Acme company. We have created a new high severity incident for Commodity Malware. Press 1 to acknowledge this alert and stop the call tree. Press 2 for the incident's description. Press 3 for the host's IP address. ")

    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']

        # <Say> a different message depending on the caller's choice
        if choice == '1':
            #Need to record the response somehow here...
            resp.say('Thank you, your response has been recorded and the call tree stopped', voice="alice", language="en-US")
            resp.redirect('/')
        elif choice == '2':
            resp.say('The incident summary is Zeus/Zbot (or Variant) Infection - 10.46.14.208', voice="alice", language="en-US")
            resp.redirect('/') #Redirect back to to the main.
        elif choice == '3':
            resp.say('The affected host is located at 10.46.14.208. Is this better? 10 Dot. 4 6 Dot. 14 Dot. 2 0 8.', voice="alice", language="en-US")
            resp.redirect('/')
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.", voice="alice", language="en-US")

    # Start our <Gather> verb
    gather = Gather(num_digits=1)
    gather.say('Hello this is Acme company. We have created a new high severity incident for Commodity Malware. Press 1 to acknowledge this alert and stop the call tree. Press 2 for the incident description. Press 3 for the IP address.', voice="alice", language="en-US")
    resp.append(gather)

    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/')


    return str(resp)
if __name__ == "__main__":
    app.run(debug=True, port=5001)

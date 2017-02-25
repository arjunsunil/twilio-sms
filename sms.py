from twilio.rest import TwilioRestClient

account_sid = "************" # Your Account SID from www.twilio.com/console
auth_token  = "********"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)
text=raw_input("enter the text to send to \n")
message = client.messages.create(body=text,
    to="*********",    # Replace with your phone number
    from_="*******") # Replace with your Twilio number

print(message.sid)

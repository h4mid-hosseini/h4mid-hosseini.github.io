import base64

message = input("enter the string: ")
print("original string: ",message)
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print("encoded string: ",base64_message)
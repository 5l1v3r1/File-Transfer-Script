import socket

HOST = "" # Put Server IP Address here
PORT = 3000

BYTE_SIZE = 200000 # Size of file you send (measured in bytes)

def SocketReceiveFile():
    # Establish Connection with Server
    while (True):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Listening for Connection...")
            client.connect((HOST,PORT))
        except (socket.error, Exception):
            print("No Connection found, retrying...")
        else: break
    
    # Create a file and write the bytes received from server
    bytes = client.recv(BYTE_SIZE) # Receive Bytes
    file = open("file.txt", "wb") # Include file name for receiving
    file.write(bytes) # Write the bytes
    file.close() # Close the file
    print("[+] File Successfully Received!")
    
SocketReceiveFile()
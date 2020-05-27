import socket

HOST = "0.0.0.0" # Keep Default Address
PORT = 3000

def SocketSendFile():
    # Establish Connection with Client
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, Exception) as e1:
        print("[1] Error Occured: "+str(e1))
        
    try:
        server.bind((HOST,PORT))
        server.listen(20)
        print("Listening for Connection...")
    except (socket.error, Exception) as e2:
        print("[2] Error Occured: "+str(e2))
        
    # Accept Connection
    while (True):
        try:
            conn, address = server.accept()
            
            # Read the files as (rb): read bytes and send it
            file = open("client.exe", "rb") # Include file name for sending
            conn.send(file.read()) # Read the bytes from file + send
            file.close() # Close the file
            
            print("[+] File Successfully transfered!")
            return (True)
        except (socket.error, Exception) as e3:
            print("[3] Error Occured: "+str(e3))
            continue
        
SocketSendFile()
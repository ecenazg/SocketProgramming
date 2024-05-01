import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Let the user define a port number
    port = int(input("Enter port number: "))
    client_socket.bind(('localhost', port))  # Bind to the user-defined port

    server_address = ('localhost', 5000)

    try:
        while True:
            message = input("Enter message or type 'exit' to quit: ")
            if message.lower() == 'exit':
                break

            # Send message to the server
            client_socket.sendto(message.encode(), server_address)

            # Receive and print server response
            response, _ = client_socket.recvfrom(1024)
            print("Server response:", response.decode())

            # Close client if the port is not allowed to communicate
            if response.decode() == "Port is not allowed to communicate":
                print("Disconnected by the server: port not allowed.")
                break

    except Exception as e:
        print("Client Error:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()

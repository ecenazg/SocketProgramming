import socket

def main():
    try:
        # Create a UDP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Ask user to define a port number
        port = int(input("Enter port number: "))

        # Connect to server
        server_address = ('localhost', port)

        while True:
            # Get user input for message
            message = input("Enter message: ")

            # Check if the message is empty
            if not message:
                print("Invalid Message")
                continue

            # Check message format
            if port == 1234:
                if not message.startswith("Permission"):
                    print("Invalid Message")
                    continue
                elif not message[10:].isdigit():
                    print("Invalid Message")
                    continue
            elif port == 3333:
                if not message.startswith("Request"):
                    print("Invalid Message")
                    continue
                elif not message[7:].isdigit():
                    print("Invalid Message")
                    continue

            # Send message to server
            client_socket.sendto(message.encode(), server_address)

            # Receive server response
            response, _ = client_socket.recvfrom(1024)
            print("Server response:", response.decode())

    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
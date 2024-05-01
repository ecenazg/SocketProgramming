
import socket

def main():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to localhost and a specific port
    server_socket.bind(('localhost', 9999))

    # List to keep track of permitted numbers
    permitted_numbers = []

    # Counter to keep track of the number of clients
    client_count = 0

    try:
        while True:
            # Receive message from client
            message, client_address = server_socket.recvfrom(1024)
            client_count += 1

            # Extract port number from client address
            client_port = client_address[1]

            # Print received message and client address
            print("Received message:", message.decode())
            print("From client:", client_address)

            # Check if total number of clients is greater than or equal to 4
            if client_count >= 4:
                print("Closing server socket.")
                break

            # Handle messages based on client port
            if client_port == 1234:
                # Process messages for port 1234
                if message.decode().startswith("Permission"):
                    try:
                        number = int(message.decode().split()[-1])  # Extract the last element as the number
                        if number not in permitted_numbers:
                            permitted_numbers.append(number)
                            server_socket.sendto("Permission Accepted".encode(), client_address)
                        else:
                            server_socket.sendto("Already Permitted".encode(), client_address)
                    except ValueError:
                        server_socket.sendto("Invalid Message".encode(), client_address)
                else:
                    server_socket.sendto("Invalid Message".encode(), client_address)

            elif client_port == 3333:
                # Process messages for port 3333
                if message.decode().startswith("Request"):
                    try:
                        number = int(message.decode().split()[-1])  # Extract the last element as the number
                        if number in permitted_numbers:
                            server_socket.sendto("Request Accepted".encode(), client_address)
                        else:
                            server_socket.sendto("Request Rejected".encode(), client_address)
                    except ValueError:
                        server_socket.sendto("Invalid Message".encode(), client_address)
                else:
                    server_socket.sendto("Invalid Message".encode(), client_address)

            else:
                # Send "Port is not allowed to communicate" response
                server_socket.sendto("Port is not allowed to communicate".encode(), client_address)

    except Exception as e:
        print("Error:", e)
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()

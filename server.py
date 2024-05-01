import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 5000))  # Server listens on a fixed port

    permitted_numbers = []
    client_ports = set()  # Set to track unique client ports

    try:
        while len(client_ports) < 4:
            data, addr = server_socket.recvfrom(1024)
            message = data.decode().strip()
            client_port = addr[1]

            print("Message:", message)
            print("Client Address:", addr)

            # Attempt to add client port to set of unique ports
            client_ports.add(client_port)  # Track all unique client ports

            response = "Invalid Message"

            # Specific handling for allowed ports
            if client_port == 1234:
                if message.lower().startswith("permission") and message[len("permission"):].isdigit():
                    number = int(message[len("permission"):])
                    if number in permitted_numbers:
                        response = "Already Permitted"
                    else:
                        permitted_numbers.append(number)
                        response = "Permission Accepted"
                else:
                    response = "Invalid Message"
            elif client_port == 3333:
                if message.lower().startswith("request") and message[len("request"):].isdigit():
                    number = int(message[len("request"):])
                    if number in permitted_numbers:
                        response = "Request Accepted"
                    else:
                        response = "Request Rejected"
                else:
                    response = "Invalid Message"
            else:
                # Send a specific message for non-allowed ports
                response = "Port is not allowed to communicate"

            server_socket.sendto(response.encode(), addr)

    except Exception as e:
        print("Server Error:", e)
    finally:
        server_socket.close()
        print(f"The number of connected clients is: {len(client_ports)}")

if __name__ == "__main__":
    main()

import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 5000))  # Server listens on a fixed port

    permitted_numbers = []
    client_count = 0

    try:
        while client_count < 4:
            data, addr = server_socket.recvfrom(1024)
            message = data.decode().strip()  # Decode and strip any leading/trailing whitespace
            lower_message = message.lower()  # Convert message to lowercase for case-insensitive comparison
            client_port = addr[1]

            print("Received message:", message)
            print("From client:", addr)

            response = "Invalid Message"
            should_count = False  # Indicator to determine if the client count should be incremented

            if client_port == 1234:
                if lower_message.startswith("permission") and lower_message[len("permission"):].isdigit():
                    number = int(lower_message[len("permission"):])
                    if number in permitted_numbers:
                        response = "Already Permitted"
                    else:
                        permitted_numbers.append(number)
                        response = "Permission Accepted"
                        should_count = True  # Valid new message, should count
                else:
                    response = "Invalid Message"
            elif client_port == 3333:
                if lower_message.startswith("request") and lower_message[len("request"):].isdigit():
                    number = int(lower_message[len("request"):])
                    if number in permitted_numbers:
                        response = "Request Accepted"
                        should_count = True  # Valid new message, should count
                    else:
                        response = "Request Rejected"
                else:
                    response = "Invalid Message"
            else:
                response = "Port is not allowed to communicate"

            server_socket.sendto(response.encode(), addr)

            # Increment client count only for new valid messages
            if should_count:
                client_count += 1

            if client_count >= 4:
                print("Maximum client messages received. Closing server.")
                break

    except Exception as e:
        print("Server Error:", e)
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()

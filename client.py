import socket

HOST = "127.0.0.1"
PORT = 65432

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        while True:
            message = input("Enter message (type 'bye' to quit): ")
            client_socket.sendall(message.encode())

            response = client_socket.recv(1024).decode()
            print(f"Server replied: {response}")

            if message.lower() == "bye":
                break

    except ConnectionRefusedError:
        print("Error: Server is not running.")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()
        print("Client shut down.")

if __name__ == "__main__":
    run_client()
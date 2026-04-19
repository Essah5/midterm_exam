import socket

HOST = "127.0.0.1"
PORT = 65432

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")

            while True:
                data = conn.recv(1024)
                if not data:
                    print("Client disconnected.")
                    break

                message = data.decode()
                print(f"Client says: {message}")

                if message.lower() == "bye":
                    conn.sendall("Goodbye from server.".encode())
                    break

                response = f"Server received: {message}"
                conn.sendall(response.encode())

    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()
        print("Server shut down.")

if __name__ == "__main__":
    run_server()
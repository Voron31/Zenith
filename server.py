import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 9090))  # Слушаем на всех интерфейсах
    server_socket.listen(1)
    print("Ожидание подключения...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключено: {client_address}")

        data = client_socket.recv(1024).decode("utf-8")
        print(f"Получено сообщение: {data}")

        if data:
            client_socket.sendall(data.encode("utf-8"))
        client_socket.close()

if __name__ == "__main__":
    start_server()

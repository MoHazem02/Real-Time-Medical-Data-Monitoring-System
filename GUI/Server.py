import socket, json, redis
class Server:
    def __init__(self, client):
        self.socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_connection.bind(("192.168.1.4", 5050))
        self.socket_connection.listen(1)
        self.step = 1 # Timestep for the generated vitals, updated every 2 seconds
        self.redis_connection = redis.Redis(host='localhost', port=6379)
        self.client = client
        self.steps = [1]

    def receive_data(self):
        while True:
            conn, _ = self.socket_connection.accept()
            try:
                data = conn.recv(1024)
                if data:
                    data = json.loads(data.decode())
            except Exception as e:
                print("Error:", e)
            finally:
                conn.close()
                break
        self.register_data(data)
            
    def register_data(self, data):
        # {'1': 35, '2': 38, '3': 38, '4': 35, '5': 39}
        for key, value in data.items():
            print(f"Patient {key} temperature: {value}")
            self.redis_connection.set(f"{key}_{self.step}", value) # Format is {patient_id}_{step}
        self.step += 1
        self.steps.append(self.step)
        self.client.update_readings()

    def return_data(self, patient_id) -> int:
        result = self.redis_connection.get(f"{patient_id}_{self.step}")
        if result:
            return int(result)
        return None
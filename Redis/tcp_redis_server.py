import socket
import json
import redis

# Function to retrieve patient data from Redis
def get_patient_data(patient_id, redis_client):
    redis_key = f"patient:{patient_id}"
    data = redis_client.get(redis_key)
    if data:
        return json.loads(data)
    else:
        return None

# Function to handle client connections
def handle_client(client_socket, redis_client):
    # Receive data from the client
    data = client_socket.recv(1024)
    if not data:
        return
    
    # Decode JSON data received from the client
    try:
        data_decoded = json.loads(data.decode('utf-8'))
    except json.JSONDecodeError:
        print("Invalid JSON data received from client")
        return
    
    # Extract patient ID and vital signs from the received data
    patient_id = data_decoded.get('patient_id')
    vital_signs = data_decoded.get('vital_signs')
    
    # Store the data in Redis
    redis_key = f"patient:{patient_id}"
    redis_client.set(redis_key, json.dumps(vital_signs))
    print(f"Data stored in Redis: {patient_id} - {vital_signs}")

# Main function to run the TCP server
def run_server(host, port):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    
    # Create a Redis client
    redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
    
    try:
        while True:
            # Accept incoming connections
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            
            # Handle client connection in a separate thread
            handle_client(client_socket, redis_client)
            
            # Close the client socket
            client_socket.close()
    except KeyboardInterrupt:
        print("Server stopped")

# Run the TCP server on localhost and port 8000
if __name__ == "__main__":
    run_server('localhost', 8000)

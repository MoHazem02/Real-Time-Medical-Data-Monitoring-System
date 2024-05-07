import redis

class RedisManager:
    def __init__(self, host='localhost', port=6379, db=0):
        self.host = host
        self.port = port
        self.db = db
        self.connection = None

    def connect(self):
        self.connection = redis.Redis(host=self.host, port=self.port, db=self.db)

    def set_data(self, key, value):
        self.connection.set(key, value)

    def get_data(self, key):
        return self.connection.get(key)

    def close(self):
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    redis_manager = RedisManager()
    redis_manager.connect()

    # Set data
    redis_manager.set_data('her_you_type_the_key', 'Her you type the value or the massage you want to store in the key.')

    # Get data
    value = redis_manager.get_data('her_you_type_the_key')
    print(value)

    redis_manager.close()

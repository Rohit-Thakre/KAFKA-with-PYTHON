from kafka import KafkaProducer

TOPIC = 'test-topic'

# Kafka Producer
def produce_messages():
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    for i in range(10):
        message = f"Message {i}"
        producer.send(TOPIC, message.encode('utf-8'))
        print(f"Produced: {message}")
    producer.close()


if __name__ == "__main__":
    produce_messages()
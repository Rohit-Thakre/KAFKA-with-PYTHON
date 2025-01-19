from kafka import KafkaConsumer

TOPIC = 'test-topic'

def consume_messages():
    print("Consuming messages...")
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest',
        group_id='test-group'
    )
    for message in consumer:
        print(f"Consumed: {message.value.decode('utf-8')}")

if __name__ == "__main__":
    consume_messages()

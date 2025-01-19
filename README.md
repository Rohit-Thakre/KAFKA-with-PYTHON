README
# KAFKA-with-PYTHON

## Directory Structure

```
/project
  ├── docker-compose.yml
  ├── python_app
      ├── Dockerfile
      ├── consumer.py
      ├── producer.py
      ├── requirements.txt
```

## Setup 
run the following command in shell to start the containers
```
docker compose up --build
```

Enter the Python container
```
docker exec -it python_app bash
```

Start the Consumer
```
python python-app/consumer.py
```

Start the Producer
```
python python-app/producer.py
```


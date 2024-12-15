from kafka import KafkaProducer
import requests
import json
import time

# Configurer le producteur Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# API Binance pour récupérer les prix des cryptomonnaies
BINANCE_API_URL = "https://api.binance.com/api/v3/ticker/price"

try:
    print("Envoi de données depuis Binance au topic 'test'...")
    while True:
        response = requests.get(BINANCE_API_URL)
        prices = response.json()  # Liste des paires de trading et leurs prix
        for price in prices:
            data = {
                "symbol": price["symbol"],
                "price": float(price["price"]),
                "timestamp": time.time()
            }
            producer.send('test', data)
            print(f"Envoyé : {data}")
        time.sleep(5)  # Pause de 5 secondes entre chaque requête
except KeyboardInterrupt:
    print("Producteur arrêté.")
finally:
    producer.close()




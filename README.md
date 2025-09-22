### Etat des données
``` bash
ID
BPM
Température
PourcentageBatterie
Alerte
Longitude
Latitude
Timestamp
```

### Lancement des containers
```bash
sudo docker compose up --build -d --scale producer=5
```

### Visualisation des topics
```bash
sudo docker compose exec kafka kafka-topics --bootstrap-server kafka:9092 --list
```

### Visualisation des messages
```bash
sudo docker compose exec kafka kafka-console-consumer --bootstrap-server kafka:9092 --topic pacemaker --from-beginning
```

### Arrêt des containers
```bash
sudo docker compose down -v --remove-orphans
```
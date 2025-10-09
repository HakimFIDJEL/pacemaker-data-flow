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

### Accéder à l'UI PHPMYADMIN
```bash
http://localhost:8081
```

### Accéder à l'UI NIFI
```bash
http://localhost:8443/nifi
```

### Arrêt des containers
```bash
sudo docker compose down -v --remove-orphans
```
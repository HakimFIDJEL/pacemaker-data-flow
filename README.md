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

## Configuration NIFI

Une fois connecté, glisser un **processor** sur la grille, sélectionnez comme *type* **Consume Kafka**. Double cliquer dessus, dans l'onglet *Settings*, lui donner le *name* **ConsumeKafka**, dans l'onglet *Properties*, cliquez sur les 3 points à droite de *Kafka Connection Service* et cliquez sur *Create new service* et sélectionnez **Kafka3ConnectionService**, re cliquez sur les 3 points puis sur *Go to service*, cliquez sur les 3 points du service puis sur *Edit*, remplissez *BootstrapServers* par **kafka:9092** puis appliquez et *enable* le service. Retournez sur le *Processor*, dans l'onglet *Properties* et remplissez *Group ID* par **nifi-consumer** et *topics* par **pacemaker** puis apply. Faites glissez un *funnel* sur la grille et reliez la flèche du *processor* vers le *funnel* puis cliquez sur l'éclair du *processor* pour enable.

Une fois connecté, glisser un **processor** sur la grille, sélectionnez comme *type* **PutDatabaseRecord**. Double cliquer dessus, dans l'onglet *Properties*, cliquez sur les 3 points à droite de *Database Connection Pooling Service* et cliquez sur *Create new service*, remplissez *DatabaseConnectionURL* par **jdbc:mysql://mysql:3306/pacedb?characterEncoding=UTF-8&serverTimezone=UTC**, remplissez *Database Driver Class Name* par **com.mysql.cj.jdbc.Driver**, remplissez *Database Drive Location(s)* par **/opt/nifi/nifi-current/lib/mysql-connector-j-8.4.0.jar**, remplissez *Database User* par **root** puis *Password* par **password** puis *Apply* puis *enable*. Revenez en arrière, dans *Record Reader* faites **Record Reader → … → Create new service → JsonTreeReader → Enable**, puis remplissez *Table name* par **pacemaker_events**, sélectionnez pour *Statement Type* avec **INSERT** puis *Apply*.
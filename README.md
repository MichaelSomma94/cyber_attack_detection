# cyber_attack_detection


## Prerequisites

- Kafka and Zookeeper are assumed to be installed. If not, download from [Apache Kafka](https://kafka.apache.org/downloads) and extract using the following command:

  ```bash
  tar -xzf kafka_2.13-2.8.0.tgz -C /path/to/destination
  ```

  Replace `/path/to/destination` with your preferred installation directory, such as `~/kafka`.

## Step 1: Configuring Zookeeper

Edit the `config/zookeeper.properties` file in your Kafka directory:

```properties
dataDir=/path/to/kafka/data/zookeeper  # Path to Zookeeper data directory
clientPort=2181
maxClientCnxns=0
```

## Step 2: Configuring Kafka

Modify the `config/server.properties` file:

```properties
log.dirs=/path/to/kafka/data/kafka  # Path to Kafka logs directory
broker.id=0
listeners=PLAINTEXT://:9092
zookeeper.connect=localhost:2181
```

## Step 3: Starting Zookeeper

Open a terminal and execute:

```bash
/path/to/kafka/bin/zookeeper-server-start.sh /path/to/kafka/config/zookeeper.properties
```

## Step 4: Starting Kafka

In a new terminal window, run:

```bash
/path/to/kafka/bin/kafka-server-start.sh /path/to/kafka/config/server.properties
```

## Step 5: Creating Kafka Topics

Create the topics for network data and detected anomalies.

### Create Network Data Topic

```bash
/path/to/kafka/bin/kafka-topics.sh --create --topic network_data_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### Create Detected Anomalies Topic

```bash
/path/to/kafka/bin/kafka-topics.sh --create --topic detected_anomalies --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

## Verification

To verify the creation of the topics:

```bash
/path/to/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```


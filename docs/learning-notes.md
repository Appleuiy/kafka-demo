# Kafka 学习笔记

## 核心概念

### Topic（主题）
- Kafka 中消息的分类
- 类似于数据库中的表
- 可以有多个分区（Partition）

### Partition（分区）
- Topic 的物理分割
- 每个分区是一个有序的、不可变的记录序列
- 分区允许并行处理

### Producer（生产者）
- 向 Topic 发送消息的客户端
- 可以指定消息发送到哪个分区

### Consumer（消费者）
- 从 Topic 读取消息的客户端
- 可以组成 Consumer Group 进行负载均衡

### Consumer Group（消费者组）
- 多个消费者组成的组
- 组内的消费者共同消费一个 Topic
- 每个分区只能被组内的一个消费者消费

### Offset（偏移量）
- 消费者在分区中的位置
- 用于记录消费者读取进度

## 常用命令

### 创建 Topic
```bash
kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
```

### 列出所有 Topic
```bash
kafka-topics.sh --list --bootstrap-server localhost:9092
```

### 查看 Topic 详情
```bash
kafka-topics.sh --describe --topic test-topic --bootstrap-server localhost:9092
```

### 发送消息
```bash
kafka-console-producer.sh --topic test-topic --bootstrap-server localhost:9092
```

### 消费消息
```bash
kafka-console-consumer.sh --topic test-topic --from-beginning --bootstrap-server localhost:9092
```

## 学习资源

- [Kafka 官方文档](https://kafka.apache.org/documentation/)
- [Kafka 快速入门](https://kafka.apache.org/quickstart)

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

## Kafka 架构演进：从 Zookeeper 到 KRaft

### 为什么 Kafka 放弃 Zookeeper？

Kafka 从 2.8.0 版本开始引入 **KRaft 模式**（Kafka Raft），并在 3.3.0 版本中正式生产可用。从 Kafka 4.0 开始，Zookeeper 模式将被完全移除。

#### Zookeeper 模式的问题

1. **架构复杂性**
   - 需要维护两套系统：Kafka Broker 和 Zookeeper 集群
   - 增加了运维成本和故障点
   - Zookeeper 需要单独的服务器资源

2. **性能瓶颈**
   - Zookeeper 的元数据存储限制了 Kafka 的扩展性
   - 大量分区（如 100,000+）时，Zookeeper 成为性能瓶颈
   - 元数据变更需要同步到 Zookeeper，存在延迟

3. **扩展性限制**
   - Zookeeper 不适合存储大量元数据
   - 分区数量受限于 Zookeeper 的性能
   - 无法支持超大规模集群

4. **运维困难**
   - 需要同时管理 Kafka 和 Zookeeper 的配置
   - Zookeeper 的故障会影响整个 Kafka 集群
   - 升级和迁移更加复杂

#### KRaft 模式的优势

1. **简化架构**
   - 不再需要 Zookeeper
   - 元数据直接存储在 Kafka 内部
   - 减少了系统组件，降低运维复杂度

2. **更好的性能**
   - 元数据操作更快
   - 支持更大规模的分区（百万级分区）
   - 启动时间显著减少（从分钟级降到秒级）

3. **更强的扩展性**
   - 可以支持更多分区和主题
   - 元数据管理更加高效
   - 支持更快的元数据变更

4. **更简单的运维**
   - 只需要管理 Kafka 集群
   - 配置更简单
   - 升级和迁移更容易

#### KRaft 模式的工作原理

KRaft 使用 **Raft 一致性算法**来管理元数据：
- Controller 节点通过 Raft 协议选举 Leader
- 元数据存储在 Kafka 内部的特殊 Topic（`__cluster_metadata`）
- 所有 Broker 都可以访问元数据，无需依赖外部系统

#### 迁移时间线

- **Kafka 2.8.0** (2021年): 引入 KRaft 模式（早期访问）
- **Kafka 3.3.0** (2022年): KRaft 模式生产可用
- **Kafka 3.5.0** (2023年): 改进 KRaft 模式稳定性
- **Kafka 4.0** (计划中): 完全移除 Zookeeper 支持

#### 当前项目说明

本项目使用的是 **Zookeeper 模式**（Kafka 7.5.0），因为：
- 更成熟稳定，兼容性好
- 学习资料和示例更多
- 大多数现有项目仍在使用

如果要使用 KRaft 模式，需要：
1. 使用 Kafka 3.3.0+ 版本
2. 配置 `KAFKA_PROCESS_ROLES` 环境变量
3. 移除 Zookeeper 依赖

## 学习资源

- [Kafka 官方文档](https://kafka.apache.org/documentation/)
- [Kafka 快速入门](https://kafka.apache.org/quickstart)
- [KRaft 模式文档](https://kafka.apache.org/documentation/#kraft)

# Kafka 学习演示项目

这是一个用于学习 Apache Kafka 的演示项目。

## 📚 学习内容

### 基础概念
- Kafka 架构和核心概念
- Topics、Partitions、Replicas
- Producers 和 Consumers
- Consumer Groups
- Offset 管理

### 实践示例
- [ ] 生产者示例
- [ ] 消费者示例
- [ ] 流处理示例
- [ ] 连接器示例

## 🚀 快速开始

### 前置要求
- Java 8+ 或 Python 3.7+
- Apache Kafka（本地安装或 Docker）
- 可选：Docker 和 Docker Compose

### 安装 Kafka

#### 使用 Docker（推荐）
```bash
docker-compose up -d
```

#### 本地安装
下载并解压 Kafka，然后启动 Zookeeper 和 Kafka：
```bash
# 启动 Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# 启动 Kafka
bin/kafka-server-start.sh config/server.properties
```

## 📁 项目结构

```
kafka-demo/
├── README.md           # 项目说明
├── docker-compose.yml  # Docker 配置（待添加）
├── java/               # Java 示例代码
├── python/             # Python 示例代码
├── config/             # 配置文件
└── docs/               # 学习文档
```

## 🔧 示例代码

### Java 示例
查看 `java/` 目录下的示例代码。

### Python 示例
查看 `python/` 目录下的示例代码。

## 📖 学习资源

- [Apache Kafka 官方文档](https://kafka.apache.org/documentation/)
- [Kafka 中文文档](https://kafka.apachecn.org/)

## 📝 学习笔记

在此记录学习过程中的重要知识点和遇到的问题。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

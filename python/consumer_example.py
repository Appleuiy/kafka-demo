"""
Kafka 消费者示例
演示如何从 Kafka Topic 消费消息
"""

from kafka import KafkaConsumer
import json

# 配置 Kafka Consumer
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',  # 从最早的消息开始读取
    enable_auto_commit=True,  # 自动提交 offset
    group_id='my-consumer-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    key_deserializer=lambda k: k.decode('utf-8') if k else None
)

def consume_messages():
    """消费消息"""
    print("开始消费消息...")
    print("按 Ctrl+C 停止消费\n")
    
    try:
        for message in consumer:
            print(f"收到消息:")
            print(f"  Topic: {message.topic}")
            print(f"  Partition: {message.partition}")
            print(f"  Offset: {message.offset}")
            print(f"  Key: {message.key}")
            print(f"  Value: {message.value}")
            print("-" * 50)
    except KeyboardInterrupt:
        print("\n停止消费消息")
    finally:
        consumer.close()
        print("Consumer 已关闭")

if __name__ == "__main__":
    consume_messages()

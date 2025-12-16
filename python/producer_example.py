"""
Kafka 生产者示例
演示如何向 Kafka Topic 发送消息
"""

from kafka import KafkaProducer
import json
import time

# 配置 Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: k.encode('utf-8') if k else None
)

def send_message(topic, key, value):
    """发送消息到指定的 Topic"""
    try:
        future = producer.send(topic, key=key, value=value)
        # 等待消息发送完成
        record_metadata = future.get(timeout=10)
        print(f"消息已发送到 Topic: {record_metadata.topic}, "
              f"Partition: {record_metadata.partition}, "
              f"Offset: {record_metadata.offset}")
        return True
    except Exception as e:
        print(f"发送消息失败: {e}")
        return False

if __name__ == "__main__":
    topic_name = "test-topic"
    
    # 发送几条测试消息
    for i in range(10):
        message = {
            "id": i,
            "message": f"这是第 {i} 条消息",
            "timestamp": time.time()
        }
        send_message(topic_name, f"key-{i}", message)
        time.sleep(1)
    
    # 关闭 Producer
    producer.close()
    print("Producer 已关闭")

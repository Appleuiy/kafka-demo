# Kafka 瀛︿範婕旂ず椤圭洰

杩欐槸涓€涓敤浜庡涔?Apache Kafka 鐨勬紨绀洪」鐩€?

## 馃摎 瀛︿範鍐呭

### 鍩虹姒傚康
- Kafka 鏋舵瀯鍜屾牳蹇冩蹇?
- Topics銆丳artitions銆丷eplicas
- Producers 鍜?Consumers
- Consumer Groups
- Offset 绠＄悊

### 瀹炶返绀轰緥
- [ ] 鐢熶骇鑰呯ず渚?
- [ ] 娑堣垂鑰呯ず渚?
- [ ] 娴佸鐞嗙ず渚?
- [ ] 杩炴帴鍣ㄧず渚?

## 馃殌 蹇€熷紑濮?

### 鍓嶇疆瑕佹眰
- Java 8+ 鎴?Python 3.7+
- Apache Kafka锛堟湰鍦板畨瑁呮垨 Docker锛?
- 鍙€夛細Docker 鍜?Docker Compose

### 瀹夎 Kafka

#### 浣跨敤 Docker锛堟帹鑽愶級
```bash
docker-compose up -d
```

#### 鏈湴瀹夎
涓嬭浇骞惰В鍘?Kafka锛岀劧鍚庡惎鍔?Zookeeper 鍜?Kafka锛?
```bash
# 鍚姩 Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# 鍚姩 Kafka
bin/kafka-server-start.sh config/server.properties
```

## 馃搧 椤圭洰缁撴瀯

```
kafka-demo/
鈹溾攢鈹€ README.md           # 椤圭洰璇存槑
鈹溾攢鈹€ docker-compose.yml  # Docker 閰嶇疆锛堝緟娣诲姞锛?
鈹溾攢鈹€ java/               # Java 绀轰緥浠ｇ爜
鈹溾攢鈹€ python/             # Python 绀轰緥浠ｇ爜
鈹溾攢鈹€ config/             # 閰嶇疆鏂囦欢
鈹斺攢鈹€ docs/               # 瀛︿範鏂囨。
```

## 馃敡 绀轰緥浠ｇ爜

### Java 绀轰緥
鏌ョ湅 `java/` 鐩綍涓嬬殑绀轰緥浠ｇ爜銆?

### Python 绀轰緥
鏌ョ湅 `python/` 鐩綍涓嬬殑绀轰緥浠ｇ爜銆?

## 馃摉 瀛︿範璧勬簮

- [Apache Kafka 瀹樻柟鏂囨。](https://kafka.apache.org/documentation/)
- [Kafka 涓枃鏂囨。](https://kafka.apachecn.org/)

## 馃摑 瀛︿範绗旇

鍦ㄦ璁板綍瀛︿範杩囩▼涓殑閲嶈鐭ヨ瘑鐐瑰拰閬囧埌鐨勯棶棰樸€?

## 馃 璐＄尞

娆㈣繋鎻愪氦 Issue 鍜?Pull Request锛?

## 馃搫 璁稿彲璇?

MIT License

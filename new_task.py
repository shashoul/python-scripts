import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port="5672")
)

channel = connection.channel()

channel.queue_declare(queue="myqueue", durable=True, arguments={'x-queue-type': 'quorum'})

message = "Hello World..."

channel.basic_publish(exchange="", routing_key="myqueue", body=message, properties=pika.BasicProperties(delivery_mode=2))

print(" [x] Sent %r" % message)

connection.close()
import pika

# Configuração da conexão com o RabbitMQ
connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

# Estabelecendo a conexão
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# Declarando a fila (certifique-se de que a fila exista)
channel.queue_declare(queue="data_queue", durable=True)

# Publicando uma mensagem na fila
mensagem = 'vamos ?'
channel.basic_publish(
    exchange='',
    routing_key='data_queue',
    body=mensagem,
    properties=pika.BasicProperties(
        delivery_mode=2,  # Faz com que a mensagem seja durável
    )
)

print(f"Mensagem enviada: {mensagem}")
connection.close()

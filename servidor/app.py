# app.py (Microserviço 2)

from flask import Flask, request
import pika
import time

app = Flask(__name__)

# Função para estabelecer conexão com o RabbitMQ
def connect_to_rabbit():
    try:
        connection_parameters = pika.ConnectionParameters(
            host="rabbitmq",
            port=5672,
            credentials=pika.PlainCredentials(
                username="guest",
                password="guest"
            )
        )
        # Estabelecendo a conexão
        connection = pika.BlockingConnection(connection_parameters)
        channel = connection.channel()
        print("Conectado ao RabbitMQ")
        return connection, channel
    except Exception as e:
        print(f"Falha ao conectar ao RabbitMQ: {str(e)}")
        return None, None

# Tentar conectar ao RabbitMQ




@app.route('/notificar', methods=['POST'])
def notificar():
    connection, channel = connect_to_rabbit()
    if channel == None:
        return 'erro rba' , 500
    teste = request.json
    data = 'deu bommm!!!!'
    try:
        channel.basic_publish(
            exchange='',
            routing_key='data_queue',
            body=data,
            properties=pika.BasicProperties(
                delivery_mode=2,
            )
        )
        connection.close()
        return 'Mensagem enviada com sucesso!'
    except Exception as e:
        return f"Erro ao enviar mensagem: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

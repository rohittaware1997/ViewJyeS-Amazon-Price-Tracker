from flask import Flask, jsonify
import pika
from flask_cors import CORS


main_message = []
app = Flask(__name__)
CORS(app)



def on_message_received (ch, method, properties, body):
    data1 = body.decode()
    main_message.append(data1)
    print(data1)
    print(type(data1))
    ch.queue_purge('output_queue')
    ch.connection.close()

@app.route('/add')
def get_my_data():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='output_queue')

    channel.basic_consume(queue='output_queue', auto_ack=True, on_message_callback=on_message_received)

    print("Starting consuming")

    channel.start_consuming()
    while(True):
        print(len(main_message))
        if len(main_message) != 0:
            return jsonify(main_message)




# print("received new message", result)
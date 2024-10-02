# Sistema_Distribuido

    Trabalho 1: Elaboração de Infraestrutura Distribuída...


**Como subir os serviços no Docker:**

    1. Baixar o repositorio com os arquivos.

    2. Abra o cmd ou o seu editor de código, e executer o arquivo "Docker-compose.yml" que esta localizado na raiz do projeto com o seguinte comando "docker-compose up --build".

    3. Aguarde as imagens ser baixadas e os conteiners serem executados.

    4. Certifique que o Rabbitmq está rodando acessando "http://localhost:15672", usuario e senha para acesso "guest".

**Requisições:**

    1. Para enviar uma mensagem para a fila de mensageria devera fazer uma requisição 'POST' para o endpoint "http://localhost:5000/pagar", o corpo da requisição derar ser um JSON a seguir:

    {
        "mensagem": "Mensagem que queira enviar"
    }

    2. Caso queria cosumir as mensagens que estão na fila, deverar fazer uma requisção 'GET' para o endpoint "http://localhost:5001/consumir" que retornara as mensagens que esta na fila.
    
    Se preferir verificar as menssagens manualmente pode-se acessar "http://localhost:15672", usuario e senha para acesso "guest".

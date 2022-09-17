# rigapp back-end

## Rodando localmente

pip install -r requirements.txt

python3 app.py

## Rodando via Docker

docker-compose up -d

### Em caso de problemas ao construir a imagem com o docker-compose

docker build . -t rigapp-be:latest

docker-compose up -d

## Documentação do Flask RESTx

https://flask-restx.readthedocs.io/en/latest/quickstart.html

## Rodar o migrate e dar o start na aplicação

flask db init

flask db migrate

flask db upgrade

flask run
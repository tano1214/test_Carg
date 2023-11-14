FROM python:3.9

WORKDIR /usr/src/app

# Instalar pg_config
RUN apt-get update && apt-get install -y libpq-dev

# Copiar archivos de la aplicación
COPY . .

# Instalar requisitos
RUN pip install -r requirements.txt

EXPOSE 8080
ENTRYPOINT python main.py


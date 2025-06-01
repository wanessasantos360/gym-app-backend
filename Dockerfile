# Usar uma imagem base oficial do Python.
FROM python:3.9-slim

# Definir o diretório de trabalho na imagem do container.
WORKDIR /app

# Prevenir que o Python gere ficheiros .pyc e armazene em buffer stdout e stderr.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copiar o ficheiro de requisitos primeiro para aproveitar o cache do Docker.
COPY ./requirements.txt /app/requirements.txt

# Instalar as dependências.
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar todo o conteúdo do diretório atual (onde o Dockerfile está) para o diretório de trabalho no container.
COPY . /app/

# Expor a porta em que a aplicação FastAPI será executada.
EXPOSE 8000

# Comando para executar a aplicação Uvicorn.
# Para desenvolvimento, pode usar --reload. Para produção, remova --reload.
# O comando com --reload será usado no docker-compose.yml para desenvolvimento.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
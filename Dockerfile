# Usa a imagem oficial do Python como base
FROM python:3.11

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos do seu projeto para o contêiner
COPY . .

# Instala as dependências corretamente
RUN pip install --no-cache-dir fastapi uvicorn sqlmodel

# Expõe a porta da aplicação
EXPOSE 8000

# Comando para rodar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

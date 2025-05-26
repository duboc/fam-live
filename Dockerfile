# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo de dependências para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta em que o Flask está rodando
EXPOSE 5000

# Comando para rodar a aplicação quando o container iniciar
CMD ["python", "app.py"]

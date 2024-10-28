# Используем официальный образ Python
FROM python:3.8-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы приложения
COPY . .

# Указываем, что приложение будет слушать на порту 5000
EXPOSE 5000

# Команда для запуска приложения
CMD ["python", "app.py"]

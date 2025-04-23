# Gunakan image Python resmi  
FROM python:3.9-slim  

# Set working directory  
WORKDIR /app  

# Install dependencies  
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy semua file  
COPY . .  

# Jalankan script  
CMD ["python", "./src/detector.py"]  
# use original python image. In which language developed this project is python. 
#   
FROM python:3.10-slim  

# set environment variables here 1 is yes and 0 means no 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set workdir it is work directory 
WORKDIR /app 

# Install OS dependencies 
RUN apt-get update && apt-get install -y build-essential poppler-utils && rm -rf /var/lib/apt/lists/* 

# Copy requirements from local directory to  current container  directory as we have written dot(.) 
COPY requirements.txt . 

COPY .env . 

# Copy project files copy entire code of local directory to this container current directory  
COPY . .      

# install dependencies 
RUN pip install --no-cache-dir -r requirements.txt 

# Expose port 
EXPOSE 8080 

# Run fastapi with unicorn 
#CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"] 

# replace last CMD in prod 
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "4"]
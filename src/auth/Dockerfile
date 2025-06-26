FROM python:3.10-slim-bullseye

# Install system dependencies
RUN apt-get update \
  && apt-get install --no-install-suggests --install-recommends -y \
     build-essential default-libmysqlclient-dev pkg-config \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY ./requirements.txt /app  
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir --requirement /app/requirements.txt

# Copy application code
COPY . /app

# Expose port and define startup command
EXPOSE 5000
CMD ["python3", "server.py"]

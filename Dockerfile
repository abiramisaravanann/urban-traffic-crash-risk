# Base Image
FROM python:3.11-slim

# Install Java (PySparkக்கு required)
RUN apt-get update && apt-get install -y \
    default-jdk \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH=$PATH:$JAVA_HOME/bin

# Install PySpark
RUN pip install pyspark

# Create working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies (if any)
RUN pip install --no-cache-dir requests pandas

# Default command
CMD ["tail", "-f", "/dev/null"]
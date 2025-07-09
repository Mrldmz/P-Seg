# Use older Python base for better GLIBC compatibility (faster build)
FROM python:3.11-slim-bullseye

# Set working directory
WORKDIR /app

# Install system dependencies needed for pynput
RUN apt-get update && apt-get install -y \
    python3-tk \
    python3-dev \
    gcc \
    libc6-dev \
    libxkbcommon-x11-0 \
    libx11-6 \
    libxtst6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages separately for better error tracking
RUN pip install --no-cache-dir pynput
RUN pip install --no-cache-dir pyinstaller

# Copy the Python script
COPY keylogger.py .

# Build the executable with new name
RUN pyinstaller --onefile --name=keylogger_v2 keylogger.py

# The executable will be in /app/dist/keylogger_v2
CMD ["echo", "Build complete! Executable is in /app/dist/keylogger_v2"]

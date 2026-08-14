# Define the base image to use.
FROM alpine

# Set the working directory.
WORKDIR /home/peacefield

# Install Python.
RUN apk add python3

# Copy our source code.
COPY backend.py backend.py
COPY index.html index.html

# Create a non-root user with no password (-D).
RUN adduser -D peacefield -h /home/peacefield

# Set permissions.
RUN chown -R peacefield:peacefield /home/peacefield

# Switch to a non-root user.
USER peacefield

# Identify what TCP port will be used by our server.
EXPOSE 8000

# Start the server.
CMD ["python", "backend.py"]
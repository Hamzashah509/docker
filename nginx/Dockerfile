# Use the official Nginx image from the Docker Hub
FROM nginx:latest

# Copy custom configuration file from the current directory
COPY nginx.conf /etc/nginx/nginx.conf

# Start Nginx when container launches
CMD ["nginx", "-g", "daemon off;"]

#!/usr/bin/env bash
# Sets up my web servers for deployment for web_static

#Install nginx if not already installed
sudo apt-get update
sudo apt-get install nginx

# Creates directories if they do not exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Creates a fake HTML
echo "<html>
<head>
</head>
<body>
  Holberton School
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Creates a symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Grant ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update nginx config to serve /data/web_static/current/ at /hbnb_static
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart nginx
sudo service nginx restart

# Exit successfully
exit 0

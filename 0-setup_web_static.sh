#!/usr/bin/env bash
#setsup webser to create a website using nginx
sudo apt-get update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo chown -R ubuntu:ubuntu /data/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i '48i\\n\tlocation /hbnb_static/ {' /etc/nginx/sites-available/default
sudo sed -i '50i\\t\talias /data/web_static/current/;' /etc/nginx/sites-available/default
sudo sed -i '51i\\t}' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0

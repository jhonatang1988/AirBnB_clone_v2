#!/usr/bin/env bash
#setsup webser to create a website using nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/ /data/{web_static/,web_static/releases/,web_static/shared/,web_static/releases/test/}
sudo chown -R ubuntu:ubuntu /data/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sed -i '48i\\n\tlocation /hbnb_static/ {' /etc/nginx/sites-available/default
sed -i '50i\\t\talias /data/web_static/current/;' /etc/nginx/sites-available/default
sed -i '51i\\t}' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0

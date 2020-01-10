#!/usr/bin/env bash
#setsup webser to create a website using nginx
sudo apt-get -y update
sudo apt-get -y install nginx
ufw allow 'Nginx HTTP'
sudo service nginx start
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Probando el pollo
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo chown -R ubuntu:ubuntu /data/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo sed -i '43i\\n' /etc/nginx/sites-available/default
sudo sed -i '44i\\tlocation /hbnb_static {' /etc/nginx/sites-available/default
sudo sed -i '45i\\t\talias /data/web_static/current;' /etc/nginx/sites-available/default
sudo sed -i '46i\\t}' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0

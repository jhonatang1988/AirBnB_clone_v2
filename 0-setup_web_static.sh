#!/usr/bin/env bash
#setsup webser to create a website using nginx
sudo apt-get -y update
sudo apt-get -y install nginx
ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Probando el pollo
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i "43i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo chown -R ubuntu:ubuntu /data/
sudo service nginx restart
exit 0

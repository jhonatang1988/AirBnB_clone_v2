#!/usr/bin/env bash
#Prepare your web servers
sudo apt-get update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/ /data/{web_static/,web_static/releases/,web_static/shared/,web_static/releases/test/}
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '42i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0

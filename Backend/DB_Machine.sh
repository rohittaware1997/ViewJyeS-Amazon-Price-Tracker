apt update
apt upgrade -y
apt install mysql-server -y
systemctl start mysql.service

sudo mysql_secure_installation

CREATE USER 'akhil'@'%' IDENTIFIED BY 'akhil@05';
GRANT ALL PRIVILEGES ON *.* TO 'akhil'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
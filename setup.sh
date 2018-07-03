# clone 代码到 /root/zxd-bbs

# 换源
ln -f -s /root/zxd-bbs/misc/sources.list /etc/apt/sources.list
mkdir -p /root/.pip
ln -f -s /root/zxd-bbs/misc/pip.conf /root/.pip/pip.conf

# 装依赖
add-apt-repository -y ppa:deadsnakes/ppa
apt update
debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'
apt -y install mysql-server git supervisor nginx curl ufw

apt install -y python3.6
curl https://bootstrap.pypa.io/get-pip.py > /tmp/get-pip.py
python3.6 /tmp/get-pip.py

# apt-get update
# apt-get install -y python3-pip git supervisor nginx
pip3 install flask eventlet flask-socketio  gunicorn PyMySQL SQLAlchemy

# 系统设置
# apt -y install curl ufw
ufw allow 22
ufw allow 80
ufw allow 443
ufw default deny incoming
ufw default allow outgoing
ufw status verbose
ufw -f enable


# 删掉 nginx default 设置
rm -f /etc/nginx/sites-enabled/default
rm -f /etc/nginx/sites-available/default

# 建立一个软连接
ln -s -f /root/zxd-bbs/zxd-bbs.conf /etc/supervisor/conf.d/web20.conf
# 不要再 sites-available 里面放任何东西
ln -s -f /root/zxd-bbs/zxd-bbs.nginx /etc/nginx/sites-enabled/web20

# 重启服务器
service supervisor restart
service nginx restart

echo 'succsss'
echo 'ip'
hostname -I
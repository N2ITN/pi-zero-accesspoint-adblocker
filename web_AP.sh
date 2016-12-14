sudo create_ap -n wlan0 zer0 adzapper &
sudo pkill dnsmasq
sleep 10
export WLAN_ADDR=`ifconfig wlan0 | grep 'inet addr' | awk '{print $2}' | sed -e 's/:/\n/' | grep 192`
touch resolv.conf && echo "$WLAN_ADDR ad-zero.io" >> resolv.conf && chmod 644 resolv.conf
cd ~/zer0
touch resolv.conf && chmod 644 resolv.conf
sudo mv resolv.conf /etc/resolv.conf
sudo python3 ~/fakedns/fakedns.py $WLAN_ADDR
sudo python webserver.py 

import subprocess 
from time import sleep




try:


    def run_serial(commandList):
        if len(commandList) == 1:
            command = commandList[0]
            print (command)
        else: 
            command = "; ".join(commandList)
        print (command)
        try:
            subprocess.Popen(command,shell=True)
        except Exception as e:
            print (e)
        print ()

    def terminus():
        print ('terminating processes')    
        for x in [ap, fnds,ws]:
            try:
                x.terminate()
            except Exception as e:
                print (e)
        run_serial(restoreConf)
        run_serial(envReset)

    wireless_AP = ["sudo create_ap -n wlan0 zer0 adzapper" ]
    envConf = ["export WLAN_ADDR=`ifconfig wlan0 | grep 'inet addr' | awk '{print $2}' | sed -e 's/:/\\n/' | grep 192`",
    'touch ~/zer0/resolv.conf && echo "nameserver $WLAN_ADDR" >> ~/zer0/resolv.conf && chmod 644 ~/zer0/resolv.conf',
    'sudo mv resolv.conf /etc/resolv.conf', 'touch ~/zer0/dnsmasq.hosts && echo "$WLAN_ADDR ad-zero.io" >> ~/zer0/dnsmasq.hosts && chmod 644 ~/zer0/dnsmasq.hosts',
    'sudo mv dnsmasq.hosts /etc/dnsmasq.hosts']
    fakeDNS = ["cd ~/fakedns && sudo python3 fakedns.py $WLAN_ADDR"]
    webServer = ["sudo pkill dnsmasq",'sudo python webserver.py']
    restoreConf = ['sudo echo -n "" > /etc/dnsmasq.host', 'sudo echo -n "" > /etc/resolv.conf']
    envReset = ['touch ~/zer0/resolv.conf && chmod 644 ~/zer0/resolv.conf', 'sudo mv resolv.conf /etc/resolv.conf', 
    'touch ~/zer0/dnsmasq.hosts && chmod 644 ~/zer0/dnsmasq.hosts','sudo mv dnsmasq.hosts /etc/dnsmasq.hosts']


except KeyboardInterrupt:
    print ("KeyboardInterrupt")
    terminus()
    print (ws), print (type(ws))




    

    

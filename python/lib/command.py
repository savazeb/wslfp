class CMD:
    WSL_IP =  "wsl hostname -I | gawk '{print $1}'"
    PORTPROXY_LIST = "netsh interface portproxy show all"
    PORTPROXY_ADD = "netsh interface portproxy add v4tov4 listenport={} listenaddress={} connectport={} connectaddress={}"
    PORTPROXY_DELETE = "netsh interface portproxy delete v4tov4 listenport={} listenaddress={}"

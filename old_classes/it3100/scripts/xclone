#!/bin/bash

user_name=acoulter
serv_ip=ssh.cs.dixie.edu







cd /root
if [ ! -d .ssh ]; then
    mkdir .ssh
fi
chmod 700 .ssh
cd .ssh
touch authorized_keys
chown root:root authorized_keys
chmod 600 authorized_keys
ssh $user_name@$serv_ip<<EOF
cat ~/.ssh/id_rsa.pub
EOF>> authorized_keys
echo "done"
exit

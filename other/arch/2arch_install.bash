#!/bin/bash

#### config #####
is_static=n
#my_name=arch_laptop

# enable network
systemctl enable dhcpcd
systemctl start dhcpcd


# host name
echo "What name do you want for the computer?"
read my_name

# set language
vi /etc/locale.gen
locale-gen
echo LANG=en_US.UTF-8 > /etc/locale.conf
export LANG=en_US.UTF-8

# Time zone
ln -s /usr/share/zoneinfo/America/Denver /etc/localtime
hwclock --systohc --utc

# hostname
echo $my_name > /etc/hostname

# network
# echo "Do you want to set a static ip?"
# echo "y for yes n for no"
# read is_static

# if [ "$is_static" = "y" ]; then
#     echo "
#     interface enp6s0
#     static ip_address=144.38.204.102/24
#     static domain_name_servers=8.8.8.8 8.8.4.4
#     " >> /etc/dhcpcd.conf

#     systemctl restart dhcpcd.service
# fi

# set root password
echo "set root password"
passwd

## grub config
pacman-db-upgrade
pacman -S grub
pacman -S os-prober
pacman -S git
pacman -S openssh
echo "Type the dev to install grub on but only sdx"
read drive
grub-install --target=i386-pc --recheck /dev/$drive
grub-mkconfig -o /boot/grub/grub.cfg
 

#!/bin/bash

# laguage setup
# vi /etc/locale.gen
# locale-gen
# export LANG=en_US.UTF-8


#### static ip address ####

# echo "Press y to setup static ip address and n for no"
# read is_static

# if [ "$is_static" = "y" ]; then
#     # ip link
#     # echo "choose an interface from above."
#     # read inter
#     echo "
#     interface enp6s0
#     static ip_address=144.38.204.102/24
#     static domain_name_servers=8.8.8.8 8.8.4.4
#     " >> /etc/dhcpcd.conf

#     systemctl restart dhcpcd.service
# fi


#### make partitions ####

# if disk needs label
# parted /dev/sda mklabel gpt
# parted -s /dev/sda mkpart ext3 1MiB 8MiB 
# parted -s /dev/sda mkpart primary 9M 10G
# parted -s /dev/sda mkpart primary 10G 100%
# mkfs.ext4 /dev/sda3
# mkswap /dev/sda2
# swapon /dev/sda2
# parted /dev/sda set 1 bios_grub on



## mount drives
# mount /dev/sda6 /mnt
# mkdir /mnt/boot
# mount /dev/sda3 /mnt/boot

# check if mounts worked
# df
# echo "did mounts work"
# read mwork

## Test network
# ping -w 3 www.google.com 
# echo "did ping work?"
# read mwork
# if [ "$mwork" = "n" ]; then
#     exit
# fi

# select mirror
# vi /etc/pacman.d/mirrorlist


# install base system
pacstrap -i /mnt base base-devel
genfstab -U -p /mnt >> /mnt/etc/fstab
vi /mnt/etc/fstab

echo " arch-chroot /mnt /bin/bash "

#!/bin/bash

# list off all the applications to install one per line
apps=(
sudo
virtualbox
awesome
xf86-video-intel 
xf86-video-nouveau
xf86-video-vesa 
xf86vidmodeproto 
gnome
kde
xfce4
xfce4-goodies
xsel
xdotool
cdspell
shopt
terminator
emacs
libreoffice-fresh
anamnesis
mplayer
git
lutris
)
# xsel will output highlighted text to terminal
# xdotool can automate gui things
# cdspell will make is so if you misspell a dirrectory it will just guess
# shopt can turn programs on and off
# cmatrix 
# anamnesis clipboard manager
# lutris: installing games

pacman --noconfirm -Syu
#pacman --noconfirm -S $(< laptop_pkglist.txt)

# update mirrorlist
# cat ~/homework/old_classes/arch_laptop/mirrorlist > /etc/pacman.d/mirrorlist

# number of apps in the array has to have
numb_apps=$(echo $((${#apps[@]}-1)))

# install apps in the array
for i in $(seq $numb_apps); do
    pacman --noconfirm -S ${apps[$i]}
done


# make user
# usrname="andrew"
useradd -m -g users -G wheel -s /bin/bash andrew
echo "type password for andew"
passwd andrew

# add user to sudo
echo 'andrew  ALL=(ALL:ALL) ALL' >> /etc/sudoers

# configure ssh
# emacs /etc/ssh/sshd_config
# systemctl start sshd.service
# systemctl enable sshd.service
# systemctl restart sshd



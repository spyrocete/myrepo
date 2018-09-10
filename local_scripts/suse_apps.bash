#!/bin/bash

# install vlc codecs
sudo zypper ar -cfp 90 http://ftp.gwdg.de/pub/linux/misc/packman/suse/openSUSE_Tumbleweed/ packman
sudo zypper ref
sudo zypper dup
sudo zypper in vlc-codecs

# install google-chrome
sudo zypper ar http://dl.google.com/linux/chrome/rpm/stable/x86_64 Google-Chrome
sudo zypper ref
wget https://dl.google.com/linux/linux_signing_key.pub
sudo rpm --import linux_signing_key.pub
sudo zypper in google-chrome-stable

# Other applications
apps=(
    terminator
    emacs
)


# number of apps in the array has to have
numb_apps=$(echo $((${#apps[@]}-1)))

# install apps in the array
for i in $(seq $numb_apps); do
    sudo zypper in ${apps[$i]}
done





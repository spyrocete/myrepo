#!/bin/bash

echo "
if [ -f $HOME/homework/bash/.bashrc ]; then
        source $HOME/homework/bash/.bashrc
fi
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
" > ~/.bashrc
source ~/.bashrc

# setup alias for starting xserver
if [ "$1" = "a" ]; then
    echo "
    #!/bin/sh
    #
    # ~/.xinitrc
    #
    # Executed by startx (run your window manager from here)

    if [ -d /etc/X11/xinit/xinitrc.d ]; then
	for f in /etc/X11/xinit/xinitrc.d/*; do
	    [ -x ""$f"" ] && . ""$f""
	done
	unset f
    fi


    session=${1:-xfce}

    case $session in
	awesome           ) exec awesome;;
	bspwm             ) exec bspwm;;
	catwm             ) exec catwm;;
	cinnamon          ) exec cinnamon-session;;
	dwm               ) exec dwm;;
	enlightenment     ) exec enlightenment_start;;
	ede               ) exec startede;;
	fluxbox           ) exec startfluxbox;;
	gnome             ) exec gnome-session;;
	gnome-classic     ) exec gnome-session --session=gnome-classic;;
	i3|i3wm           ) exec i3;;
	icewm             ) exec icewm-session;;
	jwm               ) exec jwm;;
	kde               ) exec startkde;;
	mate              ) exec mate-session;;
	monster|monsterwm ) exec monsterwm;;
	notion            ) exec notion;;
	openbox           ) exec openbox-session;;
	unity             ) exec unity;;
	xfce|xfce4        ) exec startxfce4;;
	xmonad            ) exec xmonad;;
	# No known session, try to run it as command
	*) exec $1;;
    esac
    " > .xinitrc
fi
    

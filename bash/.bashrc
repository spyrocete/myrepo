# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# For scripts
export PATH=$PATH":$HOME/homework/local_scripts"
export LANGUAGE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8


# To log what computers are being logged into
curr=$(tail -1 ~/current.txt | head -1)
if [ "$curr" != $HOSTNAME ]; then
    hostname >> current.txt
fi

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
#[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if theal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

##################################################################
##################   Defined colors for ps1  #####################
##################################################################

txtblk='0;30m' # Black - Regular
txtred='0;31m' # Red
txtgrn='0;32m' # Green
txtylw='0;33m' # Yellow
txtblu='0;34m' # Blue
txtpur='0;35m' # Purple
txtcyn='0;36m' # Cyan
txtwht='0;37m' # White
bldblk='1;30m' # Black - Bold
bldred='1;31m' # Red
bldgrn='1;32m' # Green
bldylw='1;33m' # Yellow
bldblu='1;34m' # Blue
bldpur='1;35m' # Purple
bldcyn='1;36m' # Cyan
bldwht='1;37m' # White
unkblk='4;30m' # Black - Underline
undred='4;31m' # Red
undgrn='4;32m' # Green
undylw='4;33m' # Yellow
undblu='4;34m' # Blue
undpur='4;35m' # Purple
undcyn='4;36m' # Cyan
undwht='4;37m' # White
bakblk='40m'   # Black - Background
bakred='41m'   # Red
bakgrn='42m'   # Green
bakylw='43m'   # Yellow
bakblu='44m'   # Blue
bakpur='45m'   # Purple
bakcyn='46m'   # Cyan
bakwht='47m'   # White
txtrst='0m'    # Text Reset

# Terminal 
t_farrow=$txtred    # ┌──[
t_root=$txtwht      # root user
t_at=$txtylw        # @
t_host=$txtwht      # hostname
t_user=$txtblu      # user
t_brhost=$txtred    # ]-[
t_tilda=$txtgrn     # file path ~
t_brclose=$txtred   # ]
t_arrow=$txtred     # └──╼
t_dollar=$txtylw    # $


if [ "$color_prompt" = yes ]; then
    PS1="\[\033[0;31m\]\342\224\214\342\224\200\$([[ \$? != 0 ]] && echo \"[\[\033[0;31m\]\342\234\227\[\033[0;37m\]]\342\224\200\")[$(if [[ ${EUID} == 0 ]]; then echo '\[\033[01;31m\]root\[\033[01;33m\]@\[\033[01;96m\]\h'; else echo '\[\033["$t_user"\]\u\[\033[01;33m\]@\[\033[01;96m\]\h'; fi)\[\033[0;31m\]]\342\224\200[\[\033[0;32m\]\w\[\033[0;31m\]]\n\[\033[0;31m\]\342\224\224\342\224\200\342\224\200\342\225\274 \[\033[0m\]\[\e[01;33m\]\\$\[\e[0m\]"
else
    PS1='┌──[\u@\h]─[\w]\n└──(^) \$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
# amc
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\033[$t_farrow\]\342\224\214\342\224\200\$([[ \$? != 0 ]] && echo \"[\[\033[0;31m\]\342\234\227\[\033[0;37m\]]\342\224\200\")[$(if [[ ${EUID} == 0 ]]; then echo '\[\033[$t_root\]root\[\033[01;33m\]@\[\033[01;96m\]\h'; else echo '\[\033[$t_user\]\u\[\033[$t_at\]@\[\033[$t_host\]\h'; fi)\[\033[$t_brhost\]]\342\224\200[\[\033[$t_tilda\]\w\[\033[$t_brclose\]]\n\[\033[$t_arrow\]\342\224\224\342\224\200\342\224\200\342\225\274 \[\033[0m\]\[\e[$t_dollar\]\\$\[\e[0m\] "
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
fi


# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi


# mine
# The paths for the different bash files
export PATH=$PATH":/usr/games:$HOME/homework/local_scripts"

source ~/myrepo/bash/.bash_alias
#source ~/homework/bash/.bash_profile

# Unused files
# source ~/homework/bash/.bash_env

# To remove the long file path
cd

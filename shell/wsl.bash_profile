# Custom profile specifically for WSL bash

echo ".bash_profile loaded"
. ~/.profile
clear
echo "Welcome `whoami` to `hostname`"
echo

# No pycache trash
export PYTHONDONTWRITEBYTECODE=1
alias pytest='pytest -p no:cacheprovider'

alias cds='cd /local/git/Scripts'
alias viprofile='vi ~/.bash_profile'
alias ll='ls -aGhlp'                            # List all, colors, size suffixes, long, slashes after dirs
alias cat='cat -v'                              # Always output nonprinting characters
alias mkdir='mkdir -p'                          # Create multiple dirs when given
alias ~='cd ~'                                  # Go to home dir
alias ..='cd ../'                               # Go back 1 directory level
alias rgrep='egrep -iR'

# Green background highlighting on grep results
export GREP_COLOR='1;42'

# Enable history appending instead of overwriting.
shopt -s histappend
shopt -s cmdhist
HISTFILESIZE=1000000
HISTSIZE=1000000
HISTCONTROL=ignoreboth
HISTTIMEFORMAT='%F %T   '

export PS1="\u@\h \$(smiley) \$(pwd) \$ "       # Set prompt to include user, host, current dir, and RC smiley
export BLOCKSIZE=1k                             # Get consistent block output across "du", "df", and "ls -s"
export CLICOLOR=1                               # Get colors in Terminal
export LSCOLORS=ExFxBxDxCxegedabagacad          # Specify Terminal colors

ffiles() { find . -type f; }

fname() { find . -iname "*${1}*"; }

mkcd() { mkdir -p "$1" && cd "$1"; }            # Makes new Dir and jumps inside

cd() { builtin cd "$@" && ll; }                 # Run ll after changing dir

CD() { builtin cd "$@"; }                       # Force dir change to NOT run ll (with the power of ALL CAPS!)

psgrep() { ps -ef | egrep -i "${1}" | grep -v grep; }

curly() {
  if [ -z "$1" ] ; then
    echo "No arguments specified"
    echo "Usage: curly <URL> [max-redirs]"
    echo "Runs this command: curl -ILk -w '%{url_effective}\\n\\n' [--max-redirs \"\$2\"] \"\$1\""
    echo "Example: curly http://www.mathworks.com/license/mll/license.txt 4"
  else
    if [ -z "$2" ] ; then
      curl -ILk -w '%{url_effective}\n\n' --max-redirs 10 "$1"
    else
      curl -ILk -w '%{url_effective}\n\n' --max-redirs $2 "$1"
    fi
  fi
}

backup() {
  if [ -z "$1" ] ; then
    echo "No arguments specified"
    echo "Usage: backup <[pathTo/]thing> [place]"
    echo
    return
  else
    #thing="${1%/}"
    sourceDir=$(dirname $1)
    sourceThing=$(basename $1)
  fi
  if [ -z "$2" ] ; then
    destDir="."
  else
    destDir="${2%/}"
  fi
  datestamp=`date +%Y%m%d`
  cp -ap "$sourceDir/$sourceThing" "$destDir"/"BACKUP_"$sourceThing"_"$datestamp && echo "Backup of "$sourceThing" created at "$destDir"/"BACKUP_"$sourceThing"_"$datestamp"
  echo
}

smiley() {
  RC="$?"
  GOODCOLOR='\e[32m'
  BADCOLOR='\e[31m'
  ENDCOLOR='\e[0m'
  if [ "${RC}" == 0 ] ; then
    echo -e "\001${GOODCOLOR}\002:)\001${ENDCOLOR}\002"
  else
    echo -e "\001${BADCOLOR}\002:( ${RC}\001${ENDCOLOR}\002"
  fi
}

tempme() {
  datestamp=`date +%Y%m%d`
  mkcd ~/temp/${datestamp}
}

how() {
  if [ -z $1 ]; then
    echo "USAGE: how <thing>"
    echo -e "EXAMPLES:\n\thow docker\n\thow git\n"
  else
    less /local/git/Scripts/how/${1}.how
  fi
}


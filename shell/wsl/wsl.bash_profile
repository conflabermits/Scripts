# Custom profile specifically for WSL bash

echo ".bash_profile loaded"
. ~/.profile
clear
echo "Welcome `whoami` to `hostname`"
echo

export PROFILE="/home/chris/.bash_profile"
export MYGIT="/local/git/Scripts"
export SCREENDIR="/home/chris/.screen"
if [ -d /usr/local/go/bin ]; then
    export PATH=$PATH:/usr/local/go/bin
fi

# No pycache trash
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'

alias cds='cd $MYGIT && echo && git remote update && git status && echo'
alias cdgit='cd $MYGIT && echo && git remote update && git status && echo'
alias viprofile='vi ~/.bash_profile'
alias ll='ls -aGhlp'                            # List all, colors, size suffixes, long, slashes after dirs
alias cat='cat -v'                              # Always output nonprinting characters
alias mkdir='mkdir -p'                          # Create multiple dirs when given
alias ~='cd ~'                                  # Go to home dir
alias ..='cd ../'                               # Go back 1 directory level
alias rgrep='egrep -iR'
alias myrsync='time rsync -rtv --progress --stats'

# Green background highlighting on grep results
export GREP_COLOR='1;42'

# Enable history appending instead of overwriting.
shopt -s histappend
shopt -s cmdhist
export HISTFILESIZE=1000000
export HISTSIZE=1000000
export HISTCONTROL=ignoreboth
export HISTTIMEFORMAT='%F %T   '

export PS1="\u@\h \$(smiley) \$(pwd) \$ "       # Set prompt to include user, host, current dir, and RC smiley
export BLOCKSIZE=1k                             # Get consistent block output across "du", "df", and "ls -s"
#export CLICOLOR=1                               # Get colors in Terminal
#export LSCOLORS=ExFxBxDxCxegedabagacad          # Specify Terminal colors

ffiles() { find . -type f; }

fname() { find . -iname "*${1}*"; }

mkcd() { mkdir -p "$1" && cd "$1"; }            # Makes new Dir and jumps inside

cd() { builtin cd "$@" && ll; }                 # Run ll after changing dir

CD() { builtin cd "$@"; }                       # Force dir change to NOT run ll (with the power of ALL CAPS!)

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

up () {
    if [ -z $1 ]; then
      COUNT=1
    else
      if [ $1 -ge 0 2>/dev/null ]; then
        if [ $1 -le $(grep -o '/' <<<$PWD | wc -l) 2>/dev/null ]; then
          COUNT=$1
        else
          echo "I'm sorry $USER, I can't do that"
          return
        fi
      else
        echo "up [integer]"
        return
      fi
    fi

    for ((i=1;i<=$COUNT;i++)); do
      builtin cd ..
    done

    ll
}

smiley() {
  RC="$?"
  spRC="     $RC"
  stRC="${spRC:(-3):3}"
  GOODCOLOR='\e[32m'
  BADCOLOR='\e[31m'
  ENDCOLOR='\e[0m'
  if [ "${RC}" == 0 ] ; then
    echo -e "\001${GOODCOLOR}\002:)   0\001${ENDCOLOR}\002"
  else
    echo -e "\001${BADCOLOR}\002:( ${stRC}\001${ENDCOLOR}\002"
  fi
}

tempme() {
  datestamp=`date +%Y%m%d`
  mkcd ~/temp/${datestamp}
}

how() {
  if [ -z $1 ]; then
    echo "USAGE: how <thing>"
    echo -e "EXAMPLES:\n\thow docker\n\thow git"
    echo "AVAILABLE HOW FILES:"
    for file in $(ls -1 $MYGIT/how/ | awk -F".how" '{print $1}')
    do
      echo -e "\t${file}\n"
    done
  else
    less $MYGIT/how/${1}.how
  fi
}

psgrep() {
  if [ -z $1 ]; then
    echo "USAGE: psgrep \"<string>\""
    echo "COMMAND: ps -ef | egrep -i \"\${1}\" | grep -v grep"
  else
    ps -ef | egrep -i "${1}" | grep -v grep
  fi
}

autobackup() {
  if [ ! -d "/mnt/$1" ] || [ -z $1 ]; then
    echo "USAGE: autobackup <driveletter>"
    echo "AVAILABLE DRIVE LETTERS FOR BACKING UP:"
    for drive in $(ls -1 /mnt/)
    do
      echo -e "\t${drive}\n"
    done
  else
    driveletter="${1}"
    echo "driveletter is: \"${driveletter}\""
    sourcehost="$(hostname)"
    time rsync -rtv --delete-during --delete-excluded --ignore-errors --whole-file --progress --stats --itemize-changes --log-file=/home/chris/autobackup/logs/autobackup-`date +%Y%m%d-%H%M%S`-${driveletter}.log --exclude-from=/home/chris/autobackup/rsync_excludes.txt /mnt/${driveletter} chris@ubuntuServer:/media/chris/SuperDrive/BACKUPS/${sourcehost}/
  fi
}

## WSL: Start ssh if not started
if [ $(ps -ef | egrep "/usr/sbin/sshd|sshd: /usr/sbin" | grep -v grep | wc -l) == "0" ] ; then
  sudo /etc/init.d/ssh start
fi


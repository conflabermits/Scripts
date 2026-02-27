# Custom profile specifically for MacOS bash

echo "mac.bash_profile loaded"
clear
echo "Welcome `whoami` to `hostname`"
echo

export PROFILE="$HOME/mac.bash_profile"
export MYGITROOT="$HOME/local/git"
export MYGITSCRIPTS="$MYGITROOT/Scripts"
export SCREENDIR="$HOME/.screen"
export GOROOT='/usr/local/go'
export GOPATH='/Users/chris/go'
if [ -d $GOROOT/bin ]; then
    export PATH=$PATH:$GOROOT/bin
fi
if [ -d $GOPATH/bin ]; then
    export PATH=$PATH:$GOPATH/bin
fi

# No pycache trash
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'

# Stream shortcuts
#alias donorbox='cd ~/local/git/stream/tools/donorbox-overlay/ && go run main.go -port 38080 -timeout 61 -url https://donorbox.org/support-black-girls-code/fundraiser/christopher-dunaj'
#alias oauth='cd ~/local/git/stream/tools/chatbot/twitch-oauth-authorization-code-example/ && for line in $(cat ../.creds); do export ${line}; done && go run main.go'
#alias chatbot='cd ~/local/git/stream/tools/chatbot/chatgpt-chatbot-example/ && vi ../.creds  && for line in $(cat ../.creds); do export ${line}; done && go run main.go'
alias chatbot='cd ${MYGITROOT}/stream-chatbot/ && go run main.go'

alias cds='cd $MYGITSCRIPTS && echo && git remote update && git status && echo'
alias viprofile='vi $PROFILE'
alias ll='ls -aGhlp'                            # List all, colors, size suffixes, long, slashes after dirs
alias cat='cat -v'                              # Always output nonprinting characters
alias mkdir='mkdir -p'                          # Create multiple dirs when given
alias ~='cd $HOME'                              # Go to home dir
alias ..='cd ../'                               # Go back 1 directory level
alias rgrep='egrep -iR'
alias myrsync='time rsync -rtv --progress --stats'
alias alphab='/Users/chris/local/git/Scripts/shell/alphab/alphab.sh'

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

ffiles() { find . -type f -not -path "*/.git/*"; }

fname() { find . -iname "*${1}*"; }

mkcd() { mkdir -p "$1" && cd "$1"; }            # Makes new Dir and jumps inside

cd() { builtin cd "$@" && ll; }                 # Run ll after changing dir

CD() { builtin cd "$@"; }                       # Force dir change to NOT run ll (with the power of ALL CAPS!)

cdgit() {
  CD $MYGITROOT
  if [ -z "$1" ] ; then
    ls -1 | egrep -v "^BACKUP|^OLD" && read -p "Choose a git directory: " USERINPUT
  else
    USERINPUT="$1"
  fi
  if [ -d "$USERINPUT" ] ; then
    cd $USERINPUT && echo && git remote update && git status && echo
  else
    echo "Directory not found" && echo && ll
  fi
}

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
  #GOODCOLOR='\e[32m'
  #BADCOLOR='\e[31m'
  #ENDCOLOR='\e[0m'
  GOODCOLOR=''
  BADCOLOR=''
  ENDCOLOR=''
  if [ "${RC}" == 0 ] ; then
    echo -e "\001${GOODCOLOR}\002:)   0\001${ENDCOLOR}\002"
  else
    echo -e "\001${BADCOLOR}\002:( ${stRC}\001${ENDCOLOR}\002"
  fi
}

tempme() {
  datestamp=`date +%Y%m%d`
  mkcd $HOME/temp/${datestamp}
}

how() {
  if [ -z $1 ]; then
    echo "USAGE: how <thing>"
    echo -e "EXAMPLES:\n\thow docker\n\thow git"
    echo "AVAILABLE HOW FILES:"
    for file in $(ls -1 $MYGITSCRIPTS/how/ | awk -F".how" '{print $1}')
    do
      echo -e "\t${file}\n"
    done
  else
    less $MYGITSCRIPTS/how/${1}.how
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


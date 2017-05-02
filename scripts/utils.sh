BOLD=$(tput bold)
NORMAL=$(tput sgr0)

# Action notification header
function notify {
    echo $BOLD
    echo '============================================='
    echo  " ${1}"
    echo '============================================='
    echo $NORMAL
}
# print out a bolded test
function printBold {
    echo "${BOLD}${1}${NORMAL}"
}
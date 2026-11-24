set -uo pipefail

APPS=("iMovie" "Sphero Edu" "GarageBand" "Company Portal" "Google Chrome" "Microsoft Edge")
reply=""

ask() {
    printf '%s' "$1"
    IFS= read -r reply || exit 0
}

block() {
    local name=$1 app="/Applications/$1.app"
    echo "Blocking $name..."
    sudo rm -rf "$app/Contents"
    sudo chflags hidden "$app"
    sudo chflags schg "$app"
    echo "successfully blocked"
}

unblock() {
    local name=$1 app="/Applications/$1.app"
    echo "Unblocking $name..."
    if [[ -e $app ]]; then
        sudo chflags noschg "$app"
        sudo chflags nohidden "$app"
    fi
    sudo rm -rf "$app"
    echo "successfully unblocked"
}

while true; do
    echo "*Deleter*"
    echo "(type a number)"
    ask "1) iMovie      4) Company Portal
2) Sphero Edu  5) Google Chrome
3) GarageBand  6) Microsoft Edge
=> "

    case $reply in
        1|2|3|4|5|6)
            name=${APPS[reply-1]}
            echo "*$name*"
            ask "1) Block
2) Unblock
=> "
            case $reply in
                1) block "$name" ;;
                2) unblock "$name" ;;
                *) echo "Give a valid answer" ;;
            esac
            ;;
    esac
done

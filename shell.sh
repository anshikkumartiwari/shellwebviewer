#!/bin/bash

is_url() {
    if [[ $1 =~ ^https?:// ]]; then
        return 0
    else
        return 1
    fi
}

to_google_search_url() {
    local query="$1"
    local search_url="https://www.google.com/search?q=$(echo $query | sed 's/ /+/g')"
    echo $search_url
}

RED='\033[0;31m'
NC='\033[0m'

figlet -c "Web Viewer" | lolcat

echo -ne "${RED}Enter the URL or search query: ${NC}"
read input

if is_url "$input"; then
    url="$input"
else
    url=$(to_google_search_url "$input")
fi

python3 app.py "$url"


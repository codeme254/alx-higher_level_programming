#!/usr/bin/env bash

FILE_NAME=$1

touch "$FILE_NAME"
echo "#!/usr/bin/node" > "$FILE_NAME"
chmod a+x "$FILE_NAME"


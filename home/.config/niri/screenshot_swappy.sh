#!/bin/bash

tmpfile=$(mktemp)
grim -g "$(slurp)" - >"$tmpfile" && notify_view "swappy"
swappy -f - <"$tmpfile"
rm "$tmpfile"


#!/bin/bash

window_ids=()
window_titles=()

while read i; do
  declare -a line_array="($i)"
  window_ids+=(${line_array[0]})
  window_titles+=("${line_array[1]} - ${line_array[2]} \0icon\x1f${line_array[1]}")
done <<<$(niri msg --json windows | jq -r '.[] | [ .id, .app_id, .title] | "\""+join ("\" \"")+"\""')

result=$(printf "%b\n" "${window_titles[@]}" | fuzzel --counter --dmenu --index)

if [ "x$result" != "x" ] && [ $result != -1 ]; then
  niri msg action focus-window --id ${window_ids[result]}
fi

#!/usr/bin/env fish

while true
    sleep 0.2s

    niri msg --json workspaces \
        | jq -r ".[] | if .is_active then \"󰪥\" else \"󰄰\" end" \
        | string join " "
end

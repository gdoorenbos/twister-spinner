#!/bin/bash

declare -ra limb_strs=("right hand" "left hand" "right foot" "left foot")
declare -ra color_strs=("blue" "green" "yellow" "red")

while read -s; do
    limb_num=$((RANDOM % 4))
    color_num=$((RANDOM % 4))
    echo "${limb_strs[limb_num]} ${color_strs[color_num]}"
done

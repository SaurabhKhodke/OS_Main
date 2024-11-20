#!/bin/bash
# Bubble Sort implementation in Bash

# Function to perform Bubble Sort
bubble_sort() {
    local array=("$@")
    local n=${#array[@]}
    for ((i = 0; i < n; i++)); do
        for ((j = 0; j < n-i-1; j++)); do
            if (( array[j] > array[j+1] )); then
                # Swap elements
                temp=${array[j]}
                array[j]=${array[j+1]}
                array[j+1]=$temp
            fi
        done
    done
    # Print the sorted array
    echo "Sorted array: ${array[*]}"
}

# Check if there are arguments
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 num1 num2 num3 ..."
    exit 1
fi

# Call the bubble_sort function with the provided arguments
bubble_sort "$@"

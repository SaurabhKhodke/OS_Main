#!/bin/bash

# Function to check if a string is a palindrome
is_palindrome() {
    local str="$1"
    local reversed_str=""

    # Reverse the string using a loop
    local len=${#str}
    for (( i=$len-1; i>=0; i-- )); do
        reversed_str="${reversed_str}${str:$i:1}"
    done

    # Compare original and reversed string
    if [ "$str" = "$reversed_str" ]; then
        echo "true"
    else
        echo "false"
    fi
}

# Read input string
echo "Enter a string to check if it's a palindrome:"
read input_string

# Call the function with the input string
result=$(is_palindrome "$input_string")

# Check the result and print the outcome
if [ "$result" = "true" ]; then
    echo "The string '$input_string' is a palindrome."
else
    echo "The string '$input_string' is not a palindrome."
fi


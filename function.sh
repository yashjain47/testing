#!/bin/bash


# Function in shell

<< function_comment

How to create a function:

Function <function_name>() {

operations
conditions
etc

}

    ---------- OR   ---------

<function_name>() {

operations
conditions
etc

}


How to call a function : 
<function_name> <function_arguments>


function_comment







# read -p "Enter a number : " num
echo $1

is_even() {
if [ $(($1%2)) -eq 0 ];  then
    echo "Number is Even"
else
    echo "Number is Not Even"
fi
}


# This is Function Call
is_even $1
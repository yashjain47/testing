#!/bin/bash

<< Loops
For Loops and while Loops
Loops


# ----------------------------------------------------------------------------


read -p "Please enter the Number of Files:" file_number
read -p "Please enter the Name of Files:" file_name
for ((i=1 ; i<= $file_number ; i++))
do 
    touch "$file_name$i"
done



# ----------------------------------------------------------------------------

file_number=0
num=0s


# while [[ $file_number -le 10 ]]
# do 
#     echo "Low File Number:  $file_number"
#     file_number=$((file_number+1))
# done


# read -p "Please enter a number: " num


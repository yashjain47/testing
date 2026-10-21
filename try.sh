#!/bin/bash

which bash

<< comment
This is the comment section in shell scripting. you can wite anything after "<<".
bash try.sh yash 23 manesar
comment

read -p "Please enter your Name:" name
read -p "Please enter your age:" age
read -p "Enter Your Location" location

echo "Hello $name, Dated: $(date)"
echo "Your age is $age, Location : $location"

# echo "System Argumemts are :$0 $1 $2 $3 "

if [[ $age > 18 && $age < 70 ]]; then
    echo "You are eligible to vote"
elif [[ $age > 70 ]]; then
    echo "You are eligible to vote, after 70"
else
    echo "You are not eligible to vote"
fi


if [[ $age -ge 23 ]]; then
    echo "AGE IS CORRECT"
else
    echo "AGE IS NOT CORRECT"
fi


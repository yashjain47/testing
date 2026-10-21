#!/bin/bash




create_directory() {
    mkdir demo
}


# create_directory

if ! create_directory; then
    echo "Directory already Exists....."
    exit 1
else
    echo "Directory Created Successfully....."
fi



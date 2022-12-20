#!/bin/bash

file1=$1
file2=$2
n=0
re_s="[+-]?[0-9]+[.]?[0-9]*"
while [[ $n -lt 3 ]]; do
    if [[ $1 == "-v" ]]; then 
    	verbose=1
    else 
    	if [[ -z $file1 ]]; then
    	    file1=$1
    	else 
    	    file2=$1
    	fi
    fi
    shift
    n=$(($n + 1))
done

if [ -z $file1 -o -z $file2 ]; then
    if [ -n $verbose ]; then
        echo "Incorrect input"
    fi
    exit 2
fi

if [ ! -f $file1 -o ! -f $file2 ]; then
    if [ -n $verbose ]; then
        echo "One of files is not a file or not exists"
    fi
    exit 3
fi


if [ -n $verbose ]; then
    echo "Correct input"
fi

nums1=$(grep -owE $re_s $file1)
nums2=$(grep -owE $re_s $file2)

if [ -n $verbose ]; then
    echo "Numbers from file 1: "$nums1
    echo "Numbers from file 2: "$nums2 
fi

if [[ $nums1 == $nums2 ]]; then
    if [ -n $verbose ]; then
        echo "Files have the same content"
    fi
  exit 0
else
    if [ -n $verbose ]; then
        echo "Files does not have the same content"
    fi
  exit 1
fi


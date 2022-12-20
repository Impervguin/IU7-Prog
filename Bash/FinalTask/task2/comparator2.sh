#!/bin/bash

n=0

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

text1=$(cat $file1)
text2=$(cat $file2)
sep='string:'

before1=${text1%%"$sep"*}
ind1=${#before1}
after1=${text1:$(($ind1))}
if [[ -z $after1 ]]; then
    after1=$before1
fi

before2=${text2%%"$sep"*}
ind2=${#before2}
after2=${text2:$(($ind2))}
if [[ -z $after2 ]]; then
    after2=$before2
fi

if [ -n $verbose ]; then
    echo "Text from file 1: "$after1
    echo "Text from file 2: "$after2
fi

if [[ $after1 == $after2 ]]; then
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

#!/bin/zsh

for i in {1..100}
    if [ $(expr $i % 3) -eq 0 ] && [ $(expr $i % 5) -eq 0 ]
      then echo "$i", "FizzBuzz"
    elif [ $(expr $i % 3) -eq 0 ]
	     then echo "$i", "Fizz"
    elif [ $(expr $i % 5) -eq 0 ]
	     then echo "$i","Buzz"
fi


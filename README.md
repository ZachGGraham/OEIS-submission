# OEIS-submission
Submission for OEIS

Hamming distance is defined as the number of bits one must invert in order to "transform" a binary number from one to the other. 
My code finds the smallest consecutive integers whose Hamming distances are the n-th prime.

Start with 0. The first prime is 2, so the next number in the sequence must be a Hamming distance of 2 away from 0. The smallest number that satisfies these conditions is 3 (11). The next prime is 3, so the next number must be 4 (100), etc. 

While I admit my code is rather slow when n exceeds ~9, I think it provides an adequate method of getting the first few numbers of the sequence. But as the sequence grows exponentially and my code checks every single integer, the process gets very slow very fast. A faster method would be to perform simple bitwise operations, but as this was my first foray back into Python in a very long time, I do not remember how to do them in Python. 

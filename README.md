# Run_Length_Encoding
An implementation of the RLE data compression algorithm in Python.

###Algorithm
1. Pick the first character from source string.
2. Append the picked character to the destination string.
3. Count the number of subsequent occurrences of the picked character and append the count to destination string.
4. Pick the next character and repeat steps 2, 3 and 4 if end of string is NOT reached.

###Example
```
Enter String: wwwwwwwwwwwwwwjkkkkkkkkkkssss
Stats:
Length= 29
Size= 66

Encoded-  14:w/1:j/10:k/4:s/
Stats:
Length= 18
Size= 55
```

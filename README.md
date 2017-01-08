# Run_Length_Encoding
An implementation of the RLE data compression algorithm in Python.

Algorithm:
*a) Pick the first character from source string.
*b) Append the picked character to the destination string.
*c) Count the number of subsequent occurrences of the picked character and append the count to destination string.
*d) Pick the next character and repeat steps b) c) and d) if end of string is NOT reached.

Example:
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

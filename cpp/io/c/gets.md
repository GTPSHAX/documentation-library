---
title: std::gets
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/gets
---

ddcl | header=cstdio | deprecated=c++11 | removed=c++14 |
char* gets( char* str );
Reads `stdin` into given character string until a newline character is found or end-of-file occurs.

## Parameters


### Parameters


## Return value

`str` on success, a null pointer on failure.
If the failure has been caused by end of file condition, additionally sets the ''eof'' indicator (see `std::feof()`) on `stdin`. If the failure has been caused by some other error, sets the ''error'' indicator (see `std::ferror()`) on `stdin`.

## Notes

The `std::gets()` function does not perform bounds checking. Therefore, this function is extremely vulnerable to buffer-overflow attacks. It cannot be used safely (unless the program runs in an environment which restricts what can appear on `stdin`). For this reason, the function was deprecated in C++11 and removed altogether in C++14. `std::fgets()` may be used instead.

## Example


### Example


**Output:**
```
Never use std::gets(). Use std::fgets() instead!
Enter a string:
>Living on Earth is expensive, but it does include a free trip around the Sun.
The input string:
[Living on Earth] is truncated and has the length 15 characters.
```


## See also


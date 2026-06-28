---
title: std::basic_ostream::put
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ostream/put
---

ddcl |
basic_ostream& put( char_type ch );
Behaves as an *UnformattedOutputFunction*. After constructing and checking the sentry object, writes the character `ch` to the output stream.
If the output fails for any reason, sets `badbit`.

## Parameters


### Parameters


## Return value

`*this`

## Notes

This function is not overloaded for the types `signed char` or `unsigned char`, unlike the formatted `operator<<`.
Unlike formatted output functions, this function does not set the `failbit` if the output fails.

## Example


## See also

de:cpp/io/basic ostream/put
es:cpp/io/basic ostream/put
fr:cpp/io/basic ostream/put
it:cpp/io/basic ostream/put
ja:cpp/io/basic ostream/put
pt:cpp/io/basic ostream/put
ru:cpp/io/basic ostream/put
zh:cpp/io/basic ostream/put

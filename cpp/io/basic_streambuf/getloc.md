---
title: std::basic_streambuf::getloc
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/getloc
---

ddcl |
std::locale getloc() const;
Returns the associated locale.
The associated locale is the value supplied to `pubimbue()` on the last call, or, if that function has not been called, the value of the global locale (`std::locale`) at the time of the construction of the streambuf.

## Parameters

(none)

## Return value

The associated locale.

## Example


## See also

de:cpp/io/basic streambuf/getloc
es:cpp/io/basic streambuf/getloc
fr:cpp/io/basic streambuf/getloc
it:cpp/io/basic streambuf/getloc
ja:cpp/io/basic streambuf/getloc
pt:cpp/io/basic streambuf/getloc
ru:cpp/io/basic streambuf/getloc
zh:cpp/io/basic streambuf/getloc

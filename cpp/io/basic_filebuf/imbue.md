---
title: std::basic_filebuf::imbue
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/imbue
---

ddcl |
protected:
virtual void imbue( const std::locale& loc )
Changes the associated locale so that all characters inserted or extracted after this call (and until another call to `imbue()`) are converted using the `std::codecvt` facet of `loc`.
If the old locale's encoding is state-dependent and file is not positioned at the beginning, then the new locale must have the same `std::codecvt` facet as the one previously imbued.

## Parameters


### Parameters


## Return value

(none)

## Example


## See also

de:cpp/io/basic filebuf/imbue
es:cpp/io/basic filebuf/imbue
fr:cpp/io/basic filebuf/imbue
it:cpp/io/basic filebuf/imbue
ja:cpp/io/basic filebuf/imbue
pt:cpp/io/basic filebuf/imbue
ru:cpp/io/basic filebuf/imbue
zh:cpp/io/basic filebuf/imbue

---
title: std::basic_streambuf::showmanyc
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/showmanyc
---

ddcl | 1=
protected:
virtual std::streamsize showmanyc();
Estimates the number of characters available for input in the associated character sequence. `underflow()` is guaranteed not to return `Traits::eof()` or throw an exception until at least that many characters are extracted.

## Parameters

(none)

## Return value

The number of characters that are certainly available in the associated character sequence, or `-1` if `showmanyc` can determine, without blocking, that no characters are available. If `showmanyc` returns `-1`, `underflow()` and `uflow()` will definitely return `Traits::eof` or throw.
The base class version returns `0`, which has the meaning of "unsure if there are characters available in the associated sequence".

## Notes

The name of this function stands for "stream: how many characters?", so it is pronounced "S how many C", rather than "show many C".

## Example


## Defect reports


## See also


| cpp/io/basic_streambuf/dsc in_avail | (see dedicated page) |
| cpp/io/basic_filebuf/dsc showmanyc | (see dedicated page) |


---
title: vprint_unicode(std::ostream)
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ostream/vprint_unicode
---


# vprint_unicodesmall|(std::ostream)

ddcl|header=ostream|since=c++23|
void vprint_unicode( std::ostream& os,
std::string_view fmt, std::format_args args );
Format `args` according to the format string `fmt`, and writes the result to the output stream `os`. Behaves as *FormattedOutputFunction* of `os`, except that some details of error reporting differ.
Performs the following operations in order:
# First, the function constructs and checks the `sentry` object.
# Initializes an automatic variable as if by `1=std::string out = std::vformat(os.getloc(), fmt, args);`.
# Writes `out` to `os`:
:* If `os` refers to a terminal that is only capable of displaying Unicode via a native Unicode API, flushes `os` and writes `out` to the terminal using the native Unicode API.
:* Otherwise, inserts the character sequence [out.begin(), out.end()) into `os`.
If writing to the terminal or inserting into `os` fails, calls `os.setstate(std::ios_base::badbit)`.
rrev|since=c++26|
After writing characters to `os`, establishes an observable checkpoint.
If `out` contains invalid Unicode [Character encoding#Terminology|code units](https://en.wikipedia.org/wiki/Character encoding#Terminology|code units) when the native Unicode API is used, the behavior is undefined.

## Parameters


### Parameters

- `os` - output stream to insert data into
- `fmt` - 
- `args` - arguments to be formatted

## Exceptions


## Notes

If invoking the native Unicode API requires transcoding, the invalid code units are substituted with `U+FFFD` REPLACEMENT CHARACTER (see "The Unicode Standard - Core Specification", Chapter 3.9).

## Example


## Defect reports


## See also


| cpp/io/basic_ostream/dsc vprint_nonunicode | (see dedicated page) |
| cpp/io/basic_ostream/dsc print | (see dedicated page) |
| cpp/io/basic_ostream/dsc operator ltlt2 | (see dedicated page) |
| cpp/io/dsc vprint_unicode | (see dedicated page) |
| cpp/utility/format/dsc format | (see dedicated page) |


## External links


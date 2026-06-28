---
title: vprint_nonunicode(std::ostream)
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ostream/vprint_nonunicode
---


# vprint_nonunicodesmall|(std::ostream)

ddcl|header=ostream|since=c++23|
void vprint_nonunicode( std::ostream& os,
std::string_view fmt, std::format_args args );
Behaves as *FormattedOutputFunction* (except that some details of error reporting differ).
Performs the following operations in order:
# First, constructs and checks the `sentry` object.
# Then, initializes an automatic variable as if by `1=std::string out = std::vformat(os.getloc(), fmt, args);`.
# Finally, inserts the character sequence [out.begin(), out.end()) into `os`.
rrev|since=c++26|
After writing characters to `os`, establishes an observable checkpoint.

## Parameters


### Parameters

- `os` - output stream to insert data into
- `fmt` - 
- `args` - arguments to be formatted

## Exceptions


## Notes


## Example


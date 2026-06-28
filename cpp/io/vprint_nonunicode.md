---
title: std::vprint_nonunicode
type: Input/output
source: https://en.cppreference.com/w/cpp/io/vprint_nonunicode
---


```cpp
**Header:** `<`print`>`
dcl|num=1|since=c++23|
void vprint_nonunicode( std::FILE* stream,
std::string_view fmt, std::format_args args );
dcl|num=2|since=c++23|
void vprint_nonunicode_buffered
( std::FILE* stream, std::string_view fmt, std::format_args args );
dcl|num=3|since=c++23|
void vprint_nonunicode_buffered
( std::string_view fmt, std::format_args args );
```

Format `args` according to the format string `fmt`, and writes the result to the output stream.
1. While holding the lock on `stream`, writes the character representation of formatting arguments provided by `args` formatted according to specifications given in `fmt` to `stream`.
@@ If `stream` is not a valid pointer to an output C stream, the behavior is undefined.

```cpp
std::string out = std::vformat(fmt, args);
std::vprint_nonunicode(stream, "{}", std::make_format_args(out));
```

3. Equivalent to `std::vprint_nonunicode_buffered(stdout, fmt, args)`.
rrev|since=c++26|
After writing characters to the output stream, establishes an observable checkpoint.

## Parameters


### Parameters

- `stream` - output file stream to write to
- `fmt` - 
- `args` - arguments to be formatted

## Exceptions


## Notes


## Example


### Example

```cpp
<!--
#include <print>

int main()
{
}
-->
```


## Defect reports


## See also


| cpp/io/dsc vprint_unicode | (see dedicated page) |
| cpp/io/basic_ostream/dsc vprint_nonunicode | (see dedicated page) |
| cpp/io/dsc print | (see dedicated page) |
| cpp/utility/format/dsc format | (see dedicated page) |


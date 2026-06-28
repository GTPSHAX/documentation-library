---
title: std::filesystem::u8path
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/u8path
---


```cpp
**Header:** `<`filesystem`>`
dcl|num=1|since=c++17|deprecated=c++20|1=
template< class Source >
std::filesystem::path u8path( const Source& source );
dcl|num=2|since=c++17|deprecated=c++20|1=
template< class InputIt >
std::filesystem::path u8path( InputIt first, InputIt last );
```

Constructs a path `p` from a UTF-8 encoded sequence of `char`s<sup>(since C++20)</sup>  or `char8_t`s, supplied either as an `std::string`, or as `std::string_view`, or as a null-terminated multibyte string, or as a `[first, last)` iterator pair.
* If `path::value_type` is `char` and native encoding is UTF-8, constructs a path directly as if by `path(source)` or `path(first, last)`. Note: this is the typical situation of a POSIX system that uses Unicode, such as Linux.
* Otherwise, if `path::value_type` is `wchar_t` and native encoding is UTF-16 (this is the situation on Windows), or if `path::value_type` is `char16_t` (native encoding guaranteed UTF-16) or `char32_t` (native encoding guaranteed UTF-32), then first converts the UTF-8 character sequence to a temporary string `tmp` of type `path::string_type` and then the new path is constructed as if by `path(tmp)`.
* Otherwise (for non-UTF-8 narrow character encodings and for non-UTF-16 `wchar_t`), first converts the UTF-8 character sequence to a temporary UTF-32-encoded string `tmp` of type `std::u32string`, and then the new path is constructed as if by `path(tmp)` (this path is taken on a POSIX system with a non-Unicode multibyte or single-byte encoded filesystem).

## Parameters


### Parameters

- `source` - a UTF-8 encoded `std::string`, `std::string_view`, a pointer to a null-terminated multibyte string, or an input iterator with char value type that points to a null-terminated multibyte string
- `first, last` - pair of *InputIterator*s that specify a UTF-8 encoded character sequence

**Type requirements:**

- `InputIt`

## Return value

The path constructed from the input string after conversion from UTF-8 to the filesystem's native character encoding.

## Exceptions

May throw `std::bad_alloc` if memory allocation fails.

## Notes

On systems where native path format differs from the generic path format (neither Windows nor POSIX systems are examples of such OSes), if the argument to this function is using generic format, it will be converted to native.

## Example


## See also


| cpp/filesystem/dsc path | (see dedicated page) |


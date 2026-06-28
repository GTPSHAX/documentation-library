---
title: std::filesystem::path::operator+=
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/concat
---


```cpp
dcl|num=1|since=c++17|1=
path& operator+=( const path& p );
dcl|num=2|since=c++17|1=
path& operator+=( const string_type& str );
path& operator+=( std::basic_string_view<value_type> str );
dcl|num=3|since=c++17|1=
path& operator+=( const value_type* ptr );
dcl|num=4|since=c++17|1=
path& operator+=( value_type x );
dcl|num=5|since=c++17|1=
template< class CharT >
path& operator+=( CharT x );
dcl|num=6|since=c++17|1=
template< class Source >
path& operator+=( const Source& source );
dcl|num=7|since=c++17|1=
template< class Source >
path& concat( const Source& source );
dcl|num=8|since=c++17|1=
template< class InputIt >
path& concat( InputIt first, InputIt last );
```

Concatenates the current path and the argument
@1-3,6,7@ Appends `path(p).native()` to the pathname stored in `*this` in the native format. This directly manipulates the value of `native()` and may not be portable between operating systems.
@4,5@ Same as `1=return *this += std::basic_string_view(&x, 1);`.
8. Same as `1=return *this += path(first, last);`.

## Parameters


### Parameters

- `p` - path to append
- `str` - string or string view to append
- `ptr` - pointer to the beginning of a null-terminated string to append
- `x` - single character to append
- `source` - `std::basic_string`, `std::basic_string_view`, null-terminated multicharacter string, or an input iterator pointing to a null-terminated multicharacter sequence, which represents a path name (either in portable or in native format)
- `first, last` - pair of *InputIterator*s that specify a multicharacter sequence that represents a path name

**Type requirements:**

- `InputIt`

## Return value

`*this`

## Exceptions

May throw `std::bad_alloc` if memory allocation fails.

## Notes

Unlike with `append()` or `operator/, additional directory separators are never introduced.

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
#include <string>

int main()
{
    std::filesystem::path p1; // an empty path
    p1 += "var"; // does not insert a separator
    std::cout << R"("" + "var" --> )" << p1 << '\n';
    p1 += "lib"; // does not insert a separator
    std::cout << R"("var" + "lib" --> )" << p1 << '\n';
    auto str = std::string{"1234567"};
    p1.concat(std::begin(str) + 3, std::end(str) - 1);
    std::cout << "p1.concat --> " << p1 << '\n';
}
```


**Output:**
```
"" + "var" --> "var"
"var" + "lib" --> "varlib"
p1.concat --> "varlib456"
```


## Defect reports


## See also


| cpp/filesystem/path/dsc append | (see dedicated page) |
| cpp/filesystem/path/dsc operator/ | (see dedicated page) |


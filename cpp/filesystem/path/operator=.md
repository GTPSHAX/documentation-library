---
title: std::filesystem::path::operator=
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/operator=
---


```cpp
dcl|num=1|since=c++17|1=
path& operator=( const path& p );
dcl|num=2|since=c++17|1=
path& operator=( path&& p ) noexcept;
dcl|num=3|since=c++17|1=
path& operator=( string_type&& source );
dcl|num=4|since=c++17|1=
template< class Source >
path& operator=( const Source& source );
```

1. Replaces the contents of `*this` with a pathname whose both native and generic format representations equal those of `p`.
2. Replaces the contents of `*this` with a pathname whose both native and generic format representations equal those of `p`, possibly using move semantics: `p` is left in a valid, but unspecified state.
3. Replaces the contents of `*this` with a new path value constructed from detected-format `source`, which is left in valid, but unspecified state. Equivalent to `assign(std::move(source))`.
4. Replaces the contents of `*this` with a new path value constructed from detected-format `source` as if by overload  of the path constructor. Equivalent to `assign(source)`.

## Parameters


### Parameters

- `p` - a path to assign
- `source` - a `std::basic_string`, `std::basic_string_view`, pointer to a null-terminated character/wide character string, or an input iterator that points to a null-terminated character/wide character sequence. The character type must be one of `char`, <sup>(since C++20)</sup> `char8_t`, `char16_t`, `char32_t`, `wchar_t`

## Return value

`*this`

## Example


### Example

```cpp
#include <filesystem>
namespace fs = std::filesystem;

int main()
{
    fs::path p = "C:/users/abcdef/AppData/Local";
    p = p / "Temp"; // move assignment
    const wchar_t* wstr = L"D:/猫.txt";
    p = wstr; // assignment from a source
}
```


## Defect reports


## See also


| cpp/filesystem/path/dsc assign | (see dedicated page) |
| cpp/filesystem/path/dsc constructor | (see dedicated page) |


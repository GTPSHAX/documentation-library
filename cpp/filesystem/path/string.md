---
title: std::filesystem::path::wstring
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/string
---


```cpp
dcl|num=1|since=c++17|1=
template< class CharT, class Traits = std::char_traits<CharT>,
class Alloc = std::allocator<CharT> >
std::basic_string<CharT,Traits,Alloc>
string( const Alloc& a = Alloc() ) const;
dcl|num=2|since=c++17|
std::string string() const;
dcl|num=3|since=c++17|
std::wstring wstring() const;
dcl|num=4|since=c++17|
std::u16string u16string() const;
dcl|num=5|since=c++17|
std::u32string u32string() const;
dcl rev multi|num=6|since1=c++17|until1=c++20|dcl1=
std::string u8string() const;
|dcl2=
std::u8string u8string() const;
```

Returns the internal pathname in native pathname format, converted to specific string type. Conversion, if any, is performed as follows:
1. All memory allocations are performed by `a`.
6. The result encoding in the case of `u8string()` is always UTF-8.

## Return value

The internal pathname in native pathname format, converted to specified string type.

## Example


### Example

```cpp
#include <clocale>
#include <cstdio>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <locale>

int main()
{
    const char* const localeName = "ja_JP.utf-8";
    std::setlocale(LC_ALL, localeName);
    std::locale::global(std::locale(localeName));

    const std::filesystem::path p(u8"要らない.txt");
    std::ofstream(p) << "File contents";

    // native string representation can be used with OS APIs
    if (std::FILE* const f = std::fopen(p.string().c_str(), "r"))
    {
        for (int ch; (ch = std::fgetc(f)) != EOF;)
            std::putchar(ch);

        std::fclose(f);
    }

    // multibyte and wide representation can be used for output
    std::cout << "\nFile name in narrow multibyte encoding: " << p.string() << '\n';

    // wstring() will throw in stdlibc++ (as per gcc-12.1.0), see:
    // https://gcc.gnu.org/bugzilla/show_bug.cgi?id=95048
    // https://gcc.gnu.org/bugzilla/show_bug.cgi?id=102839
    // works with more recent gcc-12.2.1 (2023/02/01) and clang-10+
    std::wcout << "File name in wide encoding: " << p.wstring() << '\n';

    std::filesystem::remove(p);
}
```


**Output:**
```
File contents
File name in narrow multibyte encoding: 要らない.txt
File name in wide encoding: 要らない.txt
```


## See also


| cpp/filesystem/path/dsc generic string | (see dedicated page) |


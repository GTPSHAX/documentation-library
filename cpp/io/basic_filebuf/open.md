---
title: std::basic_filebuf::open
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/open
---


```cpp
dcl|num=1|
basic_filebuf* open( const char* s, std::ios_base::openmode mode );
dcl|num=2|since=c++11|
basic_filebuf* open( const std::string& str, std::ios_base::openmode mode );
dcl|num=3|since=c++17|
basic_filebuf* open( const std::filesystem::path& p,
std::ios_base::openmode mode );
dcl|num=4|since=c++17|
basic_filebuf* open( const std::filesystem::path::value_type* s,
std::ios_base::openmode mode );
```

If the associated file was already open (`1=is_open() != false`), returns a null pointer right away.
Otherwise, opens the file with the given name (`s`<sup>(since C++17)</sup> , `p.c_str()` or `str.c_str()`, depending on the overload). `std::ios_base::openmode` values may be written as, e.g., `std::ios_base::out .
<sup>(since C++17)</sup> Overload
The file is opened as if by calling `std::fopen` with the second argument (file access mode) determined by the result of `mode & ~std::ios_base::ate` as follows, `open()` fails if the result is not some combination of flags shown in the table:


| - |
| colspan="6" | c | mode & ~std::ios_base::ate |
| rowspan="2" | lc | std::fopen<br>access<br>mode |
| rowspan="2" | Action if file already exists |
| rowspan="2" | Action if file does not exist |
| -style="text-align:center" |
| style="width: 68px;" | ltt | cpp/io/ios_base/openmode | binary |
| style="width: 68px;" | ltt | cpp/io/ios_base/openmode | in |
| style="width: 68px;" | ltt | cpp/io/ios_base/openmode | out |
| style="width: 68px;" | ltt | cpp/io/ios_base/openmode | trunc |
| style="width: 68px;" | ltt | cpp/io/ios_base/openmode | app |
| ltt | cpp/io/ios_base/openmode | noreplace<br><sup>(C++23)</sup> |
| - |
| no | - |
| yes | + |
| no | - |
| no | - |
| no | - |
| no | - |
| c | "r" |
| rowspan="4" | Read from start |
| rowspan="2" | Failure to open |
| - |
| yes | + |
| yes | + |
| no | - |
| no | - |
| no | - |
| no | - |
| c | "rb" |
| - |
| no | - |
| yes | + |
| yes | + |
| no | - |
| no | - |
| no | - |
| c | "r+" |
| rowspan="2" | Error |
| - |
| yes | + |
| yes | + |
| yes | + |
| no | - |
| no | - |
| no | - |
| c | "r+b" |
| - |
| no | - |
| no | - |
| yes | + |
| no | - |
| no | - |
| no | - |
| rowspan="2" | c | "w" |
| rowspan="6" | Destroy contents |
| rowspan="6" | Create new |
| - |
| no | - |
| no | - |
| yes | + |
| yes | + |
| no | - |
| no | - |
| - |
| yes | + |
| no | - |
| yes | + |
| no | - |
| no | - |
| no | - |
| rowspan="2" | c | "wb" |
| - |
| yes | + |
| no | - |
| yes | + |
| yes | + |
| no | - |
| no | - |
| - |
| no | - |
| yes | + |
| yes | + |
| yes | + |
| no | - |
| no | - |
| c | "w+" |
| - |
| yes | + |
| yes | + |
| yes | + |
| yes | + |
| no | - |
| no | - |
| c | "w+b" |
| - |
| no | - |
| no | - |
| yes | + |
| no | - |
| no | - |
| yes | + |
| rowspan="2" | c | "wx" |
| rowspan="6" | Failure to open |
| rowspan="6" | Create new |
| - |
| no | - |
| no | - |
| yes | + |
| yes | + |
| no | - |
| yes | + |
| - |
| yes | + |
| no | - |
| yes | + |
| no | - |
| no | - |
| yes | + |
| rowspan="2" | c | "wbx" |
| - |
| yes | + |
| no | - |
| yes | + |
| yes | + |
| no | - |
| yes | + |
| - |
| no | - |
| yes | + |
| yes | + |
| yes | + |
| no | - |
| yes | + |
| c | "w+x" |
| - |
| yes | + |
| yes | + |
| yes | + |
| yes | + |
| no | - |
| yes | + |
| c | "w+bx" |
| - |
| no | - |
| no | - |
| yes | + |
| no | - |
| yes | + |
| no | - |
| rowspan="2" | c | "a" |
| rowspan="8" | Write to end |
| rowspan="8" | Create new |
| - |
| no | - |
| no | - |
| no | - |
| no | - |
| yes | + |
| no | - |
| - |
| yes | + |
| no | - |
| yes | + |
| no | - |
| yes | + |
| no | - |
| rowspan="2" | c | "ab" |
| - |
| yes | + |
| no | - |
| no | - |
| no | - |
| yes | + |
| no | - |
| - |
| no | - |
| yes | + |
| yes | + |
| no | - |
| yes | + |
| no | - |
| rowspan="2" | c | "a+" |
| - |
| no | - |
| yes | + |
| no | - |
| no | - |
| yes | + |
| no | - |
| - |
| yes | + |
| yes | + |
| yes | + |
| no | - |
| yes | + |
| no | - |
| rowspan="2" | c | "a+b" |
| - |
| yes | + |
| yes | + |
| no | - |
| no | - |
| yes | + |
| no | - |

If the open operation succeeds and `1=(openmode & std::ios_base::ate) != 0` (the `ate` bit is set), repositions the file position to the end of file, as if by calling `std::fseek(file, 0, SEEK_END)`, where `file` is the pointer returned by calling `std::fopen`. If the repositioning fails, calls `close()` and returns a null pointer to indicate failure.

## Parameters


### Parameters

- `s, str, p` - the file name to open; `s` must point to a null-terminated string
- `openmode` - the file opening mode, a binary OR of the `std::ios_base::openmode` modes

## Return value

`this` on success, a null pointer on failure.

## Notes

`open()` is typically called through the constructor or the `open()` member function of `std::basic_fstream`.

## Example


### Example

```cpp
#include <fstream>
#include <iostream>

int main()
{
    std::string filename = "Test.b";
    std::filebuf fb;

    // prepare a file to read
    double d = 3.14;
    if (!fb.open(filename, std::ios::binary {{!
```

{
std::cout << "Open file " << filename << " for write failed\n";
return 1;
}
fb.sputn(reinterpret_cast<char*>(&d), sizeof d);
fb.close();
// open file for reading
double d2 = 0.0;
if (!fb.open(filename, std::ios::binary | std::ios::in))
{
std::cout << "Open file " << filename << " for read failed\n";
return 1;
}
auto got = fb.sgetn(reinterpret_cast<char*>(&d2), sizeof d2);
if (sizeof(d2) != got)
std::cout << "Read of " << filename << " failed\n";
else
std::cout << "Read back from file: " << d2 << '\n';
}
|output=
Read back from file: 3.14

## Defect reports


## See also


| cpp/io/basic_filebuf/dsc is_open | (see dedicated page) |
| cpp/io/basic_filebuf/dsc close | (see dedicated page) |


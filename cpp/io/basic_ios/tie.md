---
title: std::basic_ios::tie
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/tie
---


```cpp
dcl|num=1|
std::basic_ostream<CharT, Traits>* tie() const;
dcl|num=2|
std::basic_ostream<CharT, Traits>* tie( std::basic_ostream<CharT, Traits>* str );
```

Manages the tied stream. A tied stream is an output stream which is synchronized with the sequence controlled by the stream buffer (`rdbuf()`), that is, `flush()` is called on the tied stream before any input/output operation on `*this`.
1. Returns the current tied stream. If there is no tied stream, a null pointer is returned.
2. Sets the current tied stream to `str`. Returns the tied stream before the operation. If there is no tied stream, a null pointer is returned. If `str` is not null and `tie()` is reachable by traversing the linked list of tied stream objects starting from `str->tie()`, the behavior is undefined.

## Parameters


### Parameters

- `str` - an output stream to set as the tied stream

## Return value

The tied stream, or a null pointer if there was no tied stream.

## Notes

By default, the standard stream `std::cout` is tied to `std::cin` and `std::cerr`. Similarly, its wide counterpart `std::wcout` is tied to `std::wcin` and `std::wcerr`.

## Example


### Example

```cpp
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>

int main()
{
    std::ofstream os("test.txt");
    std::ifstream is("test.txt");
    std::string value("0");

    os << "Hello";
    is >> value;

    std::cout << "Result before tie(): " << std::quoted(value) << "\n";
    is.clear();
    is.tie(&os);

    is >> value;

    std::cout << "Result after tie(): " << std::quoted(value) << "\n";
}
```


**Output:**
```
Result before tie(): "0"
Result after tie(): "Hello"
```


## Defect reports


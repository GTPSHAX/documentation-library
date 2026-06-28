---
title: std::ios_base::seekdir
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base/seekdir
---


```cpp
dcl|
typedef /*implementation defined*/ seekdir;
dcl|1=
static constexpr seekdir beg = /*implementation defined*/
static constexpr seekdir end = /*implementation defined*/
static constexpr seekdir cur = /*implementation defined*/
```

Specifies file seeking direction type. The following constants are defined:

## Example


### Example

```cpp
#include <iostream>
#include <sstream>
#include <string>

int main()
{
    std::istringstream in("Hello, World!");
    std::string word1, word2, word3, word4, word5;

    in >> word1;
    in.seekg(0, std::ios_base::beg); // <- rewind
    in >> word2;
    in.seekg(1, std::ios_base::cur); // -> seek from cur pos toward the end
    in >> word3;
    in.seekg(-6, std::ios_base::cur); // <- seek from cur pos (end) toward begin
    in >> word4;
    in.seekg(-6, std::ios_base::end); // <- seek from end toward begin
    in >> word5;

    std::cout << "word1 = " << word1 << '\n'
              << "word2 = " << word2 << '\n'
              << "word3 = " << word3 << '\n'
              << "word4 = " << word4 << '\n'
              << "word5 = " << word5 << '\n';
}
```


**Output:**
```
word1 = Hello,
word2 = Hello,
word3 = World!
word4 = World!
word5 = World!
```


## See also


| cpp/io/basic_istream/dsc seekg | (see dedicated page) |
| cpp/io/basic_ostream/dsc seekp | (see dedicated page) |
| cpp/io/basic_streambuf/dsc pubseekoff | (see dedicated page) |


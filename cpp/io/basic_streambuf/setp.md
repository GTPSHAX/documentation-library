---
title: std::basic_streambuf::setp
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/setp
---

ddcl|1=
protected:
void setp( char_type* pbeg, char_type* pend );
Sets the values of the pointers defining the put area.
After the call, `1=pbase() == pbeg`, `1=pptr() == pbeg` and `1=epptr() == pend` are all `true`.
If any of [pbeg, pend) is not a valid range, the behavior is undefined.

## Parameters


### Parameters

- `pbeg` - pointer to the new beginning of the put area
- `pend` - pointer to the new end of the put area

## Example


### Example

```cpp
#include <array>
#include <cstddef>
#include <iostream>

// Buffer for std::ostream implemented by std::array
template<std::size_t size, class CharT = char>
struct ArrayedStreamBuffer : std::basic_streambuf<CharT>
{
    using Base = std::basic_streambuf<CharT>;
    using char_type = typename Base::char_type;

    ArrayedStreamBuffer()
    {
        // put area pointers to work with “buffer”
        Base::setp(buffer.data(), buffer.data() + size);
    }

    void print_buffer()
    {
        for (char_type i : buffer)
        {
            if (i == 0)
                std::cout << "\\0";
            else
                std::cout << i;
            std::cout << ' ';
        }
        std::cout << '\n';
    }

private:
    std::array<char_type, size> buffer{}; // value-initialize “buffer”
};

int main()
{
    ArrayedStreamBuffer<10> streambuf;
    std::ostream stream(&streambuf);

    stream << "hello";
    stream << ",";

    streambuf.print_buffer();
}
```


**Output:**
```
h e l l o , \0 \0 \0 \0
```


## Defect reports


## See also


| cpp/io/basic_streambuf/dsc setg | (see dedicated page) |


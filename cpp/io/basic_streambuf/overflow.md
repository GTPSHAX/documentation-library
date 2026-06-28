---
title: std::basic_streambuf::overflow
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/overflow
---

ddcl|1=
protected:
virtual int_type overflow( int_type ch = Traits::eof() );
The intent of this function is to transmit characters from the put area of the stream buffer to the associated character sequence.
Formally, this function ensures that there is space at the put area for at least one character. The base class version always fails, and a possibly-succeeding implementation can only be provided in derived classes (see implementation requirements). The standard library provides <sup>(until C++26)</sup> `std::strstreambuf::overflow()`, `std::basic_stringbuf::overflow()` and .

## Parameters


### Parameters

- `ch` - the character to store in the put area

## Return value

`Traits::eof()`

## Implementation requirements

Every overriding definition of this virtual function must obey the following constraints, otherwise the behavior is undefined:
* The effect of the function is to consume some initial subsequence of the characters of the . The pending sequence is defined as the concatenation of the following sequences:
** The put area (formally, empty sequence if `pbase()` is null, otherwise `pptr() - pbase()` characters beginning at `pbase()`).
** The character `ch` or nothing if ch is EOF (formally, if `Traits::eq_int_type(ch, Traits::eof())` returns `true`).
* After consumption, the put area pointers are updated to hold the remaining characters, if any. Formally, let `r` be the number of characters in the pending sequence not consumed:
** If `r` is non-zero, then `pbase()` and `pptr()` are set so that all following conditions are satisfied:
*** `pptr() - pbase()` is `r`.
*** The `r` characters starting at `pbase()` are the associated output stream.
** If `r` is zero (all characters of the pending sequence have been consumed), then either `pbase()` is set to a null value, or `pbase()` and `pptr()` are both set to the same non-null value.
* The function may fail if either appending some character to the associated output stream fails or if it is unable to establish `pbase()` and `pptr()` according to the above rules.
* If the function succeeds, returns some value other than `Traits::eof()`. Typically, `ch` is returned to indicate success, except when `Traits::eq_int_type(ch, Traits::eof())` returns `true`, in which case `Traits::not_eof(ch)` is returned.
* If the function fails, returns `Traits::eof()` or throws an exception.

## Note

The `sputc()` and `sputn()` call this function in case of an overflow (`1=pptr() == nullptr` or `1=pptr() >= epptr()`).

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
    using int_type = typename Base::int_type;

    ArrayedStreamBuffer()
    {
        // put area pointers to work with 'buffer'
        Base::setp(buffer.data(), buffer.data() + size);
    }

    int_type overflow(int_type ch) 
    {
        std::cout << "overflow\n";
        return Base::overflow(ch);
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
    std::array<char_type, size> buffer{}; // value-initialize buffer
};

int main()
{
    ArrayedStreamBuffer<10> streambuf;
    std::ostream stream(&streambuf);

    stream << "hello";
    streambuf.print_buffer();
    if (stream.good())
        std::cout << "stream is good\n";

    stream << "world";
    streambuf.print_buffer();
    if (stream.good())
        std::cout << "stream is good\n";

    stream << "!";
    streambuf.print_buffer();
    if (!stream.good())
        std::cout << "stream is not good\n";
}
```


**Output:**
```
h e l l o \0 \0 \0 \0 \0
stream is good
h e l l o w o r l d 
stream is good
overflow
h e l l o w o r l d 
stream is not good
```


## See also


| cpp/io/basic_streambuf/dsc uflow | (see dedicated page) |
| cpp/io/basic_streambuf/dsc underflow | (see dedicated page) |
| cpp/io/basic_filebuf/dsc overflow | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc overflow | (see dedicated page) |
| cpp/io/strstreambuf/dsc overflow | (see dedicated page) |


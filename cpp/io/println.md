---
title: std::println
type: Input/output
source: https://en.cppreference.com/w/cpp/io/println
---


```cpp
**Header:** `<`print`>`
dcl|num=1|since=c++23|
template< class... Args >
void println( std::format_string<Args...> fmt, Args&&... args );
dcl|num=2|since=c++23|
template< class... Args >
void println( std::FILE* stream,
std::format_string<Args...> fmt, Args&&... args );
dcla|num=3|since=c++26|
void println();
dcl|num=4|since=c++26|
void println( std::FILE* stream );
```

Format `args` according to the format string `fmt` with appended `'\n'` (which means that each output ends with a new-line), and print the result to a stream.
1. Equivalent to `std::println(stdout, fmt, std::forward<Args>(args)...)`.

```cpp
std::print(stream, std::dynamic_format(std::string(fmt.get()) + '\n'),
           std::forward<Args>(args)...)
```

3. Equivalent to `std::println(stdout)`.
4. Equivalent to `std::print(stream, "\n")`.
If `std::formatter<Ti, char>` does not meet the *BasicFormatter* requirements for any `Ti` in `Args` (as required by `std::make_format_args`), the behavior is undefined.

## Parameters


### Parameters

- `stream` - output file stream to write to
- `fmt` - 
- `args...` - arguments to be formatted

## Exceptions


## Notes

Although overloads  are added in C++26, all known implementations make them available in C++23 mode.

## Example


### Example

```cpp
#include <print>

int main()
{
    // Each call to std::println ends with new-line
    std::println("Please"); // overload (1)
    std::println("enter"); // (1)

    std::print("pass");
    std::print("word");

    std::println(); // (3); valid since C++26; same effect as std::print("\n"); 
}
```


**Output:**
```
Please
enter
password

<nowiki/>
```


## See also


| cpp/io/dsc print | (see dedicated page) |
| cpp/io/basic_ostream/dsc println | (see dedicated page) |
| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/io/c/dsc fprintf | (see dedicated page) |


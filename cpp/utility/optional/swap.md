---
title: std::optional::swap
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/optional/swap
---

ddcl|since=c++17|notes=<sup>(constexpr C++20)</sup>|
void swap( optional& other ) noexcept(/* see below */);
Swaps the contents with those of `other`.
* If neither `*this` nor `other` contain a value, the function has no effect.
* If only one of `*this` and `other` contains a value (let's call this object `in` and the other `un`), the contained value of `un` is direct-initialized from `std::move(*in)`, followed by destruction of the contained value of `in` as if by `in->T::~T()`. After this call, `in` does not contain a value; `un` contains a value.
* If both `*this` and `other` contain values, the contained values are exchanged by calling `using std::swap; swap(**this, *other)`.
The program is ill-formed unless type `T` is *Swappable* and `std::is_move_constructible_v<T>` is `true`.

## Parameters


### Parameters

- `other` - the `optional` object to exchange the contents with

## Return value

(none)

## Exceptions

noexcept|std::is_nothrow_move_constructible_v<T> &&
std::is_nothrow_swappable_v<T>
In the case of thrown exception, the states of the contained values of `*this` and `other` are determined by the exception safety guarantees of `swap` of type `T` or `T`'s move constructor, whichever is called. For both `*this` and `other`, if the object contained a value, it is left containing a value, and the other way round.

## Notes


## Example


### Example

```cpp
#include <iostream>
#include <optional>
#include <string>

int main()
{
    std::optional<std::string> opt1("First example text");
    std::optional<std::string> opt2("2nd text");

    enum Swap { Before, After };
    auto print_opts = [&](Swap e)
    {
        std::cout << (e == Before ? "Before swap:\n" : "After swap:\n");
        std::cout << "opt1 contains '" << opt1.value_or("") << "'\n";
        std::cout << "opt2 contains '" << opt2.value_or("") << "'\n";
        std::cout << (e == Before ? "---SWAP---\n": "\n");
    };

    print_opts(Before);
    opt1.swap(opt2);
    print_opts(After);

    // Swap with only 1 set
    opt1 = "Lorem ipsum dolor sit amet, consectetur tincidunt.";
    opt2.reset();

    print_opts(Before);
    opt1.swap(opt2);
    print_opts(After);
}
```


**Output:**
```
Before swap:
opt1 contains 'First example text'
opt2 contains '2nd text'
---SWAP---
After swap:
opt1 contains '2nd text'
opt2 contains 'First example text'

Before swap:
opt1 contains 'Lorem ipsum dolor sit amet, consectetur tincidunt.'
opt2 contains ''
---SWAP---
After swap:
opt1 contains ''
opt2 contains 'Lorem ipsum dolor sit amet, consectetur tincidunt.'
```


## Defect reports


## See also


| cpp/utility/optional/dsc swap2 | (see dedicated page) |


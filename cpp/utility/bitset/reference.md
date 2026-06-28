---
title: std::bitset::reference
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/bitset/reference
---

ddcl|
class reference;
The `std::bitset` class includes `std::bitset::reference` as a publicly-accessible nested class. This class is used as a proxy object to allow users to interact with individual bits of a bitset, since standard C++ types (like references and pointers) are not built with enough precision to specify individual bits.
The primary use of `std::bitset::reference` is to provide an lvalue that can be returned from `operator[]`.
Any reads or writes to a bitset that happen via a `std::bitset::reference` potentially read or write to the entire underlying bitset.

## Member functions


| cpp/utility/bitset/reference/dsc operator bool | (see dedicated page) |

member|reference|2=
ddcla|since=c++11|constexpr=c++23|1=
reference( const reference& ) = default;
Constructs the reference from another reference.<sup>(until C++11)</sup>  The copy constructor is implicitly declared.
Other constructors can only be accessed by `std::bitset`.
member|~reference|2=
ddcla|constexpr=c++23|
~reference();
Destroys the reference.
member|operator|2=

```cpp
dcla|num=1|noexcept=c++11|constexpr=c++23|1=
reference& operator=( bool x );
dcla|num=2|noexcept=c++11|constexpr=c++23|1=
reference& operator=( const reference& x );
```

Assigns a value to the referenced bit.

## Parameters


### Parameters

- `x` - value to assign

## Return value

`*this`
member|operator bool|2=
ddcla|noexcept=c++11|constexpr=c++23|
operator bool() const;
Returns the value of the referenced bit.

## Return value

The referenced bit.
member|operator~|2=
ddcla|noexcept=c++11|constexpr=c++23|
bool operator~() const;
Returns the inverse of the referenced bit.

## Return value

The inverse of the referenced bit.
member|flip|2=
ddcla|noexcept=c++11|constexpr=c++23|
reference& flip();
Inverts the referenced bit.

## Return value

`*this`

## Example


### Example

```cpp
#include <bitset>
#include <iostream>

int main()
{
    std::bitset<4> bs{0b1110};
    std::bitset<4>::reference ref = bs[2];

    auto info = [&](int id)
    {
        std::cout << id << ") bs: " << bs << "; ref bit: " << ref << '\n';
    };

    info(1);
    ref = false;
    info(2);
    ref = true;
    info(3);
    ref.flip();
    info(4);
    ref = bs[1]; // operator=( const reference& x )
    info(5);

    std::cout << "6) ~ref bit: " << ~ref << '\n';
}
```


**Output:**
```
1) bs: 1110; ref bit: 1
2) bs: 1010; ref bit: 0
3) bs: 1110; ref bit: 1
4) bs: 1010; ref bit: 0
5) bs: 1110; ref bit: 1
6) ~ref bit: 0
```


## See also


| cpp/utility/bitset/dsc operator at | (see dedicated page) |


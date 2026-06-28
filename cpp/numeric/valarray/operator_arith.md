---
title: std::valarray::operators
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/operator_arith
---


```cpp
dcl|num=1|
valarray<T> operator+() const;
dcl|num=2|1=
valarray<T> operator-() const;
dcl|num=3|1=
valarray<T> operator~() const;
dcl|num=4|1=
valarray<bool> operator!() const;
```

Applies unary operators to each element in the numeric array.

## Parameters

(none)

## Return value

A numeric array containing elements with values obtained by applying corresponding operator to the values in `*this`.

## Notes

Each of the operators can only be instantiated if the following requirements are met:
:* The indicated operator can be applied to type `T`.
:* The result value can be unambiguously converted to `T` (1-3) or `bool` (4).

## Example


### Example

```cpp
#include <iostream>
#include <string_view>
#include <valarray>

template<typename T>
void print(std::string_view const note,
           std::valarray<T> const vala, // by-value, see Notes above
           std::string_view const term = "\n")
{
    std::cout << note << std::boolalpha << std::showpos;
    for (T const element : vala)
        std::cout << '\t' << element;
    std::cout << term;
}

int main()
{
    std::valarray<int> x{1, 2, 3, 4};
    print<int>("x: ", x);
    print<int>("+x: ", +x);
    print<int>("+ + x: ", + + x);
    print<int>("-x: ", -x);
    print<int>("- - x: ", - - x, "\n\n");

    std::valarray<short> y{0, 1, -1, 0x7fff};
    print<short>("y: ", y);
    print<short>("~y: ", ~y);
    print<short>("~~y: ", ~~y, "\n\n");

    std::valarray<bool> z{true, false};
    print<bool>("z: ", z);
    print<bool>("!z: ", !z);
    print<bool>("!!z: ", !!z);
}
```


**Output:**
```
x:      +1      +2      +3      +4
+x:     +1      +2      +3      +4
+ + x:  +1      +2      +3      +4
-x:     -1      -2      -3      -4
- - x:  +1      +2      +3      +4

y:      +0      +1      -1      +32767
~y:     -1      -2      +0      -32768
~~y:    +0      +1      -1      +32767

z:      true    false
!z:     false   true
!!z:    true    false
```


## See also


| cpp/numeric/valarray/dsc operator_arith2 | (see dedicated page) |
| cpp/numeric/valarray/dsc operator_arith3 | (see dedicated page) |


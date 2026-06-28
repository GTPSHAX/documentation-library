---
title: std::regular
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/regular
---

ddcl|header=concepts|since=c++20|1=
template< class T >
concept regular = std::semiregular<T> && std::equality_comparable<T>;
The `regular` concept specifies that a type is ''regular'', that is, it is copyable, default constructible, and equality comparable. It is satisfied by types that behave similarly to built-in types like `int`, and that are comparable with `1===`.

## Example


### Example

```cpp
#include <concepts>
#include <iostream>

template<std::regular T>
struct Single
{
    T value;
    friend bool operator==(const Single&, const Single&) = default;
};

int main()
{
    Single<int> myInt1{4};
    Single<int> myInt2;
    myInt2 = myInt1;

    if (myInt1 == myInt2)
        std::cout << "Equal\n";

    std::cout << myInt1.value << ' ' << myInt2.value << '\n';
}
```


**Output:**
```
Equal
4 4
```


## References


## See also


| cpp/concepts/dsc semiregular | (see dedicated page) |


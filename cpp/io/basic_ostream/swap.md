---
title: std::basic_ostream::swap
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ostream/swap
---


```cpp
dcl|since=c++11|1=
protected:
void swap( basic_ostream& rhs );
```

Calls `basic_ios::swap(rhs)` to swap all data members of the base class, except for `rdbuf()`, between `*this` and `rhs`. This swap function is protected: it is called by the swap functions of the swappable output stream classes `std::basic_ofstream` and `std::basic_ostringstream`, which know how to correctly swap the associated streambuffers.

## Parameters


### Parameters

- `rhs` - a basic_ostream of the same type to swap with

## Example


### Example

```cpp
#include <iostream>
#include <sstream>
#include <utility>

int main()
{
    std::ostringstream s1("hello");
    std::ostringstream s2("bye");

    s1.swap(s2); // OK, ostringstream has a public swap()
    std::swap(s1, s2); // OK, calls s1.swap(s2)

//  std::cout.swap(s2); // ERROR: swap is a protected member

    std::cout << s1.str() << '\n';
}
```


**Output:**
```
hello
```


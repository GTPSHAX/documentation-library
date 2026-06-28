---
title: std::basic_ostream::operator=
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ostream/operator=
---


```cpp
dcl|num=1|1=
protected:
basic_ostream& operator=( const basic_ostream& rhs ) = delete;
dcl|num=2|since=c++11|1=
protected:
basic_ostream& operator=( basic_ostream&& rhs );
```

1. The copy assignment operator is protected, and is deleted. Output streams are not *CopyAssignable*.
2. The move assignment operator exchanges all data members of the base class, except for , with `rhs`, as if by calling `swap(*rhs)`. This move assignment operator is protected: it is only called by the move assignment operators of the derived movable output stream classes `std::basic_ofstream` and `std::basic_ostringstream`, which know how to correctly move-assign the associated streambuffers.

## Parameters


### Parameters

- `rhs` - the `basic_ostream` object from which to assign to `*this`

## Example


### Example

```cpp
#include <iostream>
#include <sstream>
#include <utility>

int main()
{
    std::ostringstream s;
//  std::cout = s;            // ERROR: copy assignment operator is deleted
//  std::cout = std::move(s); // ERROR: move assignment operator is protected
    s = std::move(std::ostringstream() << 42); // OK, moved through derived
    std::cout << s.str() << '\n';
}
```


**Output:**
```
42
```


## Defect reports


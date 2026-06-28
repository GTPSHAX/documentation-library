---
title: std::swap(std::function)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function/swap2
---


```cpp
**Header:** `<`functional`>`
dcl|since=c++11|
template< class R, class... Args >
void swap( std::function<R(Args...)>& lhs, std::function<R(Args...)>& rhs ) noexcept;
```

Overloads the `std::swap` algorithm for `std::function`. Exchanges the state of `lhs` with that of `rhs`. Effectively calls `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - polymorphic function wrappers whose states to swap

## Return value

(none)

## Example


### Example

```cpp
#include <functional>
#include <iostream>

void foo(const char* str, int x)
{
    std::cout << "foo(\"" << str << "\", " << x << ")\n";
}

void bar(const char* str, int x)
{
    std::cout << "bar(\"" << str << "\", " << x << ")\n";
}

int main()
{
    std::function<void(const char*, int)> f1{foo};
    std::function<void(const char*, int)> f2{bar};

    f1("f1", 1);
    f2("f2", 2);

    std::cout << "std::swap(f1, f2);\n";
    std::swap(f1, f2);

    f1("f1", 1);
    f2("f2", 2);
}
```


**Output:**
```
foo("f1", 1)
bar("f2", 2)
std::swap(f1, f2);
bar("f1", 1)
foo("f2", 2)
```


## Defect reports


## See also


| cpp/utility/functional/function/dsc swap | (see dedicated page) |
| cpp/utility/functional/move_only_function/dsc swap2 | (see dedicated page) |


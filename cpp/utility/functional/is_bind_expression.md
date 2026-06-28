---
title: std::is_bind_expression
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/is_bind_expression
---


```cpp
**Header:** `<`functional`>`
dcl|since=c++11|1=
template< class T >
struct is_bind_expression;
```

If `T` is a type produced by a call to `std::bind` (but not `std::bind_front` or `std::bind_front|std::bind_back`), this template is derived from `std::true_type`. For any other type (unless user-specialized), this template is derived from `std::false_type`.
A program may specialize this template for a  `T` to implement *UnaryTypeTrait* with base characteristic of `std::true_type` to indicate that `T` should be treated by `std::bind` as if it were the type of a bind subexpression: when a bind-generated function object is invoked, a bound argument of this type will be invoked as a function object and will be given all the unbound arguments passed to the bind-generated object.

## Helper variable template

ddcl|since=c++17|1=
template< class T >
constexpr bool is_bind_expression_v = is_bind_expression<T>::value;

## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <type_traits>

struct MyBind
{
    typedef int result_type;
    int operator()(int a, int b) const { return a + b; }
};

namespace std
{
    template<>
    struct is_bind_expression<MyBind> : public true_type {};
}

int f(int n1, int n2)
{
    return n1 + n2;
}

int main()
{
    // as if bind(f, bind(MyBind(), _1, _2), 2)
    auto b = std::bind(f, MyBind(), 2); 

    std::cout << "Adding 2 to the sum of 10 and 11 gives " << b(10, 11) << '\n';
}
```


**Output:**
```
Adding 2 to the sum of 10 and 11 gives 23
```


## Defect reports


## See also


| cpp/utility/functional/dsc bind | (see dedicated page) |


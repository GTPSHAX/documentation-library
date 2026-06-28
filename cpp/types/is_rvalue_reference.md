---
title: std::is_rvalue_reference
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_rvalue_reference
---

cpp/types/traits/is|1=is_rvalue_reference
|description=
Checks whether `T` is an rvalue reference type. Provides the member constant `value` which is equal to `true`, if `T` is an rvalue reference type. Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is an rvalue reference type

## Possible implementation

eq fun
|1=
template<class T> struct is_rvalue_reference : std::false_type {};
template<class T> struct is_rvalue_reference<T&&> : std::true_type {};

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>

class A {};

static_assert
(
    std::is_rvalue_reference_v<A> == false and
    std::is_rvalue_reference_v<A&> == false and
    std::is_rvalue_reference_v<A&&> != false and
    std::is_rvalue_reference_v<char> == false and
    std::is_rvalue_reference_v<char&> == false and
    std::is_rvalue_reference_v<char&&> != false
);

template <typename T>
void test(T&& x)
{
    static_assert(std::is_same_v<T&&, decltype(x)>);
    std::cout << "T\t" << std::is_rvalue_reference<T>::value << '\n';
    std::cout << "T&&\t" << std::is_rvalue_reference<T&&>::value << '\n';
    std::cout << "decltype(x)\t" << std::is_rvalue_reference<decltype(x)>::value << '\n';
}

int main()
{
    std::cout << std::boolalpha;
    std::cout << "A\t" << std::is_rvalue_reference<A>::value << '\n';
    std::cout << "A&\t" << std::is_rvalue_reference<A&>::value << '\n';
    std::cout << "A&&\t" << std::is_rvalue_reference<A&&>::value << '\n';
    std::cout << "char\t" << std::is_rvalue_reference<char>::value << '\n';
    std::cout << "char&\t" << std::is_rvalue_reference<char&>::value << '\n';
    std::cout << "char&&\t" << std::is_rvalue_reference<char&&>::value << '\n';

    std::cout << "\ntest(42)\n";
    test(42);

    std::cout << "\ntest(x)\n";
    int x = 42;
    test(x);
}
```


**Output:**
```
A	false
A&	false
A&&	true
char	false
char&	false
char&&	true

test(42)
T	false
T&&	true
decltype(x)	true

test(x)
T	false
T&&	false
decltype(x)	false
```


## See also


| cpp/types/dsc is_lvalue_reference | (see dedicated page) |
| cpp/types/dsc is_reference | (see dedicated page) |


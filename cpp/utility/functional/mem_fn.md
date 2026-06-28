---
title: std::mem_fn
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/mem_fn
---

ddcl|header=functional|since=c++11|notes=<sup>(constexpr C++20)</sup>|1=
template< class M, class T >
/* unspecified */ mem_fn( M T::* pm ) noexcept;
Function template `std::mem_fn` generates wrapper objects for pointers to members, which can store, copy, and invoke a pointer to member. Both references and pointers (including smart pointers) to an object can be used when invoking a `std::mem_fn`.

## Parameters


### Parameters

- `pm` - pointer to member that will be wrapped

## Return value

`std::mem_fn` returns a call wrapper `fn` of unspecified type that has the following members:
member| ''return type''|2=
rrev|until=c++20|

## Member types


| Item | Description |
|------|-------------|
| **type** | definition |


## Member function


```cpp
dcla|constexpr=c++20|1=
template< class... Args >
/* see below */ operator()(Args&&... args) /* cvref-qualifiers */
noexcept(/* see below */);
```

The expression `fn(args)` is equivalent to , where `pmd` is the *Callable* object held by `fn`, it is of type `M T::*` and is direct-non-list-initialized with `pm`.
Thus, the return type of `operator()` is `std::result_of<decltype(pm)(Args&&...)>::type` <sup>(since C++17)</sup> or equivalently `std::invoke_result_t<decltype(pm), Args&&...>`, and the value in `noexcept` specifier is equal to `std::is_nothrow_invocable_v<decltype(pm), Args&&...>)`.
Each argument in `args` is perfectly forwarded, as if by `std::forward<Args>(args)...`.

## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <memory>

struct Foo
{
    void display_greeting()
    {
        std::cout << "Hello, world.\n";
    }

    void display_number(int i)
    {
        std::cout << "number: " << i << '\n';
    }

    int add_xy(int x, int y)
    {
        return data + x + y;
    }

    template<typename... Args> int add_many(Args... args)
    {
        return data + (args + ...);
    }

    auto add_them(auto... args) // C++20 required
    {
        return data + (args + ...);
    }

    int data = 7;
};

int main()
{
    auto f = Foo{};

    auto greet = std::mem_fn(&Foo::display_greeting);
    greet(f);

    auto print_num = std::mem_fn(&Foo::display_number);
    print_num(f, 42);

    auto access_data = std::mem_fn(&Foo::data);
    std::cout << "data: " << access_data(f) << '\n';

    auto add_xy = std::mem_fn(&Foo::add_xy);
    std::cout << "add_xy: " << add_xy(f, 1, 2) << '\n';

    auto u = std::make_unique<Foo>();
    std::cout << "access_data(u): " << access_data(u) << '\n';
    std::cout << "add_xy(u, 1, 2): " << add_xy(u, 1, 2) << '\n';

    auto add_many = std::mem_fn(&Foo::add_many<short, int, long>);
    std::cout << "add_many(u, ...): " << add_many(u, 1, 2, 3) << '\n';

    auto add_them = std::mem_fn(&Foo::add_them<short, int, float, double>);
    std::cout << "add_them(u, ...): " << add_them(u, 5, 7, 10.0f, 13.0) << '\n';
}
```


**Output:**
```
Hello, world.
number: 42
data: 7
add_xy: 10
access_data(u): 7
add_xy(u, 1, 2): 10
add_many(u, ...): 13
add_them(u, ...): 42
```


## Defect reports


## See also


| cpp/utility/functional/dsc function | (see dedicated page) |
| cpp/utility/functional/dsc move_only_function | (see dedicated page) |
| cpp/utility/functional/dsc bind | (see dedicated page) |


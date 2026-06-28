---
title: operators (std::function)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function/operator_cmp
---


# operator==


```cpp
**Header:** `<`functional`>`
dcl|since=c++11|num=1|1=
template< class R, class... ArgTypes >
bool operator==( const std::function<R(ArgTypes...)>& f,
std::nullptr_t ) noexcept;
dcl|since=c++11|until=c++20|num=2|1=
template< class R, class... ArgTypes >
bool operator==( std::nullptr_t,
const std::function<R(ArgTypes...)>& f ) noexcept;
dcl|since=c++11|until=c++20|num=3|1=
template< class R, class... ArgTypes >
bool operator!=( const std::function<R(ArgTypes...)>& f,
std::nullptr_t ) noexcept;
dcl|since=c++11|until=c++20|num=4|1=
template< class R, class... ArgTypes >
bool operator!=( std::nullptr_t,
const std::function<R(ArgTypes...)>& f ) noexcept;
```

Compares a `std::function` with a null pointer. Empty functions (that is, functions without a callable target) compare equal, non-empty functions compare non-equal.
rrev|since=c++20|

## Parameters


### Parameters

- `f` - `std::function` to compare

## Return value

@1,2@ `!f`
@3,4@ `(bool) f`

## Example


### Example

```cpp
#include <functional>
#include <iostream>

using SomeVoidFunc = std::function<void(int)>;

class C
{
public:
    C(SomeVoidFunc void_func = nullptr) : void_func_(void_func)
    {
        if (void_func_ == nullptr) // specialized compare with nullptr
            void_func_ = std::bind(&C::default_func, this, std::placeholders::_1);
        void_func_(7);
    }

    void default_func(int i) { std::cout << i << '\n'; };

private:
    SomeVoidFunc void_func_;
};

void user_func(int i)
{
    std::cout << (i + 1) << '\n';
}

int main()
{
    C c1;
    C c2(user_func);
}
```


**Output:**
```
7
8
```


## See also


| cpp/utility/functional/move_only_function/dsc operator{{== | (see dedicated page) |


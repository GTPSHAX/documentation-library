---
title: std::exchange
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/exchange
---

ddcl|header=utility|since=c++14|notes=<sup>(constexpr C++20)</sup><br>|1=
template< class T, class U = T >
T exchange( T& obj, U&& new_value );
Replaces the value of `obj` with `new_value` and returns the old value of `obj`.

## Parameters


### Parameters

- `obj` - object whose value to replace
- `new_value` - the value to assign to `obj`

**Type requirements:**

- `T`

## Return value

The old value of `obj`.

## Exceptions

rrev multi|since2=c++23
|rev1=(none)
|rev2=
noexcept|
std::is_nothrow_move_constructible_v<T> &&
std::is_nothrow_assignable_v<T&, U>

## Possible implementation

eq fun|1=
template<class T, class U = T>
constexpr // Since C++20
T exchange(T& obj, U&& new_value)
noexcept( // Since C++23
std::is_nothrow_move_constructible<T>::value &&
std::is_nothrow_assignable<T&, U>::value
)
{
T old_value = std::move(obj);
obj = std::forward<U>(new_value);
return old_value;
}

## Notes

`std::exchange` can be used when implementing s and, for the members that don't require special cleanup, move assignment operators:

```cpp
struct S
{
    int n;

    S(S&& other) noexcept : n{std::exchange(other.n, 0)} {}

    S& operator=(S&& other) noexcept
    {
        n = std::exchange(other.n, 0); // Move n, while leaving zero in other.n
        // Note: in case of self-move-assignment, n is unchanged
        // Also note: if n is an opaque resource handle that requires
        //            special cleanup, the resource is leaked.
        return *this;
    }
};
```


## Example


### Example

```cpp
#include <iostream>
#include <iterator>
#include <utility>
#include <vector>

class stream
{
public:
    using flags_type = int;

public:
    flags_type flags() const { return flags_; }

    // Replaces flags_ by newf, and returns the old value.
    flags_type flags(flags_type newf) { return std::exchange(flags_, newf); }

private:
    flags_type flags_ = 0;
};

void f() { std::cout << "f()"; }

int main()
{
    stream s;

    std::cout << s.flags() << '\n';
    std::cout << s.flags(12) << '\n';
    std::cout << s.flags() << "\n\n";

    std::vector<int> v;

    // Since the second template parameter has a default value, it is possible
    // to use a braced-init-list as second argument. The expression below
    // is equivalent to std::exchange(v, std::vector<int>{1, 2, 3, 4});

    std::exchange(v, {1, 2, 3, 4});

    std::copy(begin(v), end(v), std::ostream_iterator<int>(std::cout, ", "));

    std::cout << "\n\n";

    void (*fun)();

    // The default value of template parameter also makes possible to use a
    // normal function as second argument. The expression below is equivalent to
    // std::exchange(fun, static_cast<void(*)()>(f))
    std::exchange(fun, f);
    fun();

    std::cout << "\n\nFibonacci sequence: ";
    for (int a{0}, b{1}; a < 100; a = std::exchange(b, a + b))
        std::cout << a << ", ";
    std::cout << "...\n";
}
```


**Output:**
```
0
0
12

1, 2, 3, 4,

f()

Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
```


## See also


| cpp/algorithm/dsc swap | (see dedicated page) |
| cpp/atomic/dsc atomic_exchange | (see dedicated page) |


---
title: std::swap
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/swap
---


```cpp
**Header:** `<`algorithm|notes=
**Header:** `<`utility|notes=
**Header:** `<`string_view`>`
<br><sup>(constexpr C++20)</sup>|1=
template< class T >
void swap( T& a, T& b );
<br><sup>(constexpr C++20)</sup>|1=
template< class T2, std::size_t N >
void swap( T2 (&a)[N], T2 (&b)[N] );
```

Exchanges the given values.
1. Swaps the values `a` and `b`.
rrev|since=c++17|
.
2. Swaps the arrays `a` and `b`. Equivalent to `std::swap_ranges(a, a + N, b)`.
rrev|since=c++17|
.

## Parameters


### Parameters

- `a, b` - the values to be swapped

**Type requirements:**

- `T2`

## Return value

(none)

## Exceptions

1. rrev multi|until1=c++11
|rev1=(none)
|rev2=
noexcept|
std::is_nothrow_move_constructible<T>::value &&
std::is_nothrow_move_assignable<T>::value
2. rrev multi|since1=c++11|rev1=
The lookup for the identifier `swap` in the exception specification finds this function template in addition to anything found by the usual lookup rules, making the exception specification equivalent to C++17 `std::is_nothrow_swappable`.
|since2=c++17|rev2=

## Complexity

1. Constant.
2. Linear in `N`.

## Specializations

rrev|until=c++20|
`std::swap` may be specialized in namespace std for program-defined types, but such specializations are not found by ADL (the namespace std is not the associated namespace for the program-defined type).
The expected way to make a  swappable is to provide a non-member function swap in the same namespace as the type: see *Swappable* for details.
The following overloads are already provided by the standard library:


| cpp/utility/pair/dsc swap2 | (see dedicated page) |
| cpp/utility/tuple/dsc swap2 | (see dedicated page) |
| cpp/memory/shared_ptr/dsc swap2 | (see dedicated page) |
| cpp/memory/weak_ptr/dsc swap2 | (see dedicated page) |
| cpp/memory/unique_ptr/dsc swap2 | (see dedicated page) |
| cpp/utility/functional/function/dsc swap2 | (see dedicated page) |
| cpp/string/basic_string/dsc swap2 | (see dedicated page) |
| cpp/container/dsc swap2|array | (see dedicated page) |
| cpp/container/dsc swap2|deque | (see dedicated page) |
| cpp/container/dsc swap2|forward_list | (see dedicated page) |
| cpp/container/dsc swap2|list | (see dedicated page) |
| cpp/container/dsc swap2|vector | (see dedicated page) |
| cpp/container/dsc swap2|map | (see dedicated page) |
| cpp/container/dsc swap2|multimap | (see dedicated page) |
| cpp/container/dsc swap2|set | (see dedicated page) |
| cpp/container/dsc swap2|multiset | (see dedicated page) |
| cpp/container/dsc swap2|unordered_map | (see dedicated page) |
| cpp/container/dsc swap2|unordered_multimap | (see dedicated page) |
| cpp/container/dsc swap2|unordered_set | (see dedicated page) |
| cpp/container/dsc swap2|unordered_multiset | (see dedicated page) |
| cpp/container/dsc swap2|queue | (see dedicated page) |
| cpp/container/dsc swap2|priority_queue | (see dedicated page) |
| cpp/container/dsc swap2|stack | (see dedicated page) |
| cpp/numeric/valarray/dsc swap2 | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc swap2 | (see dedicated page) |
| cpp/io/basic_stringstream/dsc swap2|basic_istringstream | (see dedicated page) |
| cpp/io/basic_stringstream/dsc swap2|basic_ostringstream | (see dedicated page) |
| cpp/io/basic_stringstream/dsc swap2|basic_stringstream | (see dedicated page) |
| cpp/io/basic_filebuf/dsc swap2 | (see dedicated page) |
| cpp/io/basic_fstream/dsc swap2|basic_ifstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc swap2|basic_ofstream | (see dedicated page) |
| cpp/io/basic_fstream/dsc swap2|basic_fstream | (see dedicated page) |
| cpp/io/basic_syncbuf/dsc swap2 | (see dedicated page) |
| cpp/io/basic_spanbuf/dsc swap2 | (see dedicated page) |
| cpp/io/basic_spanstream/dsc swap2|basic_ispanstream | (see dedicated page) |
| cpp/io/basic_spanstream/dsc swap2|basic_ospanstream | (see dedicated page) |
| cpp/io/basic_spanstream/dsc swap2|basic_spanstream | (see dedicated page) |
| cpp/regex/basic_regex/dsc swap2 | (see dedicated page) |
| cpp/regex/match_results/dsc swap2 | (see dedicated page) |
| cpp/thread/thread/dsc swap2|thread | (see dedicated page) |
| cpp/thread/unique_lock/dsc swap2 | (see dedicated page) |
| cpp/thread/shared_lock/dsc swap2 | (see dedicated page) |
| cpp/thread/promise/dsc swap2 | (see dedicated page) |
| cpp/thread/packaged_task/dsc swap2 | (see dedicated page) |
| cpp/utility/optional/dsc swap2 | (see dedicated page) |
| cpp/utility/any/dsc swap2 | (see dedicated page) |
| cpp/utility/variant/dsc swap2 | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc swap2 | (see dedicated page) |
| cpp/filesystem/path/dsc swap2 | (see dedicated page) |
| cpp/utility/expected/dsc swap2 | (see dedicated page) |
| cpp/thread/thread/dsc swap2|jthread | (see dedicated page) |
| cpp/utility/functional/move_only_function/dsc swap2 | (see dedicated page) |
| cpp/thread/stop_source/dsc swap2 | (see dedicated page) |
| cpp/thread/stop_token/dsc swap2 | (see dedicated page) |
| <!--TODOs: | |
| swap(std::flat_map) | |
| swap(std::flat_set) | |
| swap(std::flat_multimap) | |
| swap(std::flat_multiset) | |
| swap(std::unexpected) | |
| swap(std::mdspan) | |
| --> | |


## Example


### Example

```cpp
#include <algorithm>
#include <iostream>

namespace Ns
{
    class A
    {
        int id {};

        friend void swap(A& lhs, A& rhs)
        {
            std::cout << "swap(" << lhs << ", " << rhs << ")\n";
            std::swap(lhs.id, rhs.id);
        }

        friend std::ostream& operator<<(std::ostream& os, A const& a)
        {
            return os << "A::id=" << a.id;
        }

    public:
        A(int i) : id {i} {}
        A(A const&) = delete;
        A& operator = (A const&) = delete;
    };
}

int main()
{
    int a = 5, b = 3;
    std::cout << a << ' ' << b << '\n';
    std::swap(a, b);
    std::cout << a << ' ' << b << '\n';

    Ns::A p {6}, q {9};
    std::cout << p << ' ' << q << '\n';
//  std::swap(p, q); // error, type requirements are not satisfied
    swap(p, q);      // OK, ADL finds the appropriate friend `swap`
    std::cout << p << ' ' << q << '\n';
}
```


**Output:**
```
5 3
3 5
A::id=6 A::id=9
swap(A::id=6, A::id=9)
A::id=9 A::id=6
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-809 | C++98 | arrays could not be swapped | added overload v |


## See also


| cpp/utility/ranges/dsc swap | (see dedicated page) |
| cpp/algorithm/dsc iter_swap | (see dedicated page) |
| cpp/algorithm/dsc swap_ranges | (see dedicated page) |
| cpp/utility/dsc exchange | (see dedicated page) |


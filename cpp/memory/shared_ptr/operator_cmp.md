---
title: operators (<=>)
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/shared_ptr/operator_cmp
---


# 1=operator==, !=, <, <=, >, >=, <=> <small>(std::shared_ptr)</small>


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++11|constexpr=c++26|1=
template< class T, class U >
bool operator==( const std::shared_ptr<T>& lhs,
const std::shared_ptr<U>& rhs ) noexcept;
dcl|num=2|since=c++11|until=c++20|1=
template< class T, class U >
bool operator!=( const std::shared_ptr<T>& lhs,
const std::shared_ptr<U>& rhs ) noexcept;
dcl|num=3|since=c++11|until=c++20|1=
template< class T, class U >
bool operator<( const std::shared_ptr<T>& lhs,
const std::shared_ptr<U>& rhs ) noexcept;
dcl|num=4|since=c++11|until=c++20|1=
template< class T, class U >
bool operator>( const std::shared_ptr<T>& lhs,
const std::shared_ptr<U>& rhs ) noexcept;
dcl|num=5|since=c++11|until=c++20|1=
template< class T, class U >
bool operator<=( const std::shared_ptr<T>& lhs,
const std::shared_ptr<U>& rhs ) noexcept;
dcl|num=6|since=c++11|until=c++20|1=
template< class T, class U >
bool operator>=( const std::shared_ptr<T>& lhs,
const std::shared_ptr<U>& rhs ) noexcept;
dcla|num=7|since=c++20|constexpr=c++26|1=
template< class T, class U >
std::strong_ordering operator<=>( const std::shared_ptr<T>& lhs,
const std::shared_ptr<U>& rhs ) noexcept;
dcla|num=8|since=c++11|constexpr=c++26|1=
template< class T >
bool operator==( const std::shared_ptr<T>& lhs, std::nullptr_t ) noexcept;
dcl|num=9|since=c++11|until=c++20|1=
template< class T >
bool operator==( std::nullptr_t, const std::shared_ptr<T>& rhs ) noexcept;
dcl|num=10|since=c++11|until=c++20|1=
template< class T >
bool operator!=( const std::shared_ptr<T>& lhs, std::nullptr_t ) noexcept;
dcl|num=11|since=c++11|until=c++20|1=
template< class T >
bool operator!=( std::nullptr_t, const std::shared_ptr<T>& rhs ) noexcept;
dcl|num=12|since=c++11|until=c++20|1=
template< class T >
bool operator<( const std::shared_ptr<T>& lhs, std::nullptr_t ) noexcept;
dcl|num=13|since=c++11|until=c++20|1=
template< class T >
bool operator<( std::nullptr_t, const std::shared_ptr<T>& rhs ) noexcept;
dcl|num=14|since=c++11|until=c++20|1=
template< class T >
bool operator>( const std::shared_ptr<T>& lhs, std::nullptr_t ) noexcept;
dcl|num=15|since=c++11|until=c++20|1=
template< class T >
bool operator>( std::nullptr_t, const std::shared_ptr<T>& rhs ) noexcept;
dcl|num=16|since=c++11|until=c++20|1=
template< class T >
bool operator<=( const std::shared_ptr<T>& lhs, std::nullptr_t ) noexcept;
dcl|num=17|since=c++11|until=c++20|1=
template< class T >
bool operator<=( std::nullptr_t, const std::shared_ptr<T>& rhs ) noexcept;
dcl|num=18|since=c++11|until=c++20|1=
template< class T >
bool operator>=( const std::shared_ptr<T>& lhs, std::nullptr_t ) noexcept;
dcl|num=19|since=c++11|until=c++20|1=
template< class T >
bool operator>=( std::nullptr_t, const std::shared_ptr<T>& rhs ) noexcept;
dcla|num=20|since=c++20|constexpr=c++26|1=
template< class T >
std::strong_ordering operator<=>( const std::shared_ptr<T>& lhs,
std::nullptr_t ) noexcept;
```

Compares two `shared_ptr<T>` objects or compares `shared_ptr<T>` with a null pointer.
Note that the comparison operators for `shared_ptr` simply compare pointer values; the actual objects pointed to are ''not'' compared.  Having `operator<` defined for `shared_ptr` allows `shared_ptr`s to be used as keys in associative containers, like `std::map` and `std::set`.
rrev|since=c++20|

## Parameters


### Parameters

- `lhs` - the left-hand `shared_ptr` to compare
- `rhs` - the right-hand `shared_ptr` to compare

## Return value

1. `lhs.get()
2. `1=!(lhs == rhs)`
3. `std::less<V>()(lhs.get(), rhs.get())`, where V is the composite pointer type of `std::shared_ptr<T>::element_type*` and `std::shared_ptr<U>::element_type*`.
4. `rhs < lhs`
5. `!(rhs < lhs)`
6. `!(lhs < rhs)`
7. }
8. `!lhs`
9. `!rhs`
10. `(bool)lhs`
11. `(bool)rhs`
12. `std::less<std::shared_ptr<T>::element_type*>()(lhs.get(), nullptr)`
13. `std::less<std::shared_ptr<T>::element_type*>()(nullptr, rhs.get())`
14. `nullptr < lhs`
15. `rhs < nullptr`
16. `!(nullptr < lhs)`
17. `!(rhs < nullptr)`
18. `!(lhs < nullptr)`
19. `!(nullptr < rhs)`
20. }

## Notes

In all cases, it is the stored pointer (the one returned by `get()`) that is compared, rather than the managed pointer (the one passed to the deleter when `use_count` goes to zero). The two pointers may differ in a `std::shared_ptr|shared_ptr` created using the aliasing constructor.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

int main()
{
    std::shared_ptr<int> p1(new int(42));
    std::shared_ptr<int> p2(new int(42));

    std::cout << std::boolalpha
        << "(p1 == p1)       : " << (p1 == p1) << '\n'
        << "(p1 <=> p1) == 0 : " << ((p1 <=> p1) == 0) << '\n' // Since C++20

    // p1 and p2 point to different memory locations, so p1 != p2
        << "(p1 == p2)       : " << (p1 == p2) << '\n'
        << "(p1 < p2)        : " << (p1 < p2) << '\n'
        << "(p1 <=> p2) < 0  : " << ((p1 <=> p2) < 0) << '\n'   // Since C++20
        << "(p1 <=> p2) == 0 : " << ((p1 <=> p2) == 0) << '\n'; // Since C++20
}
```


**Output:**
```
(p1 == p1)       : true
(p1 <=> p1) == 0 : true
(p1 == p2)       : false
(p1 < p2)        : true
(p1 <=> p2) < 0  : true
(p1 <=> p2) == 0 : false
```


## Defect reports


## See also


| cpp/memory/shared_ptr/dsc get | (see dedicated page) |


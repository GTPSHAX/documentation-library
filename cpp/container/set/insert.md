---
title: std::set::insert
type: Containers
source: https://en.cppreference.com/w/cpp/container/set/insert
---


```cpp
dcl|num=1|
std::pair<iterator, bool> insert( const value_type& value );
dcl|num=2|since=c++11|
std::pair<iterator, bool> insert( value_type&& value );
dcl rev multi|num=3|anchor=3|until1=c++11
|dcl1=
iterator insert( iterator pos, const value_type& value );
|dcl2=
iterator insert( const_iterator pos, const value_type& value );
dcl|num=4|since=c++11|
iterator insert( const_iterator pos, value_type&& value );
dcla|num=5|
template< class InputIt >
void insert( InputIt first, InputIt last );
dcl|num=6|since=c++11|
void insert( std::initializer_list<value_type> ilist );
dcl|num=7|since=c++17|
insert_return_type insert( node_type&& nh );
dcl|num=8|since=c++17|
iterator insert( const_iterator pos, node_type&& nh );
dcla|num=9|since=c++23|
template< class K >
std::pair<iterator, bool> insert( K&& x );
dcl|num=10|since=c++23|
template< class K >
iterator insert( const_iterator pos, K&& x );
```

Inserts element(s) into the container, if the container doesn't already contain an element with an equivalent key.
@1,2@ Inserts `value`.
@3,4@ Inserts `value` in the position as close as possible to the position just prior to `pos`.
5. Inserts elements from range [first, last).
6. Inserts elements from initializer list `ilist`.
9. If `*this` already contains an element which transparently compares ''equivalent'' to `x`, does nothing. Otherwise, constructs an object `u` of the `value_type` with `std::forward<K>(x)` and then inserts `u` into `*this`. If `1=equal_range(u) == equal_range(x)` is `false`, the behavior is undefined. The `value_type` must be *EmplaceConstructible* into `set` from `std::forward<K>(x)`.
10. If `*this` already contains an element which transparently compares ''equivalent'' to `x`, does nothing. Otherwise, constructs an object `u` of the `value_type` with `std::forward<K>(x)` and then inserts `u` into `*this` in the position as close as possible to the position just prior to `pos`. If `1=equal_range(u) == equal_range(x)` is `false`, the behavior is undefined. The `value_type` must be *EmplaceConstructible* into `set` from `std::forward<K>(x)`. This overload participates in overload resolution only if:
* `std::is_convertible_v<K&&, const_iterator>` and `std::is_convertible_v<K&&, iterator>` are both `false`, and
* the qualified-id `Compare::is_transparent` is valid and denotes a type,
which together allows calling this function without constructing an instance of `Key`.

## Parameters


### Parameters

- `pos` - iterator to the position before which the new element will be inserted
- `value` - element value to insert
- `[3=to insert, range=source}})` - 
- `ilist` - initializer list to insert the values from
- `nh` - a compatible 
- `x` - a value of any type that can be transparently compared with a key

**Type requirements:**

- `InputIt`

## Return value

@1,2@
@3,4@
@5,6@ (none)
9.
10.

## Exceptions

@1-4@ If an exception is thrown by any operation, the insertion has no effect.

## Complexity

@1,2@ Logarithmic in the size of the container, `O(log(size()))`.
@3,4@ Amortized constant if the insertion happens in the position just <sup>(until C++11)</sup> ''after''<sup>(since C++11)</sup> ''before'' `pos`, logarithmic in the size of the container otherwise.
@5,6@ `O(N&middot;log(size() + N))`, where `N` is the number of elements to insert.
7. Logarithmic in the size of the container, `O(log(size()))`.
8. Amortized constant if the insertion happens in the position just ''before'' `pos`, logarithmic in the size of the container otherwise.
9. Logarithmic in the size of the container, `O(log(size()))`.
10. Amortized constant if the insertion happens in the position just ''before'' `pos`, logarithmic in the size of the container otherwise.

## Notes

The overloads  are often implemented as a loop that calls the overload  with `end()` as the hint; they are optimized for appending a sorted sequence (such as another `std::set`) whose smallest element is greater than the last element in `*this`.

## Example


### Example

```cpp
#include <cassert>
#include <iostream>
#include <set>

int main()
{
    std::set<int> set;

    auto result_1 = set.insert(3);
    assert(result_1.first != set.end()); // it is a valid iterator
    assert(*result_1.first == 3);
    if (result_1.second)
        std::cout << "insert done\n";

    auto result_2 = set.insert(3);
    assert(result_2.first == result_1.first); // same iterator
    assert(*result_2.first == 3);
    if (!result_2.second)
        std::cout << "no insertion\n";
}
```


**Output:**
```
insert done
no insertion
```


## Defect reports


## See also


| cpp/container/dsc emplace|set | (see dedicated page) |
| cpp/container/dsc emplace_hint|set | (see dedicated page) |
| cpp/iterator/dsc inserter | (see dedicated page) |


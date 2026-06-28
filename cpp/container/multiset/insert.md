---
title: std::multiset::insert
type: Containers
source: https://en.cppreference.com/w/cpp/container/multiset/insert
---


```cpp
dcl|num=1|
iterator insert( const value_type& value );
dcl|num=2|since=c++11|
iterator insert( value_type&& value );
dcl rev multi|num=3|until1=c++11
|dcl1=
iterator insert( iterator pos, const value_type& value );
|dcl2=
iterator insert( const_iterator pos, const value_type& value );
dcl|num=4|since=c++11|
iterator insert( const_iterator pos, value_type&& value );
dcl|num=5|
template< class InputIt >
void insert( InputIt first, InputIt last );
dcl|num=6|since=c++11|
void insert( std::initializer_list<value_type> ilist );
dcl|num=7|since=c++17|
iterator insert( node_type&& nh );
dcl|num=8|since=c++17|
iterator insert( const_iterator pos, node_type&& nh );
```

Inserts element(s) into the container. The order of the remaining equivalent elements is preserved.
@1,2@ Inserts `value`. If the container has elements with equivalent key, inserts at the upper bound of that range.
@3,4@ Inserts `value` in the position as close as possible to the position just prior to `pos`.
5. Inserts elements from range [first, last).
6. Inserts elements from initializer list `ilist`.

## Parameters


### Parameters

- `pos` - iterator to the position before which the new element will be inserted
- `value` - element value to insert
- `[3=to insert, range=source}})` - 
- `ilist` - initializer list to insert the values from
- `nh` - a compatible node handle

**Type requirements:**

- `InputIt`

## Return value

@1-4@ An iterator to the inserted element.
@5,6@ (none)

## Exceptions

@1-4,7,8@ If an exception is thrown by any operation, the insertion has no effect.
@5,6@ No exception safety guarantee.

## Complexity

@1,2,7@ `O(log(size()))`
@3,4,8@ Amortized constant if the insertion happens in the position just before `pos`, `O(log(size()))` otherwise.
@5,6@ `O(N&middot;log(size() + N))`, where `N` is the number of elements to insert.

## Example


## See also


| cpp/container/dsc emplace|multiset | (see dedicated page) |
| cpp/container/dsc emplace_hint|multiset | (see dedicated page) |
| cpp/iterator/dsc inserter | (see dedicated page) |


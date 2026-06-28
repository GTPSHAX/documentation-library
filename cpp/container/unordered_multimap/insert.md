---
title: std::unordered_multimap::insert
type: Containers
source: https://en.cppreference.com/w/cpp/container/unordered_multimap/insert
---


```cpp
**Header:** `<`unordered_map`>`
dcl|num=1|since=c++11|
iterator insert( const value_type& value );
dcl|num=2|since=c++17|
iterator insert( value_type&& value );
dcl|num=3|since=c++11|
template< class P >
iterator insert( P&& value );
dcl|num=4|since=c++11|
iterator insert( const_iterator hint, const value_type& value );
dcl|num=5|since=c++17|
iterator insert( const_iterator hint, value_type&& value );
dcl|num=6|since=c++11|
template< class P >
iterator insert( const_iterator hint, P&& value );
dcl|num=7|since=c++11|
template< class InputIt >
void insert( InputIt first, InputIt last );
dcl|num=8|since=c++11|
void insert( std::initializer_list<value_type> ilist );
dcl|num=9|since=c++17|
iterator insert( node_type&& nh );
dcl|num=10|since=c++17|
iterator insert( const_iterator hint, node_type&& nh );
```

Inserts element(s) into the container.
@1-3@ Inserts `value`.
@@ Overload  is equivalent to `emplace(std::forward<P>(value))` and only participates in overload resolution if `1=std::is_constructible<value_type, P&&>::value == true`.
@4-6@ Inserts `value`, using `hint` as a non-binding suggestion to where the search should start.
@@ Overload  is equivalent to `emplace_hint(hint, std::forward<P>(value))` and only participates in overload resolution if `1=std::is_constructible<value_type, P&&>::value == true`.
7. Inserts elements from range [first, last).
@@ If [first, last) is not a valid range, or `first` and/or `last` are iterators into `*this`, the behavior is undefined.
8. Inserts elements from initializer list `ilist`.

## Parameters


### Parameters

- `hint` - iterator, used as a suggestion as to where to insert the content
- `value` - element value to insert
- `[3=to insert, range=source}})` - 
- `ilist` - initializer list to insert the values from
- `nh` - a compatible node handle

**Type requirements:**

- `InputIt`

## Return value

@1-6@ An iterator to the inserted element.
@7,8@ (none)

## Exceptions

@1-6@
@7,8@ No exception safety guarantee.
@9,10@

## Complexity

@1-6@ Average case: `O(1)`, worst case `O(size())`.
@7,8@ Average case: `O(N)`, where N is the number of elements to insert. Worst case: `O(N * size() + N)`.
@9,10@ Average case: `O(1)`, worst case `O(size())`.

## Example


## See also


| cpp/container/dsc emplace|unordered_multimap | (see dedicated page) |
| cpp/container/dsc emplace_hint|unordered_multimap | (see dedicated page) |
| cpp/iterator/dsc inserter | (see dedicated page) |


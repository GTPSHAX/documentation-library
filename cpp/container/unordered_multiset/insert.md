---
title: std::unordered_multiset::insert
type: Containers
source: https://en.cppreference.com/w/cpp/container/unordered_multiset/insert
---


```cpp
dcl|num=1|since=c++11|
iterator insert( const value_type& value );
dcl|num=2|since=c++11|
iterator insert( value_type&& value );
dcl|num=3|since=c++11|
iterator insert( const_iterator hint, const value_type& value );
dcl|num=4|since=c++11|
iterator insert( const_iterator hint, value_type&& value );
dcl|num=5|since=c++11|
template< class InputIt >
void insert( InputIt first, InputIt last );
dcl|num=6|since=c++11|
void insert( std::initializer_list<value_type> ilist );
dcl|num=7|since=c++17|
iterator insert( node_type&& nh );
dcl|num=8|since=c++17|
iterator insert( const_iterator hint, node_type&& nh );
```

Inserts element(s) into the container.
@1,2@ Inserts `value`.
@3,4@ Inserts `value`, using `hint` as a non-binding suggestion to where the search should start.
5. Inserts elements from range [first, last).
6. Inserts elements from initializer list `ilist`.

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

@1-4@ An iterator to the inserted element.
@5,6@ (none)

## Exceptions

@1-4@ If an exception is thrown by any operation, the insertion has no effect.

## Complexity

@1-4@ Average case: `O(1)`, worst case `O(size())`.
@5,6@ Average case: `O(N)`, where N is the number of elements to insert. Worst case: `O(N * size() + N)`.
@7,8@ Average case: `O(1)`, worst case `O(size())`.

## Example


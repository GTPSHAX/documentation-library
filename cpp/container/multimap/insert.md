---
title: std::multimap::insert
type: Containers
source: https://en.cppreference.com/w/cpp/container/multimap/insert
---


```cpp
dcl|num=1|
iterator insert( const value_type& value );
dcl|num=2|since=c++17|
iterator insert( value_type&& value );
dcl|num=3|since=c++11|
template< class P >
iterator insert( P&& value );
dcl rev multi|num=4|until1=c++11
|dcl1=
iterator insert( iterator pos, const value_type& value );
|dcl2=
iterator insert( const_iterator pos, const value_type& value );
dcl|num=5|since=c++17|
iterator insert( const_iterator pos, value_type&& value );
dcl|num=6|since=c++11|
template< class P >
iterator insert( const_iterator pos, P&& value );
dcl|num=7|
template< class InputIt >
void insert( InputIt first, InputIt last );
dcl|num=8|since=c++11|
void insert( std::initializer_list<value_type> ilist );
dcl|num=9|since=c++17|
iterator insert( node_type&& nh );
dcl|num=10|since=c++17|
iterator insert( const_iterator pos, node_type&& nh );
```

Inserts element(s) into the container.
@1-3@ Inserts `value`. If the container has elements with equivalent key, inserts at the upper bound of that range.
@@ Overload  is equivalent to `emplace(std::forward<P>(value))` and only participates in overload resolution if `1=std::is_constructible<value_type, P&&>::value == true`.
@4-6@ Inserts `value` in the position as close as possible to the position just prior to `pos`.
@@ Overload  is equivalent to `emplace_hint(hint, std::forward<P>(value))` and only participates in overload resolution if `1=std::is_constructible<value_type, P&&>::value == true`.
7. Inserts elements from range [first, last).
8. Inserts elements from initializer list `ilist`.

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

@1-6@ An iterator to the inserted element.
@7,8@ (none)

## Exceptions

@1-6@ If an exception is thrown by any operation, the insertion has no effect.
@7,8@ No exception safety guarantee.
@9,10@ If an exception is thrown by any operation, the insertion has no effect.

## Complexity

@1-3@ `O(log(size()))`
@4-6@ Amortized constant if the insertion happens in the position just before `pos`, `O(log(size()))` otherwise.
@7,8@ `O(N&middot;log(size() + N))`, where `N` is the number of elements to insert.
9. `O(log(size()))`
10. Amortized constant if the insertion happens in the position just before `pos`, `O(log(size()))` otherwise.

## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <map>
#include <string>
#include <string_view>
#include <utility>

template<class M>
void print(const std::string_view rem, const M& mmap)
{
    std::cout << rem << ' ';
    for (const auto& e : mmap)
        std::cout << '{' << e.first << ',' << e.second << "} ";
    std::cout << '\n';
}

int main()
{
    // list-initialize
    std::multimap<int, std::string, std::greater<int>> mmap
        {{2, "foo"}, {2, "bar"}, {3, "baz"}, {1, "abc"}, {5, "def"
```

print("#1", mmap);
// insert using value_type
mmap.insert(decltype(mmap)::value_type(5, "pqr"));
print("#2", mmap);
// insert using pair
mmap.insert(std::pair{6, "uvw"});
print("#3", mmap);
mmap.insert({7, "xyz"});
print("#4", mmap);
// insert using initializer_list
mmap.insert(5, "one"}, {5, "two");
print("#5", mmap);
// insert using a pair of iterators
mmap.clear();
const auto il = {std::pair{1, "ä"}, {2, "ё"}, {2, "ö"}, {3, "ü";
mmap.insert(il.begin(), il.end());
print("#6", mmap);
}
|output=
#1 {5,def} {3,baz} {2,foo} {2,bar} {1,abc}
#2 {5,def} {5,pqr} {3,baz} {2,foo} {2,bar} {1,abc}
#3 {6,uvw} {5,def} {5,pqr} {3,baz} {2,foo} {2,bar} {1,abc}
#4 {7,xyz} {6,uvw} {5,def} {5,pqr} {3,baz} {2,foo} {2,bar} {1,abc}
#5 {7,xyz} {6,uvw} {5,def} {5,pqr} {5,one} {5,two} {3,baz} {2,foo} {2,bar} {1,abc}
#6 {3,ü} {2,ё} {2,ö} {1,ä}

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-371 | C++98 | the order of equivalent elements<br>was not guaranteed to be preserved | required to be preserved |


## See also


| cpp/container/dsc emplace|multimap | (see dedicated page) |
| cpp/container/dsc emplace_hint|multimap | (see dedicated page) |
| cpp/iterator/dsc inserter | (see dedicated page) |


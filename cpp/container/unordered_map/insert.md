---
title: std::unordered_map::insert
type: Containers
source: https://en.cppreference.com/w/cpp/container/unordered_map/insert
---


```cpp
dcl|num=1|since=c++11|
std::pair<iterator, bool> insert( const value_type& value );
dcl|num=2|since=c++17|
std::pair<iterator, bool> insert( value_type&& value );
dcl|num=3|since=c++11|
template< class P >
std::pair<iterator, bool> insert( P&& value );
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
insert_return_type insert( node_type&& nh );
dcl|num=10|since=c++17|
iterator insert( const_iterator hint, node_type&& nh );
```

Inserts element(s) into the container, if the container doesn't already contain an element with an equivalent key.
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

@1-3@
@4-6@
@7,8@ (none)

## Exceptions

@1-6@
@7,8@ No exception safety guarantee.
@9,10@

## Complexity

@1-6@ Average case: `O(1)`, worst case `O(size())`.
@7,8@ Average case: `O(N)`, where N is the number of elements to insert. Worst case: `O(N * size() + N)`.
@9,10@ Average case: `O(1)`, worst case `O(size())`.

## Notes


## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int main ()
{
    std::unordered_map<int, std::string> dict = {<!---->{1, "one"}, {2, "two"}<!---->};
    dict.insert({3, "three"});
    dict.insert(std::make_pair(4, "four"));
    dict.insert({<!---->{4, "another four"}, {5, "five"}<!---->});

    const bool ok = dict.insert({1, "another one"}).second;
    std::cout << "inserting 1 => \"another one\" "
              << (ok ? "succeeded" : "failed") << '\n';

    std::cout << "contents:\n";
    for (auto& p : dict)
        std::cout << ' ' << p.first << " => " << p.second << '\n';
}
```


**Output:**
```
inserting 1 => "another one" failed
contents:
 5 => five
 1 => one
 2 => two
 3 => three
 4 => four
```


## Defect reports


## See also


| cpp/container/dsc emplace|unordered_map | (see dedicated page) |
| cpp/container/dsc emplace_hint|unordered_map | (see dedicated page) |
| cpp/container/dsc insert_or_assign|unordered_map | (see dedicated page) |
| cpp/iterator/dsc inserter | (see dedicated page) |


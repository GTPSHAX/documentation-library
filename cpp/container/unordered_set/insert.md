---
title: std::unordered_set::insert
type: Containers
source: https://en.cppreference.com/w/cpp/container/unordered_set/insert
---


```cpp
dcl|num=1|since=c++11|
std::pair<iterator,bool> insert( const value_type& value );
dcl|num=2|since=c++11|
std::pair<iterator,bool> insert( value_type&& value );
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
insert_return_type insert( node_type&& nh );
dcl|num=8|since=c++17|
iterator insert( const_iterator hint, node_type&& nh );
dcla|num=9|since=c++23|
template< class K >
std::pair<iterator, bool> insert( K&& obj );
dcl|num=10|since=c++23|
template< class K >
iterator insert( const_iterator hint, K&& obj );
```

Inserts element(s) into the container, if the container doesn't already contain an element with an equivalent key.
@1,2@ Inserts `value`.
@3,4@ Inserts `value`, using `hint` as a non-binding suggestion to where the search should start.
5. Inserts elements from range [first, last).
6. Inserts elements from initializer list `ilist`.
9. If `*this` already contains an element which transparently compares ''equivalent'' to `obj`, does nothing. Otherwise, constructs an object `u` of `value_type` with `std::forward<K>(obj)` and then inserts `u` into `*this`. If `1=equal_range(u) != hash_function()(obj)  is `true`, the behavior is undefined. The `value_type` must be *EmplaceConstructible* into `unordered_set` from `std::forward<K>(obj)`.
10. If `*this` already contains an element which transparently compares ''equivalent'' to `obj`, does nothing.
Otherwise, constructs an object `u` of `value_type` with `std::forward<K>(obj)` and then inserts `u` into `*this`.  is used as a non-binding suggestion to where the search should start. If `1=equal_range(u) != hash_function()(obj)  is `true`, the behavior is undefined.
The `value_type` must be *EmplaceConstructible* into `unordered_set` from `std::forward<K>(obj)`. This overload participates in overload resolution only if:
* `std::is_convertible_v<K&&, const_iterator>` and `std::is_convertible_v<K&&, iterator>` are both `false`, and
* `Hash::is_transparent` and `KeyEqual::is_transparent` are valid and each denotes a type. This assumes that such `Hash` is callable with both `K` and `Key` type, and that the `KeyEqual` is transparent,
which, together, allows calling this function without constructing an instance of `Key`.

## Parameters


### Parameters

- `hint` - iterator, used as a suggestion as to where to insert the content
- `value` - element value to insert
- `[3=to insert, range=source}})` - 
- `ilist` - initializer list to insert the values from
- `nh` - a compatible node handle
- `obj` - a value of any type that can be transparently compared with a key

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

@1-4@ Average case: `O(1)`, worst case `O(size())`.
@5,6@ Average case: `O(N)`, where N is the number of elements to insert. Worst case: `O(N * size() + N)`.
@7-10@ Average case: `O(1)`, worst case `O(size())`.

## Notes


## Example


### Example

```cpp
#include <array>
#include <iostream>
#include <unordered_set>

std::ostream& operator<<(std::ostream& os, std::unordered_set<int> const& s)
{
    for (os << '[' << s.size() << "] { "; int i : s)
        os << i << ' ';
    return os << "}\n";
}

int main ()
{
    std::unordered_set<int> nums{2, 3, 4};

    std::cout << "1) Initially: " << nums << std::boolalpha;
    auto p = nums.insert(1); // insert element, overload (1)
    std::cout << "2) '1' was inserted: " << p.second << '\n';
    std::cout << "3) After insertion: " << nums;

    nums.insert(p.first, 0); // insert with hint, overload (3)
    std::cout << "4) After insertion: " << nums;

    std::array<int, 4> a = {10, 11, 12, 13};
    nums.insert(a.begin(), a.end()); // insert range, overload (5)
    std::cout << "5) After insertion: " << nums;

    nums.insert({20, 21, 22, 23}); // insert initializer_list, (6)
    std::cout << "6) After insertion: " << nums;

    std::unordered_set<int> other_nums = {42, 43};
    auto node = other_nums.extract(other_nums.find(42));
    nums.insert(std::move(node)); // insert node, overload (7)
    std::cout << "7) After insertion: " << nums;

    node = other_nums.extract(other_nums.find(43));
    nums.insert(nums.begin(), std::move(node)); // insert node with hint, (8)
    std::cout << "8) After insertion: " << nums;
}
```


**Output:**
```
1) Initially: [3] { 4 3 2 }
2) '1' was inserted: true
3) After insertion: [4] { 1 2 3 4 }
4) After insertion: [5] { 0 1 2 3 4 }
5) After insertion: [9] { 13 12 11 10 4 3 2 1 0 }
6) After insertion: [13] { 23 22 13 12 11 10 21 4 20 3 2 1 0 }
7) After insertion: [14] { 42 23 22 13 12 11 10 21 4 20 3 2 1 0 }
8) After insertion: [15] { 43 42 23 22 13 12 11 10 21 4 20 3 2 1 0 }
```


## See also


| cpp/container/dsc emplace|unordered_set | (see dedicated page) |
| cpp/container/dsc emplace_hint|unordered_set | (see dedicated page) |
| cpp/iterator/dsc inserter | (see dedicated page) |


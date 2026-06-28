---
title: Node handle
type: Containers
source: https://en.cppreference.com/w/cpp/container/node_handle
---


# ''node-handle''

ddcla|since=c++17|expos=yes|
template</* unspecified */>
class /*node-handle*/;
A ''node handle'' is an object that accepts ownership of a single element from an  and . It may be used to transfer that ownership to another container with compatible nodes.
A node handle has two possible states:
* It refers to an element extracted from a container, or
* it is .
If a node handle is not empty, then it contains an allocator that is equal to the allocator of the previously extracted container.
For all map containers (`std::map`, `std::multimap`, `std::unordered_map`, and `std::unordered_multimap`) whose `key_type` is `Key` and `mapped_type` is `T`, the behavior of operations involving node handles is undefined if a user-defined specialization of `std::pair` exists for `std::pair<Key, T>` or `std::pair<const Key, T>`.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| cpp/container/dsc key_type|node_handle | (see dedicated page) |
| cpp/container/dsc mapped_type|node_handle | (see dedicated page) |
| cpp/container/dsc value_type|node_handle | (see dedicated page) |
| cpp/container/dsc allocator_type|node_handle | (see dedicated page) |

See *AssociativeContainer* and *UnorderedAssociativeContainer* for the actual definitions of the non-exposition-only nested types.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |
| dsc expos mem obj|ptr_|id=ptr|spec=box/core| | |
| <br> | |
| |a pointer to a container node containing the referred object | |


## Member functions

member|''node-handle''|2=

```cpp
dcl|num=1|
constexpr /*node-handle*/() noexcept;
dcla|num=2|constexpr=c++26|
/*node-handle*/( /*node-handle*/&& other ) noexcept;
```

1. The default constructor initializes the node handle to the empty state.
2. The move constructor takes ownership of the container element from `other`.
*  is initialized with .
*  is move constructed with .
* Assigns `nullptr` to .
* Assigns `std::nullopt` to .

## Parameters


### Parameters

- `other` - another node handle

## Notes

There is no user-provided copy destructor.  is not *CopyConstructible*.
Besides move construction and move assignment, a non-empty  can only be created by calling the `extract` member functions of (unordered) associative containers.
member|operator|2=
ddcla|constexpr=c++26|1=
/*node-handle*/& operator=( /*node-handle*/&& other );
The move assignment operator replaces state of `*this` with the state of `other` using move semantics.
# If  is `true`, destroys the element referred to by `*this` by calling , then deallocates the storage for the referred element by calling .
# Assigns  to .
# If  is `true`, move assigns  to .
# Assigns `nullptr` to  and assigns `std::nullopt` to .
:
*
*
*

## Parameters


### Parameters

- `other` - another node handle

## Return

`*this`

## Exceptions

Throws nothing.

## Notes

There is no user-provided copy assignment operator.  is not *CopyAssignable*.
member|~''node-handle''|2=
ddcla|constexpr=c++26|
~/*node-handle*/();
If  is `true`, destroys the element referred to by `*this` by calling , then deallocates the container element by calling .
Otherwise, does nothing.
member|empty|2=
ddcla|constexpr=c++26|
bool empty() const noexcept;
Returns `true` if the node handle is empty, `false` otherwise.

## Return value

member|operator bool|2=
ddcla|constexpr=c++26|
explicit operator bool() const noexcept;
Converts to `false` if the node handle is empty, `true` otherwise.

## Return value

member|get_allocator|2=
ddcla|constexpr=c++26|
allocator_type get_allocator() const;
Returns a copy of the stored allocator.
.

## Return value


## Exceptions

Throws nothing.
member|value |2=
ddcla|constexpr=c++26|
value_type& value() const;
Returns a reference to the element referred to by `*this`.
.

## Return value

As described above.

## Exceptions

Throws nothing.
member|key |2=
ddcla|constexpr=c++26|
key_type& key() const;
Returns a non-const reference to the `key_type` member of the element referred to by `*this`.
.

## Return value

As described above.

## Exceptions

Throws nothing.

## Notes

This function makes it possible to modify the key of a node extracted from a map, and then re-insert it into the map, without ever copying or moving the element.
member|mapped |2=
ddcla|constexpr=c++26|
mapped_type& mapped() const;
Returns a reference to the `mapped_type` member of the element referred to by `*this`.
.

## Return value

As described above.

## Exceptions

Throws nothing.
member|swap|2=
ddcla|constexpr=c++26|
void swap( /*node-handle*/& other ) noexcept(/* see below */);
Calls . If any of the following values is `true`, also calls :
*
*
*
:
*
*
*
*

## Exceptions

noexcept|ator_traits::propagate_on_container_swap::value
ator_traits::is_always_equal::value

## Non-member functions

member|std::swap|2=
ddcla|constexpr=c++26|
friend void swap(/*node-handle*/& lhs, /*node-handle*/& rhs)
noexcept(noexcept(lhs.swap(rhs)));
Effectively executes `x.swap(y)`.

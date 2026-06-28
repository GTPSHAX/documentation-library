---
title: operators (std::filesystem::path)
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/operator_cmp
---


# 1=operator==,!=,<,<=,>,>=,<=>small|(std::filesystem::path)


```cpp
dcl|num=1|since=c++17|1=
friend bool operator==( const path& lhs, const path& rhs ) noexcept;
dcl|num=2|since=c++17|until=c++20|1=
friend bool operator!=( const path& lhs, const path& rhs ) noexcept;
dcl|num=3|since=c++17|until=c++20|1=
friend bool operator<( const path& lhs, const path& rhs ) noexcept;
dcl|num=4|since=c++17|until=c++20|1=
friend bool operator<=( const path& lhs, const path& rhs ) noexcept;
dcl|num=5|since=c++17|until=c++20|1=
friend bool operator>( const path& lhs, const path& rhs ) noexcept;
dcl|num=6|since=c++17|until=c++20|1=
friend bool operator>=( const path& lhs, const path& rhs ) noexcept;
dcl|num=7|since=c++20|1=
friend std::strong_ordering
operator<=>( const path& lhs, const path& rhs ) noexcept;
```

Compares two paths lexicographically.
1. Checks whether `lhs` and `rhs` are equal. Equivalent to `!(lhs < rhs) && !(rhs < lhs)`.
2. Checks whether `lhs` and `rhs` are not equal. Equivalent to `!(lhs .
3. Checks whether `lhs` is less than `rhs`. Equivalent to `lhs.compare(rhs) < 0`.
4. Checks whether `lhs` is less than or equal to `rhs`. Equivalent to `!(rhs < lhs)`.
5. Checks whether `lhs` is greater than `rhs`. Equivalent to `rhs < lhs`.
6. Checks whether `lhs` is greater than or equal to `rhs`. Equivalent to `!(lhs < rhs)`.
7. Obtains the three-way comparison result of `lhs` and `rhs`. Equivalent to `1=lhs.compare(rhs) <=> 0`.
This prevents undesirable conversions in the presence of a `using namespace std::filesystem;` ''using-directive''.
rrev|since=c++20|

## Parameters


### Parameters

- `lhs, rhs` - the paths to compare

## Return value

@1-6@ `true` if the corresponding comparison yields, `false` otherwise.
7. `std::strong_ordering::less` if `lhs` is less than `rhs`, otherwise `std::strong_ordering::greater` if `rhs` is less than `lhs`, otherwise `std::strong_ordering::equal`.

## Notes

Path equality and equivalence have different semantics.
In the case of equality, as determined by `operator, only lexical representations are compared. Therefore, `1=path("a") == path("b")` is never `true`.
In the case of equivalence, as determined by `std::filesystem::equivalent()`, it is checked whether two paths ''resolve'' to the same file system object. Thus `equivalent("a", "b")` will return `true` if the paths resolve to the same file.

## Example


## See also


| cpp/filesystem/path/dsc compare | (see dedicated page) |
| cpp/filesystem/dsc equivalent | (see dedicated page) |


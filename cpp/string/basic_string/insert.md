---
title: std::basic_string::insert
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/insert
---


```cpp
|
basic_string& insert( size_type index, size_type count, CharT ch );
|
basic_string& insert( size_type index, const CharT* s );
|
basic_string& insert( size_type index, const CharT* s, size_type count );
|
basic_string& insert( size_type index, const basic_string& str );
dcl rev multi|num=5
|dcl1=
basic_string& insert( size_type index, const basic_string& str,
size_type s_index, size_type count );
|since2=c++14|notes2=<sup>(constexpr C++20)</sup>|dcl2=
basic_string& insert( size_type index, const basic_string& str,
size_type s_index, size_type count = npos );
dcl rev multi|num=6
|dcl1=
iterator insert( iterator pos, CharT ch );
|since2=c++11|notes2=<sup>(constexpr C++20)</sup>|dcl2=
iterator insert( const_iterator pos, CharT ch );
dcl rev multi|num=7
|dcl1=
void insert( iterator pos, size_type count, CharT ch );
|since2=c++11|notes2=<sup>(constexpr C++20)</sup>|dcl2=
iterator insert( const_iterator pos, size_type count, CharT ch );
dcl rev multi|num=8
|dcl1=
template< class InputIt >
void insert( iterator pos, InputIt first, InputIt last );
|since2=c++11|notes2=<sup>(constexpr C++20)</sup>|dcl2=
template< class InputIt >
iterator insert( const_iterator pos, InputIt first, InputIt last );
|
iterator insert( const_iterator pos, std::initializer_list<CharT> ilist );
|
template< class StringViewLike >
basic_string& insert( size_type index, const StringViewLike& t );
|1=
template< class StringViewLike >
basic_string& insert( size_type index, const StringViewLike& t,
size_type t_index, size_type count = npos );
```

Inserts characters into the string.
1. Inserts `count` copies of character `ch` at the position `index`.
2. Inserts null-terminated character string pointed to by `s` at the position `index`. The length of the string is determined by the first null character using `Traits::length(s)`.
3. Inserts the characters in the range [s, s + count) at the position `index`. The range can contain null characters.
4. Inserts string `str` at the position `index`.
5. Inserts a string, obtained by `str.substr(s_index, count)` at the position `index`.
6. Inserts character `ch` before the character pointed by `pos`.
7. Inserts `count` copies of character `ch` before the element (if any) pointed by `pos`.
8. Inserts characters from the range [first, last) before the element (if any) pointed by `pos`, as if by `insert(pos - begin(), basic_string(first, last, get_allocator()))`.
rrev|since=c++11|
This overload does not participate in overload resolution if `InputIt` does not satisfy *InputIterator*.
9. Inserts elements from initializer list `ilist` before the element (if any) pointed by `pos`.
10.
11. cpp/string/sv hack|inserts, before the element (if any) pointed by `index`, the characters from the subview [t_index, t_index + count) of `sv`.
* If the requested subview lasts past the end of `sv`, or if `1=count == npos`, the resulting subview is [t_index, sv.size()).
* If `t_index > sv.size()`, or if `index > size()`, `std::out_of_range` is thrown
If `pos` is not a valid iterator on `*this`, the behavior is undefined.

## Parameters


### Parameters

- `index` - position at which the content will be inserted
- `pos` - iterator before which the characters will be inserted
- `ch` - character to insert
- `count` - number of characters to insert
- `s` - pointer to the character string to insert
- `str` - string to insert
- `first, last` - range defining characters to insert
- `s_index` - position of the first character in `str` to insert
- `ilist` - `std::initializer_list` to insert the characters from
- `t` - object (convertible to `std::basic_string_view`) to insert the characters from
- `t_index` - position of the first character in `t` to insert

**Type requirements:**

- `InputIt`

## Return value

@1-5@ `*this`
@6-9@ An iterator which refers to the copy of the first inserted character or `pos` if no characters were inserted (`1=count == 0` or `1=first == last` or `1=ilist.size() == 0`)
@10,11@ `*this`

## Exceptions

@1-4,10@ Throws `std::out_of_range` if `index > size()`.
5. Throws `std::out_of_range` if `index > size()` or if `s_index > str.size()`.
11. Throws `std::out_of_range` if `index > size()` or if `t_index > sv.size()`.
In all cases, throws `std::length_error` if `size() + ins_count > max_size()` where `ins_count` is the number of characters that will be inserted.
rrev|since=c++20|
In all cases, if `std::allocator_traits<Allocator>::allocate` throws an exception, it is rethrown.

## Example


### Example

```cpp
#include <cassert>
#include <iterator>
#include <string>

using namespace std::string_literals;

int main()
{
    std::string s = "xmplr";

    // insert(size_type index, size_type count, char ch)
    s.insert(0, 1, 'E');
    assert("Exmplr" == s);

    // insert(size_type index, const char* s)
    s.insert(2, "e");
    assert("Exemplr" == s);

    // insert(size_type index, string const& str)
    s.insert(6, "a"s);
    assert("Exemplar" == s);

    // insert(size_type index, string const& str,
    //        size_type s_index, size_type count)
    s.insert(8, " is an example string."s, 0, 14);
    assert("Exemplar is an example" == s);

    // insert(const_iterator pos, char ch)
    s.insert(s.cbegin() + s.find_first_of('n') + 1, ':');
    assert("Exemplar is an: example" == s);

    // insert(const_iterator pos, size_type count, char ch)
    s.insert(s.cbegin() + s.find_first_of(':') + 1, 2, '=');
    assert("Exemplar is an:== example" == s);

    // insert(const_iterator pos, InputIt first, InputIt last)
    {
        std::string seq = " string";
        s.insert(s.begin() + s.find_last_of('e') + 1,
            std::begin(seq), std::end(seq));
        assert("Exemplar is an:== example string" == s);
    }

    // insert(const_iterator pos, std::initializer_list<char>)
    s.insert(s.cbegin() + s.find_first_of('g') + 1, {'.'});
    assert("Exemplar is an:== example string." == s);
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-847 | C++98 | there was no exception safety guarantee | added strong exception safety guarantee |


## See also


| cpp/string/basic_string/dsc insert_range | (see dedicated page) |
| cpp/string/basic_string/dsc append | (see dedicated page) |
| cpp/string/basic_string/dsc push_back | (see dedicated page) |


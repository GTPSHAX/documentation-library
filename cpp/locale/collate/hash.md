---
title: std::collate::hash
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/collate/hash
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
long hash( const CharT* beg, const CharT* end ) const;
dcl|num=2|1=
protected:
virtual long do_hash( const CharT* beg, const CharT* end ) const;
```

1. Public member function, calls the protected virtual member function `do_hash` of the most derived class.
2. Converts the character sequence [beg, end) to an integer value that is equal to the hash obtained for all strings that collate equivalent in this locale (`compare()` returns `0`). For two strings that do not collate equivalent, the probability that their hashes are equal should be very small, approaching `1=1.0 / std::numeric_limits<unsigned long>::max()`.

## Parameters


### Parameters

- `beg` - pointer to the first character in the sequence to hash
- `end` - one past the end pointer for the sequence to hash

## Return value

The hash value that respects collation order.

## Note

The system-supplied locales normally do not collate two strings as equivalent (`compare()` does not return `0`) if  returns `false`, but a user-installed `std::collate` facet may provide different collation rules, for example, it may treat strings as equivalent if they have the same Unicode normalized form.

## Example


### Example

```cpp
#include <iostream>
#include <locale>
#include <string>
#include <unordered_set>

struct CollateHash
{
    template<typename CharT>
    long operator()(const std::basic_string<CharT>& s) const
    {
        return std::use_facet<std::collate<CharT>>(std::locale()).hash(
                   &s[0], &s[0] + s.size()
               );
    }
};
struct CollateEq
{
    template<typename CharT>
    bool operator()(const std::basic_string<CharT>& s1,
                    const std::basic_string<CharT>& s2) const
    {
        return std::use_facet<std::collate<CharT>>(std::locale()).compare(
                     &s1[0], &s1[0] + s1.size(),
                     &s2[0], &s2[0] + s2.size()
               ) == 0;
    }
};

int main()
{
    std::locale::global(std::locale("en_US.utf8"));
    std::wcout.imbue(std::locale());

    std::unordered_set<std::wstring, CollateHash, CollateEq> s2 = {L"Foo", L"Bar"};
    for (auto& str : s2)
        std::wcout << str << ' ';
    std::cout << '\n';
}
```


**Output:**
```
Bar Foo
```


## See also


| cpp/string/basic_string/dsc hash | (see dedicated page) |


---
title: std::messages::open
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/messages/open
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
catalog open( const std::string& name, const std::locale& loc ) const;
dcl|num=2|1=
protected:
virtual catalog do_open( const std::string& name, const std::locale& loc ) const;
```

1. Public member function, calls the protected virtual member function `do_open` of the most derived class.
2. Obtains a value of type `catalog` (inherited from `std::messages_base`), which can be passed to `get()` to retrieve messages from the message catalog named by `name`. This value is usable until passed to `close()`.

## Parameters


### Parameters

- `name` - name of the message catalog to open
- `loc` - a locale object that provides additional facets that may be required to read messages from the catalog, such as `std::codecvt` to perform wide/multibyte conversions

## Return value

The non-negative value of type `catalog` that can be used with `get()` and `close()`. Returns a negative value if the catalog could not be opened.

## Notes

On POSIX systems, this function call usually translates to a call to `[https://pubs.opengroup.org/onlinepubs/9699919799/functions/catopen.html catopen()]`. In GNU libstdc++, it calls `[https://gcc.gnu.org/onlinedocs/libstdc++/manual/facets.html textdomain]`.
The actual catalog location is implementation-defined: for the catalog `"sed"` (message catalogs installed with the Unix utility `'sed'`) in German locale, for example, the file opened by this function call may be `/usr/lib/nls/msg/de_DE/sed.cat`, `/usr/lib/locale/de_DE/LC_MESSAGES/sed.cat`, or `/usr/share/locale/de/LC_MESSAGES/sed.mo`.

## Example


## See also


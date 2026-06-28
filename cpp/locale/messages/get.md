---
title: std::messages::get
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/messages/get
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
string_type get( catalog cat, int set, int msgid, const string_type& dfault ) const;
dcl|num=2|1=
protected:
virtual string_type do_get( catalog cat, int set, int msgid, const string_type& dfault ) const;
```

1. Public member function, calls the protected virtual member function `do_get` of the most derived class.
2. Obtains a message from the open message catalog `cat` using the values `set`, `msgid` and `dfault` in implementation-defined manner. If the expected message is not found in the catalog, returns a copy of `dfault`.

## Parameters


### Parameters

- `cat` - identifier of message catalog obtained from `open()` and not yet passed to `close()`
- `set` - implementation-defined argument, message set in POSIX
- `msgid` - implementation-defined argument, message id in POSIX
- `dfault` - the string to look up in the catalog (if the catalog uses string look-up) and also the string to return in case of a failure

## Return value

The message from the catalog or a copy of `dfault` if none was found.

## Notes

On POSIX systems, this function call usually translates to a call to `[https://pubs.opengroup.org/onlinepubs/9699919799/functions/catgets.html catgets()]`, and the parameters `set`, `msgid`, and `dfault` are passed to `catgets()` as-is. In GNU libstdc++, this function ignores `set` and `msgid` and simply calls GNU `gettext(dfault)` in the required locale.

## Example


## See also


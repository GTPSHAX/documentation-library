---
title: std::messages::do_close
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/messages/close
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
void close( catalog c ) const;
dcl|num=2|1=
protected:
virtual void do_close( catalog c ) const;
```

1. Public member function, calls the protected virtual member function `do_close` of the most derived class.
2. Releases the implementation-defined resources associated with an open catalog that is designated by the value `c` of type `catalog` (inherited from `std::messages_base`), which was obtained from `open()`.

## Parameters


### Parameters

- `c` - a valid open catalog identifier, on which `close()` has not yet been called

## Return value

(none)

## Notes

On POSIX systems, this function call usually translates to a call to `[https://pubs.opengroup.org/onlinepubs/9699919799/functions/catclose.html catclose()]`. In GNU libstdc++, which is implemented in terms of GNU `gettext()`, it does nothing.

## Example


## See also


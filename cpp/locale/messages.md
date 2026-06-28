---
title: std::messages
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/messages
---

ddcl|header=locale|
template< class CharT >
class messages;
Class template `std::messages` is a standard locale facet that encapsulates retrieval of strings from message catalogs, such as the ones provided by GNU [https://www.gnu.org/s/gettext/ gettext] or by POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/catgets.html `catgets`].
The source of the messages is implementation-defined.

## Specializations

The standard library is guaranteed to provide the following specializations (they are `required to be implemented by any locale object`):


| locale | |


## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/locale/messages/dsc open | (see dedicated page) |
| cpp/locale/messages/dsc get | (see dedicated page) |
| cpp/locale/messages/dsc close | (see dedicated page) |


## Protected member functions


| cpp/locale/messages/dsc do_open | (see dedicated page) |
| cpp/locale/messages/dsc do_get | (see dedicated page) |
| cpp/locale/messages/dsc do_close | (see dedicated page) |


## See also


| cpp/locale/dsc messages_base | (see dedicated page) |
| cpp/locale/dsc messages_byname | (see dedicated page) |


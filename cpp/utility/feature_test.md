---
title: Library feature-test macros
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/feature_test
---


# Library feature-test macros mark since c++20

Each of following macros is defined if the header  or one of the corresponding headers specified in the table is included.
A hardened implementation also defines the following macros.

## Notes

Each value in "Value" column follows the pattern: `"yyyymmL"`, where `"yyyy"` is a year, and `"mm"` is a month when the corresponding feature-set was accepted for standardization. Some values where increased since the time of their introduction, if capabilities of given feature where extended. The table above contains only the most recent values (that is, taken from the latest C++ language draft standard). A full set of values, including the initial and intermediate ones, can be found in this table.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-4126 | C++20<br>C++23 | some feature-test macros for fully<br>freestanding features were not freestanding | they are also<br>freestanding |


## See also


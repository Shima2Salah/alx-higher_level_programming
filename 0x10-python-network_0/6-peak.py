#!/usr/bin/python3
"""Finds a peak in a listusing binary search."""

def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted int"""
    li = list_of_integers
    if not li:
        return None
    start, end = 0, len(li) - 1
    while start < end:
        mid = start + (end - start) // 2
        if li[mid] > li[mid - 1] and li[mid] > li[mid + 1]:
            return li[mid]
        elif li[mid] < li[mid + 1]:
            start = mid + 1
        else:
            end = mid
    return li[start]

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#

def check_all_sides_positive(a, b, c):
    if (a <= 0 or b <= 0 or c <= 0):
        raise TriangleError


def check_triangle_existence(a, b, c):
    if a + b <= c:
        raise TriangleError
    if a + c <= b:
        raise TriangleError
    if b + c <= a:
        raise TriangleError


def triangle(a, b, c):
    check_all_sides_positive(a, b, c)
    check_triangle_existence(a, b, c)

    sides_set = {a, b, c}
    if len(sides_set) == 1:
        return 'equilateral'
    if len(sides_set) == 2:
        return 'isosceles'
    return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass

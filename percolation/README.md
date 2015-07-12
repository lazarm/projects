# Percolation problem

## Description
Given the system as an N-by-N grid of sites, which are either open or blocked, a percolation path is any path that starts at the open site at top row and finds its way to an open site at bottow row by moving through open sites in left, right or down direction.

This program uses functional programming approach to find a total number of different paths in a given system. 
Function _numAllPercs(grid, numStreams)_ takes a grid and a number of streams that flow through the system simultaneously. Function _f_ returns a list of open sites' indexes in the first row and _g_ returns a list of combinations C(_f_, _numStreams_). _fun_ returns a number of different percolations for each combination and sum of its outputs yields the final result.

System is described as a list of strings, where each string represents one row. Space character represents an open site and 'X' character represents the blocked one."

# Business Trip Algorithm

## Problem Description

Given a graph representing direct flights and their costs between cities, and an array of city names representing a business trip itinerary, the task is to determine whether the trip is possible with direct flights and calculate the total cost of the trip if possible.

## Visual :
![GraphDay27](https://github.com/mohammadalsmadi2000/data-structures-and-algorithms/assets/60603704/ef2a45a3-b1d1-45e3-bb70-55e75876e46f)

## Class: Graph




## Algorithm

1. Initialize `total_cost` to 0.

2. Iterate through the `path` array from index 0 to `len(path) - 1`:

   a. Get the current city and the next city from the `path`.

   b. Check if there is a direct flight between the current city and the next city using the `direct_flight` method of the `graph`.

   c. If there is no direct flight, return `None` as the trip is not possible.

   d. If there is a direct flight, add the cost of the flight between the current city and the next city to `total_cost`.

3. After iterating through the entire itinerary, return the `total_cost`.

## Big O
Time complexity  O(N)

Space complexity : O(N)

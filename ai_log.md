1. What is sorted key and how should I write it?

   Sorted key is sorting criterion

   Write key = <function>as the second argument in the sorted()

2. How can I place two expression in parallel for the key of sorted()?

   Use tuple.

   key = lambda x:(expression1,expression2)

3. Why the tuple can fulfill the requirement?

   The tuple's built-in comparison logic is: given two value, the program compare the firs value first. It will only compare the second value if the first values are equal.
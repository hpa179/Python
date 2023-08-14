"""Number of Days
Given the number of the month, your task is to calculate the number of days present in the particular month.

Note:- Consider non-leap year.

Input Format
An integer M, denoting the number of the month.

Output Format
Return the number of days in the month corresponding to the given number. Consider a non-leap year.

Example 1
Input

1
Output

31
Explanation

January has 31 days.

Example 2
Input

3
Output

31
Explanation

March has 31 days."""

x=int(input("Enter a number to find out the number of days in that month: "))


if x == 1:
  print("31")
elif x == 2:
  print("28")
elif x == 3:
  print("31")
elif x == 4 :
  print("30")
elif x == 5:
  print("31")
elif x == 6:
  print("30")
elif x == 7:
  print("31")
elif x == 8:
  print("31")
elif x == 9:
  print("30")
elif x == 10:
  print("31")
elif x == 11:
  print("30")
elif x == 12:
  print("31")
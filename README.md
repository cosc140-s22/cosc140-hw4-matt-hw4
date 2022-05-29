# COSC140 homework 4

## Homework feedback

 * How long did you spend on this homework?
3 Hours
 * What did you think about it?  What was good?  What could be improved?
It was a nice hands on experience with Django. 
## Feedback

N

For the `age_range` method, if the min and max are the same your method should just return 'Age 2' (or whatever the age) but it currently says 'Ages 2 to 2'.  The problem in your method is actually just the order of the `if` statements; if the last one was moved up, the method would likely return the correct thing.

Everything else looked good.


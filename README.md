# Python-Discord: Revival Of Code 2022

Hello, This is the place I'm putting my answers in for the Revival of Code 2022.

I'm going to do this **Python**, (If possible) in my EsoLang, **NumberScript** and **JavaScript** (from time to time).

## Challenges

### Day 1: Santa Floor Tracker (Not Quite Lisp)

#### link: https://adventofcode.com/2015/day/1

#### folder: `/Day-1-Santa-Floor-Tracker`

#### Puzzle Description:
    
_Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time._

_An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor._

_The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors._

_For example:_

_(()) and ()() both result in floor 0._

_((( and (()(()( both result in floor 3._

_))((((( also results in floor 3._

_()) and ))( both result in floor -1 (the first basement level)._

_))) and )())()) both result in floor -3._

_To what **floor** do the instructions take Santa?_

### Day 2: Elf Gift Wrapping Calculator(I Was Told There Would Be No Math)

#### Link: https://adventofcode.com/2015/day/2

#### Folder: `/Day-2-Elf-Gift-Wrapping-Calculator`

#### Description

_The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need._

_Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2\*l\*w + 2\*w\*h + 2\*h\*l. The elves also need a little extra paper for each present: the area of the smallest side._

_For example:_

_A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet._

_A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet._

_All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?_
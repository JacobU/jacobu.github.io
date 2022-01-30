---
layout: post
title: "Bertrand's Paradox or Why Anselm's Ontological Argument Sucks"
abstract: Bertrand's Paradox can show us that even when we think we know what a word or concept means, we often don't. Getting a strict definition of a word through programming it with computer-level strictness can get us to see when we don't know what we're talking about. Also, Anselm's Ontological Argument sucks.
categories: [programming, philosophy, theology]
author: Kieren Underwood
---

<div class='toc'>
<ol>
    <li>The Paradox</li>
    <li>The Methods</li>
    <ol>
        <li>The Endpoint Method</li>
        <li>The Radius Method</li>
        <li>The Midpoint Method</li>
    </ol>
    <li>The Code</li>
    <ol>
        <li>Method No. 1</li>
        <li>Method No. 2</li>
        <li>Method No. 3</li>
    </ol>
    <li>Why Anselm's Ontological Argument Sucks</li>
    <ol>
        <li>Defining Greater</li>
        <li>Existing is Greater</li>
    </ol>
</ol>
</div>

<a href="http://www.viridiandesign.org/notes/1-25/Note%2000002.txt">Attention Conservation Notice</a>: *The author uses Python to explain Bertrand's Paradox when he isn't a good Python programmer, and inserts needless jabs at long-dead Christian philosophers.*

<hr>

Bertrand's Paradox is a problem in probability theory about the "[principle of indifference](https://en.wikipedia.org/wiki/Principle_of_indifference)", a principle that says when we don't have any information about what we should believe, we should consider all possibilities as having the same probability. 

But I don't think about the principle of indifference when I look at the paradox. When I consider Bertrand's Paradox, I'm thinking about the slippery meaning of words: in this case, the word "random".

## The Paradox

To me, Bertrand's Paradox is all about the meaning of the word "random". <small>If my explanation of the paradox doesn't make sense, check out Wikipedia's [entry](https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)) on the topic, which is, as usual, fantastic.</small>[^1] 

Bertrand tells us to consider the following scenario. An equilateral triangle is inscribed in a circle. You must *randomly* choose a chord <small>a straight line whose endpoints lie on the circle arc</small>[^2] on the circle. What is the probability that the chord's length is longer than side of the triangle?


But if you go to calculate this probability, you'll realise that there's more than one way to *randomly* choose this chord. What does *random* really mean here? Bertrand, in *Calcul des probabilites* (1889), gave three such random methods.

## The Methods

The three methods Bertrand described were: 1) The Endpoint method, 2) the Radius method, and 3) the Midpoint method.<small>Descriptions of the methods have been taken from Wikipedia.</small>[^3]

### The Endpoint Method
<img src="/../assets/images/Bertrand1-figure.svg" alt="Bertrand's Paradox Method #1" height="150" width="150" class="center">
<blockquote>
"Choose two random points on the circumference of the circle and draw the chord joining them. To calculate the probability in question imagine the triangle rotated so its vertex coincides with one of the chord endpoints. Observe that if the other chord endpoint lies on the arc between the endpoints of the triangle side opposite the first point, the chord is longer than a side of the triangle. The length of the arc is one third of the circumference of the circle, therefore the probability that a random chord is longer than a side of the inscribed triangle is 1/3."
</blockquote>

### The Radius Method
<img src="/../assets/images/Bertrand2-figure.svg" alt="Bertrand's Paradox Method #2" height="150" width="150" class="center">
<blockquote>
"Choose a radius of the circle, choose a point on the radius and construct the chord through this point and perpendicular to the radius. To calculate the probability in question imagine the triangle rotated so a side is perpendicular to the radius. The chord is longer than a side of the triangle if the chosen point is nearer the center of the circle than the point where the side of the triangle intersects the radius. The side of the triangle bisects the radius, therefore the probability a random chord is longer than a side of the inscribed triangle is 1/2."
</blockquote>

### The Midpoint Method
<img src="/../assets/images/Bertrand3-figure.svg" alt="Bertrand's Paradox Method #3" height="150" width="150" class="center">
<blockquote>
"Choose a point anywhere within the circle and construct a chord with the chosen point as its midpoint. The chord is longer than a side of the inscribed triangle if the chosen point falls within a concentric circle of radius 1/2 the radius of the larger circle. The area of the smaller circle is one fourth the area of the larger circle, therefore the probability a random chord is longer than a side of the inscribed triangle is 1/4."
</blockquote>

Depending on which method you choose to use, the probability is different!

## The Code

People have worked on the paradox since 1889 and keep coming up with different ways to "solve" it. While some, most notably Edwin Jaynes, have proposed that one method of *random* is more truly random than the rest,<small> Jaynes, E. T. (1973), ["The Well-Posed Problem"](http://bayes.wustl.edu/etj/articles/well.pdf), Foundations of Physics, 3 (4): 477–493, </small>[^4] others, like Aerts & Bianchi<small>See Aerts, D. & Sassoli de Bianchi, M. (2014), "Solving the hard problem of Bertrand's paradox", Journal of Mathematical Physics, 55 (8).</small>[^5] require that for the method to be truly random, you have to randomise which method you use!

All this discussion tells me Bertrand has put together a situation where we really don't know what the word random means. The problem, besides its implications for the principle of indifference, is that the word random is a big category which covers many different types of definitions. And since we don't specify which of these definitions we use in the question, we get into problems. 

This becomes especially clear when we view the problem through the lens of code. 

In Python, "random" can mean many different things. It could be referring to the random *library*, a collection of functions dedicated to letting you get a large number of different random things: a random shuffling of numbers, a random pick of a list, a random number from a range. Even the Python function "random()" could be implemented in a number  of different ways. Different algorithms for generating random numbers will give you different results. And further, when generating our random chords, we use a specific implementation of "random()" that, if we really wanted, could be different! 

So until we sit down and write specific instructions for our computer to calculate a *random* chord, it's all just vague words.

Here are the functions I used to produce the three methods.

<figure class="center">
    <img src="/../assets/images/bertrandone.gif" alt="Bertrand's Paradox Animation #1" class="center">
    <figcaption>Method 1</figcaption>
</figure>
<figure class="center">
    <img src="/../assets/images/bertrandtwo.gif" alt="Bertrand's Paradox Animation #2" class="center">
    <figcaption>Method 2</figcaption>
</figure>

<figure class="center">
    <img src="/../assets/images/bertrandthree.gif" alt="Bertrand's Paradox Animation #3" class="center">
    <figcaption>Method 3</figcaption>
</figure>


### Method No. 1:
```
'''
We choose a point on a unit circle randomly. 
We return a tuple in the form of (x, y)
'''
def get_random_point():
    degrees = random.random() * math.pi  * 2
    x = 1 * math.sin(degrees) 
    y = 1 * math.cos(degrees)
    return (x,y)

'''
The two points just have to be on the unit circle
'''
def get_chord_method_one():
    return (get_random_point(), get_random_point())
```

### Method No. 2:
```
'''
This will choose a radius length and then calculate the 
position of the points based off this radius and the unit circle.
'''
=def get_points_from_radius():
    radius = random.random()
    xAxisDist = math.sqrt(1 - math.pow(radius, 2))
    point1 = (xAxisDist, radius)
    point2 = (-xAxisDist, radius) 
    return (point1, point2)

'''
We use a rotation matrix to rotate the points in the x-y axis.
point1 and point2 should be in the form of (x,y)
'''
def rotate_points(point1, point2):
    angleToRotate = random.random() * math.tau

    xn1 = point1[0] * math.cos(angleToRotate) - point1[1] * math.sin(angleToRotate)
    yn1 = point1[0] * math.sin(angleToRotate) + point1[1] * math.cos(angleToRotate)
    xn2 = point2[0] * math.cos(angleToRotate) - point2[1] * math.sin(angleToRotate)
    yn2 = point2[0] * math.sin(angleToRotate) + point2[1] * math.cos(angleToRotate)

    point1 = (xn1, yn1)
    point2 = (xn2, yn2)
    return (point1, point2)

def get_chord_method_two():
    points = get_points_from_radius()
    return rotate_points(points[0], points[1])
```

### Method No. 3:
```
def add_cartesian_points(point1, point2):
    x = point1[0] + point2[0]
    y = point1[1] + point2[1]
    return (x,y)

def polar_to_cartesian_coordinates(length, angle):
    x = length * math.cos(angle)
    y = length * math.sin(angle)
    return (x, y)

def cartesian_to_polar_coordinates(x, y):
    length = math.sqrt(math.pow(x,2) + math.pow(y,2))
    angle = math.atan2(y,x)
    return (length, angle)
'''
Chooses the midpoint of a chord in the form of (length, angle)
'''
def choose_midpoint():
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    # Check if the point is outside the circle
    while(math.sqrt(math.pow(x,2) + math.pow(y,2)) > 1):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
    midpoint = cartesian_to_polar_coordinates(x, y)
    return midpoint

'''
You input a point in polar coordinates.
This point is the midpoint of the chord you will construct intersecting
the unit circle.
'''
def get_chord_from_midpoint(length, angle):
    midpointCartesian = polar_to_cartesian_coordinates(length, angle)
    halfChordLength = math.sqrt(1 - math.pow(length, 2))
    '''
    After we have the center of the chord we simply find the points of the chord
    by adding the halfChordLength as a polar coordinate with an angle 
    of +pi/2 and -pi/2 for each point respectively.
    ''' 
    halfChordNegative = polar_to_cartesian_coordinates(halfChordLength, angle - (math.pi / 2))
    halfChordPositive = polar_to_cartesian_coordinates(halfChordLength, angle + (math.pi / 2))
    point1 = add_cartesian_points(midpointCartesian, halfChordNegative)
    point2 = add_cartesian_points(midpointCartesian, halfChordPositive)
    return (point1, point2)

def get_chord_method_three():
    midpoint = choose_midpoint()
    chord = get_chord_from_midpoint(midpoint[0], midpoint[1])
    return chord
```

The important thing about this code is not the differences themselves, but the fact that they *are* different. In each method, the Python code gets interpreted by the computer it's running on, and the computer does different operations. Ones and zeros are being thrown around in specific, varied ways. 

When we get careful about what the word *random* means and how we want to use it, we begin to see very clearly the problem with thinking we have a good grasp on what words really mean.

So, if a word that at first seems self-explanatory--like random--can be so deceptive, what about more complex words?

## Why Anselm's Ontological Argument Sucks

This brings me to Anselm's famous [Ontological Argument](https://en.wikipedia.org/wiki/Ontological_argument).<small>Actually, this doesn't follow naturally. Obviously I'm shoehorning Anselm into this article because I don't like his argument--or more specifically, the fact that after hundreds of years, it still gets brough up in debates when it should have died an early death.</small>[^6] Anselm was an 11th century Catholic theologian and philosopher whose ontological argument for the existence of a god has been the basis for a whole number of arguments of similar form--some of the latest belonging to Alvin Plantinga and William Lane Craig.<small>Of course, Anselm really only cares about this argument if in the end, the god whose existence he is proving turns out to be Yahweh, the ancient god of the Israelites who commanded them to take slaves of the surrounding nations, forbid inter-racial marriage, condoned genocide, etc, etc.</small>[^7]

The argument is as follows. (But note that I only really care about one word here, the word *greater*.)

1. By definition, God is a being than which none greater can be imagined.
2. A being that necessarily exists in reality is greater than a being that does not necessarily exist.
3. Thus, by definition, if God exists as an idea in the mind but does not necessarily exist in reality, then we can imagine something that is greater than God.
4. But we cannot imagine something that is greater than God.
5. Thus, if God exists in the mind as an idea, then God necessarily exists in reality.
6. God exists in the mind as an idea.
7. Therefore, God necessarily exists in reality.

I'm not here to debate the validity of this argument, that is, whether each statement does indeed lead to the next.<small>Please note that this is not a very good definition of the well-defined philosophical principle of being "valid".</small>[^8] Some of the greatest philosophers of all time have already done that and come to different conclusions. What I want to focus on is Anselm's use of the word greater.

When looking at Bertrand's Paradox, we saw that underneath the hood of the word *random* was a number of very specific operations that can be defined and sent to a computer. The same can be done with the word greater.

But, unfortunately for Anselm's argument, he seems to be completely oblivious to the fact that he skips over this massive task.

### Defining Greater

I want to look at what would happen if you tried to translate Anselm's first statement into code that could run on a computer. (For all the programmers who care, the examples are pseudo-Python.)

Anselm says that "by definition, God is a being ... greater" than anything else we can be imagined. In code, this means that we could set up a function called `checkIfGreaterThanGod`. This function would take a definition of what "greater" is and a representation of God. It would then compare "God" with any other *thing* that we can possibly imagine.<small>Please do not try to run any of this code!</small>[^9]

```
def greater(anything_we_can_imagine):
    if anything_we_can_imagine > God:
        return false
    else:
        return true

def checkIfGreaterThanGod(greater, anything_we_can_imagine):
    return greater(God, anything_we_can_imagine):
```

The first thing I notice is that such an infinite comparison is not possible. Anselm has conviniently definied God as *greater* than anything else we can ever imagine. This is good for his argument, but bad if we ever want to know what God is. Every time we think of some new *thing* we have to check it against God with our function to see whether God is still the greatest thing around. This is a lot of work ... in fact, infinite work!

Let's see what it could look like. Our God would have all sorts of attributes, and we could say that in order to be greater than any other *thing*, our God would have to best every *thing* in every attribute.

```
class God:
    love = 100
    strength = 100
    sexiness = 100
    power = 9000
    ...

def greater(anything_we_can_imagine):
    if God.love > anything_we_can_imagine.love
        && God.strength > anything_we_can_imagine.strength
        && God.sexiness > anything_we_can_imagine.sexiness
        && God.power > anything_we_can_imagine.power
        ...
        return true
    else:
        return false 
```

But lets think back to the problem with the word *random* in Bertrand's paradox. The word *random* can be written in code many different ways. The same goes for *greater*. 

There are other ways to define greater.<small>I would argue that if there are infinite attributes that a being can have, there are infinite ways to define a "greater than" function.</small>[^10] Take, for example, the case where a being is greater in some attributes, but not in others, compared with God. We could represent, for example, Marilyn Monroe in our code, and imagine, with good reason, that she has a higher level of sexiness than God. 

```
class MarilynMonroe:
    love = 10
    strength = 1
    sexiness = 101
    ...
```

What happens when we feed our `greater` function God and Marilyn Monroe? Well, since for our God to be greater, it has to be greater in *all* attributes, it fails our `greater` function! God is not greater than Marilyn Monroe. 

Of course, Anselm could do many things to counter this, one of them being to claim that his God (Yahweh) is sexier than Marilyn Monroe. He could also decide to change the `greater` function, by only requiring that God have higher stats in a *majority* of attributes. 

But all this is beside the point. The real problem is that Anselm, and everyone else after him, simply never tries to define *greater*. We're just supposed to have an intuitive grasp of what greater means, and end our thoughts there. This is a big problem.

### Existing is Greater

Anselm then tells us that: 

<blockquote>
A being that necessarily exists in reality is greater than a being that does not necessarily exist.
</blockquote>

Yet, because Anselm is yet to define what *greater* means, this statement is completely meaningless. He wants us to take his word for it, that existence is a good trait, something that makes everything obviously greater.

What about The Greatest Murderer we can imagine? This murderer has perfect stats but doesn't exist: 

```
class GreatestMurderer:
    strength = 100
    stealth = 100
    killing_efficiency = 100
    ...
    exists = false
```

Now if we change `exists` to `true`, is this Greatest Murderer better or worse? Does a murder happening in real life make it greater? That's an open question (although one I have an opinion on). 

Same goes for Anselm's God.  

Others, such as Mulla Sadra (c. 1571-1640) and Kurt Godel, used the words "perfection" and "positive properties" to extend Anselm's argument. They all fall into the same trap. Unless these words are defined, they remain meaningless. And as Bertrand's Paradox shows us with the word random, this is something far from straightforward.

Unluckily for Anselm, you don't get to pretend to have a mathematical proof for God if you've never done the hard work of making your definitions mathematical as well.

[^1]: If my explanation of the paradox doesn't make sense, check out Wikipedia's [entry](https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)) on the topic, which is, as usual, fantastic.
[^2]: a straight line whose endpoints lie on the circle arc
[^3]: Descriptions of the methods have been taken from Wikipedia.
[^4]:  Jaynes, E. T. (1973), ["The Well-Posed Problem"](http://bayes.wustl.edu/etj/articles/well.pdf), Foundations of Physics, 3 (4): 477–493, 
[^5]: See Aerts, D. & Sassoli de Bianchi, M. (2014), "Solving the hard problem of Bertrand's paradox", Journal of Mathematical Physics, 55 (8).
[^6]: Actually, this doesn't follow naturally. Obviously I'm shoehorning Anselm into this article because I don't like his argument--or more specifically, the fact that after hundreds of years, it still gets brough up in debates when it should have died an early death.
[^7]: Of course, Anselm really only cares about this argument if in the end, the god whose existence he is proving turns out to be Yahweh, the ancient god of the Israelites who commanded them to take slaves of the surrounding nations, forbid inter-racial marriage, condoned genocide, etc, etc.
[^8]: Please note that this is not a very good definition of the well-defined philosophical principle of being "valid".
[^9]: Please do not try to run any of this code!
[^10]: I would argue that if there are infinite attributes that a being can have, there are infinite ways to define a "greater than" function.

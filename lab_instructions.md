# General Instructions

Like always, each Lab should have the following header:
```
"""
Author: Your Name
Date: Today's Date/Due Date
FileName: The File's Name
Purpose: What the program is about
"""
```

## Lab 5a: Mood Playlist Generator

Suppose its finals week at UOG, and the stress is lowkey real. You just finished a CS201 exam (that you totally did great on) in the Student Success Center (because its take home... we will talk about it later), and the pressure is as if you are lifting the earth. Depending on your mood right now whether you have aced your test or are completely drained, you want to listen to the perfect set of music.

But you're too tired to hunt through Spotify. Its okay, lets make a program to pick for you!

You will make a program called `mood_generator.py` that will do the following:

- Stores a collection of popular pop songs organized by mood using a **dictionary**. The dictionary is structured where your keys are the moods and the values are a list of songs. Below is an example (you may use it as well)
```
mood_to_songs = {
    "happy": ["APT. - ROSÉ & Bruno Mars", "Espresso - Sabrina Carpenter"],
    "chill": [],
    "angry": [],
    "sad": [],
    "focus": [],
    "island vibe": []
}
```
- Asks the user to input their current mood (happy, chill, angry, sad, focus, or island vibe).
- Recommends 3 randomly selected songs from that mood’s list (no duplicates in one recommendation).

Note: You need a minimum of 3 moods, each with 5 songs to randomly choose. You are not limited to the amount of songs or moods, don't go overboard though.

Recommended functions/operations: `random.sample()`

## Lab5b: Destroying a pyramid!

A followup from Lab3a, lets build upon this project.

Update your existing `create_pyramid.py` program (from Lab 3a) so that it:

- Still asks the user for the number of rows (height) of the pyramid.
- Builds the full pyramid as a list of strings (each string = one row of the pyramid).
- Then asks the user: “Which rows do you want to destroy? (enter numbers separated by commas)”
- Removes the chosen rows from the list.
- Finally prints the surviving (modified) pyramid, nicely centered.

Note: You may assume that the user will enter the removed rows in order.

Example:
```
Hello user, lets create a pyramid!
How many rows will this pyramid have (blocks tall): 11
           🧱
          🧱🧱
         🧱🧱🧱
        🧱🧱🧱🧱
       🧱🧱🧱🧱🧱
      🧱🧱🧱🧱🧱🧱
     🧱🧱🧱🧱🧱🧱🧱
    🧱🧱🧱🧱🧱🧱🧱🧱
   🧱🧱🧱🧱🧱🧱🧱🧱🧱
  🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
 🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
Great pyramid!
What rows would you like removed?: 3,6,10
           🧱
          🧱🧱
        🧱🧱🧱🧱
       🧱🧱🧱🧱🧱
     🧱🧱🧱🧱🧱🧱🧱
    🧱🧱🧱🧱🧱🧱🧱🧱
   🧱🧱🧱🧱🧱🧱🧱🧱🧱
 🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
It...uhm... looks great!
```

Recommended Functions/Methods: You can put the rows into a 1D list of strings! Then use `.pop()` to remove the specific rows. Remember that once you pop, the size of the list changes, so think of ways to account for the changing size! Otherwise, you may remove the incorrect rows!

## Lab 5c: Something, idk, placeholder

## Lab 5d: Calculus Numerical Intergration 

In Calculus I, the definite integral \(\int_a^b f(x) \, dx\) represents the **area under the curve** of a function \(f(x)\) from \(x = a\) to \(x = b\).

We use integration in real life for things like calculating total distance traveled from velocity, total work done, or accumulated rainfall.

However, there are many functions are hard to integrate by hand. Hence we use **numerical methods** to approximate the area.

In this lab, you will use the **Left Riemann Sum** (also called Left Rectangle Method). This is one of the simplest ways to approximate the area under a curve.

Here is the basic rundown:
- We split the interval from `a` to `b` into `n` equal parts.
- For each part, we draw a **rectangle**.
- The **width** of each rectangle is $\Delta x = \dfrac{b - a}{n}$.
- The **height** of each rectangle is the value of the function at the **left** side of that interval only. For left Riemann, it would be $f(x_{i - 1})$
- Then we get all left side x points of the rectangle.
- We calculate the area of each rectangle (`width × height`) and add them all up.

So for example, suppose we wanted to find the area under the curve of $f(x) = x^2$ between $x = 0$ and $x = 2$.

The formula for reimann sum is:

\[ \sum_{i = 1}^n f(x_i^*) \cdot \Delta x_i \]

Where $x_i^*$ is the type of reimann sum. Since we are doing left, we have $x_i^* = x_{i - 1}$.

If we decided to create 4 subdivisions (4 rectangles) we have the following:

$$
\sum_{i = 1}^4 f(x_i^*) \cdot \Delta x_i = \Delta x_i \cdot \sum_{i = 1}^4 f(x_{i - 1}) \\
= \Delta x_i \cdot \Big(f(x_0) + f(x_1) + f(x_2) + f(x_3)\Big) \\
= \dfrac{1}{2} \Big(f(0) + f(0.5) + f(1) + f(1.5) \Big) \\
= \dfrac{1}{2} \Big(0^2 + 0.5^2 + 1^2 + 1.5^2 \Big) \\
= \dfrac{1}{2} \Big(0 + 0.25 + 1 + 2.25 \Big) \\
= \dfrac{1}{2}(3.5) = 1.75
$$

We get the following figure:

![four_sub_integration](Figures/numerical_integration1.png)

Notice that its not a very good approximation. To get a more accurate result, you would create more subdivisions!

If we decided for $n = 10$:
\[\Delta x = \dfrac{2 - 0}{10} = \dfrac{1}{5} = 0.2\]

\[x = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]\]

where $x_0 = a = 0$ and $x_{10} = b = 2$

\[
\sum_{i = 1}^{10} f(x_i^*) \cdot \Delta x = \Delta x \cdot \sum_{i = 1}^{10} f(x_{i - 1}) = \Delta x \cdot \Big(f(x_0) + f(x_1) + \cdots + f(x_9)\Big) = \dfrac{1}{5} \Big(f(0) + f(0.2) + \cdots + f(1.8)\Big) = \dfrac{1}{5} \Big(0 + 0.04 + \cdots + 3.24\Big) = \dfrac{1}{5} (11.4) = 2.28
\]

Below is the figure for the following result:

![ten_sub_integration](Figures/numerical_integration2.png)

As you can see, a much more accurate result! Still quite rough...

Now that you got the basic idea, the theory is that if we keep increasing n, we get a more accuracte result to the area. 

If we did $n = 100$:

![hundred_sub_integration](Figures/numerical_integration3.png)

We almost get the entire area under the curve.

Eventually, if we do a big number like $n = 10000$, it should emcompass the entire area under the curve:

![ten_thousand_sub_integration](Figures/numerical_integration4.png)

Note that this is an approximation such that: 

\[ \sum_{i = 1}^n f(x_i^*) \cdot \Delta x_i \approx \int_a^b f(x) dx = F(b) - F(a)\]

If we do the actual integral we have the following:

\[ \int_0^2 x^2dx = \dfrac{x^3}{3} \Big|_0^2 = \dfrac{2^3}{3} - \dfrac{0^3}{3} = \dfrac{8}{3} \approx 2.667\]. 

With the main idea down, your task is to create a program called `numerical_integration.py` that does the following:

- Asks the user for the `formula` they want to integrate (Note: They need to write it in python syntax)
- Asks the user for the lower bound `a` and upper bound `b`
- Asks the user for the sub divisions `n`
- Calculate $\Delta x = b - a / n$
- Create a list of left endpoints: x\_left $= [a, a + \Delta x, a + 2\Delta x, ...]$
- Create a list of y-values (the height) by evaluating `f(x)` at each endpoint
- Create a list of areas of each rectangle by evaluating $\Delta x \cdot $ y_values$[i]$
- Return the approximate area by summing all the rectangles

Example Output: 
```
Please insert formula: x**2
Enter lower bound a: 0
Enter upper bound b: 2
Enter sub divisions n: 10
x_points: [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8]
y_points: [0.0, 0.04, 0.16, 0.36, 0.64, 1.0, 1.44, 1.96, 2.56, 3.24]
rectangle areas: [0.0, 0.008, 0.032, 0.072, 0.128, 0.2, 0.288, 0.392, 0.512, 0.648]
Approximate area: 2.28
```

For this lab, please use the following template below:
```
def numerical_integration(f, lower_bound, upper_bound, sub_divisions):
    """
    Calculate the Left Riemann Sum approximation.
    
    Returns: [area, x_points, y_points, rectangles]
    """
    # Step 1: Calculate the width of each rectangle
    # TODO: Compute delta_x = (b - a) / n
    delta_x = 0
    
    # Step 2: Create list of left endpoints (x_points)
    # TODO: Compute x_points
    x_points = []
    
    # Step 3: Calculate y-values by evaluating f at each x_point
    # TODO: Compute y_points based on x_points
    $ Hint: Since f is a formula, you can do f(x_point)
    y_points = []
    
    # Step 4: Calculate area of each rectangle (width × height) 
    # TODO: Compute rectangle areas
    rectangles = []
    
    # Step 5: Sum all rectangle areas to get total approximation
    total_area = sum(rectangles)
    
    # Step 6: Return all data as a list
    return [total_area, x_points, y_points, rectangles]


# ============================================================
# TESTING CODE (Do not modify below)
# ============================================================
if __name__ == "__main__":
    # Run the test first
    test_with_known_function()
    
    # Then get user input for custom function
    print("="*50)
    print("CUSTOM FUNCTION INTEGRATION")
    print("="*50)
    
    formula = input("Please insert formula (use x, e.g., x**2): ")
    lower_bound = int(input("Enter lower bound a: "))
    upper_bound = int(input("Enter upper bound b: "))
    sub_divisions = int(input("Enter sub divisions n: "))
    
    # Create function from user input
    user_function = lambda x: eval(formula)
    
    # Calculate approximation
    result = numerical_integration(user_function, lower_bound, upper_bound, sub_divisions)
    
    # Display results
    print("\n" + "-"*50)
    print(f"x_points: {result[1]}")
    print(f"y_points: {result[2]}")
    print(f"Rectangle areas: {result[3]}")
    print(f"\nApproximate area: {result[0]}")
    print("-"*50)
```


## Lab 5e: RPG Battle Manager!

A player of your random rpg game has the following info about.

There is also a leveling system, we use this to keep track of when the player levels up and gets stronger! There are a lot of exp calculations but lets make it simple and use the following:

EXP_TO_NEXT_LVL $= 100 × 1.3^{(level-1)}$

```
player = {"class" : "Warrior", 
          "level" : 20,
          "current_exp" : 1374,
          "health" : 520,
          "attributes" : [10, 4, 2, 9, 6, 7], # STR, INT, DEX, VIT, CON, CHR
          "inventory" : [["apple", 10], ["health potion", 3], ["key", 1], ["stick", 1]]}
```

Your job is to create 3 functions:

##### Function one, `level_manager(player)`
The first function relates with the leveling system. Lets call it `level_manager(player)` where player is a dictionary.
- Check if the player is close to leveling up by checking thier current exp. 
- If their exp is over the the exp to next level:
  - Subtract the current exp by the exp to next level 
  - Level up the character, then prompt the user to ask what attribute they want to level up by one point!

For example:
```
Level up! You are now level 21!
Current attributes: STR=10, INT=4, DEX=2, VIT=9, CON=6, CHR=7
Which attribute would you like to increase? (STR/INT/DEX/VIT/CON/CHR): STR
STR increased to 11!
```

Extra Credit (5pts): Handle cases when the player levels up more than once. 

##### Function two, `use_item(player, item_name)`
This function allows the player to use items from their inventory:

To make things simple, lets only look at two items
Item effects:
- `"apple"`: Restore 50 health (cannot exceed max health)
- `"health_potion"`: Restore 100 health + 10% of their max health (cannot exceed max health)

During combat, if a player uses an item, update the count of said item accordingly and return a message describing what happened. 

If there is zero of the item, tell the user they cannot use the item, they don't have any. 

For example:
```
# Assuming max_health = 520
use_item(player, "apple")
# Returns: "Used apple! Restored 50 HP. Current health: 520/520"

use_item(player, "health_potion")  
# Returns: "Used health potion! Restored 152 HP. Current health: 520/520"
```

##### Function three, `battle_manager(player, enemy)`
This function relates with combat. It takes in two parameters where:
  - player is a dictonary
  - enemy is another dictonary

When a battle occurs, here is the flow:
  - Show both the player's and enemy's stats
  - Alternates between player and enemy
  - Continue until either the player or enemy reaches 0 health
  - Player turn:
    - Calculate the damage based on STR attribute 
    - Player deals damage to enemy
    - Show damage dealt and enemy's remaining health
    - If enemy dies, break out of loop
  - Enemy turn:
    - Enemy deals damage to player
    - Show damage taken and player's remaining health
    - If player dies, break out of loop
  - After combat
    - If player wins: Award EXP based on the following calculation: `enemy['level'] * 50`
    - Call `level_manager(player)` to check for level ups
    - Return `True` if player won, `False` if player lost
    - If player won, restore health equal to 20% of their max health
  
Please use the following dictionary for the enemy:
```
enemy = {
    "name": "Goblin",
    "level": 5,
    "health": 80,
    "attack": 15,
    "exp_reward": 75
}
```

Here is a sample run:
```
You have encountered a goblin!
=== BATTLE START ===
Warrior [Level 20] | HP: 520 | STR: 10
vs
Goblin [Level 5] | HP: 80 | ATK: 15
====================

Turn 1:
You attack the Goblin for 20 damage!
Goblin has 60 HP remaining.
---
Goblin attacks you for 15 damage!
You have 505 HP remaining.
---

Turn 2:
You attack the Goblin for 20 damage!
Goblin has 40 HP remaining.
---
Goblin attacks you for 15 damage!
You have 490 HP remaining.
---

Turn 3:
You attack the Goblin for 20 damage!
Goblin has 20 HP remaining.
---
Goblin attacks you for 15 damage!
You have 475 HP remaining.
---

Turn 4: 
You attack the Goblin for 20 damage!
Goblin has 0 HP remaining!

You defeated the Goblin! Gained 250 EXP!
After battle, you restored 20% of your max health!
Health: 475/520 -> 520/520
```

Please use the following template to create your functions:
```
def level_manager(player):
    # TODO: Calculate EXP needed
    exp_needed = 100 * (1.3 ** (player["level"] - 1))
    
    # TODO: Use while loop for multiple level ups
    while player["current_exp"] >= exp_needed:
        # TODO: Subtract exp and increase level
        # TODO: Ask for attribute to increase
        # TODO: Recalculate exp_needed for new level
    pass

def use_item(player, item_name):
    # TODO: Find item in inventory
    # TODO: Check quantity > 0
    # TODO: Apply healing effect
    # TODO: Update 
    # TODO: Return message
    pass

def battle_manager(player, enemy):
    # TODO: Display battle stats
    # TODO: Combat loop (player attacks first)
    # TODO: Player turn (damage = STR * random.uniform(1.5, 2))
    # TODO: Enemy turn
    # TODO: Victory or defeat logic
    # TODO: Award EXP and restore health if win
    pass
```
Note that dictionaries are mutable, so any changes within the function which reflect!


# texasholdem
While I was at a brewery the world series of poker was on tv. Each time a hand was dealt or when cards were turned over, the screen showed the likelyhood each of the players had in winning the hand. I figured this would be pretty easy to write and a fun project to do while learning more about object oriented programming in Python.

After digging into the details of the game and putting together a plan of how I wanted to tackle the program, I realized my first few ideas would be pretty inefficent and there was probably a better way. I did some reading online and found content from a CS course at Emory college (http://www.mathcs.emory.edu/~cheung/Courses/170/Syllabus/10/pokerValue.html) for an into to Java class that handled the scoring of each hand in a mathmatical fashion, which was a much better method than running a bunch of for loops to scan each players hand and count the score.

So far I have the players, the dealer and their hands implemented, but need to write out the code to calculate and display the win percents for each player, as well as let the user increment the game in the normal fashion, initial 2 cards being dealt to each player, 3 for the dealer, one for the turn and one for the river card.
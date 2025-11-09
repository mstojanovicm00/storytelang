hero "Henry" ;
friend "Larry" ;
enemy "Leonard" ;
enemy "professor" ;
set health, 100 ;
keep health > 0 ;
clamp health <= 100 ;
function sum a b:
return a + b ;
leave
function max a b:
set max, b ;
if a > max:
set max, a ;
end
return max ;
leave
scene start:
pick "chocolate" ;
say "Henry's standing in front of the college building with a book in his hands and a fear in his heart." ;
say "Larry's waving at him from a distance." ;
tell "Larry", "Henry", "Oh come on, get inside, the exam is already set to begin." ;
if health < 10:
say "He can't even look up" ;
exit ;
end
choice "go to the classroom" -> $classroom ;
choice "run to the cafeteria" -> $mensa ;
leave
scene mensa:
say "Henry is running towards the cafeteria, hoping that a nice schnitzel could rip his fears off his chest." ;
say "Leonard sits at the table and laughs." ;
tell "Leonard", "Henry", "Running away again, hum?" ;
set health, health - 30 ;
say "Henry slips a bit of beans down his throat. Health: ", health ;
if health < 20:
say "He's feeling the semester running rapidly." ;
exit ;
end
else:
say "He sums up his courage and goes to the classroom." ;
enter classroom ;
end
leave
scene classroom:
say "Henry enters the classroom. The professor's looking at him with no smile on his face." ;
say "Henry looks at the writing on the blackboard: 'Compilers Exam - 10 tasks, 0 hopes'" ;
pick "pen" ;
say "Henry takes his pen and repeats to himself: 'Don't panic, you know one question at least.'" ;
if has "chocolate":
say "The chocolate from his pocket gives him a little strength." ;
set health, health + 10 ;
end
say "Leonard sits in front of him and whispers " ;
tell "Leonard", "Henry", "Buddy, what is a lambda?" ;
set health, health - 20 ;
enter exam ;
leave
scene exam:
say "Henry solves the first task. On the second one he sees 'this is not required from students'." ;
if health > 50:
say "He writes surely, he even starts to smile as he sees the infinite loop." ;
end
else:
say "His hands are shaking, and his pen doesn't even want to write anymore." ;
end
choice "finish the test" -> results ;
leave
scene results:
say "The professor is correcting the tests. Henry's sweating as if in a sauna." ;
rand res, 0, 100, 1 ;
if res >= 91:
tell "professor", "Henry", "Not bad!" ;
say "Henry gets an A" ;
end
else if res >= 51:
tell "professor", "Henry", "Passable" ;
say "Henry gets a D" ;
end
else:
tell "professor", "Henry", "See you over the summer!" ;
say "Henry fails... for now... again." ;
exit ;
end
say "The exam has been survived." ;
leave
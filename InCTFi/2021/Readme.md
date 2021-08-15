# InCTF International 2021

InCTF International is a premier hacking event targeted at hackers of all ages, and as always, we will be carefully moulding challenges, loaded with the latest vulnerabilities, responsibly innovating to help you stay current and have an enjoyable time and experience.

| Title | Category | Points | Submitted | Solution | Official WriteUp | Flag |
|-------|----------|--------|-----------|----------|------------------|------|
| Sanity Check | Misc | 10 | ✔️ | ✔️ | ❌ | ✔️ |
| Alpha Pie | Misc | 100 | ✔️ | ✔️ | ❌ | ✔️ |

---

## Sanity Check

**Challenge**

Welcome to InCTFi 2021!

To get the flag, please grab it from #general in our discord: https://discord.gg/CZCYZNqC4B

**Solution**

Join the Discord server and check #general description banner.

Done! We have our flag "`inctf{welcome_t0_inctf_internationals_2021}`"

## Alpha Pie

**Challenge**

We have created a mini game to test your skills. Go grab the flag!!

authors : careless_finch, malf0y

nc misc.challenge.bi0s.in 1337

**Solution**

First let’s look at the rules:
```
Welcome to Alpha pie game!!!
Rules:
1. To complete one level you have match the left matrix to the right one by moiving each letter to their position in the right matrix
2. Moving to only adjecent column or row is possible.
3. Diagonal movements are not possible
4. negative numbers are not allowed in the input
5. The input format should be 'current-x-cord,current-y-cord,to-x-cord,to-y-cord'.
   eg : 0,0,0,1 (Will move letter at position 0,0 to position 0,1 if a letters is present at 0,0 and no letter is present at 0,1).
7. Number of moves will be limited for each level.
8. The game has a time limit of 'n' minutes.
9. You will lose the game if you enter certain number of invalid moves
10. After you pass 9 levels you will ge the flag.
   Good luck ! Enjoy the game 👍
```

To be more exact with rule 8, the game lasts a total of `500 seconds`.


We have about 1 minute per level, which is not much, so we will create a script that will calculate for us the movements we have to make in the game.


Take, for example, Level 1:
```
Level-1
Max number of moves allowed: 5
+-------+  +-------+
| 0 | 0 |  | s | h |
| h | s |  | 0 | 0 |
+-------+  +-------+
Current moves : 0
Enter move in the format 'current-x-cord,current-y-cord,to-x-cord,to-y-cord ' :
```

s must do:
- 1,1,0,1
- 0,1,0,0

then h must do:
- 1,0,1,1
- 1,1,0,1

So we simply use an `A-Star` algorithm.

You can find my script here: [alphapie.py](./alphapie.py)

Credits to Ryan Collingwood and Nicholas Swift for their A-Star algorithm: [astar.py](https://gist.github.com/ryancollingwood/32446307e976a11a1185a5394d6657bc)

You can find my full game here: [alphapie.txt](./alphapie.txt)

Done! We have our flag "`inctf{G00d_Job_e33ac7bae54893252e60c0187e793ef5d13d7dfa85fafa7984f8753b591247b9}`"
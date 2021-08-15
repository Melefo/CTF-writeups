# InCTF International 2021

InCTF International is a premier hacking event targeted at hackers of all ages, and as always, we will be carefully moulding challenges, loaded with the latest vulnerabilities, responsibly innovating to help you stay current and have an enjoyable time and experience.

| Title | Category | Points | Solves | Submitted | Solution | Flag | Official WriteUp |
|-------|----------|--------|--------|-----------|----------|------------------|------|
| [Sanity Check](#sanity-check) | Misc | 10 | 552 | ✔️ | ✔️ | ✔️ | ❔ |
| [Alpha Pie](#alpha-pie) | Misc | 100 | 58 | ✔️ | ✔️ | ✔️ | ❔ |
| [blackStab Cloud Services](#blackstab-cloud-services) | Misc | 1000 | 2 | ❌ | ❌ | ❌ | ✔️ |
| [Ancient_House](#ancienthouse) | Pwn | 545 | 33 | ❌ | ❌ | ❌ | ❔ |
| [Node Keeper](#node-keeper) | Pwn | 925 | 14 | ❌ | ❌ | ❌ | ❔ |
| [Kqueue](#kqueue) | Pwn | 984 | 7 | ❌ | ❌ | ❌ | ❔ |
| [Baby Glob](#baby-glob) | Pwn | 993 | 5 | ❌ | ❌ | ❌ | ❔ |
| [DeadlyFastGraph](#deadlyfastgraph) | Pwn | 996 | 4 | ❌ | ❌ | ❌ | ❕ |
| [MultiStorage](#multistorage) | Pwn | 1000 | 1 | ❌ | ❌ | ❌ | ❔ |

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

`nc misc.challenge.bi0s.in 1337`

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

## blackStab Cloud Services

**Challenge**

Presenting you, blackStab Cloud Services a secure VM provider which lets you spawn your own VMs on the cloud with your favorite OS (may it be Arch or even Windows)

Note: On the occasion of inaguration, we're giving out 1000$ worth blackStab cloud credits for new users!!

Author: [f4lc0n](https://twitter.com/theevilsyn)

`misc.challenge.bi0s.in:1133`

[blackstab.zip](./blackstab.zip)

**Official WriteUp**

[Google Slides](
https://docs.google.com/presentation/d/1PrApTgj9wM3Z0No-hNXaMlsiNSy7o0GINlRI95pjkak/edit?usp=sharing)

## Ancient_House

**Challenge**

Someone's gotta stop those glibc nerds

The challenge runs the DEBUG build of jemalloc

Author : [Pwn-Solo](https://twitter.com/Pwn_Solo)

`nc pwn.challenge.bi0s.in 1230`

[Handout.zip](./Ancient_House.zip)

## Node Keeper

**Challenge**

Author: [3agl3](https://twitter.com/3agl31)

`nc pwn.challenge.bi0s.in 1234`

[handout.zip](./Node_Keeper.zip)

## Kqueue

**Challenge**

A long queue awaits you in ring0.

md5sum : bzImage - `d7c173966e9fb6e79eaef8d351cb8f09` : kqueue.ko - `702ab39064a7b4ee1d33f7c484eeb77a`

Author - [Cyb0rG](https://twitter.com/_Cyb0rG)

username : password - `ctf:kqueue`

`nc pwn.challenge.bi0s.in 1279`

[Handout.zip](./Kqueue.zip)

## Baby Glob

**Challenge**

Super secure path finder from your own 2017.

md5sum : chall - `60aedc6cf9a7b163254cfc2ffea64c04`

Note - Standard `ubuntu 20.04` docker has been used.

Author - [Cyb0rG](https://twitter.com/_Cyb0rG)

`nc pwn.challenge.bi0s.in 1299`

[Handout.zip](./Baby_Glob.zip)

## DeadlyFastGraph

**Challenge**

I decided that DFG wasn't fast enough.

Author: [DarkKnight](https://twitter.com/_d4rkkn1gh7)

`nc pwn.challenge.bi0s.in 1212`

[DFGHandout.zip](./DFGHandout.zip) [DFGServer.zip](./DFGServer.zip)

**Official WriteUp**

Exploit:
[GitHub gist](https://gist.github.com/d4rk-kn1gh7/9bcd1d49dc07f05c371603fb4b96a651)

`Full writeup coming soon :)`

## MultiStorage

**Challenge**

You can now store two types of data in kernel.

Author: [3agl3](https://twitter.com/3agl31)

`nc pwn.challenge.bi0s.in 1235`

<details>
<summary>Hint</summary>
<p>Functions that may look irrelevant might have bigger affect than you think!</p>
</details>

[handout.zip](./MultiStorage.zip)
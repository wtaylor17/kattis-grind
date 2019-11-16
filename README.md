# This is where I plan to store solutions to kattis problems in the future
I'm currently adding some functionalities which Chris (@chrismacdonaldw) may choose to incorporate later.

# Will's attempted updates
* Got python testing working on windows (need to specify interpreter name)
* Added basic checking for numeric precision errors through `--precision <p>` argument to `test.py` script.
* Still need to check for correct structure

# Kattis Grind
A small easy-to-use package of Python 3 scripts which can help speed up the process for competitive programming on [Kattis](https://open.kattis.com). The scripts will download a local copy of the question (html file), and can automate testing inputs / outputs.

# Requirements
The Kattis Grind setup requires two modules. To install them:
```console
foo@bar:~$ pip3 install bs4
foo@bar:~$ pip3 install fake-useragent
```
# How do I use it?
## Fetch a question
```console
foo@bar:~/kattis-grind$ ./fetch.py
Enter ID:
```console
If you prefer to use command line arguments instead, you can! For example, if I wanted to get question 'hello':
```console
foo@bar:~/kattis-grind$ ./fetch.py --id hello
```

## Test your solution!
```console
foo@bar:~/kattis-grind$ ./test.py
Enter ID:
```
Similarly to fetching a question, you can pass in an optional ID argument! Using 'hello' as an example again:
```console
foo@bar:~/kattis-grind$ ./test.py --id hello
```
The `--precision` argument automatically checks numeric precision of output. The below example tests a problem with max error 1/10000.
```console
foo@bar:~/kattis-grind$ ./test.py --id tetration --precision 0.00001
```
*Note: On windows, the python interpreter must be referenced when running a script.*
## Generating random questions!
The best feature of this program is that you can fetch random questions from Kattis too! If I was interested in five questions between a range of 1.4 to 1.6, I can run the script like this:
```console
foo@bar:~/kattis-grind$ ./rand.py
Enter lower bound: 1.4
Enter upper bound: 1.6
How many questions: 5
```
It's as simple as that! But as you may have guessed, there are optional command line arguments for these too! Although they're less useful, you can use them like this:
```console
foo@bar:~/kattis-grind$ ./rand.py --lobound 1.4 --upbound 1.6 --qamount 5
```
Depending on how many questions you want, and what range they're between, this operation *may* take several seconds (sometimes a good 10 - 40 seconds!!). Keep in mind that while it takes long, it definitely works!

# License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

# Acknowledgments
* Thanks to [JarateKing](https://github.com/JarateKing) and [Ben Boyle](https://github.com/benbdevd) for the original grinding idea.
* Thanks to [Will Taylor](https://github.com/wtaylor17) for fixing test.py to work on Windows machines.
* Thanks to the UPEI SMCSS for all the motivation!!!

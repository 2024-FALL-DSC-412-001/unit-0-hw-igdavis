# Getting Started
Passing all test cases is required for you to finish this workshop.

You can run your tests in terminal by doing the following:

Make sure your terminal is in this directory. You can confirm that is true by typing `pwd` in terminal.

Create a virtual environment with

`python -m venv ./.venv`

Then activate it in terminal:

Windows: `.\.venv\Scripts\activate`

Mac: `source ./.venv/bin/activate`

Linux: `source ./.venv/bin/activate`


You should see `.venv` appear in the terminal on the left side of teh command line.

Then run `pip install -r requirements.txt` in terminal

Now run `pytest` in terminal.

^ If that does not work try `python -m pytest`

When you first start you will see every test is failing. Your goal is to pass every test with the instructions below. Happy coding!


# Explaining What is going on

Hopefully you have this open in VS Code. If not you should have gotten a link to clone this repo onto your computer. You can then open the folder (the repo) that was cloned in VS Code. Use the "Mark Down All in On" Extension to open this readme.md file to see it easier. The button should be in the top right area of the screen. 

We will be using Github Classroom to make grading easier. This will let you automatically see your grade every time you upload (or push) your work. I will walk you through how to do that. 


# What will be graded?

In this unit, file `unit-0-hw.ipynb` will be graded. That is the file you will want to modify. You can see how it will be graded in the `test_hw.py` file. The goal is to pass all tests in the `test_hw.py` file. 
<br><br>
Lets start by passing one test, seeing if we passed it locally, then uploading it to Github Classroom to get your grade. 
<br><br>


# Saving and Grading your Code

How do you upload and grade your code? 
<br><br>

One way you got this starter template was through using Github. Github is a place where code is stored online and shared in *repos*. It helps other developer's not reinvent the wheel, and use other people's Python tools to accelerate their works. 

We will being using Github to upload your code to your personal repo.

Below I will explain how to upload your code and it graded. There are multiple of the same explanations below.

There are 3 basic steps to uploading your code, and they are are placed in terminal. 

1.) Adding to stage

2.) Committing from stage

3.) Pushing commit to online repo 

# Using VS Code UI to submit

Make a change to your homework file.

*Make sure all your files are saved*

1. Click on the "Source Control" icon on the left

![click on the source control icon](https://user-images.githubusercontent.com/65638400/192014627-2a370104-63b9-48d7-860b-d94b14c7997b.png)

2. Under the "Changes" section, press the + button next to the hw file. 

![click stage changes](https://user-images.githubusercontent.com/65638400/192014789-9ad2947c-dabf-4f7e-9fd3-35c5badfcc26.png)


3. Then type a short message about your homework in the "Message" box under the "Source Control" section. 

![add commit message](https://user-images.githubusercontent.com/65638400/192014814-ce341536-c8d0-41d4-a1d3-dc6a98318896.png)

4. Hit the commit button! 

![commit the file and message](https://user-images.githubusercontent.com/65638400/192014867-72fb4225-39c5-46f1-bdfc-586b7ba0d8d1.png)

5. Now open the Commits Section and the most recent commit. You should see the file you committed there. 

![commited and moved to commit section](https://user-images.githubusercontent.com/65638400/192014921-0170e62b-1341-4c4b-8fe1-900803b6ad2a.png)

6. Next click on the "..." in the Source Control *section* (not window). Go to step 7

7. Click Push. 

![image](https://user-images.githubusercontent.com/65638400/192015256-ab089720-31c5-4d76-9ab4-7885cdad9a32.png)


You have submitted your homework! You will want to do these steps every time you make a change to your homework.



# Using Terminal to submit

Make a change to your homework file.

*Make sure all your files are saved*

In terminal type:

`git add -A`

This means: github add -A (all) files to *stage*

Stage is where files can then be committed.
You can check what is staged by using `git status` in terminal. 

`git commit -m "<some message>" `

This will commit any code you have staged. If you forget the -m and message, press `:q!` and try again. If that does not work press "esc" multiple times then type in `:q!` again.

Then finally 
`git push` 
will push your commit to the github repo. 

Your code will then be graded automatically. 

<br><br>
Another way to think about this:

A *commit* is a package we would like to upload online.

*stage* is like a temporary places to hold what we want to commit. 

We create the package using the `add` command to add code to *stage*

Once we are done adding code to *stage*, we can then seal the package with the `commit` command. We give the commit a message like `commit -m "some message"`

We then need to send the package online, so we call `push`, which pushes your code into your repo 

<br><br>
All 4 commands used in order: 

`git status`, can be called anytime to see what is in stage

`git add <file path>` or `git add -A`, can stage specific files or use `-A` to stage all files (-A is recommended for now)

`git commit -m "some message"`, sealing stage in a commit with an attached message

`git push` push the commit to online branch. 

You can call as many commits before a push as you would like. You can also push as many new commits as you want. 

Here is a general workflow:

Modify file_we_want_to_grade.py

You want to grade file_we_want_to_grade.py

`git add -A`

`git commit -m "new: some comment about implementation"`

`git push`

file_we_want_to_grade.py is then graded

# Looking at your Grade

The https:// link you clone, put that in your brower.

Click on the red x or green check mark to see what tests you are failing (or if you passed all the tests!)


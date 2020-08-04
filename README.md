# Learning how to use GitHub!

### McIntosh Lab GitHub tutorial


[Git cheat sheet here](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)

Frequently used in the tutorial:
* `git status`
* `git log`

## Tutorial steps:

* Create repository on site

* `git init`

* `git add remote origin <link>`

* `git status`

* `git add (-A)`

* `git status`

* `git commit -m 'first commit'`

* git may ask for user details
  * `git config (--global) user.email "<email>"`
  * `git config (--global) user.name "<name>"`

* `git push -u origin master`
  * fill in credentials
    * git may try to use a pop-up box on Linux
      * do `unset GIT_ASKPASS` or `unset SSH_ASKPASS` to fix

* `git log`

* Make .gitignore file
  * `vim/nano .gitignore`
  * add `*.log` to .gitignore and save

* To execute changes to .gitignore:
  * `git rm -r --cached`
  * `git add -A`
  * this will untrack all files and retrack with updated .gitignore file
  * `git status`

* `git commit -m 'added .gitignore'`
* `git push origin master`

* Let's make a mistake in our code
* `git add -A`
* `git push origin master`

* We realize we made a mistake and want to undo the commit we pushed
* `git log` will show us the commit hash of the last good commit
* `git reset --hard <commit>`

* Let's fix the remote version too
* `git push origin master --force`

###Basic branching

* let's say we want to test out a change before committing it to the master branch

* `git checkout -b large`
  * creates branch called 'large' and takes us into the branch

* make some changes

* `git status`
* `git add -A`
* `git commit -m 'testing change to planet sizes'`
* `git push origin large`
  * note different remote name

* merge branch on GitHub

* `git pull origin master`
  * syncs remote changes to local directory

* Resetting uncommitted changes
  * useful if you did a bunch of stuff since the last commit and you want to undo it

* let's make another mistake

* `git diff`

* `git log -2 -p`
  * show diff from last two commits

* `git reset --hard`
  * resets our branch to state as of last commit
  * will DELETE all changes


## Storybro's Magically Lewd Sleepover Adventure: Visual Novel Edition ##

This is the main page for the visual novel adaptation. We are currently looking for artists; both background and character.

To use this project in [Ren'Py](www.renpy.org), just clone this project to your projects folder. This is usually `Documents/Ren'Py/` or `Documents/Ren'Py/renpy-[version]-sdk`. In Linux-style commands:

```
cd ~/Documents/Ren'Py/
git clone https://github.com/snoozbuster/Storybro-VN
```

In Windows, you can download something like [MinGW](mingw.org) or [Cygwin](www.cygwin.com) to give you a Linux-like terminal. You can also use the [GitHub for Windows](http://windows.github.com) client.

To contribute, add files you've made to the `game/` folder and make a [pull request](https://help.github.com/articles/creating-a-pull-request). It's recommended that when doing work, you should create a seperate branch to use; then make a pull request on that branch instead of `master`. Once the request is accepted, it will be merged into `master`; at that point you can pull the changes from origin and then delete the branch. This isn't strictly necessary, but recommended for larger contributions.

The relevant commands are as follows:

```
git checkout -b new_branch_name
# alternatively, "git branch new_branch_name" and "git checkout new_branch_name" can be used, but "checkout -b" combines these features
# ...
# push new branch
git push origin new_branch_name:new_branch_name
# after pull request is accepted, pull the changes and delete the branch
git pull
git branch -d new_branch_name
```

For more help, you can check out [this](https://help.github.com/articles/what-are-other-good-resources-for-learning-git-and-github) page on learning git and GitHub.

# Contributing to Python Extensive Project Framework Architect (PyEPFA)

First off, thank you for considering contributing to PyEPFA! It's people like you that make PyEPFA such a great tool.

## Where do I go from here?

If you've noticed a bug or have a feature request, make sure to check our [Issues](https://github.com/your-username/PyEPFA/issues) page to see if someone else in the community has already created a ticket. If not, go ahead and make one!

## Fork & create a branch

If this is something you think you can fix, then fork PyEPFA and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

```bash
git checkout -b 325-add-japanese-localisation
```

## Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first.

## Get the code

The first thing you'll need to do is get the PyEPFA code. To do this, you'll need to fork the repository.

## Make a Pull Request

At this point, you should switch back to your master branch and make sure it's up to date with PyEPFA's master branch:

```bash
git remote add upstream https://github.com/your-username/PyEPFA.git
git checkout master
git pull upstream master
```

Then update your feature branch from your local copy of master, and push it!

```bash
git checkout 325-add-japanese-localisation
git rebase master
git push --set-upstream origin 325-add-japanese-localisation
```

Finally, go to GitHub and make a Pull Request.

## Keeping your Pull Request updated

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

To learn more about rebasing in Git, there are a lot of good [resources](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) but here's the suggested workflow:

```bash
git checkout 325-add-japanese-localisation
git pull --rebase upstream master
git push --force-with-lease origin 325-add-japanese-localisation
```

## What if my Pull Request gets rejected?

In some cases, we might decide to reject your Pull Request. If we do, we'll let you know why. This isn't a reflection on you, and we encourage you to keep participating in our community!

Remember, it's always worth asking for clarification if you don't understand why your Pull Request was rejected.

## Thank you for your contributions!

We're really glad you're reading this, and we're excited to see what you'll bring to PyEPFA.

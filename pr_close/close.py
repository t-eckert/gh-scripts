"""PR closing script

This script fetches all PRs on a given GitHub repository and adds a comment

Expects 2 arguments, a repository as OWNER/REPOSITORY and the path to a text
file which will be the content of the comments.

```python
python3 comment.py OWNER/REPOSITORY ./comment.md
```
"""

from json import loads
from subprocess import PIPE, run
from sys import argv


def fetch(repo: str) -> bytes:
    # returns a byte array of JSON with the number ids of each PR on the given repo
    return run(
        ["gh", "pr", "list", "--json", '"number"', "-R", repo], stdout=PIPE
    ).stdout


def format(prs: bytes) -> list[int]:
    # returns the number ids of the PRs for the given bytes array of JSON
    return [pr["number"] for pr in loads(prs.decode("utf-8"))]


def close(prs: list[int], repo: str) -> str:
    # closes all open pull requests on the repository
    return "".join(
        run(
            ["gh", "pr", "close", str(pr), "-R", repo],
            stdout=PIPE,
        ).stdout.decode("utf-8")
        for pr in prs
    )


if __name__ == "__main__":
    repo = argv[1]
    prs = format(fetch(repo))
    response = input(
        f"Close all {len(prs)} pull requests to the {repo} repository? [y/N] "
    )
    if response in ("y", "Y"):
        close(prs, repo)
        print("Done")

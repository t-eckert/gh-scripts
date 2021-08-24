# Mass PR Closing Scropt

This script allows the user to close every open pull request in a given repository.

## Prerequisites

- [Python](https://www.python.org/)
  ```bash
  brew install python
  ```
- [GitHub CLI](https://cli.github.com/)
  ```bash
  brew install gh
  ```

## Usage

```bash
python3 close.py OWNER/REPO
```

The first argument is the repository whose open pull requests will closed.

The script will collect the number ids of each open pull request and prompt you for confirmation before creating the comments.

```bash
Close all 19 pull requests to the hashicorp/consul-helm repository? [y/N]
```


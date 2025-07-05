# Xmake `pre-commit` hooks

This is a collection of [`pre-commit`](https://pre-commit.com/)
hooks for running [`xmake`](https://xmake.io) commands.

## Available hooks

### Formatting your project

Example:

```yml
- repo: https://github.com/seffradev/xmake-pre-commit-hooks
  rev: v1.0.0
  hooks:
  - id: format
```

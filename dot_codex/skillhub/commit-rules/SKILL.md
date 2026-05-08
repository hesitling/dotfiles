---
name: commit-rules
description: Commit hygiene rules for creating git commits. Use when Codex is asked to commit changes, prepare commit messages, split staged or unstaged work into commits, review commit scope, create squash-and-merge commit text, or otherwise decide how repository changes should be committed.
---

# Commit Rules

## Commit Shape

- Use Conventional Commits: `<type>(<scope>): <summary>` when a scope is clear, or `<type>: <summary>` when no useful scope exists.
- Keep each commit small, clean, and focused on one logical change.
- Avoid large mixed commits. If staged or unstaged work contains multiple logical changes, split it into multiple commits.
- Do not include unrelated work just because it is present in the worktree. Inspect status and staged diff before committing.
- Prefer imperative, concise summaries under roughly 72 characters.

Common types:

- `feat`: user-visible behavior or capability
- `fix`: bug fix
- `docs`: documentation only
- `test`: tests only
- `refactor`: behavior-preserving code restructuring
- `chore`: maintenance, metadata, generated artifacts, or workflow housekeeping

## Splitting Work

When one commit would be too large or mixed, propose or create a list of conventional commits. Group by behavior and ownership, not by file extension alone.

Use this format when proposing a split:

```text
- feat(render): derive hostname at runtime
- test(render): cover hostname template context
- docs(render): document hostname variable usage
```

If committing directly, stage only the paths or hunks for the current logical commit, commit them, then continue with the next logical group.

## Squash And Merge Exception

For squash-and-merge commit text, use one brief introduction line, which may itself be Conventional Commit style, followed by a list of conventional commit messages that describe the squashed logical changes.

Format:

```text
feat(render): simplify hostname handling

- feat(render): derive hostname at runtime
- test(render): cover hostname template context
- docs(render): document hostname variable usage
```

Keep the introduction brief. Do not expand it into a long PR summary.

## Before Committing

- Run or report relevant verification for the staged change when practical.
- Check `git status --short` and the staged diff summary before `git commit`.
- If the repository requires escalation for `.git/index.lock`, request it for `git add` or `git commit` instead of working around git.

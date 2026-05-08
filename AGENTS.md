# Repository Notes

- Keep user-level non-secret chezmoi variables in `.chezmoidata/user.yml`, nested under `user`.
- Keep secrets in `.chezmoidata/secrets.yml`.
- Service configuration should use unified keys under `user.services.<service>.*`.

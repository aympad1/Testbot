services:
  - type: web
    name: telegram-bot-ayman
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn bot:app
    envVars:
      - key: 7995929975:AAFTBmjRbWDdte9bzvNmXJWhOr5SytqhRVE
        sync: false

# Today
The mixi.today website

## Local test
First, set the `DATABASE_URL` in the virtualenv console

    export DATABASE_URL='postgres://<usr>:<pwd>@localhost:<port>/today'

## Deploy
- Append the EXPORT lines to the postactivate file
- run `python manage.py collectstatic`

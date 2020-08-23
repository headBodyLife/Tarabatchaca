import os

os.system("""
rm -r migrations app/database.db

flask db init
flask db migrate
flask db upgrade
""")

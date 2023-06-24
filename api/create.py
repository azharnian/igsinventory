from application import db, create_app
from application.models.users import *
from application.models.items import *
from application.models.locations import *
from application.models.activities import *
from application.models.logs import *

app = create_app()

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
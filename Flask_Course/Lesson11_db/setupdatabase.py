from basic1 import db, Puppy, app

# Set up the application context
with app.app_context():
    # Creates all the tables: Model -> DB Table
    db.create_all()

    sam = Puppy('Sammy', 3)
    frank = Puppy('Frankie', 4)

    print(sam.id)  # None
    print(frank.id)  # None

    db.session.add_all([sam, frank])
    db.session.commit()

    print(sam.id)  # Should print the assigned ID after commit
    print(frank.id)  # Should print the assigned ID after commit

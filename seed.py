from app import app
from models import db, Production, CastMember


with app.app_context():
    Production.query.delete()
    print("Seeeding Productions.....🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 ")

    # Array of productions
    productions = []

    p1 = Production(title='Movie A', genre='Action', budget=5000000.00, image='movie_a.jpg',
                    director='John Doe', description='An action-packed thriller', ongoing=True)
    productions.append(p1)

    p2 = Production(title='Movie B', genre='Comedy', budget=3000000.00, image='movie_b.jpg', director='Jane Smith', description='A hilarious comedy with an ensemble cast', ongoing=False
                    )
    productions.append(p2)

    p3 = Production(title='Movie C', genre='Drama', budget=2000000.00, image='movie_c.jpg', director='Sam Johnson', description='A heartfelt story of love and sacrifice', ongoing=True
                    )
    productions.append(p3)

    p4 = Production(title='Movie D', genre='Sci-Fi', budget=8000000.00, image='movie_d.jpg', director='Emily Williams', description='An epic science fiction adventure', ongoing=False
                    )
    productions.append(p4)

    print("FInished.....🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 ")

    # 3add all the products to db session
    db.session.add_all(productions)
    db.session.commit()

# ===================================================CASTMEMEBER SEED=================================================
    # Delete existing cast member data
    CastMember.query.delete()

    print("Seeding CastMembers.....🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 ")

    # Array of cast members
    cast_members = []

    cm1 = CastMember(
        name='Actor 1',
        role='Role 1',
        production_id=1
    )
    cast_members.append(cm1)

    cm2 = CastMember(
        name='Actor 2',
        role='Role 2',
        production_id=1
    )
    cast_members.append(cm2)

    cm3 = CastMember(
        name='Actor 3',
        role='Role 3',
        production_id=2
    )
    cast_members.append(cm3)

    cm4 = CastMember(
        name='Actor 4',
        role='Role 4',
        production_id=2
    )
    cast_members.append(cm4)

    cm5 = CastMember(
        name='Actor 5',
        role='Role 5',
        production_id=3
    )
    cast_members.append(cm5)

    cm6 = CastMember(
        name='Actor 6',
        role='Role 6',
        production_id=3
    )
    cast_members.append(cm6)

    print("Finished.....🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 🍀 ")

    # Add all the cast members to the db session
    db.session.add_all(cast_members)
    db.session.commit()

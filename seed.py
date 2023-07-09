from app import app
from models import db, Production

with app_context():
    Production.query.delete()

    # Array of productions
    productions = []

    p1 = Production(
        title='Movie A',
        genre='Action',
        budget=5000000,
        image='movie_a.jpg',
        director='John Doe',
        description='An action-packed thriller',
        ongoing=True
    )
    productions.append(p1)

    p2 = Production(
        title='Movie B',
        genre='Comedy',
        budget=3000000,
        image='movie_b.jpg',
        director='Jane Smith',
        description='A hilarious comedy with an ensemble cast',
        ongoing=False
    )
    productions.append(p2)

    p3 = Production(
        title='Movie C',
        genre='Drama',
        budget=2000000,
        image='movie_c.jpg',
        director='Sam Johnson',
        description='A heartfelt story of love and sacrifice',
        ongoing=True
    )
    productions.append(p3)

    p4 = Production(
        title='Movie D',
        genre='Sci-Fi',
        budget=8000000,
        image='movie_d.jpg',
        director='Emily Williams',
        description='An epic science fiction adventure',
        ongoing=False
    )
    productions.append(p4)

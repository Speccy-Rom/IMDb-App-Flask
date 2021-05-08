from datetime import date

from src import db
from src.models import Film


def populate_films():
    harry_potter_and_ph_stone = Film(
        title='Harry Potter and the Philosopher\'s Stone',
        release_date=date(2001, 11, 4),
        description='An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, '
                    'his family and the terrible evil that haunts the magical world.',
        distributed_by='Warner Bros. Pictures',
        length=152,
        rating=7.6,
    )
    harry_potter_and_ch_s = Film(
        title='Harry Potter and Chamber of Secrets',
        release_date=date(2002, 11, 3),
        description='An ancient prophecy seems to be coming true when a mysterious presence begins stalking the '
                    'corridors of a school of magic and leaving its victims paralyzed.',
        distributed_by='Warner Bros. Pictures',
        length=161,
        rating=7.4,
    )
    harry_potter_and_priz_az = Film(
        title='Harry Potter and the Prizoner of Azkaban',
        release_date=date(2004, 6, 4),
        description='Harry Potter, Ron and Hermione return to Hogwarts School of Witchcraft and Wizardry for their '
                    'third year of study, where they delve into the mystery surrounding an escaped prisoner who poses '
                    'a dangerous threat to the young wizard.',
        distributed_by='Warner Bros. Pictures',
        length=142,
        rating=7.9,
    )
    harry_potter_and_ph_goblet_fire = Film(
        title='Harry Potter and the Goblet of Fire',
        release_date=date(2005, 11, 6),
        description='Harry Potter finds himself competing in a hazardous tournament between rival schools of magic, '
                    'but he is distracted by recurring nightmares.',
        distributed_by='Warner Bros. Pictures',
        length=157,
        rating=7.7,
    )
    harry_potter_and_order_phoenix = Film(
        title='Harry Potter and the Order of the Phoenix',
        release_date=date(2007, 7, 19),
        description='With their warning about Lord Voldemort\'s (Ralph Fiennes\') return scoffed at, Harry (Daniel '
                    'Radcliffe) and Dumbledore (Sir Michael Gambon) are targeted by the Wizard authorities as an '
                    'authoritarian bureaucrat slowly seizes power at Hogwarts.',
        distributed_by='Warner Bros. Pictures',
        length=138,
        rating=7.5,
    )
    harry_potter_and_half_blood_prince = Film(
        title='Harry Potter and the Half-Blood Prince',
        release_date=date(2009, 7, 16),
        description='As Harry Potter (Daniel Radcliffe) begins his sixth year at Hogwarts, he discovers an old book '
                    'marked as "the property of the Half-Blood Prince" and begins to learn more about Lord '
                    'Voldemort\'s (Ralph Fiennes\') dark past.',
        distributed_by='Warner Bros. Pictures',
        length=153,
        rating=7.6,
    )
    harry_potter_and_deathly_hallows_1 = Film(
        title='Harry Potter and the Deathly Hallows part 1',
        release_date=date(2010, 11, 18),
        description='As Harry (Daniel Radcliffe), Ron (Rupert Grint), and Hermione (Emma Watson) race against time '
                    'and evil to destroy the Horcruxes, they uncover the existence of the three most powerful objects '
                    'in the wizarding world: the Deathly Hallows.',
        distributed_by='Warner Bros. Pictures',
        length=146,
        rating=7.7,
    )
    harry_potter_and_deathly_hallows_2 = Film(
        title='Harry Potter and the Deathly Hallows part 2',
        release_date=date(2011, 7, 13),
        description='Harry, Ron, and Hermione search for Voldemort\'s remaining Horcruxes in their effort to destroy '
                    'the Dark Lord as the final battle rages on at Hogwarts.',
        distributed_by='Warner Bros. Pictures',
        length=130,
        rating=8.1,
    )

    db.session.add(harry_potter_and_ph_stone)
    db.session.add(harry_potter_and_ch_s)
    db.session.add(harry_potter_and_priz_az)
    db.session.add(harry_potter_and_ph_goblet_fire)
    db.session.add(harry_potter_and_order_phoenix)
    db.session.add(harry_potter_and_half_blood_prince)
    db.session.add(harry_potter_and_deathly_hallows_1)
    db.session.add(harry_potter_and_deathly_hallows_2)

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    print('Populating db...')
    populate_films()
    print('Successfully populated!')

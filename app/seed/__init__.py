from flask_seeder import Seeder, Faker, generator
from app.models.DaftarAkun import DaftarAkun,KategoriDaftarAkun
from app import db

class DemoSeeder(Seeder):

  # run() will be called by Flask-Seeder
  def run(self):
    request_data = KategoriDaftarAkun(name='Aset')
    db.session.add(request_data)
    db.session.commit()
    
    # # Create a new Faker and tell it how to create User objects
    # faker = Faker(
    #   cls=User,
    #   init={
    #     "id_num": generator.Sequence(),
    #     "name": generator.Name(),
    #     "age": generator.Integer(start=20, end=100)
    #   }
    # )

    # # Create 5 users
    # for user in faker.create(5):
    #   print("Adding user: %s" % user)
    #   self.db.session.add(user)
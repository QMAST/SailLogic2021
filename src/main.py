# coding=utf-8

from .entities.entity import Session, engine, Base
from .entities.sailLogicModel import SailLogicModel

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
models = session.query(SailLogicModel).all()

if len(models) == 0:
    # create and persist dummy exam
    python_exam = SailLogicModel("SQLAlchemy", "Test your knowledge about SQLAlchemy.", "script")
    session.add(python_exam)
    session.commit()
    session.close()

    # reload exams
    models = session.query(SailLogicModel).all()

# show existing exams
print('### Exams:')
for model in models:
    print(f'({model.id}) {model.title} - {model.description}')
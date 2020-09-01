# coding=utf-8

from .entities.entity import Session, engine, Base
from .entities.sailLogicModel import SailLogicModel
from flask import Flask, jsonify, request
from .entities.sailLogicModel import SailLogicSchema

# creating the Flask application
app = Flask(__name__)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/sailLogicModel')
def get_models():
    # fetching from the database
    session = Session()
    model_object = session.query(SailLogicModel).all()

    # transforming into JSON-serializable objects
    schema = SailLogicSchema(many=True)
    models = schema.dump(model_object)

    # serializing as JSON
    session.close()
    return jsonify(models)


@app.route('/sailLogicModel', methods=['POST'])
def add_model():
    # mount exam object
    posted_sailLogic = SailLogicSchema(only=('title', 'description'))\
        .load(request.get_json())

    #exam = SailLogicModel(**posted_sailLogic.data, created_by="HTTP post request")
    model = SailLogicModel(**posted_sailLogic, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(model)
    session.commit()

    # return created exam
    new_model = SailLogicSchema().dump(model)
    session.close()
    return jsonify(new_model), 201
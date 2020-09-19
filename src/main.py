# coding=utf-8

from .entities.entity import Session, engine, Base
from .entities.sailLogicModel import SailLogicModel
from flask import Flask, jsonify, request
from .entities.sailLogicModel import SailLogicSchema
from flask_cors import CORS
from .entities.ExistingState import ExistingState, ExistingStateSchema
from .entities.SailLogicCommand import SailLogicCommand, SailLogicCommandSchema

# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)
# TODO define existing state schema and fix up endpoints
"""
### Existing state
@app.route('/existingState')
def get_existing_state():
    # fetching from the database
    session = Session()
    model_object = session.query(ExistingState).all()

    # transforming into JSON-serializable objects
    schema = ExistingStateSchema(many=True)
    models = schema.dump(model_object)

    # serializing as JSON
    session.close()
    return jsonify(models)

### Existing state post
@app.route('/existingState', methods=['POST'])
def add_model():
    # mount exam object
    posted_existingState= ExistingStateSchema(only=('title', 'description'))\
        .load(request.get_json())

    model = ExistingState(**posted_existingState, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(model)
    session.commit()

    # return created exam
    new_model = ExistingStateSchema().dump(model)
    session.close()
    return jsonify(new_model), 201
"""
### sail command
@app.route('/sailLogicCommand')
def get_command():
    # fetching from the database
    session = Session()
    model_object = session.query(SailLogicCommand).all()

    # transforming into JSON-serializable objects
    schema = SailLogicCommandSchema(many=True)
    models = schema.dump(model_object)

    # serializing as JSON
    session.close()
    return jsonify(models)

### sail command post post
@app.route('/sailLogicCommand', methods=['POST'])
def add_command():
    #Quick little check, leaving this in for now
    print(Base.metadata.tables.keys())
    print(Base.metadata.tables)
    # mount exam object
    posted_command = SailLogicCommandSchema(only=('commandID', 'commandValue'))\
        .load(request.get_json())
    model = SailLogicCommand(**posted_command, created_by="HTTP post request")
    # persist exam
    session = Session()
    session.add(model)
    session.commit()
    # return created exam
    new_model = SailLogicCommandSchema().dump(model)
    session.close()
    return jsonify(new_model), 201


@app.route('/sailLogicModel')
def get_models_old():
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
def add_model_old():
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
    

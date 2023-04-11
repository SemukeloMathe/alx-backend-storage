#!/usr/bin/env python3

"""This module defines a function that lists all documents in a collection."""

import pymongo
from pymongo import MongoClient


def list_all(mongo_collection):
    """lists all documents in a collection."""

    return mongo_collection.find()
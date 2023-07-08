import datetime
from dateutil.relativedelta import relativedelta
from bson.objectid import ObjectId
import pytz
import os
import pydash as py_
from operator import itemgetter

import src.enums as Enums
from src.extensions import redis_cached
import src.controllers as Controllers
import src.constants as Consts
import src.models.repo as Repo
import json
import src.functions as funcs
from bson import json_util


class FL(object):

    @classmethod
    def upload_attached_file(cls, file):
        if file.filename == '':
            raise ValueError("No file selected for uploading")

        true_filename = file.filename
        path = os.path.join(Consts.UPLOAD_FOLDER, true_filename)
        file.save(path)
        return

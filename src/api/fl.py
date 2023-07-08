from flask import request, current_app

from flask_restx import Resource, marshal
import pydash as py_
import os
import src.constants as Consts
from src.schemas import FormMeta
from src.resp_code import ResponseMsg
from src.middlewares.http import enable_cors

api = FormMeta.api


@api.route('/upload-file')
@api.doc(responses=FormMeta.RESPONSE_CODE)
class UploadAttachedFile(Resource):
    @enable_cors
    def post(self):
        """
            Upload Attached File
        """
        try:
            if 'file' not in request.files:
                return ResponseMsg.INVALID.to_json(), 400
            file = request.files["file"]
            true_filename = file.filename
            path = os.path.join(Consts.UPLOAD_FOLDER, true_filename)
            file.save(path)
        except Exception as e:
            return ResponseMsg.INVALID.to_json(), 400
        return ResponseMsg.SUCCESS.to_json(data={}), 200

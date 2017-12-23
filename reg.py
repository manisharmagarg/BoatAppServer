#
# registration APIs
#

from flask_restful import Resource, Api


class PhoneResource(Resource):

    def post(self):
        args = parser.parse_args()
        phone_no = args['phone_no']

        # TODO get 6 digit no. from db for given phone no.
        ret = {
                "err": 0, 
                "msg": "Received phone no., will send 6 digit verification code by SMS"
             }

        return ret, 201


class CodeResource(Resource):

    def post(self):
        args = parser.parse_args()
        code = args['code']

        ret = {"err": 0, "msg": "Verification done"}

        return ret, 201

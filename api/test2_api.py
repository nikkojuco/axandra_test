from flask_restplus import Namespace, Resource
from pysafebrowsing import SafeBrowsing
from collections import defaultdict
from model.test2_model import Test2Model
from model.test2_put_model import Test2PutModel
from flask import request
import pymysql
api = Namespace('WebsiteSafetyCheck', description='')


@api.route('')
class Test2Collections(Resource):
    def post(self):
        test_2_model = Test2Model()
        request_args = test_2_model.get_req_parser()
        website = request_args['website']
        KEY = 'AIzaSyBNdlz3cBi7YGJL-vZtcX53Z6Iq1qkbUew'
        s = SafeBrowsing(KEY)
        r = s.lookup_urls([website])
        print(r)
        new_dict = dict(r)
        status = new_dict[website]['malicious']

        query = "INSERT INTO exam_b(website, is_malicious) VALUES('" + str(website) + "', '" + str(status) + "' );"
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="exam")
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        resp = {
            'status' : 200,
            'message' : 'Added ' + website + ' to db'
        }
        return resp

    def get(self):
        url = request.args.get('url')
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="exam")
        query = "Select * from exam_b WHERE website='" + url + "';"
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        a_list = list()
        for row in rows:
            a_list.append(list(row))
        connection.commit()
        connection.close()
        if len(a_list) is 0:
            resp = {
                'status': 400,
                'message': 'url not found',
            }
            return resp
        else:
            resp = {
                'status': 200,
                'message': 'Success',
                'data': a_list
            }
            return resp


    def delete(self):
        url = request.args.get('url')
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="exam")
        query = "DELETE FROM exam_b WHERE website='"+url+"'; "
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
        resp = {
            'status': 200,
            'message': url + ' Deleted'
        }
        return resp

    def put(self):
        test_2_put_model = Test2PutModel()
        request_args = test_2_put_model.get_req_parser()
        website = request_args['website']
        is_malicious = request_args['is_malicious']
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="exam")
        query = "UPDATE exam_b SET is_malicious='"+is_malicious+"' WHERE website='" + website + "';"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
        resp = {
            'status': 200,
            'message': website + ' successfully updated'
            }
        return resp



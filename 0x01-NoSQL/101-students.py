#!/usr/bin/env python3
"""A python function that retuns all students sorted by average score"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """A fuction that returns students soreted by avaerage score"""
    students_list = mongo_collection.find()
    students = []
    for student in students_list:
        scores=[topic.get("score") for topic in student.get('topics')]
        student['averageScore'] = sum(scores) / len(scores)
        students.append(student)
    return sorted(students, key=lambda x: x.get('averageScore'), reverse=True)

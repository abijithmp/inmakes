# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, exceptions
from odoo.exceptions import ValidationError


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "School Student"


    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)
    note = fields.Text(string='Description')



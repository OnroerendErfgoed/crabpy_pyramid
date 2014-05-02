# -*- coding: utf-8 -*-
'''
Adapters to help render :mod:`crabpy.gateway.capakey` objects to json.

.. versionadded:: 0.1.0
'''

from crabpy.gateway import capakey

from . import(
    json_list_renderer,
    json_item_renderer
)


def list_gemeente_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.capakey.Gemeente` to json.
    '''
    return {
        'id': obj.id,
        'naam': obj.naam
    }


def list_afdeling_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.capakey.Afdeling` to json.
    '''
    return {
        'id': obj.id,
        'naam': obj.naam,
        'gemeente': obj.gemeente
    }


def list_sectie_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.capakey.Sectie` to json.
    '''
    return {
        'id': obj.id,
        'afdeling': obj.afdeling
    }


def list_perceel_adapter(obj, request):
    '''
    Adapter for rendering a list of
    :class: `crabpy.gateway.capakey.Perceel` to json.
    '''
    return {
        'id': obj.id,
        'sectie': obj.sectie,
        'capakey': obj.capakey,
        'percid': obj.percid
    }


json_list_renderer.add_adapter(capakey.Gemeente, list_gemeente_adapter)
json_list_renderer.add_adapter(capakey.Afdeling, list_afdeling_adapter)
json_list_renderer.add_adapter(capakey.Sectie, list_sectie_adapter)
json_list_renderer.add_adapter(capakey.Perceel, list_perceel_adapter)


def item_gemeente_adapter(obj, request):
    '''
    Adapter for rendering an object of
    :class: `crabpy.gateway.capakey.Gemeente` to json.
    '''
    return {
        'id': obj.id,
        'naam': obj.naam,
        'centroid': obj.centroid,
        'bounding_box': obj.bounding_box
    }


def item_afdeling_adapter(obj, request):
    '''
    Adapter for rendering an object of
    :class: `crabpy.gateway.capakey.Afdeling` to json.
    '''
    return {
        'id': obj.id,
        'naam': obj.naam,
        'gemeente': obj.gemeente,
        'centroid': obj.centroid,
        'bounding_box': obj.bounding_box
    }


def item_sectie_adapter(obj, request):
    '''
    Adapter for rendering an object of
    :class: `crabpy.gateway.capakey.Sectie` to json.
    '''
    return {
        'id': obj.id,
        'afdeling': obj.afdeling,
        'centroid': obj.centroid,
        'bounding_box': obj.bounding_box
    }


def item_perceel_adapter(obj, request):
    '''
    Adapter for rendering an object of
    :class: `crabpy.gateway.capakey.Perceel` to json.
    '''
    return {
        'id': obj.id,
        'sectie': obj.sectie,
        'capakey': obj.capakey,
        'percid': obj.percid,
        'centroid': obj.centroid,
        'bounding_box': obj.bounding_box
    }


json_item_renderer.add_adapter(capakey.Gemeente, item_gemeente_adapter)
json_item_renderer.add_adapter(capakey.Afdeling, item_afdeling_adapter)
json_item_renderer.add_adapter(capakey.Sectie, item_sectie_adapter)
json_item_renderer.add_adapter(capakey.Perceel, item_perceel_adapter)

"""Inventory Shelf Responded signal payload class for the Cynthus project"""

from .inventory_responded_payload import InventoryRespondedPayload


class InventoryShelfRespondedPayload(InventoryRespondedPayload):
    """Represents the payload part of a public.inventory.shelf.responded signal message"""

"""Inventory Shelf Requested signal payload class for the Cynthus project"""

from .inventory_requested_payload import InventoryRequestedPayload


class InventoryShelfRequestedPayload(InventoryRequestedPayload):
    """Represents the payload part of a public.inventory.shelf.requested signal message"""

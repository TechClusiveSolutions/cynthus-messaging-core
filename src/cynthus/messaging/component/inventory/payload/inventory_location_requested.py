"""Inventory Location Requested signal payload class for the Cynthus project"""

from .inventory_requested_payload import InventoryRequestedPayload


class InventoryLocationRequestedPayload(InventoryRequestedPayload):
    """Represents the payload part of a public.inventory.location.requested signal message"""

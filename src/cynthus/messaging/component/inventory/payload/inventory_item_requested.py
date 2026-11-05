"""Inventory Item Requested signal payload class for the Cynthus project"""

from .inventory_requested_payload import InventoryRequestedPayload


class InventoryItemRequestedPayload(InventoryRequestedPayload):
    """Represents the payload part of a public.inventory.item.requested signal message"""

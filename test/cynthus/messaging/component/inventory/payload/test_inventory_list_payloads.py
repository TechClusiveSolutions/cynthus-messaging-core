"""Tests for the inventory list payload classes."""

from cynthus.messaging.component.inventory.payload import InventoryListRequestedPayload, InventoryListUpdatedPayload


def test_requested_payload_filters_are_optional():
    payload = InventoryListRequestedPayload()

    assert payload.item_type is None
    assert payload.name is None
    assert payload.schema_version == 1


def test_requested_payload_keeps_the_filters():
    payload = InventoryListRequestedPayload(item_type='frozen', name='Corn')

    assert (payload.item_type, payload.name) == ('frozen', 'Corn')


def test_updated_payload_defaults_to_an_empty_list():
    assert InventoryListUpdatedPayload().items == []


def test_updated_payload_keeps_the_items():
    assert InventoryListUpdatedPayload(items=[{'name': 'Corn'}]).items == [{'name': 'Corn'}]

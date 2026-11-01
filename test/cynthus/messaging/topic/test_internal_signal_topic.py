"""Tests for cynthus.messaging.topic.internal_signal_topic (InternalSignalTopic)."""

from cynthus.messaging.topic.internal_signal_topic import InternalSignalTopic
from cynthus.messaging.topic.signal_topic import SignalTopic


def test_is_a_signal_topic():
    assert issubclass(InternalSignalTopic, SignalTopic)


def test_name_is_the_internal_service_bus_topic():
    assert InternalSignalTopic().name == 'cynthus-topic-internal'


def test_name_can_be_overridden():
    assert InternalSignalTopic(name='other').name == 'other'

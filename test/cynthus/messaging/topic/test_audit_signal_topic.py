"""Tests for cynthus.messaging.topic.audit_signal_topic (AuditSignalTopic)."""

from cynthus.messaging.topic.audit_signal_topic import AuditSignalTopic
from cynthus.messaging.topic.signal_topic import SignalTopic


def test_is_a_signal_topic():
    assert issubclass(AuditSignalTopic, SignalTopic)


def test_name_is_the_audit_service_bus_topic():
    assert AuditSignalTopic().name == 'cynthus-topic-audit'


def test_name_can_be_overridden():
    assert AuditSignalTopic(name='other').name == 'other'

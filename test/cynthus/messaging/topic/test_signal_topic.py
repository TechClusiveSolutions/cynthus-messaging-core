"""Tests for cynthus.messaging.topic.signal_topic (SignalTopic) and its three concrete topics."""

import pytest
from pydantic import BaseModel, ValidationError

from cynthus.messaging.topic.audit_signal_topic import AuditSignalTopic
from cynthus.messaging.topic.core_signal_topic import CoreSignalTopic
from cynthus.messaging.topic.internal_signal_topic import InternalSignalTopic
from cynthus.messaging.topic.signal_topic import SignalTopic

TOPICS = [
    (CoreSignalTopic, 'cynthus-topic-public'),
    (InternalSignalTopic, 'cynthus-topic-internal'),
    (AuditSignalTopic, 'cynthus-topic-audit'),
]


def test_a_topic_is_a_pydantic_model():
    assert issubclass(SignalTopic, BaseModel)


def test_a_bare_topic_requires_a_name():
    with pytest.raises(ValidationError):
        SignalTopic()


def test_a_bare_topic_keeps_the_name_it_is_given():
    assert SignalTopic(name='custom').name == 'custom'


@pytest.mark.parametrize(('topic_class', 'name'), TOPICS)
def test_each_concrete_topic_is_a_signal_topic_with_its_documented_name(topic_class, name):
    assert issubclass(topic_class, SignalTopic)
    assert topic_class().name == name


def test_the_three_topics_have_distinct_names():
    assert len({topic_class().name for topic_class, _ in TOPICS}) == 3
